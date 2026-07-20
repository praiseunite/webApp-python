from flask import Flask, render_template, request
import re
import os

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        # 1. Get username and message from the form
        pass
        
        # 2. Use regex to censor "darn", "heck", "shoot"
        pass
        
        # 3. Append to guestbook.txt
        pass

    messages = []
    # 4. Read messages from guestbook.txt (handle FileNotFoundError)
    
    
    return render_template("index.html", messages=messages)

if __name__ == "__main__":
    app.run(debug=True)
