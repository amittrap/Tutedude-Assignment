# Assignment 1
# Module 2: Basic Python Concepts
# Task 1: Perform Basic Mathematical Operations

# Step 1: Take two numbers as input from the user
# Using float() so that the program can also handle decimal values
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Step 2: Perform basic mathematical operations
# Addition
addition = num1 + num2

# Subtraction
subtraction = num1 - num2

# Multiplication
multiplication = num1 * num2

# Division (check to avoid dividing by zero)
if num2 != 0:
    division = num1 / num2
else:
    division = "Undefined (cannot divide by zero)"

# Step 3: Display the results
# f-strings are used for clear and formatted output
print("\nResults of Mathematical Operations:")
print(f"Addition: {num1} + {num2} = {addition}")
print(f"Subtraction: {num1} - {num2} = {subtraction}")
print(f"Multiplication: {num1} * {num2} = {multiplication}")
print(f"Division: {num1} / {num2} = {division}")
