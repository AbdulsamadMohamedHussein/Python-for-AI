
# =====================================================================
# DAY 016 - PYTHON TUPLES CHALLENGE
#
# PROJECT:
# STUDENT RECORDS AND ACADEMIC PERFORMANCE SYSTEM
#
# Bachelor's in Artificial Intelligence
# 90-Day Python Programming Journey
#
# MAIN CONCEPT:
# PYTHON TUPLES
#
# CONCEPTS USED:
# 1. Tuples
# 2. Nested Tuples
# 3. Tuple Indexing
# 4. Tuple Unpacking
# 5. Tuple Immutability
# 6. Lists and Tuples Together
# 7. Functions
# 8. For Loops
# 9. While Loops
# 10. Conditional Statements
# 11. Searching
# 12. Sorting
# 13. Statistics
# 14. Mathematical Calculations
#
# =====================================================================


# =====================================================================
# SECTION 1: INITIAL STUDENT DATABASE
# =====================================================================

# Each student record is a tuple.
#
# Structure:
#
# (Student ID, Name, Mathematics, Science, Python)
#
# Tuples are immutable.
#
# We use a list to hold the records because
# the database needs to support adding and deleting records.
#
# Individual student records remain tuples.

students = [

    (101, "Ali", 85, 90, 95),

    (102, "Ahmed", 75, 80, 85),

    (103, "John", 92, 88, 96),

    (104, "David", 65, 70, 75),

    (105, "Michael", 88, 85, 90)

]


# =====================================================================
# SECTION 2: WELCOME SCREEN
# =====================================================================

def welcome():

    print("\n")

    print("=" * 70)

    print("       STUDENT RECORDS AND ACADEMIC PERFORMANCE SYSTEM")

    print("=" * 70)

    print("Welcome to our Python Tuples Project!")

    print("Manage student records and analyse academic performance.")

    print("=" * 70)


# =====================================================================
# SECTION 3: MAIN MENU
# =====================================================================

def display_menu():

    print("\n" + "=" * 65)

    print("                       MAIN MENU")

    print("=" * 65)

    print("1. Add New Student")

    print("2. Display All Students")

    print("3. Search Student")

    print("4. Update Student Marks")

    print("5. Delete Student")

    print("6. Calculate Student Average")

    print("7. Display Subject Averages")

    print("8. Find Top Student")

    print("9. Rank Students")

    print("10. Generate Complete Academic Report")

    print("11. Display Database Statistics")

    print("12. Exit Application")

    print("=" * 65)


# =====================================================================
# SECTION 4: VALIDATE INTEGER INPUT
# =====================================================================

def get_integer(message):

    while True:

        try:

            number = int(input(message))

            return number

        except ValueError:

            print("Invalid input!")

            print("Please enter a valid whole number.")


# =====================================================================
# SECTION 5: VALIDATE STUDENT MARKS
# =====================================================================

# Marks must be between 0 and 100.

def get_marks(subject):

    while True:

        marks = get_integer(
            f"Enter {subject} marks (0-100): "
        )

        if 0 <= marks <= 100:

            return marks

        else:

            print("Marks must be between 0 and 100.")


# =====================================================================
# SECTION 6: SEARCH STUDENT BY ID
# =====================================================================

# We use linear search.
#
# student[0] contains the student ID.
#
# Time complexity: O(n).

def find_student_by_id(student_id):

    for student in students:

        if student[0] == student_id:

            return student

    return None


# =====================================================================
# SECTION 7: CALCULATE STUDENT TOTAL
# =====================================================================

# Tuple indexes:
#
# 0 = Student ID
# 1 = Name
# 2 = Mathematics
# 3 = Science
# 4 = Python

def calculate_total(student):

    total = sum(student[2:5])

    return total


# =====================================================================
# SECTION 8: CALCULATE STUDENT AVERAGE
# =====================================================================

# Average = Total Marks / Number of Subjects

def calculate_average(student):

    total = calculate_total(student)

    average = total / 3

    return average


# =====================================================================
# SECTION 9: CALCULATE STUDENT GRADE
# =====================================================================

def calculate_grade(average):

    if average >= 90:

        return "A+"

    elif average >= 80:

        return "A"

    elif average >= 70:

        return "B"

    elif average >= 60:

        return "C"

    elif average >= 50:

        return "D"

    else:

        return "F"


