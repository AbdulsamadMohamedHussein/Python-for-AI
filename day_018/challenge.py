
# ==========================================
# DAY 018 - PYTHON CODING CHALLENGE
# Project: Student Management System
# Topic: Python Dictionaries
# ==========================================


students = {}


# 1. Add a Student

def add_student():
    print("\n--- ADD NEW STUDENT ---")

    student_id = input("Enter Student ID: ")

    if student_id in students:
        print("Student ID already exists!")
        return

    name = input("Enter Student Name: ")

    try:
        age = int(input("Enter Student Age: "))
        marks = float(input("Enter Student Marks: "))

        if age <= 0 or not 0 <= marks <= 100:
            print("Invalid age or marks!")
            return

    except ValueError:
        print("Please enter valid numbers!")
        return

    students[student_id] = {
        "name": name,
        "age": age,
        "marks": marks
    }

    print("Student added successfully!")


# 2. View All Students

def view_students():
    print("\n--- ALL STUDENTS ---")

    if not students:
        print("No students found!")
        return

    for student_id, details in students.items():
        print("\nStudent ID:", student_id)
        print("Name:", details["name"])
        print("Age:", details["age"])
        print("Marks:", details["marks"])


# 3. Search for a Student

def search_student():
    print("\n--- SEARCH STUDENT ---")

    student_id = input("Enter Student ID: ")

    if student_id in students:
        student = students[student_id]

        print("Student Found!")
        print("Name:", student["name"])
        print("Age:", student["age"])
        print("Marks:", student["marks"])

    else:
        print("Student not found!")


# 4. Update Student Marks

def update_marks():
    print("\n--- UPDATE MARKS ---")

    student_id = input("Enter Student ID: ")

    if student_id in students:

        try:
            marks = float(input("Enter New Marks: "))

            if not 0 <= marks <= 100:
                print("Marks must be between 0 and 100!")
                return

            students[student_id]["marks"] = marks

            print("Marks updated successfully!")

        except ValueError:
            print("Please enter valid marks!")

    else:
        print("Student not found!")


# 5. Delete a Student

def delete_student():
    print("\n--- DELETE STUDENT ---")

    student_id = input("Enter Student ID: ")

    if student_id in students:
        del students[student_id]
        print("Student deleted successfully!")

    else:
        print("Student not found!")


# 6. Calculate Average Marks

def calculate_average():
    print("\n--- AVERAGE MARKS ---")

    if not students:
        print("No student records available!")
        return

    total = sum(
        student["marks"]
        for student in students.values()
    )

    average = total / len(students)

    print("Total Students:", len(students))
    print("Average Marks:", round(average, 2))


# 7. Find Top Student

def top_student():
    print("\n--- TOP STUDENT ---")

    if not students:
        print("No student records available!")
        return

    top = max(
        students.items(),
        key=lambda item: item[1]["marks"]
    )

    print("Top Student:", top[1]["name"])
    print("Student ID:", top[0])
    print("Marks:", top[1]["marks"])


# ==========================================
# MAIN MENU
# ==========================================

while True:

    print("\n================================")
    print("   STUDENT MANAGEMENT SYSTEM")
    print("================================")

    print("1. Add Student")
    print("2. View All Students")
    print("3. Search Student")
    print("4. Update Student Marks")
    print("5. Delete Student")
    print("6. Calculate Average Marks")
    print("7. Find Top Student")
    print("8. Exit")

    choice = input("\nEnter Your Choice (1-8): ")

    if choice == "1":
        add_student()

    elif choice == "2":
        view_students()

    elif choice == "3":
        search_student()

    elif choice == "4":
        update_marks()

    elif choice == "5":
        delete_student()

    elif choice == "6":
        calculate_average()

    elif choice == "7":
        top_student()

    elif choice == "8":
        print("\nThank you for using the system!")
        print("Day 018 Challenge Completed!")
        break

    else:
        print("Invalid choice! Please try again.")


# ==========================================
# END OF DAY 018 CHALLENGE
# ==========================================
