import re
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# -------------------------------------------------------
# Route 1: Home — Display the profile form
# -------------------------------------------------------
@app.route("/")
def home():
    # TODO: Render "index.html" — pass an optional 'error' message
    # return render_template("index.html", error=None)
    pass


# -------------------------------------------------------
# Route 2: Submit — Process the form data
# -------------------------------------------------------
@app.route("/submit", methods=["POST"])
def submit():
    name = request.form["name"]
    email = request.form["email"]
    phone = request.form["phone"]
    bio = request.form["bio"]

    # TODO: Validate phone using re.fullmatch() with pattern r"\d{4}-\d{3}-\d{4}"
    # If invalid: redirect back to home with error="Invalid phone format!"
    
    # TODO: Tokenize the bio and count the words
    # tokens = re.findall(r"\w+", bio.lower())
    # word_count = len(tokens)

    # TODO: Save name, email, phone, and word_count to "user_profile.txt"
    # Use the 'with open(...)' syntax from Session 6

    # TODO: Redirect to the "/profile" route
    pass


# -------------------------------------------------------
# Route 3: Profile — Display the saved profile
# -------------------------------------------------------
@app.route("/profile")
def profile():
    # TODO: Open "user_profile.txt" and read its contents
    # Handle the case where the file doesn't exist yet (try/except)
    # Render "profile.html" and pass the file contents
    pass


if __name__ == "__main__":
    app.run(debug=True)
