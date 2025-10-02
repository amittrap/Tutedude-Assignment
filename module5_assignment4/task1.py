def read_file(filename):
    try:
        with open(filename, 'r') as file:
            print("File contents:\n")
            for line in file:
                print(line.strip())  # Remove trailing newline for cleaner output
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Call the function with the filename
read_file("sample.txt")
