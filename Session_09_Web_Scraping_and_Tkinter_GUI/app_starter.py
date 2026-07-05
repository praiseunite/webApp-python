import tkinter as tk
# TODO: import your scraper_starter module (rename it to scraper.py in your project)

def load_books():
    # TODO: Call scraper.get_books() and store the result
    books = []  # Replace with scraper.get_books()

    # TODO: Clear the listbox
    # listbox.delete(0, tk.END)

    # TODO: Loop through books and insert into listbox
    # for book in books:
    #     listbox.insert(tk.END, f"{book['title']} — {book['price']}")

    # TODO: Update the count label
    # count_label.config(text=f"Total: {len(books)} books loaded")
    pass


# --- Build the Window ---
window = tk.Tk()
window.title("Book Browser")
window.geometry("500x450")

# TODO: Add title label

# TODO: Add "Load Books" button that calls load_books

# TODO: Create a Frame for the listbox and scrollbar
# frame = tk.Frame(window)
# frame.pack(...)

# TODO: Add Scrollbar
# scrollbar = tk.Scrollbar(frame)
# scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

# TODO: Add Listbox linked to scrollbar
# listbox = tk.Listbox(frame, width=65, height=15, yscrollcommand=scrollbar.set)
# listbox.pack()
# scrollbar.config(command=listbox.yview)

# TODO: Add count label at the bottom

window.mainloop()
