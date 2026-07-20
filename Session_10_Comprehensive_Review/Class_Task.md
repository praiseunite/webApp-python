# Class Task: The Quote Archiver

## Objective
Combine **Web Scraping**, **Regular Expressions**, **File Handling**, and **Tkinter** into a single application. You will build a desktop tool that scrapes quotes from a website, filters them using Regex, and saves them to a text file.

## Instructions

### Part 1: Build the UI (Tkinter)
1. Open `class_task_starter.py`.
2. Create a Tkinter window titled **"Quote Archiver"** (Size: 400x300).
3. Add the following widgets:
   - A `Label` asking "Enter Author Name (or leave blank for all):"
   - An `Entry` widget for the author name.
   - A `Button` that says "Scrape & Save" and triggers a function `process_quotes()`.
   - A `Label` for displaying status messages (e.g., "Ready", "Saved 10 quotes!").

### Part 2: Scrape the Data (Requests & BeautifulSoup)
1. Create a function `scrape_quotes()`.
2. Fetch the page `http://quotes.toscrape.com/`.
3. Extract all quotes (`<span class="text">`) and their authors (`<small class="author">`).
4. Return a list of strings in the format: `"[Quote text]" - [Author Name]`.

### Part 3: Filter with Regex & Save (RegEx & File I/O)
1. In the `process_quotes()` function (triggered by the button):
   - Call `scrape_quotes()` to get the data.
   - Get the author name from the Tkinter `Entry` widget.
   - Open a file named `archived_quotes.txt` using a `try-except` block (use `with open(...)` in append mode `'a'`).
   - Loop through the scraped quotes. Use **re.search()** to check if the user's inputted author name is in the string. If it's blank, save all of them.
   - Write the matching quotes to the file.
   - Update the status `Label` in Tkinter with the number of quotes saved (e.g., "Successfully saved 5 quotes!").

### Bonus
- Instead of just checking the author, add a checkbox (using Tkinter's `Checkbutton`) to "Remove Punctuation". If checked, use `re.sub(r'[^\w\s]', '', text)` to strip punctuation from the quote before saving it!

See `class_task_solution.py` if you need help.
