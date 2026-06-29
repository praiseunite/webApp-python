# Assignment: Shopping Cart Calculator

## What You'll Build
A command-line shopping app where users browse a menu, add items to their cart, and get a total with optional discounts. This assignment has **3 difficulty levels** — complete as many as you can!

---

## Base Level (Everyone should complete this)

Open `assignment_starter.py` and follow the TODOs to build a basic shopping cart:

1. **Create a menu dictionary** with at least 5 items and their prices:
   ```python
   menu = {
       "Burger": 1500,
       "Fries": 500,
       "Drink": 400,
       "Ice Cream": 600,
       "Shawarma": 2000
   }
   ```

2. **Display the menu** using a `for` loop that prints each item and its price neatly.

3. **Create an empty list** called `cart` to store what the user orders.

4. **Use a `while` loop** to keep asking the user what they want to order:
   - If they type `"done"`, stop the loop with `break`
   - If the item exists in the menu, add it to the `cart` list and print a confirmation
   - If the item doesn't exist, print `"Sorry, that's not on the menu."`

5. **Calculate and print the total:**
   - Loop through the `cart` list
   - Look up each item's price in the `menu` dictionary
   - Add them all together
   - Print the total

### Expected Output (Base Level)
```
=== WELCOME TO PYTHON BITES ===

--- Menu ---
  Burger - N1500
  Fries - N500
  Drink - N400
  Ice Cream - N600
  Shawarma - N2000

What would you like? (type 'done' to finish): Burger
Added Burger to your cart!

What would you like? (type 'done' to finish): Drink
Added Drink to your cart!

What would you like? (type 'done' to finish): Pizza
Sorry, that's not on the menu.

What would you like? (type 'done' to finish): Fries
Added Fries to your cart!

What would you like? (type 'done' to finish): done

=== YOUR RECEIPT ===
Items ordered: ['Burger', 'Drink', 'Fries']
Total: N2400
Thank you for shopping at Python Bites!
```

---

## Stretch Level (Push yourself!)

Add these features after completing the Base Level:

1. **Show item count:** If the user adds the same item twice, show how many of each item they ordered.
   - Hint: Use `cart.count("Burger")` to count how many times "Burger" appears.

2. **Apply a discount:** If the total is over N5000, give a 10% discount. Use an `if` statement to check and calculate the discounted total.

3. **Show a numbered receipt** like this:
   ```
   === YOUR RECEIPT ===
   1. Burger       - N1500
   2. Drink        - N400
   3. Fries        - N500
   -----------------------
   Subtotal:         N2400
   Discount (10%):  -N0
   TOTAL:            N2400
   ```

---

## Boss Level (For the brave!)

Add one or more of these advanced features:

1. **Ask for quantity:** Instead of adding one item at a time, ask "How many?" after each item and calculate the cost accordingly.

2. **Category filtering:** Organize the menu into categories using a dictionary of dictionaries:
   ```python
   menu = {
       "Food": {"Burger": 1500, "Shawarma": 2000, "Fries": 500},
       "Drinks": {"Coke": 400, "Water": 200, "Juice": 600}
   }
   ```
   Let the user pick a category first, then pick an item.

3. **Save the receipt:** Write the final receipt to a text file called `receipt.txt` using `open()` and `.write()` (preview of Session 6!).

---

## Submission
Complete your work in `assignment_starter.py` and be ready to walk through your code in the next session.
