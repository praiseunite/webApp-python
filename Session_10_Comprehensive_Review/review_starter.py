# review_starter.py
import re
import requests
from bs4 import BeautifulSoup
import tkinter as tk

# OPTION A: The Data Cleaner
def extract_contacts(filename):
    # 1. Use try-except to open and read the file
    pass

    # 2. Extract emails using re.findall()
    
    # 3. Extract phone numbers using re.findall()
    
    # 4. Write the extracted data to 'cleaned_contacts.txt'

# Uncomment the line below to test Option A after creating raw_data.txt
# extract_contacts("raw_data.txt")


# OPTION B: Book Price Scraper
def scrape_books():
    # 1. Fetch the page http://books.toscrape.com/
    
    # 2. Parse with BeautifulSoup
    
    # 3. Extract the first 5 books (title and price)
    
    # 4. Return as a list of dictionaries
    return []

# 5. Create Tkinter GUI below
# window = tk.Tk()
# window.title("Book Scraper")
# Add Button and Text widget here...

# window.mainloop()
