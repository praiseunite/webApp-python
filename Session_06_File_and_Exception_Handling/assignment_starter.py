# Mini-Project 2 Kickoff: Persistent Profile App

import profile_tools  # Import from Session 4

def get_user_info():
    name = input("Enter your name: ")

    # TODO: Wrap this in a try/except ValueError block
    age = int(input("Enter your age: "))

    # TODO: Open "user_profile.txt" in write mode and save name and age
    # with open(...) as f:
    #     f.write(...)

    print("Profile saved to user_profile.txt!")
    return name, age


def load_profile():
    # TODO: Write a try/except FileNotFoundError block
    # try:
    #     Open the file, read and print its contents
    # except FileNotFoundError:
    #     print("No saved profile found. Please create one first.")
    pass


def show_menu():
    print("\nWelcome to the Profile App!")
    print("1. Create new profile")
    print("2. Load existing profile")
    print("3. Exit")
    return input("Enter choice: ")


# --- Main Program ---
while True:
    choice = show_menu()

    if choice == "1":
        # TODO: Call get_user_info()
        pass
    elif choice == "2":
        # TODO: Call load_profile()
        pass
    elif choice == "3":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Try again.")
