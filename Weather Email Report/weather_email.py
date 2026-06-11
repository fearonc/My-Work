import os
import requests
import smtplib
from email.mime.text import MIMEText
from urllib.parse import quote
from datetime import datetime


POSTCODE = "CW8 3PA"
EMAIL_SUBJECT = "Today's weather report"
TIMEZONE = "Europe/London"

RECIPIENT_EMAIL = os.getenv("RECIPIENT_EMAIL")
SMTP_HOST = os.getenv("SMTP_HOST")
SMTP_PORT = int(os.getenv("SMTP_PORT", "587"))
EMAIL_USER = os.getenv("EMAIL_USER")
EMAIL_PASS = os.getenv("EMAIL_PASS")


def get_lat_lon_from_postcode(postcode: str):
    print(f"Looking up postcode: {postcode}")
    url = f"https://api.postcodes.io/postcodes/{quote(postcode)}"
    response = requests.get(url, timeout=20)
    print(f"Postcode API status: {response.status_code}")
    response.raise_for_status()

    data = response.json()
    print("Postcode API response received.")

    if data.get("status") != 200 or not data.get("result"):
        raise ValueError(f"Could not find postcode: {postcode}")

    result = data["result"]
    print(f"Latitude: {result['latitude']}, Longitude: {result['longitude']}")

    return {
        "latitude": result["latitude"],
        "longitude": result["longitude"],
        "admin_district": result.get("admin_district", ""),
        "region": result.get("region", ""),
        "country": result.get("country", "")
    }


def get_weather_forecast(lat: float, lon: float, timezone: str):
    print("Requesting weather forecast...")
    url = (
        "https://api.open-meteo.com/v1/forecast"
        f"?latitude={lat}"
        f"&longitude={lon}"
        "&hourly=temperature_2m,precipitation_probability,weather_code"
        "&forecast_days=1"
        f"&timezone={quote(timezone)}"
    )

    response = requests.get(url, timeout=20)
    print(f"Weather API status: {response.status_code}")
    response.raise_for_status()

    data = response.json()
    print("Weather API response received.")

    if "hourly" not in data:
        raise ValueError("Weather API response did not include hourly data.")

    return data


def weather_code_description(code: int) -> str:
    descriptions = {
        0: "clear sky",
        1: "mainly clear",
        2: "partly cloudy",
        3: "overcast",
        45: "fog",
        48: "depositing rime fog",
        51: "light drizzle",
        53: "moderate drizzle",
        55: "dense drizzle",
        56: "light freezing drizzle",
        57: "dense freezing drizzle",
        61: "slight rain",
        63: "moderate rain",
        65: "heavy rain",
        66: "light freezing rain",
        67: "heavy freezing rain",
        71: "slight snow fall",
        73: "moderate snow fall",
        75: "heavy snow fall",
        77: "snow grains",
        80: "slight rain showers",
        81: "moderate rain showers",
        82: "violent rain showers",
        85: "slight snow showers",
        86: "heavy snow showers",
        95: "thunderstorm",
        96: "thunderstorm with slight hail",
        99: "thunderstorm with heavy hail",
    }
    return descriptions.get(code, f"unknown weather code ({code})")


def build_day_summary(hourly_rows):
    temps = [row["temperature"] for row in hourly_rows]
    rain_probs = [row["rain_chance"] for row in hourly_rows]
    codes = [row["weather_code"] for row in hourly_rows]

    avg_temp = sum(temps) / len(temps)
    max_temp = max(temps)
    min_temp = min(temps)
    max_rain = max(rain_probs)

    thunder_codes = {95, 96, 99}
    heavy_rain_codes = {65, 82}
    rainy_codes = {51, 53, 55, 61, 63, 65, 80, 81, 82}
    cloudy_codes = {2, 3}
    clear_codes = {0, 1}

    thunder_hours = sum(1 for c in codes if c in thunder_codes)
    heavy_rain_hours = sum(1 for c in codes if c in heavy_rain_codes)
    rainy_hours = sum(1 for c in codes if c in rainy_codes)
    cloudy_hours = sum(1 for c in codes if c in cloudy_codes)
    clear_hours = sum(1 for c in codes if c in clear_codes)

    if thunder_hours > 0:
        headline = "Stormy day expected"
    elif heavy_rain_hours >= 2 or max_rain >= 75:
        headline = "Very wet day expected"
    elif rainy_hours >= 4 or max_rain >= 50:
        headline = "Rainy day overall"
    elif clear_hours >= cloudy_hours and max_rain < 25:
        if avg_temp >= 18:
            headline = "Warm and mostly clear day"
        else:
            headline = "Mostly clear day"
    elif cloudy_hours >= clear_hours and max_rain < 35:
        headline = "Mostly cloudy but fairly dry day"
    else:
        headline = "Mixed day with changeable conditions"

    extra = (
        f"Temperatures look to range from {min_temp:.0f}°C to {max_temp:.0f}°C, "
        f"with the highest rain chance around {max_rain:.0f}%."
    )

    return f"{headline}. {extra}"


