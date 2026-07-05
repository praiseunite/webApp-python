# Assignment: Mini-Project 3 — Scraper + Desktop Viewer App

## Objective
Combine **Web Scraping** and **Tkinter GUI** into a single integrated desktop application. The app will scrape book data from the web and display it inside a real desktop window — this is how real data dashboards work!

## Project: "Book Browser" Desktop App

### Project Structure
```
book_browser/
├── scraper.py       ← Module that handles all web scraping logic
└── app.py           ← The Tkinter GUI that calls scraper.py
```

## Instructions

### Step 1: The Scraper Module (`scraper.py`)
1. Create `scraper.py` with a function called `get_books()`.
2. Inside it, scrape `https://books.toscrape.com/` using `requests` and `BeautifulSoup`.
3. For each book, extract:
   - `title` (from `book.h3.a["title"]`)
   - `price` (from `book.find("p", class_="price_color").text`)
4. Return a **list of dictionaries**, like:
   ```python
   [{"title": "A Light in the Attic", "price": "£51.77"}, ...]
   ```

### Step 2: The GUI App (`app.py`)
1. Import `tkinter` and your `scraper` module.
2. Create a window titled **"Book Browser"** (`500x450`).
3. Add a title label at the top: `"Books to Scrape"`.
4. Add a **"Load Books"** button.
5. Add a `Listbox` (with a `Scrollbar`) to display the books.
6. Add a `Label` at the bottom to show the total book count.

### Step 3: Connect Them
1. When the "Load Books" button is clicked, call `scraper.get_books()`.
2. Clear the Listbox first (`listbox.delete(0, tk.END)`).
3. Loop through the returned list and insert each book into the Listbox:
   ```python
   listbox.insert(tk.END, f"{book['title']} — {book['price']}")
   ```
4. Update the count label: `"Total: X books loaded"`.

### Bonus Challenge
- Add a `Entry` search bar at the top.
- Add a **"Search"** button that filters the Listbox to only show books whose titles contain the search term.

## Expected Result
A running desktop app where clicking "Load Books" fetches live data from the internet and populates a scrollable list of book titles and prices!
