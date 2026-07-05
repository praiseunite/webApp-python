# Class Task: Build a Personal Portfolio Page with Flask

## Objective
Set up a Flask project from scratch, create multiple routes, and render HTML templates with dynamic Python data. By the end, you will have a live local web page displaying your own profile.

## Instructions

### Setup (Do this first!)
1. Create a new folder called `portfolio_app` inside your `Session_08` working directory.
2. Inside `portfolio_app`, create the following structure:
   ```
   portfolio_app/
   ├── app.py
   └── templates/
       ├── index.html
       └── skills.html
   ```
3. Open a terminal, navigate into `portfolio_app`, and install Flask:
   ```bash
   pip install flask
   ```

### Part A: The Home Route
1. Open `app.py` and create a Flask app.
2. Create a route for `"/"` called `home()`.
3. Create `templates/index.html` — it should display:
   - An `<h1>` with your name (passed from Python as `{{ name }}`).
   - A `<p>` with your course (passed as `{{ course }}`).
   - A navigation link to the skills page: `<a href="/skills">View My Skills</a>`
4. Pass your name and course from `app.py` using `render_template()`.

### Part B: The Skills Route
1. Create a second route for `"/skills"` called `skills()`.
2. In `app.py`, create a Python **list** called `skills` containing at least 4 items: e.g., `["Python", "File Handling", "Regex", "Flask"]`.
3. Pass this list to `templates/skills.html`.
4. In `skills.html`, use a Jinja2 `for` loop to display each skill as a list item:
   ```html
   {% for skill in skills %}
       <li>{{ skill }}</li>
   {% endfor %}
   ```

### Part C: Run and Test
1. Run `python app.py` from your terminal.
2. Open `http://127.0.0.1:5000/` and confirm your home page appears.
3. Click the skills link and confirm the skills page displays your list.

See `class_task_solution/` folder for the solution.
