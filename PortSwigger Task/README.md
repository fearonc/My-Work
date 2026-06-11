Issue: 

Like a lot of companies, our small in-house legal team gets a steady stream of low-stakes, fairly standard commercial contracts to review - mutual NDAs, small customer order forms, that kind of thing. Most are 80% boilerplate. Where we do get redlines and requests for amends, they're usually questions and edits we've seen before. Right now, every single contract still gets read by a person, and the queue is usually longer than the day. When we reach the end of month or end of quarter, and have lots of sales activity, it can get overwhelming. Your task: Please show us how AI could help with this


My Solution:

Initially, no AI would be used until the POC works, then AI can be implemented to improve the capabilities.

Assuming the email system used in Microsoft Outlook, I would create an automated flow involving Microsoft Power Automate and Microsoft Lists. This could then be used to search for key words and categorise emails based on their content and send them to different email folders based on priority. So the ones that matter can be addressed faster.

<h3>Step 1:</h3>

Setting up the list in Microsoft Lists. Below is the example I've setup with the relevant columns relating to incoming emails.

<img width="2544" height="526" alt="image" src="https://github.com/user-attachments/assets/d53a3d81-338b-45fb-a95a-0820dd85dec2" />


<h3>Power Automate:</h3>

This is where the "flow" would carry out the work to add the emails to the Microsoft List. It looks in the inbox for the legal team's email address. Converts the body of the email from HTML to plain text, then adds all the relevant details from the email into the Microsoft List.

Steps displayed in the following Screenshots:

1: Setting "When new email arrives in the inbox"

2: Converting the HTML body of the email to plain text

3: Condition: Look in the body, If it contains key word like "Urgent" (This can be expanded to include other key words)

4: True: Move email to Urgent folder

5: Fale: Run another Condition

Condition: Does Body contain "NDA" (This can be expanded to include other key words)

6: True: Move email to Standard Review folder

7: False: Move to Low Priority folder

8: Create the item in the Microsoft list for the email


1:
<img width="2543" height="1152" alt="image" src="https://github.com/user-attachments/assets/03212ef7-f4b9-40af-8486-f07775ff78a9" />

2:
<img width="1865" height="520" alt="image" src="https://github.com/user-attachments/assets/2f36182e-a403-4789-8796-460e729738c0" />

3:
<img width="2291" height="911" alt="image" src="https://github.com/user-attachments/assets/0f706178-e2b9-4793-8189-4b7b6307608e" />

4:
<img width="1494" height="880" alt="image" src="https://github.com/user-attachments/assets/678a81f7-7028-4238-9940-0856f2874f0a" />

5:
<img width="2172" height="774" alt="image" src="https://github.com/user-attachments/assets/f4d261dd-cecb-4f40-82fb-ec1ab0008522" />

6:
<img width="1827" height="966" alt="image" src="https://github.com/user-attachments/assets/09456d3b-3b50-4be0-9b46-c3937e3cb273" />

7:
<img width="2182" height="985" alt="image" src="https://github.com/user-attachments/assets/294bf19b-16a8-4459-a272-6ee60a6bc1f9" />

8:
<img width="2276" height="992" alt="image" src="https://github.com/user-attachments/assets/6739c9cb-b8d0-4a3c-b183-4146a2439a8d" />


<h3>Improving with AI</h3>

This current method would at least filter some emails to relevant folders to prioritise important emails. But to improve upon this, it could later be linked to an AI of your choosing to have the AI read the subject and email body and determine more accurately the urgency of the email based on not only keywords, but the tone and subject matter within the body of the email.
