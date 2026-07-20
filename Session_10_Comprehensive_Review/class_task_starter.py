# class_task_starter.py
import tkinter as tk
import requests
from bs4 import BeautifulSoup
import re

# Part 2: Scrape the Data
def scrape_quotes():
    # 1. Fetch the page http://quotes.toscrape.com/
    # 2. Extract quotes and authors
    # 3. Return a list of strings
    pass

# Part 3: Filter and Save
def process_quotes():
    # 1. Call scrape_quotes()
    # 2. Get author name from entry widget
    # 3. Open 'archived_quotes.txt' and save matching quotes
    # 4. Update status label
    pass

# Part 1: Build the UI
window = tk.Tk()
window.title("Quote Archiver")
window.geometry("400x300")

# Add your widgets here (Labels, Entry, Button)


window.mainloop()
