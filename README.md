# My Work
A collation of all my AI and efficiency developments

Using AI assistants such as Claude and Chat GPT I've developed a range of tools, workflow improvements, existing tool limitation workarounds, and time-saving processes for multiple teams.

<details>
<summary><strong>Excel VBA Macros</strong></summary>

<br>

(Multiple different versions for different departments) Entire Macro worksheets with different VBA modules for data validation, data transformation, and data prepping for ingesting.
Allowing a clear, simple workflow to carry out checks and automate very tedious data transformation.

<h2>Catalogue Macro Worksheet UI</h2>

<img width="1796" height="1017" alt="image" src="https://github.com/user-attachments/assets/2069b215-f0c9-4789-84a2-32d099db8c10" />


<h2>Catalogue Macro VBA project</h2>

<img width="345" height="719" alt="image" src="https://github.com/user-attachments/assets/113f4132-da4a-40e2-b3a4-9556f0c9bf2c" />


<h2>Content Macro VBA Project</h2>

<img width="487" height="1302" alt="image" src="https://github.com/user-attachments/assets/01ba2657-149e-4902-950d-c7afb0155651" />

I've developed several additional VBA macros for content that were incorporated into a single worksheet: A URL creator that produced a compliant URL based on a product title, a HTML checker to correct broken HTML and wrap plain text in correct HTML ready for ingesting, a complex Excel formula to concatenate data from a table with a lot of HTML to output a full HTML table from a sheet of product data.


</details>

<details>
<summary><strong>PowerShell Macros</strong></summary>

<br>

I've used PowerShell macros for a variety of tasks for my Catalogue team and the Content team:

<h2>Catalogue Team</h2>
<ul><li>Automating weekly and daily SQL queries and emailing the results to the whole team for someone to ingest the results. (6X different reports)</li>
<li>Automate moving files from downloads to new folders for archiving</li>
<li>Automating a weekly email to myself with all ticket numbers and corresponding product ID's I've worked on for the week, so I can search my emails to find a specific ticket as a fallback when searching the ticketing system fails</li>
<li>Shortcut to create a specific upload sheet based on the list of product ID's I copy in. (Used for loading a "Created By" attribute</li>
<li>Automate combinging multiple sheets together</li>
<li>Automate splitting large sheets to decrease ingesting file size</li>
</ul>

<h2>Content Team</h2>
<ul><li>Cropping a batch of image files by a specificed %</li>
<li>Renaming a batch of images in a specified folder using an Excel sheet to map Old -> New file names</li>
<li>A tool for also adding specific suffixes to image file names as well as duplicating the files if multiple suffixes are needed</li>
</ul>

</details>

<details>
<summary><strong>Python</strong></summary>

<br>

I've used AI to help produce Python scripts for developing tools to improve workflows and simplify certain tasks within my team.

Translation uploader - This allows a user to simply copy in a table of options with relevant translations. It will then perform a variety of SQL queries to check the database for any existing options and provide either insert or update SQL commands to write to the database. These updates do not have an audit log, so they also write the updates made, time/date, and requester's name to a live Excel doc on SharePoint, so we can keep our own audit log.
<h2>Data input UI</h2>
<img width="1351" height="940" alt="image" src="https://github.com/user-attachments/assets/812fe9bc-192f-4ef8-a7ac-d1a393c576ca" />
<h2>Output Summary</h2>
<img width="1192" height="814" alt="image" src="https://github.com/user-attachments/assets/b6f05dc2-012e-45cd-b578-586ee6f3b3a5" />
<h2>Output of Errors/Warnings</h2>
<img width="1200" height="814" alt="image" src="https://github.com/user-attachments/assets/2493558b-cb24-4bcf-b59e-17dcee318772" />


<h2>Advanced barcode search</h2>
I created an advanced Barcode search tool that can carry out multiple different SQL queries and provide concise results to search for multiple parameters (In this case, different organisations). Eliminating the need to do multiple different searches, saving users' time.

<img width="1816" height="1088" alt="image" src="https://github.com/user-attachments/assets/035105fb-55ec-408b-9880-f403c6feedb2" />

</details>

<details>
<summary><strong>JavaScript</strong></summary>

<br>
I've used JavaScript to develop multiple shortcuts, workflow improvements and tool limitation workarounds to use on our internal tools' UI on Chrome.

<h2>Bookmarklets</h2>
<img width="352" height="51" alt="image" src="https://github.com/user-attachments/assets/db696cf5-ff3f-4d14-8185-b62b2069a422" />

