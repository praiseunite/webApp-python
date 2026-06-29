# math_helpers.py — A reusable math utilities module

def calculate_average(numbers):
    return sum(numbers) / len(numbers)


def find_max(numbers):
    largest = numbers[0]
    for num in numbers:
        if num > largest:
            largest = num
    return largest


def is_even(number):
    return number % 2 == 0


def percentage(part, whole):
    return (part / whole) * 100


def countdown(n):
    if n == 0:
        print("GO!")
        return
    print(n, "...")
    countdown(n - 1)
