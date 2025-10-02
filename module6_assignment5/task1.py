def student_marks_lookup():
    # Step 1: Create dictionary with student names and marks
    student_marks = {
        "Alice": 85,
        "Bob": 78,
        "Charlie": 92,
        "Diana": 88,
        "Ethan": 76
    }

    # Step 2: Ask user to input a student's name
    name = input("Enter the student's name: ")

    # Step 3 & 4: Retrieve and display marks or show 'not found' message
    if name in student_marks:
        print(f"{name}'s marks: {student_marks[name]}")
    else:
        print(f"Student '{name}' not found in the record.")

# Run the function
student_marks_lookup()
