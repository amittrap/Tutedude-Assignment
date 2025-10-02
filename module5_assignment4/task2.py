def write_and_append_to_file():
    filename = "output.txt"

    # Step 1: Write to the file
    user_input = input("Enter text to write to the file: ")
    try:
        with open(filename, 'w') as file:
            file.write(user_input + '\n')
        print("Data successfully written to output.txt.")
    except Exception as e:
        print(f"Error writing to file: {e}")
        return

    # Step 2: Append to the file
    additional_input = input("Enter additional text to append: ")
    try:
        with open(filename, 'a') as file:
            file.write(additional_input + '\n')
        print("Data successfully appended.")
    except Exception as e:
        print(f"Error appending to file: {e}")
        return

    # Step 3: Read and display final content
    try:
        print("\nFinal content of output.txt:")
        with open(filename, 'r') as file:
            content = file.read()
            print(content)
    except Exception as e:
        print(f"Error reading the file: {e}")

# Run the function
write_and_append_to_file()