# =====================================================================
# SECTION 10: DISPLAY ONE STUDENT
# =====================================================================

def display_student(student):

    average = calculate_average(student)

    grade = calculate_grade(average)

    print("-" * 65)

    print("Student ID:", student[0])

    print("Name:", student[1])

    print("Mathematics:", student[2])

    print("Science:", student[3])

    print("Python:", student[4])

    print("Total Marks:", calculate_total(student))

    print("Average:", round(average, 2))

    print("Grade:", grade)

    print("-" * 65)


# =====================================================================
# SECTION 11: ADD NEW STUDENT
# =====================================================================

# We create a new tuple for every student.
#
# append() adds the tuple to our database list.

def add_student():

    print("\nADD NEW STUDENT")

    print("-" * 40)

    student_id = get_integer("Enter student ID: ")

    # Prevent duplicate student IDs.

    if find_student_by_id(student_id) is not None:

        print("This student ID already exists.")

        return

    name = input("Enter student name: ").strip()

    if not name:

        print("Student name cannot be empty.")

        return

    mathematics = get_marks("Mathematics")

    science = get_marks("Science")

    python_marks = get_marks("Python")

    # Create a new immutable tuple.

    new_student = (

        student_id,

        name,

        mathematics,

        science,

        python_marks

    )

    # Add the tuple to the database.

    students.append(new_student)

    print("\nStudent successfully added!")

    display_student(new_student)


# =====================================================================
# SECTION 12: DISPLAY ALL STUDENTS
# =====================================================================

def display_all_students():

    print("\nALL STUDENT RECORDS")

    print("=" * 65)

    if not students:

        print("No student records available.")

        return

    for index, student in enumerate(students, start=1):

        print(f"\nSTUDENT NUMBER: {index}")

        display_student(student)

    print("Total registered students:", len(students))


# =====================================================================
# SECTION 13: SEARCH STUDENT
# =====================================================================

def search_student():

    print("\nSEARCH STUDENT")

    student_id = get_integer("Enter student ID: ")

    student = find_student_by_id(student_id)

    if student is not None:

        print("\nStudent found successfully!")

        display_student(student)

    else:

        print("Student not found.")


# =====================================================================
# SECTION 14: UPDATE STUDENT MARKS
# =====================================================================

# IMPORTANT:
#
# Tuples are immutable.
#
# We cannot directly write:
#
# student[2] = 95
#
# Instead, we create a NEW tuple containing
# the updated marks and replace the old tuple
# in the database list.

def update_student():

    print("\nUPDATE STUDENT MARKS")

    student_id = get_integer("Enter student ID: ")

    for index, student in enumerate(students):

        if student[0] == student_id:

            print("\nStudent found!")

            display_student(student)

            print("\nSELECT SUBJECT")

            print("1. Mathematics")

            print("2. Science")

            print("3. Python")

            choice = get_integer("Select subject (1-3): ")

            if choice not in (1, 2, 3):

                print("Invalid subject selection.")

                return

            if choice == 1:

                new_marks = get_marks("Mathematics")

                updated_student = (

                    student[0],

                    student[1],

                    new_marks,

                    student[3],

                    student[4]

                )

            elif choice == 2:

                new_marks = get_marks("Science")

                updated_student = (

                    student[0],

                    student[1],

                    student[2],

                    new_marks,

                    student[4]

                )

            else:

                new_marks = get_marks("Python")

                updated_student = (

                    student[0],

                    student[1],

                    student[2],

                    student[3],

                    new_marks

                )

            # Replace the old tuple with the new tuple.

            students[index] = updated_student

            print("\nStudent marks successfully updated!")

            display_student(updated_student)

            return

    print("Student not found.")


# =====================================================================
# SECTION 15: DELETE STUDENT
# =====================================================================

def delete_student():

    print("\nDELETE STUDENT")

    student_id = get_integer("Enter student ID: ")

    for student in students:

        if student[0] == student_id:

            print("\nStudent record found.")

            display_student(student)

            confirmation = input(
                "Confirm deletion? (yes/no): "
            ).strip().lower()

            if confirmation in ("yes", "y"):

                students.remove(student)

                print("Student successfully deleted!")

            else:

                print("Deletion cancelled.")

            return

    print("Student not found.")


# =====================================================================
# SECTION 16: INDIVIDUAL AVERAGE REPORT
# =====================================================================

