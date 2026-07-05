import requests
from bs4 import BeautifulSoup

def get_books():
    """Scrapes books from toscrape.com and returns a list of dicts."""
    url = "https://books.toscrape.com/"
    try:
        response = requests.get(url, timeout=10)
        soup = BeautifulSoup(response.text, "html.parser")
        book_tags = soup.find_all("article", class_="product_pod")

        books = []
        for book in book_tags:
            title = book.h3.a["title"]
            price = book.find("p", class_="price_color").text
            books.append({"title": title, "price": price})
        return books

    except Exception as e:
        return []  # Return empty list on network error
