
# Student Management System

students = []

def add_student(student_id, name, marks):
    if student_id <= 0:
        raise ValueError("Student ID must be positive")

    if not name:
        raise ValueError("Student name cannot be empty")

    if marks < 0 or marks > 100:
        raise ValueError("Marks must be between 0 and 100")

    student = {
        "id": student_id,
        "name": name,
        "marks": marks
    }

    students.append(student)
    return "Student added successfully"


def view_students():
    return students


def search_student(student_id):
    for student in students:
        if student["id"] == student_id:
            return student
    return None


def delete_student(student_id):
    student = search_student(student_id)

    if student:
        students.remove(student)
        return "Student deleted successfully"

    return "Student not found"


if __name__ == "__main__":
    while True:
        print("\n--- Student Management System ---")
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Delete Student")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            sid = int(input("Enter Student ID: "))
            name = input("Enter Student Name: ")
            marks = float(input("Enter Marks: "))
            print(add_student(sid, name, marks))

        elif choice == "2":
            print(view_students())

        elif choice == "3":
            sid = int(input("Enter Student ID: "))
            print(search_student(sid))

        elif choice == "4":
            sid = int(input("Enter Student ID: "))
            print(delete_student(sid))

        elif choice == "5":
            print("Thank you!")
            break

        else:
            print("Invalid choice")
