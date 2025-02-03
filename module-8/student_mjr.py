import json

# Define the file name
filename = 'student.json'

# Function to load the JSON data into a Python list
def load_students(file):
    with open(file, 'r') as f:
        return json.load(f)

# Function to print the student list in the desired format
def print_student_list(student_list, message):
    print(message)
    for student in student_list:
        # Format: LastName, FirstName : ID,
        print(f"{student['L_Name']}, {student['F_Name']} : ID = {student['Student_ID']} , Email = {student['Email']}")
    print()  # blank line for spacing

# Load the students list from the JSON file
students = load_students(filename)

# Notify and print the original student list
print_student_list(students, "Original Student List:")

# Append a new student record 
new_student = {
    "F_Name": "Malachi",             # First name
    "L_Name": "Roker",               # Last name
    "Student_ID": 54832,             # Fictional ID
    "Email": "mjrok10@gmail.com"     # Email
}
students.append(new_student)

# Notify and print the updated student list
print_student_list(students, "Updated Student List:")

# Write (dump) the updated student list back to the JSON file
with open(filename, 'w') as f:
    json.dump(students, f, indent=4)

# Output notification to the user that the .json file was updated.
print("The JSON file was updated with the new student data.")