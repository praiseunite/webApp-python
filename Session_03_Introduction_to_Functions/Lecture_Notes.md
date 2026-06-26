# Session 3: Introduction to Functions

## Objective & Real-World Application
Imagine you are building a calculator app. You need to add numbers in 50 different places in your code. Instead of writing `a + b` 50 times, wouldn't it be easier to write a single block of code that handles addition and just "call" it whenever you need it? That's what **Functions** do! They make code reusable, organized, and easier to read.

## 1. What is a Function?
A function is a block of code that only runs when it is called. You can pass data into a function, and it can return data back to you.

Think of a function like a factory machine:
![Function Machine Diagram](C:/Users/DELL/.gemini/antigravity/brain/87afa76e-c759-4c10-9bf7-7612a5d99632/python_function_machine_1782468192342.png)
*(Inputs go in ➔ The Function processes them ➔ The Output comes out)*

### Types of Functions:
1. **Built-in Functions:** Functions provided by Python (e.g., `print()`, `input()`, `type()`, `len()`).
2. **User-Defined Functions:** Functions you create yourself to perform specific tasks.

## 2. Creating and Calling a Function

To create a function, use the `def` keyword (short for define).

```python
# 1. Defining the function
def say_hello():
    print("Hello from inside the function!")
    print("Welcome to Python Course.")

# 2. Calling the function
say_hello()
```
*Note: The code inside the function will NOT run until you call it!*

## 3. Parameters and Arguments

Remember the factory machine? Parameters and arguments are how we pass raw materials (data) into the machine.

- **Parameter:** The variable listed inside the parentheses in the function definition.
- **Argument:** The actual value that is sent to the function when it is called.

```python
# 'name' is the parameter
def greet_user(name):
    print("Hello", name)

# "Alice" and "Bob" are the arguments
greet_user("Alice")
greet_user("Bob")
```

### Multiple Arguments
You can pass multiple arguments by separating them with a comma.
```python
def add_numbers(num1, num2):
    total = num1 + num2
    return total  # The 'return' statement sends the result back

# We store the returned value in a variable
result = add_numbers(5, 10)
print("The sum is:", result)
```

## 4. Variables and Scope

Where you create a variable matters! This is called **Scope**.
- **Local Scope:** Variables created *inside* a function can only be used *inside* that function.
- **Global Scope:** Variables created *outside* any function can be used anywhere.

```python
global_var = "I am everywhere"

def my_function():
    local_var = "I only exist here"
    print(global_var) # This works!
    print(local_var)  # This works!

my_function()
# print(local_var) # Error! local_var doesn't exist outside the function
```

---

## 📺 Further Reading & Video Suggestions
To cement your understanding, check out these excellent YouTube resources:
- **"Python Tutorial for Beginners - Functions"** by Programming with Mosh
- **"Python Tutorial: Functions"** by Corey Schafer
- **"Python Functions | Python Tutorial for Absolute Beginners"** by CS Dojo
