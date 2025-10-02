# Assignment 2
# Module 3: Control Structures in Python
# Task 1: Check if a Number is Even or Odd

# Step 1: Take an integer input from the user
num = int(input("Enter an integer: "))

# Step 2: Check if the number is even or odd using if-else
if num % 2 == 0:
    # If remainder is 0 when divided by 2, it is even
    print(f"\nThe number {num} is Even.")
else:
    # Otherwise, it is odd
    print(f"\nThe number {num} is Odd.")
