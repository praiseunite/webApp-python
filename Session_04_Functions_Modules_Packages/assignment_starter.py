# Mini-Project 1 Refactor: Modules

# 1. Import your new module here
# TODO: import profile_tools

def get_user_info():
    name = input("Enter your name: ")
    age = int(input("Enter your age: "))
    return name, age

print("Welcome to the Profile Creator!")
user_name, user_age = get_user_info()

# 2. Call the check_age function from the module
# TODO: profile_tools.check_age(user_age)

# 3. Call the lambda function from the module to calculate birth year
# TODO: birth_year = profile_tools.get_birth_year(user_age)
# print(f"You were born around {birth_year}")
