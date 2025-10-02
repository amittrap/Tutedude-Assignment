# Assignment 3
# Module 4: Functions in Python
# Task 2: Using the Math Module for Calculations

import math   # Importing the math module

# Step 1: Ask the user for a number as input
num = float(input("Enter a number: "))

# Step 2: Perform calculations using math module

# Square root
sqrt_value = math.sqrt(num)

# Natural logarithm (log base e)
# log is only valid for positive numbers
if num > 0:
    log_value = math.log(num)
else:
    log_value = "Undefined (logarithm not defined for zero or negative numbers)"

# Sine of the number (in radians)
sine_value = math.sin(num)

# Step 3: Display the results
print(f"\nResults for number {num}:")
print(f"Square Root: {sqrt_value}")
print(f"Natural Logarithm (base e): {log_value}")
print(f"Sine (in radians): {sine_value}")
