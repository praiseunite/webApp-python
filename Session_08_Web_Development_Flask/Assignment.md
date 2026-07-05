# Assignment: Mini-Project 2 Final — Profile App Goes Live on the Web!

## Objective
Transform the CLI Profile App from Sessions 6 and 7 into a **real web application** using Flask. Instead of a terminal, users will interact with a browser-based form. Their validated data will be saved to a file, and a results page will display their profile.

## Project Structure to Create
```
profile_web_app/
├── app.py
├── templates/
│   ├── index.html      ← Form page (name, email, phone, bio)
│   └── profile.html    ← Results page showing saved profile
└── static/
    └── style.css       ← Basic styling (optional but encouraged!)
```

## Instructions

### Step 1: The Home Form (`/` — GET)
1. In `app.py`, create a `"/"` route.
2. Create `templates/index.html` with an HTML form that collects:
   - Name (`text` input)
   - Email (`email` input)
   - Phone (`text` input)
   - A short bio (`textarea`)
3. The form should submit to `"/submit"` using `method="POST"`.

### Step 2: Handle Form Submission (`/submit` — POST)
1. Create a `"/submit"` route in `app.py` that only accepts `POST` requests.
2. Use `request.form["field_name"]` to retrieve each field's value.
3. Validate the **phone number** using `re.fullmatch()` — the pattern from Session 7.
   - If invalid, redirect back to the home page with an error message using Flask's `redirect()` and `url_for()`.
4. If all data is valid:
   - Save the name, email, phone, and bio word count to `user_profile.txt` using file handling from Session 6.
   - Redirect to `"/profile"`.

### Step 3: The Profile Display Page (`/profile` — GET)
1. Create a `"/profile"` route.
2. Open `user_profile.txt` and read its contents.
3. Pass the contents to `templates/profile.html` and display the saved profile nicely.

### Step 4: Style It (Optional but Recommended!)
1. In `static/style.css`, add basic CSS to make the form and profile page look presentable.
2. Link it in your HTML with:
   ```html
   <link rel="stylesheet" href="{{ url_for('static', filename='style.css') }}">
   ```

## Expected Flow
```
User opens http://127.0.0.1:5000/
  → Sees a form (Name, Email, Phone, Bio)
  → Fills it in and clicks Submit
  → Flask validates the phone number
  → If valid: saves to file → redirects to /profile
  → /profile reads the file and displays the saved details
```
