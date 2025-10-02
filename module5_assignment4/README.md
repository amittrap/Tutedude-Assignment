# Module 5: Files, Exceptions, and Errors in Python

## 📝 Overview

This module covers basic file operations and error handling in Python. The two main tasks involve:

1. Reading a file and handling file-not-found errors.
2. Writing, appending, and displaying file content using user input.

---

## ✅ Task 1: Read a File and Handle Errors

### 📌 Problem Statement
Write a Python program that:
- Opens and reads a text file named `sample.txt`.
- Prints its content line by line.
- Handles the case where the file does not exist.

### 🧾 Example Code
```python
def read_file(filename):
    try:
        with open(filename, 'r') as file:
            print("File contents:\n")
            for line in file:
                print(line.strip())
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Call the function
read_file("sample.txt")

Here is a `README.md` file **specifically for Task 2** — *"Write and Append Data to a File"*.

---




Task 2: Write and Append Data to a File


Write a Python program that:

1. Takes user input and writes it to a file named `output.txt`.
2. Appends additional user input to the same file.
3. Reads and displays the final content of the file.

---

## 🧾 Python Code

```python
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
````

---

## 💡 How It Works

* The program first takes user input and **writes** it to `output.txt`.
* Then, it takes another user input and **appends** it to the same file.
* Finally, it **reads** the file and displays its full content.

---

## 🖥️ Sample Run

```
Enter text to write to the file: Hello, Python!
Data successfully written to output.txt.

Enter additional text to append: Learning file handling in Python.
Data successfully appended.

Final content of output.txt:
Hello, Python!
Learning file handling in Python.
```

---

## 📂 Output File

* **Filename**: `output.txt`
* **Purpose**: Stores the written and appended user input.
* **Location**: Same directory as the Python script.

---

## ⚠️ Error Handling

* The code includes `try-except` blocks for:

  * Writing to the file
  * Appending to the file
  * Reading the file
* This ensures that any runtime errors (like permission issues or file access problems) are caught and reported clearly.

---


```


