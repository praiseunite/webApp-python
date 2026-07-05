# Class Task A: Web Scraping — Quote Collector

## Objective
Scrape quotes, authors, and tags from `https://quotes.toscrape.com/` — a website made for scraping practice — and save the results to a text file.

## Instructions

### Setup
Install the required libraries first:
```bash
pip install requests beautifulsoup4
```

### Part 1: Inspect the Page
1. Open `https://quotes.toscrape.com/` in your browser.
2. Right-click on any quote and click **"Inspect"**.
3. Notice each quote is inside a `<div class="quote">` element.
4. Inside it, the quote text is in `<span class="text">` and the author is in `<small class="author">`.

### Part 2: Write the Scraper
1. Open `class_task_a_starter.py` and complete the script:
   - Use `requests.get()` to fetch the page.
   - Parse it with `BeautifulSoup`.
   - Use `find_all("div", class_="quote")` to get all quotes.
   - Loop through them and extract the `text` and `author` of each.
   - Print them to the terminal.

### Part 3: Save to File
1. Save all the scraped quotes (and their authors) to a file called `quotes.txt`.
2. Format each line as: `"[quote text]" — [Author Name]`

### Bonus
- Also extract the tags for each quote (hint: look for `<a class="tag">` elements inside each quote div).
- Count how many quotes are on the page and print it at the end.

See `class_task_a_solution.py` for the solution.

---

# Class Task B: Tkinter — Student Grade Checker App

## Objective
Build a desktop GUI application using Tkinter that takes a student's name and score, and displays their grade.

## Instructions

### Part 1: Build the Window
1. Create a window titled **"Grade Checker"** with a size of `350x250`.
2. Add a `Label` that says "Student Grade Checker" in bold at the top.

### Part 2: Add Input Widgets
1. Add a `Label` ("Student Name:") and an `Entry` widget beside it.
2. Add a `Label` ("Score (0–100):") and an `Entry` widget beside it.
3. Use `grid()` to lay these out neatly.

### Part 3: Add Logic
1. Create a function called `check_grade()`.
2. Inside it, get the values from the two entry fields.
3. Use `if/elif/else` to determine the grade:
   - 70–100 → `"A - Excellent"`
   - 60–69 → `"B - Very Good"`
   - 50–59 → `"C - Good"`
   - 40–49 → `"D - Pass"`
   - Below 40 → `"F - Fail"`
4. Display the result in a `Label` below the button.

### Part 4: Add the Button
1. Add a **"Check Grade"** button that calls `check_grade()`.
2. Add error handling: if the score field has text instead of a number, display `"Please enter a valid score!"` in the result label in red.

See `class_task_b_solution.py` for the solution.
