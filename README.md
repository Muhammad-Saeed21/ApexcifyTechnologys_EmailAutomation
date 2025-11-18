# ApexcifyTechnologys_EmailAutomation
# Email Extraction Tool
Author: Muhammad Saeed
Internship: Apexcify Technologys – Python Programming Internship
Project: Task Automation – Extract Email Addresses from Text File
📘 Project Description

This project is a simple Python automation tool that extracts all email addresses from a text file named data.txt and saves the unique email addresses into another file called emails.txt.

It uses Regular Expressions (Regex) to detect email patterns and removes duplicates while maintaining order.

🧰 Technologies Used

Python 3

Regular Expressions (re module)

File Handling

📁 Project Files

File Name	Description
extract_emails.py	Main Python script that extracts emails
data.txt	Input file containing sample text and email addresses
emails.txt	Automatically generated output containing unique emails

🚀 How the Program Works

Reads all text from data.txt

Uses regex to detect email patterns

Collects all found emails (including duplicates)

Removes duplicates while keeping order

Saves the clean list of emails into emails.txt

Prints a summary in the console

📜 Regex Pattern Used
[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}


This pattern matches:

Gmail

Yahoo

Company domains

.com, .net, .pk, .org, etc.

📂 Folder Structure (Recommended)
/EmailExtractor
   ├── Email Extraction.py
   ├── data.txt
   └── README.md

🖥️ How to Run the Program

Install Python (if not installed)

Keep data.txt in the same folder as the script

Run this command in terminal or VS Code:

python Email Extraction.py

📦 Output Example

Console Output:

Total email patterns found : 12
Unique emails saved        : 9
Output file                : emails.txt


Output File (emails.txt) will contain:

email1@example.com
sales@shop-now.com
documents@mydomain.net
...

❗ Error Handling

The program handles:

1. Missing File

If data.txt is not found:

Error: The file 'data.txt' was not found. Please create it and add sample text.

2. Unknown Errors

For unexpected issues:

An unexpected error occurred: <error message>

✅ Completion Status

✔ Task Automation
✔ File Handling
✔ Regex Pattern
✔ Clean Project Structure
✔ Internship-ready Submission
