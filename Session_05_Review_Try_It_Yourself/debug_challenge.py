# DEBUG CHALLENGE: Find and fix the 6 bugs!
# This program calculates the total price of items in a cart
# with a 10% discount if the total is over 5000.

# BUG 1: "Burger" uses = instead of :
menu = {
    "Burger" = 1500,
    "Fries": 500,
    "Drink": 400,
}

cart = ["Burger", "Fries", "Drink", "Fries"]

total = 0
# BUG 2: Missing colon at end of for line
for item in cart
    # BUG 3: Dictionaries use [] not ()
    price = menu(item)
    total = total + price

# BUG 4: Can't concatenate string + integer with +
print("Subtotal: N" + total)

if total >= 5000:
    discount = total * 10 / 100
    total = total - discount
    print("Discount applied!")

print(f"Total: N{total}")

# BUG 5: Missing colon after function definition
# BUG 6: Function defined but never called (and placed after it's needed)
def apply_discount(amount, percent)
    discounted = amount - (amount * percent / 100)
    return discounted
