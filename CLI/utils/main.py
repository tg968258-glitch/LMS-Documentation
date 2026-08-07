from filehandler import *
from input_validator import *
from numeric_validator import *
from string_sanitizer import *
import questionary


while True:

    print("\n========== LEARNING MANAGEMENT SYSTEM ==========")
    print("------- STUDENT RECORD MANAGER --------")
    choice = questionary.select(
    "Select an option:",
    choices=[
        
        "1. Add Student",
        "2. View Students",
        "3. Update Student",
        "4. Delete Student",
        "5. Search Student",
        "6. Add Course",
        "7. View Courses",
        "8. Update Course",
        "9. Delete Course",
        "10. Search Course",
        "11. Enroll Student",
        "12. View Enrollments",
        "13. Exit"
    ]
).ask()
    

    choice = input("Enter your choice: ")

    if not is_valid_choice(choice, 1, 13):
        print("Invalid choice.")
        continue

    choice = int(choice)

    # ---------------- ADD STUDENT ----------------
    if choice == 1:

        student_id = generate_student_id()
        print(f"Generated Student ID: {student_id}")

        # Name
        while True:
            name = capitalize_text(remove_spaces(input("Enter Name: ")))

            if not is_empty(name) and is_alpha(name):
                break

            print("Invalid Name! Please enter alphabets only.")

        # Age
        while True:
            age = input("Enter Age: ")

            if is_integer(age):
                age = int(age)
                break

            print("Invalid Age! Please enter a valid integer.")

        # Gender
        while True:
            gender = capitalize_text(remove_spaces(input("Enter Gender: ")))

            if gender in ["Male", "Female", "Other"]:
                break

            print("Invalid Gender! Enter Male, Female or Other.")

        # Email
        while True:
            email = to_lowercase(remove_spaces(input("Enter Email: ")))

            if is_valid_email(email):
                break

            print("Invalid Email!")

        # Phone Number
        while True:
            phone = input("Enter Phone Number: ")

            if is_phone_number(phone):
                break

            print("Invalid Phone Number!")

        # Percentage
        while True:
            percentage = input("Enter Percentage: ")

            if is_float(percentage) and in_range(percentage, 0, 100):
                percentage = float(percentage)
                break

            print("Invalid Percentage! Enter between 0 and 100.")

        student = {
            "student_id": student_id,
            "name": name,
            "age": age,
            "gender": gender,
            "email": email,
            "phone_number": phone,
            "percentage": percentage
        }

        add_student(student)
        print("Student added successfully.")

    # ---------------- VIEW STUDENT ----------------
    elif choice == 2:

        view_students()

    elif choice == 3:

        # Student ID
        while True:
            student_id = input("Enter Student ID to update: ")

            if is_integer(student_id):
                student_id = int(student_id)

                if search_student(student_id):
                    break
                else:
                    print("Student not found.")

            else:
                print("Invalid Student ID! Please enter a valid integer.")

        # Name
        while True:
            name = capitalize_text(remove_spaces(input("Enter New Name: ")))

            if not is_empty(name) and is_alpha(name):
                break

            print("Invalid Name! Enter alphabets only.")

        # Age
        while True:
            age = input("Enter New Age: ")

            if is_integer(age) and is_positive(age):
                age = int(age)
                break

            print("Invalid Age! Please enter a positive integer.")

        # Gender
        while True:
            gender = capitalize_text(remove_spaces(input("Enter New Gender (Male/Female/Other): ")))

            if gender in ["Male", "Female", "Other"]:
                break

            print("Invalid Gender! Enter Male, Female or Other.")

        # Email
        while True:
            email = to_lowercase(remove_spaces(input("Enter New Email: ")))

            if is_valid_email(email):
                break

            print("Invalid Email!")

        # Phone
        while True:
            phone = input("Enter New Phone Number: ")

            if is_phone_number(phone):
                break

            print("Invalid Phone Number! Enter 10 digits.")

        # Percentage
        while True:
            percentage = input("Enter New Percentage: ")

            if is_float(percentage) and in_range(percentage, 0, 100):
                percentage = float(percentage)
                break

            print("Invalid Percentage! Enter value between 0 and 100.")

        updated_data = {
            "name": name,
            "age": age,
            "gender": gender,
            "email": email,
            "phone_number": phone,
            "percentage": percentage
        }

        update_student(student_id, updated_data)
        print("Student updated successfully.")

    elif choice == 4:

        while True:
            student_id = input("Enter Student ID to delete: ")

            if is_integer(student_id):
                student_id = int(student_id)
                break

            print("Invalid Student ID! Please enter a valid integer.")

        if delete_student(student_id):
            print("Student deleted successfully.")
        else:
            print("Student not found.")

    elif choice == 5:

        while True:
            student_id = input("Enter Student ID: ")

            if is_integer(student_id):
                student_id = int(student_id)
                break

            print("Invalid Student ID! Please enter a valid integer.")

        student = search_student(student_id)

        if student:
            print("\n========== STUDENT FOUND ==========")
            print(f"Student ID : {student['student_id']}")
            print(f"Name       : {student['name']}")
            print(f"Age        : {student['age']}")
            print(f"Gender     : {student['gender']}")
            print(f"Email      : {student['email']}")
            print(f"Phone      : {student['phone_number']}")
            print(f"Percentage : {student['percentage']}")
        else:
            print("Student not found.")

    elif choice == 6:

        course_id = generate_course_id()
        print(f"Generated Course ID: {course_id}")

        # Course Name
        while True:
            course_name = capitalize_text(remove_spaces(input("Enter Course Name: ")))

            if (not is_empty(course_name)
                    and is_alpha(course_name)
                    and validate_length(course_name)):
                break

            print("Invalid Course Name! Enter alphabets only.")

        # Trainer Name
        while True:
            trainer = capitalize_text(remove_spaces(input("Enter Trainer Name: ")))

            if (not is_empty(trainer)
                    and is_alpha(trainer)
                    and validate_length(trainer)):
                break

            print("Invalid Trainer Name! Enter alphabets only.")

        # Duration
        while True:
            duration = input("Enter Duration (Days): ")

            if is_integer(duration) and is_positive(duration):
                duration = f"{duration} Days"
                break

            print("Invalid Duration! Enter a positive number.")

        course = {
            "course_id": course_id,
            "course_name": course_name,
            "trainer": trainer,
            "duration": duration
        }

        add_course(course)
        print("Course added successfully.")

    elif choice == 7:

        view_courses()

    elif choice == 8:

        # Course ID
        while True:
            course_id = input("Enter Course ID to update: ")

            if is_integer(course_id):
                course_id = int(course_id)

                if search_course(course_id):
                    break

                print("Course not found.")
            else:
                print("Invalid Course ID!")

        # Course Name
        while True:
            course_name = capitalize_text(remove_spaces(input("Enter New Course Name: ")))

            if (not is_empty(course_name)
                    and is_alpha(course_name)
                    and validate_length(course_name)):
                break

            print("Invalid Course Name!")

        # Trainer Name
        while True:
            trainer = capitalize_text(remove_spaces(input("Enter New Trainer Name: ")))

            if (not is_empty(trainer)
                    and is_alpha(trainer)
                    and validate_length(trainer)):
                break

            print("Invalid Trainer Name!")

        # Duration
        while True:
            duration = input("Enter New Duration (Days): ")

            if is_integer(duration) and is_positive(duration):
                duration = f"{duration} Days"
                break

            print("Invalid Duration!")

        updated_data = {
            "course_name": course_name,
            "trainer": trainer,
            "duration": duration
        }

        update_course(course_id, updated_data)
        print("Course updated successfully.")

    elif choice == 9:

        while True:
            course_id = input("Enter Course ID to delete: ")

            if is_integer(course_id):
                course_id = int(course_id)
                break

            print("Invalid Course ID!")

        if delete_course(course_id):
            print("Course deleted successfully.")
        else:
            print("Course not found.")

    elif choice == 10:

        while True:
            course_id = input("Enter Course ID: ")

            if is_integer(course_id):
                course_id = int(course_id)
                break

            print("Invalid Course ID!")

        course = search_course(course_id)

        if course:
            print("\n========== COURSE FOUND ==========")
            print(f"Course ID   : {course['course_id']}")
            print(f"Course Name : {course['course_name']}")
            print(f"Trainer     : {course['trainer']}")
            print(f"Duration    : {course['duration']}")
        else:
            print("Course not found.")

    elif choice == 11:

        # Student ID
        while True:
            student_id = input("Enter Student ID: ")

            if is_integer(student_id):
                student_id = int(student_id)

                if search_student(student_id):
                    break

                print("Student ID does not exist.")
            else:
                print("Invalid Student ID! Please enter a valid integer.")

        # Course ID
        while True:
            course_id = input("Enter Course ID: ")

            if is_integer(course_id):
                course_id = int(course_id)

                if search_course(course_id):
                    break

                print("Course ID does not exist.")
            else:
                print("Invalid Course ID! Please enter a valid integer.")

        message = enroll_student(student_id, course_id)
        print(message)

    elif choice == 12:

        view_enrollments()

    elif choice == 13:

        print("\n========================================")
        print(" Thank you for using Learning Management System ")
        print("========================================")
        break