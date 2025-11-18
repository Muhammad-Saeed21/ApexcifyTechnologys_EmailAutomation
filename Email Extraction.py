# Project : Email Extraction Tool
# Author  : Muhammad Saeed
# Internship : Apexcify Technologys - Python Programming Internship
# Description : A Python script that extracts all email addresses from a text file (data.txt)
#               and saves the unique emails into another file (emails.txt).

# Importing the 're' module for regular expression operations
import re

# Name of the input file containing raw text and email addresses
input_file = "data.txt"

# Name of the output file where extracted unique emails will be saved
output_file = "emails.txt"

try:
    # ----------------------------------------------------
    # 1) Reading the content of the input text file
    # ----------------------------------------------------
    # "with open" automatically closes the file after reading
    with open(input_file, "r", encoding="utf-8") as file:
        # Reading the entire content of the file into a string variable
        content = file.read()

    # ----------------------------------------------------
    # 2) Defining the Regular Expression pattern for emails
    # ----------------------------------------------------
    # Pattern explanation:
    # [a-zA-Z0-9._%+-]+  -> username part before '@'
    # @                  -> mandatory '@' symbol
    # [a-zA-Z0-9.-]+     -> domain name (example: gmail, yahoo)
    # \.[a-zA-Z]{2,}     -> top-level domain (example: .com, .pk)
    email_pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"

    # ----------------------------------------------------
    # 3) Finding all emails inside the file content
    # ----------------------------------------------------
    # 'findall' returns a list of all matching email addresses (may include duplicates)
    emails = re.findall(email_pattern, content)

    # ----------------------------------------------------
    # 4) Removing duplicate emails while keeping the order
    # ----------------------------------------------------
    # Using dict.fromkeys() to remove duplicates without changing the order
    unique_emails = list(dict.fromkeys(emails))

    # ----------------------------------------------------
    # 5) Writing the extracted unique email addresses into the output file
    # ----------------------------------------------------
    # Each email will be written on a new line
    with open(output_file, "w", encoding="utf-8") as file:
        for email in unique_emails:
            file.write(email + "\n")

    # ----------------------------------------------------
    # 6) Displaying a summary in the console
    # ----------------------------------------------------
    print(f"Total email patterns found : {len(emails)}")
    print(f"Unique emails saved        : {len(unique_emails)}")
    print(f"Output file                : {output_file}")

# ----------------------------------------------------
# Error handling: File not found or other issues
# ----------------------------------------------------
except FileNotFoundError:
    print(f"Error: The file '{input_file}' was not found. Please create it and add sample text.")

except Exception as e:
    print("An unexpected error occurred:", e)
