# Session 2: Programming Language Construct

## 1. Data Types in Python
In Python, every value has a specific "type".

### Core Data Types:
1. **Numeric Types:**
   - **Integer (`int`):** Whole numbers (e.g., `10`, `-5`, `0`).
   - **Float (`float`):** Decimal numbers (e.g., `3.14`).
2. **Text Type (`str`):** Strings of characters (e.g., `"Hello"`).
3. **Boolean Type (`bool`):** Represents `True` or `False`.

### Collection Data Types (Preview):
- **List (`list`):** An ordered, changeable collection `[1, 2, "apple"]`.
- **Tuple (`tuple`):** An ordered, unchangeable collection `(1, 2, "apple")`.
- **Dictionary (`dict`):** A collection of key-value pairs `{"name": "Alice", "age": 25}`.

## 2. Python Operators
### Arithmetic Operators
- `+` (Addition), `-` (Subtraction), `*` (Multiplication), `/` (Division)
- `%` (Modulus/Remainder): `10 % 3` results in `1`

### Comparison (Relational) Operators
- `==` (Equal to), `!=` (Not equal)
- `>`, `<`, `>=`, `<=`

### Logical Operators
- `and`: Returns `True` if BOTH statements are true.
- `or`: Returns `True` if ONE statement is true.
- `not`: Reverses the result.

## 3. Control Flow Statements

### Conditional Statements (`if`, `elif`, `else`)
```python
weather = "rainy"
if weather == "sunny":
    print("Let's go to the park!")
elif weather == "rainy":
    print("Take an umbrella!")
else:
    print("Stay inside just in case.")
```

### Looping Statements (`for` and `while`)

**The `for` loop:**
```python
for i in range(5):
    print("Iteration number:", i)
```

**The `while` loop:**
```python
count = 3
while count > 0:
    print("Countdown:", count)
    count = count - 1
print("Blastoff!")
```
