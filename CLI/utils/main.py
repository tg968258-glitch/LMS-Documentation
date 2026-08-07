from filehandler import *
from input_validator import *
from numeric_validator import *
from string_sanitizer import *

while True:
    print("\n========== LEARNING MANAGEMENT SYSTEM ==========")
    print("------- STUDENT RECORD MANAGER --------")
    print("1. Add Student")
    print("2. View Students")
    print("3. Update Student")
    print("4. Delete Student")
    print("5. Search Student")
   

    print("\n--------------- Course Manager ----------------")
    print("6. Add Course")
    print("7. View Courses")
    print("8. Update Course")
    print("9. Delete Course")
    print("10. Search Course")

    print("\n------------ Enrollment--------------")
    print("11. Enroll Student")
    print("12. View Enrollments")
    print("\n13. Exit")

    choice = input("Enter your choice: ")

    if not is_valid_choice(choice, 1, 13):
        print("Invalid choice.")
        continue

    choice = int(choice)

    if choice == 1:

        students = load_students()

        student_id = generate_student_id()

        print(f"Generated Student ID: {student_id}")

        name = capitalize_text(remove_spaces(input("Enter Name: ")))

        if is_empty(name) or not is_alpha(name):
            print("Invalid Name")
            continue

        age = input("Enter Age: ")

        

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
            "student_id": student_id,
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

      student_id = input("Enter Student ID: ")

      if not is_integer(student_id):
        print("Invalid Student ID")
        continue

      student = search_student (int(student_id))

      if student:
        print("\nStudent Found")
        print(f"ID         : {student['student_id']}")
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

        course_name = capitalize_text(remove_spaces(input("Enter Course Name: ")))

        trainer = capitalize_text(remove_spaces(input("Enter Trainer Name: ")))

        duration = remove_spaces(input("Enter Duration: "))

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

        course_id = input("Enter Course ID to update: ")

        if not is_integer(course_id):
            print("Invalid Course ID")
            continue

        updated_data = {
            "course_name": capitalize_text(remove_spaces(input("Enter New Course Name: "))),
            "trainer": capitalize_text(remove_spaces(input("Enter New Trainer Name: "))),
            "duration": remove_spaces(input("Enter New Duration: "))
        }

        if update_course(int(course_id), updated_data):
            print("Course updated successfully.")
        else:
            print("Course not found.")


    elif choice == 9:

        course_id = input("Enter Course ID to delete: ")

        if not is_integer(course_id):
            print("Invalid Course ID")
            continue

        if delete_course(int(course_id)):
            print("Course deleted successfully.")
        else:
            print("Course not found.")


    elif choice == 10:

        course_id = input("Enter Course ID: ")

        if not is_integer(course_id):
            print("Invalid Course ID")
            continue

        course = search_course(int(course_id))

        if course:
            print("\nCourse Found")
            print(f"Course ID   : {course['course_id']}")
            print(f"Course Name : {course['course_name']}")
            print(f"Trainer     : {course['trainer']}")
            print(f"Duration    : {course['duration']}")
        else:
            print("Course not found.")

    elif choice == 11:

        student_id = input("Enter Student ID: ")
        course_id = input("Enter Course ID: ")

        if not is_integer(student_id) or not is_integer(course_id):
            print("Invalid ID")
            continue

        message = enroll_student(int(student_id), int(course_id))
        print(message)



    elif choice == 12:

     view_enrollments()


    elif choice == 13:

        print("Thank you for using LMS!")
        break




