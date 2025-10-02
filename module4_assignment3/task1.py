# Assignment 3
# Module 4: Functions in Python
# Task 1: Calculate Factorial Using a Function

# Step 1: Define a function to calculate factorial
def factorial(n):
    """Function to calculate factorial of a given number."""
    result = 1
    # Using a loop to multiply numbers from 1 to n
    for i in range(1, n + 1):
        result *= i
    return result

# Step 2: Call the function with a sample number
sample_number = 43
fact = factorial(sample_number)

# Step 3: Print the output
print(f"The factorial of {sample_number} is: {fact}")
