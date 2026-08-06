import json

file_name = "students.json"


def load_students():
   
    try:
        with open(file_name, "r") as file:
            students = json.load(file)
        return students

    except FileNotFoundError:
        return []

    except json.JSONDecodeError:
        return []


def save_students(students):
   
    try:
        with open(file_name, "w") as file:
            json.dump(students, file, indent=4)

    except Exception as e:
        print(f"Error saving students: {e}")


def add_student(new_student):
    
    students = load_students()

    students.append(new_student)

    save_students(students)


def view_students():
   
    students = load_students()

    if not students:
        print("No students found.")
        return

    for student in students:
        print(f"ID         : {student['student_id']}")
        print(f"Name       : {student['name']}")
        print(f"Age        : {student['age']}")
        print(f"Gender     : {student['gender']}")
        print(f"Email      : {student['email']}")
        print(f"Phone      : {student['phone_number']}")
        print(f"Percentage : {student['percentage']}")
       


def update_student(student_id, updated_data):
    
    students = load_students()

    for student in students:
        if student["student_id"] == student_id:
            student.update(updated_data)
            save_students(students)
            return True

    return False


def delete_student(student_id):
   
    students = load_students()

    for student in students:
        if student["student_id"] == student_id:
            students.remove(student)
            save_students(students)
            return True

    return False