def extract_7am_to_7pm(weather_data):
    print("Extracting hourly rows...")
    hourly = weather_data["hourly"]

    times = hourly["time"]
    temps = hourly["temperature_2m"]
    rain_probs = hourly["precipitation_probability"]
    codes = hourly["weather_code"]

    rows = []

    for t, temp, rain, code in zip(times, temps, rain_probs, codes):
        dt = datetime.fromisoformat(t)
        if 7 <= dt.hour <= 19:
            rows.append({
                "datetime": dt,
                "temperature": temp,
                "rain_chance": rain,
                "weather_code": code,
                "weather_text": weather_code_description(code)
            })

    print(f"Found {len(rows)} hourly rows between 7am and 7pm.")

    if not rows:
        raise ValueError("No hourly rows found between 07:00 and 19:00.")

    return rows


def rain_colour(rain_chance):
    if rain_chance >= 60:
        return "#f8d7da"
    if rain_chance >= 30:
        return "#fff3cd"
    return "#d1ecf1"


def build_email_body(location_text: str, hourly_rows):
    print("Building email body...")
    today_str = datetime.now().strftime("%A %d %B %Y")
    summary = build_day_summary(hourly_rows)

    table_rows = []

    for row in hourly_rows:
        time_label = row["datetime"].strftime("%I:%M %p").lstrip("0")

        table_rows.append(
            f"""
            <tr>
                <td style="padding:10px; border:1px solid #dddddd; text-align:left;">{time_label}</td>
                <td style="padding:10px; border:1px solid #dddddd; text-align:center;">{row['temperature']:.1f}°C</td>
                <td style="padding:10px; border:1px solid #dddddd; text-align:center; background-color:{rain_colour(row['rain_chance'])}; font-weight:bold;">{row['rain_chance']}%</td>
                <td style="padding:10px; border:1px solid #dddddd; text-align:left;">{row['weather_text'].title()}</td>
            </tr>
            """
        )

    table_html = "\n".join(table_rows)

    html = f"""
    <html>
    <body style="margin:0; padding:20px; background-color:#f4f6f8; font-family:Arial, Helvetica, sans-serif; color:#333333;">
        <div style="max-width:720px; margin:0 auto; background-color:#ffffff; border:1px solid #dddddd; border-radius:12px; overflow:hidden;">
            
            <div style="background:linear-gradient(135deg, #4a90e2, #357abd); color:#ffffff; padding:24px 30px;">
                <h1 style="margin:0; font-size:28px;">Today's Weather Report</h1>
                <p style="margin:8px 0 0 0; font-size:15px;">{location_text}</p>
                <p style="margin:4px 0 0 0; font-size:14px; opacity:0.95;">{today_str}</p>
            </div>

            <div style="padding:24px 30px;">
                <div style="background-color:#eef6ff; border-left:5px solid #4a90e2; padding:16px; border-radius:8px; margin-bottom:24px;">
                    <h2 style="margin:0 0 8px 0; font-size:18px; color:#1f4e79;">Summary</h2>
                    <p style="margin:0; font-size:15px; line-height:1.6;">{summary}</p>
                </div>

                <h2 style="margin:0 0 16px 0; font-size:20px; color:#333333;">Hourly Breakdown (07:00 to 19:00)</h2>

                <table style="width:100%; border-collapse:collapse; font-size:14px;">
                    <thead>
                        <tr style="background-color:#4a90e2; color:#ffffff;">
                            <th style="padding:12px; border:1px solid #dddddd; text-align:left;">Time</th>
                            <th style="padding:12px; border:1px solid #dddddd; text-align:center;">Temperature</th>
                            <th style="padding:12px; border:1px solid #dddddd; text-align:center;">Rain Chance</th>
                            <th style="padding:12px; border:1px solid #dddddd; text-align:left;">Conditions</th>
                        </tr>
                    </thead>
                    <tbody>
                        {table_html}
                    </tbody>
                </table>

                <p style="margin-top:24px; font-size:12px; color:#777777;">
                    Generated automatically with Python and GitHub Actions.
                </p>
            </div>
        </div>
    </body>
    </html>
    """

    return html


def send_email(recipient: str, subject: str, body: str):
    print("Preparing SMTP email...")

    if not all([SMTP_HOST, SMTP_PORT, EMAIL_USER, EMAIL_PASS, recipient]):
        raise ValueError("Missing one or more required environment variables for email sending.")

    msg = MIMEText(body, "html")
    msg["Subject"] = subject
    msg["From"] = EMAIL_USER
    msg["To"] = recipient

    print("Connecting to SMTP server...")
    with smtplib.SMTP(SMTP_HOST, SMTP_PORT, timeout=30) as server:
        server.starttls()
        server.login(EMAIL_USER, EMAIL_PASS)
        server.send_message(msg)

    print("Email sent successfully.")


def main():
    location = get_lat_lon_from_postcode(POSTCODE)

    weather = get_weather_forecast(
        lat=location["latitude"],
        lon=location["longitude"],
        timezone=TIMEZONE
    )

    hourly_rows = extract_7am_to_7pm(weather)

    location_text = (
        f"{POSTCODE} "
        f"({location['admin_district']}, {location['region']}, {location['country']})"
    )

    email_body = build_email_body(location_text, hourly_rows)

    print("HTML email body built successfully.")

    send_email(
        recipient=RECIPIENT_EMAIL,
        subject=EMAIL_SUBJECT,
        body=email_body
    )


if __name__ == "__main__":
    main()
