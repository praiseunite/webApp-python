# Session 10: Try It Yourself (Comprehensive Review of Sessions 1-9)

## Objective
Welcome to the ultimate practice session! You've learned everything from basic variables up to building GUIs and Web Apps. This session covers the **Try It Yourself** exercises spanning Sessions 5 to 9. Pick AT LEAST ONE project to complete, and then tackle the Debugging Challenge.

---

## Choose Your Project (Pick ONE)

### Option A: The Data Cleaner (File Handling & Regular Expressions)
You have a messy text file of user registrations, and you need to extract valid email addresses and phone numbers.

**Instructions:**
1. Open `review_starter.py`.
2. Create a file named `raw_data.txt` with some dummy data (e.g., "Contact John at john.doe@email.com or 555-1234. Jane's email is jane_99@test.org and phone is 555-9876.")
3. Write a function `extract_contacts(filename)` that:
   - Uses a `try-except` block to open and read the file safely. If the file doesn't exist, print a friendly error message instead of crashing.
   - Uses `re.findall()` to extract all valid email addresses.
   - Uses `re.findall()` to extract all valid phone numbers (e.g., formats like 555-1234 or (555) 123-4567).
4. Save the extracted data into a new file called `cleaned_contacts.txt`.

### Option B: Book Price Scraper (Web Scraping & Tkinter)
Build a desktop app that scrapes a website for book prices and displays them.

**Instructions:**
1. Open `review_starter.py`.
2. Write a function `scrape_books()` that uses `requests` and `BeautifulSoup` to scrape titles and prices from `http://books.toscrape.com/`. 
   - Get the first 5 books.
   - Return them as a list of dictionaries: `[{"title": "...", "price": "..."}, ...]`.
3. Create a Tkinter GUI with a title "Book Scraper".
4. Add a Button labeled "Fetch Books".
5. When the button is clicked, call `scrape_books()` and display the results neatly in a Tkinter `Text` widget or multiple `Label`s using a loop.

---

## Debugging Challenge (Everyone does this!)

The code below is a basic text analyzer. It is supposed to read a file, find all words starting with 'A' or 'a', and print them. However, it has **5 bugs**. 

Find and fix them all in `debug_challenge.py`.

```python
import re

def analyze_text(filename)
    try:
        file = open(filename, 'r')
        content = file.read()
    except FileNotFoundError
        print("File not found!")
        return
    
    # Regex to find words starting with A or a
    pattern = "\b[aA]\w*"
    words = re.findall(pattern content)
    
    print("Words starting with A:")
    for w in words:
        print(w)
        
    file.close()

analyze_text("sample.txt")
```

### Bug Hints
<details>
<summary>Hint 1</summary>
Check the function definition syntax. Is anything missing at the end of the line?
</details>
<details>
<summary>Hint 2</summary>
Check the `except` statement syntax. Does it look complete?
</details>
<details>
<summary>Hint 3</summary>
Look closely at the regex pattern string. Python interprets `\b` as a backspace character unless it's a raw string.
</details>
<details>
<summary>Hint 4</summary>
`re.findall` requires two arguments. Are they separated correctly?
</details>
<details>
<summary>Hint 5</summary>
What happens if the code crashes before `file.close()`? Is there a better way to handle opening files so they close automatically?
</details>

---

## Answers to Debug Challenge
<details>
<summary>Click to see all 5 bugs</summary>

1. **Line 3:** Missing colon at the end of `def analyze_text(filename):`
2. **Line 7:** Missing colon at the end of `except FileNotFoundError:`
3. **Line 12:** The regex pattern needs an `r` prefix to treat `\b` correctly: `pattern = r"\b[aA]\w*"`
4. **Line 13:** Missing comma between arguments in `re.findall`: `words = re.findall(pattern, content)`
5. **Context:** Instead of manually calling `open()` and `close()`, use `with open(filename, 'r') as file:` to ensure the file is closed properly even if an error occurs.
</details>

---

*If you get stuck on the project, try breaking the problem into smaller pieces. Build one function at a time, test it, then move on. You can always peek at `review_solution.py` for guidance!*