Here are 5 bookmarklets our team use on a daily basis, for every ticket completed. In order, they do the following:
<ul><li>1: Grabs the requester name, ticket number, and current date from a Service Desk + ticket and copies it to the clipboard, ready for the user to simply paste it for renaming a downloaded file. Keeping naming standards consistent, quick and easy.</li>
<li>2: Copies a specific table element from a UI to grab all newly created SKU, copies it to the user's clipboard, so it's ready to paste into Excel. Saves the user from having to manually drag to highlight a table that can be hundreds of rows long.</li>
<li>3: Automates 4 button clicks and UI navigation to close tasks on a ticket, which needs to be done before it can be closed. Simplifying and speeding up manual steps.</li>
<li>4: Automates clicks and typing to navigate to the reply tab, type a standard reply, then open the attachments window, so the user can re-attach a feedback sheet. Simplifying, speeding up, and bringing consistency to the ticket closure process.</li>
<li>5: A multi-purpose toolkit I will cover next</li></ul>


<h2>JavaScript toolkit</h2>
I developed this toolkit which is hosted on GitHub. It contains several tools to overcome the UI limitations of internal tools.

<img width="322" height="560" alt="image" src="https://github.com/user-attachments/assets/4d2a837d-bf3c-4d6d-8d24-76ddc5cb4c8d" />

<details>
<summary><strong>1: Relationship Option Bulk Update(Sensitive Data Blurred)</strong></summary>

<br>

One of the biggest time-savers for our team. This bypasses a limitation that has been chased for 10+ years to resolve. This has saved multiple hours in a single use one multiple occasions, and frequently reduces ticket times by at least 5X on even smaller updates.

This allows a bulk process to update multiple fields on a page where it historically has to be done 1-by-1.

The boxes seen in the screenshot would have to be edited manually 1 by 1 before, this could be required for hundreds at a time. This was extremely time-consuming. 

The bulk method allows the user to have an Excel mapping of the SKUs and relevant changes. They can simply copy it into the tool and run, it will update the table dynamically for every matching SKU.
<img width="2291" height="1078" alt="image" src="https://github.com/user-attachments/assets/bdf48e91-c65b-4320-8c11-de9c9b27de0e" />

Before:
<img width="2291" height="1078" alt="image" src="https://github.com/user-attachments/assets/2dc7aadf-1e6e-4318-a947-2faf4dbbd2e0" />

Mapping for those SKUs and new options in Excel:

<img width="430" height="133" alt="image" src="https://github.com/user-attachments/assets/05c26fba-43d7-4bc8-90fe-bd0b02980277" />


Tool:
<img width="978" height="618" alt="image" src="https://github.com/user-attachments/assets/e6d27468-feb4-411c-b85f-ba89f015b2bb" />


Output:
<img width="982" height="505" alt="image" src="https://github.com/user-attachments/assets/7128c322-d38e-4dea-a2c9-b7b430b7f642" />

Results:
<img width="2237" height="676" alt="image" src="https://github.com/user-attachments/assets/73e88abf-43e2-41e6-b90f-41ca7c126b63" />


</details>

<details>
<summary><strong>2: Matrix Image Tool</strong></summary>

<br>

Matrix is the system name for the content management system. When the content team needed to re-order images in a product it was a convoluted method.

They had to manually change the "Image order" number on the individual images. But changing to an existing image order would override the previous image in that order, so they'd first have to move it to a placeholder location like 999, then move the intended image, then move it back to the correct slot.

This tool used a  UI to allow dragging and dropping of images, it then carries out the manual work of re-ordering them automatically.

Original order:

<img width="228" height="588" alt="image" src="https://github.com/user-attachments/assets/886f9a91-9874-458b-a60e-80f203190e47" />

Tool UI:

Drag and drop the images to re-order

<img width="1104" height="877" alt="image" src="https://github.com/user-attachments/assets/b775693f-28c4-4a97-bfd0-db009502c221" />

This has removed multiple steps from this process and speeds up re-ordering images a lot. There is also a tab that can be used to clean up any gaps in the image order numbering. Or to add a gap ready for inserting new images into a specific slot.

<img width="1102" height="532" alt="image" src="https://github.com/user-attachments/assets/bf7a5b2a-dcca-4961-b5ab-a93e8e288f9b" />

</details>

<details>
<summary><strong>3: Audit History Search</strong></summary>

<br>

There is an Audit history page to check any changes made to a product. This consists of drop-downs for every update. However, Ctrl+F doesn't work on this page to find specifics within those drop-downs while they are collapsed. So users have to expand each row one by one to find what they're searching for. This tool uses the Inspect Element to search through all the collapsed rows to find the data.

<img width="1857" height="528" alt="image" src="https://github.com/user-attachments/assets/a557c33b-4a65-4967-8c37-f010530365d4" />

Results:

These show each update where the search term was found and also shows the details for the upload as you cycle through the results.

<img width="268" height="165" alt="image" src="https://github.com/user-attachments/assets/ae4c45c7-dfb6-4fad-acb8-07029e356694" />

<img width="2306" height="1205" alt="image" src="https://github.com/user-attachments/assets/948fba9b-70a6-4938-8dca-751d46f23cf2" />


</details>
</details>

