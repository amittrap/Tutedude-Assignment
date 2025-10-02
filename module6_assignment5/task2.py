def list_slicing_demo():
    # Step 1: Create a list of numbers from 1 to 10
    numbers = list(range(1, 11))

    # Step 2: Extract the first five elements
    first_five = numbers[:5]

    # Step 3: Reverse the extracted list
    reversed_five = first_five[::-1]

    # Step 4: Print both lists
    print("Original list:", numbers)
    print("First five elements:", first_five)
    print("Reversed first five elements:", reversed_five)

# Run the function
list_slicing_demo()
