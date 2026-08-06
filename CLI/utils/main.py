from filehandler import *
from input_validator import *
from numeric_validator import *
from string_sanitizer import *

while True:

    print("\n===== STUDENT RECORD MANAGER =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Update Student")
    print("4. Delete Student")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if not is_valid_choice(choice, 1, 5):
        print("Invalid choice.")
        continue

    choice = int(choice)

    if choice == 1:

        students = load_students()

        student_id = input("Enter Student ID: ")

        if not is_integer(student_id):
            print("Invalid Student ID")
            continue

        if not is_unique(int(student_id), students, "student_id"):
            print("Student ID already exists")
            continue

        name = capitalize_text(remove_spaces(input("Enter Name: ")))

        if is_empty(name) or not is_alpha(name):
            print("Invalid Name")
            continue

        age = input("Enter Age: ")

        if not is_integer(age):
            print("Invalid Age")
            continue

        gender = capitalize_text(remove_spaces(input("Enter Gender: ")))

        email = to_lowercase(remove_spaces(input("Enter Email: ")))

        if not is_valid_email(email):
            print("Invalid Email")
            continue

        phone = input("Enter Phone Number: ")

        if not is_phone_number(phone):
            print("Invalid Phone Number")
            continue

        percentage = input("Enter Percentage: ")

        if not is_float(percentage):
            print("Invalid Percentage")
            continue

        student = {
            "student_id": int(student_id),
            "name": name,
            "age": int(age),
            "gender": gender,
            "email": email,
            "phone_number": phone,
            "percentage": float(percentage)
        }

        add_student(student)
        print("Student added successfully.")

    elif choice == 2:

        view_students()

    elif choice == 3:

        student_id = input("Enter Student ID to update: ")

        if not is_integer(student_id):
            print("Invalid ID")
            continue

        updated_data = {
            "name": capitalize_text(remove_spaces(input("Enter New Name: "))),
            "age": int(input("Enter New Age: ")),
            "gender": capitalize_text(remove_spaces(input("Enter New Gender: "))),
            "email": to_lowercase(remove_spaces(input("Enter New Email: "))),
            "phone_number": input("Enter New Phone Number: "),
            "percentage": float(input("Enter New Percentage: "))
        }

        if update_student(int(student_id), updated_data):
            print("Student updated successfully.")
        else:
            print("Student not found.")

    elif choice == 4:

        student_id = input("Enter Student ID to delete: ")

        if not is_integer(student_id):
            print("Invalid ID")
            continue

        if delete_student(int(student_id)):
            print("Student deleted successfully.")
        else:
            print("Student not found.")

    elif choice == 5:

        print("Thank you!")
        break