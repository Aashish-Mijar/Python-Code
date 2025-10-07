"""
Features of Student management system
Add
Update
Delete
View
Exit
"""

# Initializing dictionary
student_grades = {}

# Add a new Student
def add_student(name, grade):
    student_grades[name] = grade
    print(f"Added {name} with a grade {grade}")

# Update a student
def update_student(name, grade):
    if name in student_grades:
        student_grades[name] = grade
        print("{name} with marks are updated {grade}")

    else:
        print(f"{name} is not found")

# Delete a student
def delete_student(name):
    if name in student_grades:
        del student_grades[name]
        print(f"{name} has been successfully deleted")

    else:
        print(f"{name} is not found!")
