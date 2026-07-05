# Class Task: Contact Info Extractor

## Objective
Use `re.findall()` and `re.search()` to extract specific information from a block of messy, unstructured text — a skill used daily in data engineering and web scraping.

## Background
You've been given a raw text dump from a company's old records system. Your job is to write a Python script that automatically pulls out all the email addresses and phone numbers.

## The Raw Text
```
Company: Aptech Learning Solutions
Address: 14 Tech Avenue, Lagos, Nigeria
Contact 1 - Alice Okonkwo: alice.okonkwo@aptech.com | 0801-234-5678
Contact 2 - Bob Mensah: bob.mensah@school.org | 0702-987-6543
Contact 3 - Charlie Diallo: charlie99@mail.net | (0903) 456-7890
General Enquiries: info@aptech.com
Emergency Line: 0800-000-0001
```

## Instructions
1. Copy the raw text into a Python variable called `raw_data`.
2. Using `re.findall()`, write a pattern to extract **all email addresses** from `raw_data` and store them in a list called `emails`.
3. Using `re.findall()`, write a pattern to extract **all phone numbers** (in any format present in the text) and store them in a list called `phones`.
4. Print both lists clearly with a descriptive label.
5. **Bonus:** Use `re.sub()` to create a "redacted" version of the text where all emails are replaced with `[EMAIL REDACTED]`.

## Expected Output
```
Emails found: ['alice.okonkwo@aptech.com', 'bob.mensah@school.org', 'charlie99@mail.net', 'info@aptech.com']
Phones found: ['0801-234-5678', '0702-987-6543', '(0903) 456-7890', '0800-000-0001']
```

See `class_task_solution.py` for the solution.