def student_average_report():

    print("\nSTUDENT AVERAGE REPORT")

    student_id = get_integer("Enter student ID: ")

    student = find_student_by_id(student_id)

    if student is None:

        print("Student not found.")

        return

    average = calculate_average(student)

    grade = calculate_grade(average)

    print("\nStudent:", student[1])

    print("Average:", round(average, 2))

    print("Grade:", grade)


# =====================================================================
# SECTION 17: SUBJECT AVERAGES
# =====================================================================

def subject_averages():

    print("\nSUBJECT PERFORMANCE REPORT")

    if not students:

        print("No student records available.")

        return

    mathematics_total = sum(
        student[2] for student in students
    )

    science_total = sum(
        student[3] for student in students
    )

    python_total = sum(
        student[4] for student in students
    )

    total_students = len(students)

    mathematics_average = mathematics_total / total_students

    science_average = science_total / total_students

    python_average = python_total / total_students

    print("Mathematics average:",
          round(mathematics_average, 2))

    print("Science average:",
          round(science_average, 2))

    print("Python average:",
          round(python_average, 2))


# =====================================================================
# SECTION 18: FIND TOP STUDENT
# =====================================================================

def find_top_student():

    print("\nTOP PERFORMING STUDENT")

    if not students:

        print("No student records available.")

        return

    top_student = max(
        students,
        key=calculate_average
    )

    print("Top student identified!")

    display_student(top_student)


# =====================================================================
# SECTION 19: RANK STUDENTS
# =====================================================================

# sorted() returns a new list.
#
# The original student database remains unchanged.

def rank_students():

    print("\nSTUDENT PERFORMANCE RANKING")

    if not students:

        print("No student records available.")

        return

    ranked_students = sorted(

        students,

        key=calculate_average,

        reverse=True

    )

    for rank, student in enumerate(ranked_students, start=1):

        print(f"\nRANK: {rank}")

        display_student(student)


# =====================================================================
# SECTION 20: DATABASE STATISTICS
# =====================================================================

def database_statistics():

    print("\nDATABASE STATISTICS")

    if not students:

        print("No records available.")

        return

    averages = [

        calculate_average(student)

        for student in students

    ]

    class_average = sum(averages) / len(averages)

    highest_average = max(averages)

    lowest_average = min(averages)

    passing_students = sum(

        average >= 50 for average in averages

    )

    failing_students = len(students) - passing_students

    passing_percentage = (

        passing_students / len(students)

    ) * 100

    print("Total students:", len(students))

    print("Class average:", round(class_average, 2))

    print("Highest average:", round(highest_average, 2))

    print("Lowest average:", round(lowest_average, 2))

    print("Passing students:", passing_students)

    print("Failing students:", failing_students)

    print("Passing percentage:", round(passing_percentage, 2), "%")


# =====================================================================
# SECTION 21: COMPLETE ACADEMIC REPORT
# =====================================================================

def complete_academic_report():

    print("\n" + "=" * 65)

    print("       COMPLETE ACADEMIC PERFORMANCE REPORT")

    print("=" * 65)

    if not students:

        print("No student records available.")

        return

    display_all_students()

    subject_averages()

    database_statistics()

    find_top_student()

    print("\nACADEMIC REPORT COMPLETED!")

    print("=" * 65)


# =====================================================================
# SECTION 22: MAIN APPLICATION
# =====================================================================

def main():

    welcome()

    while True:

        display_menu()

        choice = get_integer("Select an option (1-12): ")

        if choice == 1:

            add_student()

        elif choice == 2:

            display_all_students()

        elif choice == 3:

            search_student()

        elif choice == 4:

            update_student()

        elif choice == 5:

            delete_student()

        elif choice == 6:

            student_average_report()

        elif choice == 7:

            subject_averages()

        elif choice == 8:

            find_top_student()

        elif choice == 9:

            rank_students()

        elif choice == 10:

            complete_academic_report()

        elif choice == 11:

            database_statistics()

        elif choice == 12:

            print("\nThank you for using our application!")

            print("Student Records System terminated.")

            break

        else:

            print("\nInvalid selection!")

            print("Choose an option between 1 and 12.")


# =====================================================================
# SECTION 23: START APPLICATION
# =====================================================================

if __name__ == "__main__":

    main()


# =====================================================================
# END OF DAY 016 - CHALLENGE.PY
# =====================================================================
