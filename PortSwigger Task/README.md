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

<img width="1534" height="843" alt="image" src="https://github.com/user-attachments/assets/d6245f53-c4f7-42b2-a626-782d1f23b94a" />


<img width="1474" height="637" alt="image" src="https://github.com/user-attachments/assets/90f5bc75-9df2-4ed1-8ba7-36a43cdf52c9" />

<img width="1491" height="930" alt="image" src="https://github.com/user-attachments/assets/f551a333-01f4-42b4-84a4-6cc14cae04cd" />
