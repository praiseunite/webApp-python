# Home Assignment: Guestbook Web App

## Objective
Build a complete Flask Web Application called **"The Clean Guestbook"**. 
Users will submit messages via a web form. Your app must process the message using **Regular Expressions** (to censor bad words or format it), save the cleaned message to a text file, and dynamically render all messages on the webpage.

## Instructions

### Part 1: Project Setup
1. Inside this session's folder, open `assignment_starter.py`. It has a basic Flask skeleton ready for you.
2. Create a folder named `templates` in the same directory if it doesn't exist.
3. Create an `index.html` file inside the `templates` folder.

### Part 2: Building the HTML Template (`index.html`)
1. Create a basic HTML structure.
2. Add a form that sends a `POST` request to `/`:
   - An `<input>` field for the user's Name (name="username").
   - A `<textarea>` for the Message (name="message").
   - A Submit button.
3. Below the form, use Jinja templating (`{% for msg in messages %}`) to display all the messages passed from the Flask backend.

### Part 3: The Flask Backend (`assignment_starter.py`)
1. In the `@app.route("/", methods=["GET", "POST"])` function:
   - Check if `request.method == "POST"`. If it is, get the `username` and `message` from the form using `request.form`.
   - **Regex Challenge:** Use `re.sub()` to find any instance of the words "darn", "heck", or "shoot" (case-insensitive) in the message, and replace them with `***`.
   - Open a file called `guestbook.txt` in append (`'a'`) mode. Save the entry like this: `[Name]: [Cleaned Message]\n`.
   - Read all lines from `guestbook.txt`. Make sure to handle `FileNotFoundError` gracefully (e.g., using a `try-except` block) by passing an empty list if the file doesn't exist yet.
   - Render `index.html`, passing the list of messages to it.

### Submission
Submit your `assignment_starter.py`, `templates/index.html`, and a screenshot of your working web app.

See `assignment_solution.py` and `templates/solution_index.html` if you get stuck.
