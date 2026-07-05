import re

def get_valid_email():
    while True:
        email = input("Enter your email address: ")
        # TODO: Write a regex pattern to validate the email
        # Hint: use re.fullmatch() with a pattern that checks for @ and a domain
        # If valid, return the email
        # If not, print "Invalid email format! Try again."
        pass


def get_valid_phone():
    while True:
        phone = input("Enter your phone number (e.g., 0801-234-5678): ")
        # TODO: Use re.fullmatch() to check for the format XXXX-XXX-XXXX
        # If valid, return the phone
        # If not, print "Invalid phone format! Try again."
        pass


def tokenize_bio():
    bio = input("Write a short bio about yourself: ")
    # TODO: Use re.findall(r"\w+", bio.lower()) to get the word tokens
    # Print how many words were found and the list of tokens
    # Return the token count
    pass


def save_profile(name, email, phone, word_count):
    # TODO: Use re.sub() to clean extra spaces from name before saving
    # Open "user_profile.txt" in write mode
    # Write name, email, phone, and bio word count to the file
    pass


# --- Main ---
print("=== Smart Profile Creator ===")
name = input("Enter your name: ")
email = get_valid_email()
phone = get_valid_phone()
word_count = tokenize_bio()
save_profile(name, email, phone, word_count)
print("Profile saved successfully!")
