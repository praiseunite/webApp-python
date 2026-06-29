# Assignment: Shopping Cart Calculator
# Complete the TODOs below to build your shopping cart app.

# --- Step 1: Create the menu ---
# TODO: Create a dictionary called 'menu' with at least 5 food items and their prices


# --- Step 2: Display the menu ---
print("=== WELCOME TO PYTHON BITES ===\n")
print("--- Menu ---")
# TODO: Use a for loop to print each item and its price from the menu dictionary


# --- Step 3: Create an empty cart ---
# TODO: Create an empty list called 'cart'


# --- Step 4: Ordering loop ---
# TODO: Create a while loop that:
#   - Asks the user what they want to order (use input())
#   - If they type "done", break out of the loop
#   - If the item is in the menu, add it to the cart and print a confirmation
#   - If the item is NOT in the menu, print "Sorry, that's not on the menu."
#
# Hint: To check if something is in a dictionary, use: if item in menu:


# --- Step 5: Calculate the total ---
# TODO: Create a variable called 'total' set to 0
# TODO: Use a for loop to go through each item in the cart
#   - Look up the item's price in the menu dictionary: menu[item]
#   - Add it to total


# --- Step 6: Print the receipt ---
print("\n=== YOUR RECEIPT ===")
# TODO: Print the items ordered (just print the cart list)
# TODO: Print the total
print("Thank you for shopping at Python Bites!")


# --- STRETCH: Discount ---
# TODO: If total is over 5000, apply a 10% discount
#   - Calculate discount_amount = total * 10 / 100
#   - Subtract it from total
#   - Print the discount and new total


# --- BOSS: Quantity support ---
# TODO: After adding an item, ask "How many?" and add it that many times
#   - Hint: You can use a for loop inside the while loop:
#     for _ in range(quantity):
#         cart.append(item)
