# My Work
A collation of all my AI and efficiency developments

Using AI assistants such as Claude and Chat GPT I've developed a range of tools, workflow improvements, existing tool limitation workarounds, and time-saving processes for multiple teams.

<h2>Excel VBA macros:</h2>

(Multiple different versions for different departments) Entire Macro worksheets with different VBA modules for data validation, data transformation, and data prepping for ingesting.
Allowing a clear, simple workflow to carry out checks and automate very tedious data transformation.

<h1>Catalogue Macro Worksheet UI</h1>

<img width="1796" height="1017" alt="image" src="https://github.com/user-attachments/assets/2069b215-f0c9-4789-84a2-32d099db8c10" />


<h1>Catalogue Macro VBA project</h1>

<img width="345" height="719" alt="image" src="https://github.com/user-attachments/assets/113f4132-da4a-40e2-b3a4-9556f0c9bf2c" />


<h1>Content Macro VBA Project</h1>

<img width="487" height="1302" alt="image" src="https://github.com/user-attachments/assets/01ba2657-149e-4902-950d-c7afb0155651" />

I've developed several additional VBA macros for content that were incorporated into a single worksheet: A URL creator that produced a compliant URL based on a product title, a HTML checker to correct broken HTML and wrap plain text in correct HTML ready for ingesting, a complex Excel formula to concatenate data from a table with a lot of HTML to output a full HTML table from a sheet of product data.



<h2>PowerShell Macros</h2>

I've used PowerShell macros for a variety of tasks for my Catalogue team and the Content team:

<h1>Catalogue Team</h1>
<ul><li>Automating weekly and daily SQL queries and emailing the results to the whole team for someone to ingest the results. (6X different reports)</li>
<li>Automate moving files from downloads to new folders for archiving</li>
<li>Automating a weekly email to myself with all ticket numbers and corresponding product ID's I've worked on for the week, so I can search my emails to find a specific ticket as a fallback when searching the ticketing system fails</li>
<li>Shortcut to create a specific upload sheet based on the list of product ID's I copy in. (Used for loading a "Created By" attribute</li>
<li>Automate combinging multiple sheets together</li>
<li>Automate splitting large sheets to decrease ingesting file size</li>
</ul>

<h1>Content Team</h1>
<ul><li>Cropping a batch of image files by a specificed %</li>
<li>Renaming a batch of images in a specified folder using an Excel sheet to map old -> New file names</li>
<li>A tool for also adding specific suffixes to image file names as well as duplicating the files if multiple suffixes are needed</li>
</ul>


<h2>Python</h2>

I've used AI to help produce Python scripts for developing tools to improve workflows and simplify certain tasks within my team.

Translation uploader - This allows a user to simply copy in a table of options with relevant translations. It will then perform a variety of SQL queries to check the database for any existing options, and provide either insert or update SQL commands to write to the database. These updates do not have an audit log, so it also then writes the updates made, time/date, and requestor name to a live Excel doc on sharepoint, so we can keep our own audit log.
<img width="1351" height="940" alt="image" src="https://github.com/user-attachments/assets/812fe9bc-192f-4ef8-a7ac-d1a393c576ca" />

<img width="1192" height="814" alt="image" src="https://github.com/user-attachments/assets/b6f05dc2-012e-45cd-b578-586ee6f3b3a5" />
<img width="1200" height="814" alt="image" src="https://github.com/user-attachments/assets/2493558b-cb24-4bcf-b59e-17dcee318772" />


