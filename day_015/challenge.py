
# =====================================================================
# DAY 015 - ADVANCED PYTHON LISTS CHALLENGE
#
# PROJECT:
# STUDENT PERFORMANCE AND DATASET ANALYSIS SYSTEM
#
# Bachelor's in Artificial Intelligence
# 90-Day Python Programming Journey
#
# CONCEPTS USED:
# 1. Python Lists
# 2. Nested Lists
# 3. List Indexing
# 4. List Methods
# 5. List Slicing
# 6. For Loops
# 7. While Loops
# 8. Conditional Statements
# 9. Functions
# 10. Input Validation
# 11. Sorting
# 12. Searching
# 13. Mathematical Calculations
# 14. Descriptive Statistics
#
# =====================================================================


# =====================================================================
# SECTION 1: INITIAL STUDENT DATASET
# =====================================================================

# We use a nested list to store student information.
#
# Each inner list contains:
#
# [Name, Mathematics, Science, Python]
#
# Example:
#
# ["Ali", 85, 90, 95]
#
# This is a simple structured dataset.

students = [

    ["Ali", 85, 90, 95],

    ["Ahmed", 75, 80, 85],

    ["John", 92, 88, 96],

    ["David", 65, 70, 75],

    ["Michael", 88, 85, 90]

]


# =====================================================================
# SECTION 2: DISPLAY WELCOME SCREEN
# =====================================================================

def display_welcome():

    print("\n")

    print("=" * 70)

    print("       STUDENT PERFORMANCE AND DATASET ANALYSIS SYSTEM")

    print("=" * 70)

    print("Welcome to our Python data management application!")

    print("Manage student records and analyse academic performance.")

    print("=" * 70)


# =====================================================================
# SECTION 3: DISPLAY MAIN MENU
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

    print("8. Find Top Performing Student")

    print("9. Sort Students by Performance")

    print("10. Generate Class Performance Report")

    print("11. Exit Application")

    print("=" * 65)


# =====================================================================
# SECTION 4: GET VALID INTEGER INPUT
# =====================================================================

# This function prevents the program from crashing
# when users enter letters instead of numbers.
#
# int() converts a string into an integer.
#
# try/except handles ValueError.

def get_integer(message):

    while True:

        try:

            number = int(input(message))

            return number

        except ValueError:

            print("Invalid input!")

            print("Please enter a whole number.")


# =====================================================================
# SECTION 5: GET VALID MARKS
# =====================================================================

# Marks must be between 0 and 100.
#
# This function keeps asking until
# the user enters valid marks.

def get_marks(subject):

    while True:

        marks = get_integer(f"Enter {subject} marks (0-100): ")

        if 0 <= marks <= 100:

            return marks

        else:

            print("Marks must be between 0 and 100.")


# =====================================================================
# SECTION 6: CALCULATE STUDENT AVERAGE
# =====================================================================

# Each student has three subject marks.
#
# Average formula:
#
# Average = Total Marks / Number of Subjects
#
# We use indexes:
#
# student[1] = Mathematics
# student[2] = Science
# student[3] = Python

def calculate_average(student):

    total = student[1] + student[2] + student[3]

    average = total / 3

    return average


# =====================================================================
# SECTION 7: DETERMINE STUDENT GRADE
# =====================================================================

# We assign grades based on the average marks.
#
# These are illustrative grading thresholds
# for this project.

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
# SECTION 8: DISPLAY ONE STUDENT
# =====================================================================

# This function displays the complete information
# for one student.

def display_student(student):

    average = calculate_average(student)

    grade = calculate_grade(average)

    print("-" * 65)

    print("Name:", student[0])

    print("Mathematics:", student[1])

    print("Science:", student[2])

    print("Python:", student[3])

    print("Total Marks:", sum(student[1:4]))

    print("Average:", round(average, 2))

    print("Grade:", grade)

    print("-" * 65)


# =====================================================================
# SECTION 9: ADD NEW STUDENT
# =====================================================================

# This function collects student information
# and adds a new record to our nested list.
#
# append() adds the complete student record
# as one element of the outer list.

def add_student():

    print("\nADD NEW STUDENT")

    print("-" * 40)

    name = input("Enter student name: ").strip()

    if not name:

        print("Student name cannot be empty.")

        return

    # Check whether the student already exists.

    for student in students:

        if student[0].casefold() == name.casefold():

            print("A student with this name already exists.")

            return

    mathematics = get_marks("Mathematics")

    science = get_marks("Science")

    python_marks = get_marks("Python")

    # Create a new nested list.

    new_student = [

        name,

        mathematics,

        science,

        python_marks

    ]

    # Add the record to the main dataset.

    students.append(new_student)

    print("\nStudent successfully added!")

    display_student(new_student)


# =====================================================================
# SECTION 10: DISPLAY ALL STUDENTS
# =====================================================================

# This function uses a for loop to display
# every student inside our dataset.

def display_all_students():

    print("\nALL REGISTERED STUDENTS")

    print("=" * 65)

    if not students:

        print("No student records available.")

        return

    for index, student in enumerate(students, start=1):

        print(f"\nStudent Number: {index}")

        display_student(student)

    print("Total students:", len(students))


# =====================================================================
# SECTION 11: SEARCH FOR A STUDENT
# =====================================================================

# Searching means finding a particular
# record inside a dataset.
#
# We use linear search.
#
# Time complexity: O(n)

def search_student():

    print("\nSEARCH STUDENT")

    print("-" * 40)

    name = input("Enter student name: ").strip()

    if not name:

        print("Please enter a student name.")

        return

    found = False

    for student in students:

        if student[0].casefold() == name.casefold():

            print("\nStudent found!")

            display_student(student)

            found = True

            break

    if not found:

        print("Student not found.")


# =====================================================================
# SECTION 12: UPDATE STUDENT MARKS
# =====================================================================

# This function searches for a student
# and modifies their marks.
#
# Lists are mutable, so we can update
# individual elements using their indexes.

def update_student():

    print("\nUPDATE STUDENT MARKS")

    print("-" * 40)

    name = input("Enter student name: ").strip()

    found = False

    for student in students:

        if student[0].casefold() == name.casefold():

            found = True

            print("\nStudent found!")

            display_student(student)

            print("\nWhich subject do you want to update?")

            print("1. Mathematics")

            print("2. Science")

            print("3. Python")

            choice = get_integer("Choose subject (1-3): ")

            if choice == 1:

                student[1] = get_marks("Mathematics")

            elif choice == 2:

                student[2] = get_marks("Science")

            elif choice == 3:

                student[3] = get_marks("Python")

            else:

                print("Invalid subject selection.")

                return

            print("\nMarks successfully updated!")

            display_student(student)

            break

    if not found:

        print("Student not found.")


# =====================================================================
# SECTION 13: DELETE STUDENT
# =====================================================================

# remove() deletes a matching element
# from the outer students list.
#
# We first find the student and then remove
# their complete record.

def delete_student():

    print("\nDELETE STUDENT")

    print("-" * 40)

    name = input("Enter student name: ").strip()

    found = False

    for student in students:

        if student[0].casefold() == name.casefold():

            print("\nStudent record found.")

            display_student(student)

            confirmation = input(
                "Are you sure you want to delete? (yes/no): "
            ).strip().lower()

            if confirmation in ["yes", "y"]:

                students.remove(student)

                print("Student successfully deleted!")

            else:

                print("Deletion cancelled.")

            found = True

            break

    if not found:

        print("Student not found.")


# =====================================================================
# SECTION 14: CALCULATE INDIVIDUAL AVERAGE
# =====================================================================

# This function finds a student and calculates
# their academic average.

def student_average_report():

    print("\nSTUDENT AVERAGE REPORT")

    name = input("Enter student name: ").strip()

    for student in students:

        if student[0].casefold() == name.casefold():

            average = calculate_average(student)

            grade = calculate_grade(average)

            print("\nStudent:", student[0])

            print("Average:", round(average, 2))

            print("Grade:", grade)

            return

    print("Student not found.")


# =====================================================================
# SECTION 15: CALCULATE SUBJECT AVERAGES
# =====================================================================

# We calculate the average for:
#
# Mathematics
# Science
# Python
#
# Formula:
#
# Subject Average = Total Subject Marks / Number of Students

def display_subject_averages():

    print("\nSUBJECT PERFORMANCE REPORT")

    print("=" * 50)

    if not students:

        print("No student data available.")

        return

    mathematics_total = 0

    science_total = 0

    python_total = 0

    for student in students:

        mathematics_total += student[1]

        science_total += student[2]

        python_total += student[3]

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

    print("=" * 50)


# =====================================================================
# SECTION 16: FIND TOP PERFORMING STUDENT
# =====================================================================

# We compare each student's average.
#
# The student with the highest average
# becomes the top performer.

def find_top_student():

    print("\nTOP PERFORMING STUDENT")

    print("=" * 50)

    if not students:

        print("No student records available.")

        return

    top_student = students[0]

    for student in students:

        if calculate_average(student) > calculate_average(top_student):

            top_student = student

    print("TOP STUDENT IDENTIFIED!")

    display_student(top_student)


# =====================================================================
# SECTION 17: SORT STUDENTS BY PERFORMANCE
# =====================================================================

# sorted() creates a new sorted list.
#
# We use a separate function to calculate
# each student's average.
#
# reverse=True places the highest average first.
#
# The original students list remains unchanged.

def sort_students():

    print("\nSTUDENTS RANKED BY PERFORMANCE")

    print("=" * 60)

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
# SECTION 18: CALCULATE CLASS STATISTICS
# =====================================================================

# We calculate:
#
# 1. Total number of students.
# 2. Highest average.
# 3. Lowest average.
# 4. Class average.
# 5. Number of passing students.
# 6. Number of failing students.
#
# Passing threshold: 50.

def class_statistics():

    if not students:

        print("No student data available.")

        return

    averages = []

    passing_students = 0

    failing_students = 0

    for student in students:

        average = calculate_average(student)

        averages.append(average)

        if average >= 50:

            passing_students += 1

        else:

            failing_students += 1

    class_average = sum(averages) / len(averages)

    highest_average = max(averages)

    lowest_average = min(averages)

    print("\nCLASS STATISTICS")

    print("-" * 50)

    print("Total students:", len(students))

    print("Class average:", round(class_average, 2))

    print("Highest average:", round(highest_average, 2))

    print("Lowest average:", round(lowest_average, 2))

    print("Passing students:", passing_students)

    print("Failing students:", failing_students)

    print("-" * 50)


# =====================================================================
# SECTION 19: GENERATE COMPLETE CLASS REPORT
# =====================================================================

# This function combines several reports
# into one comprehensive analysis.

def class_performance_report():

    print("\n" + "=" * 65)

    print("          COMPLETE CLASS PERFORMANCE REPORT")

    print("=" * 65)

    if not students:

        print("No student records available.")

        return

    display_all_students()

    display_subject_averages()

    class_statistics()

    find_top_student()

    print("\nCLASS REPORT COMPLETED!")

    print("=" * 65)


# =====================================================================
# SECTION 20: MAIN APPLICATION
# =====================================================================

# The main function controls the entire program.
#
# It displays the menu and calls the correct
# function according to the user's choice.

def main():

    display_welcome()

    while True:

        display_menu()

        choice = get_integer("Select an option (1-11): ")


        # -------------------------------------------------------------
        # OPTION 1: ADD STUDENT
        # -------------------------------------------------------------

        if choice == 1:

            add_student()


        # -------------------------------------------------------------
        # OPTION 2: DISPLAY ALL STUDENTS
        # -------------------------------------------------------------

        elif choice == 2:

            display_all_students()


        # -------------------------------------------------------------
        # OPTION 3: SEARCH STUDENT
        # -------------------------------------------------------------

        elif choice == 3:

            search_student()


        # -------------------------------------------------------------
        # OPTION 4: UPDATE MARKS
        # -------------------------------------------------------------

        elif choice == 4:

            update_student()


        # -------------------------------------------------------------
        # OPTION 5: DELETE STUDENT
        # -------------------------------------------------------------

        elif choice == 5:

            delete_student()


        # -------------------------------------------------------------
        # OPTION 6: INDIVIDUAL AVERAGE
        # -------------------------------------------------------------

        elif choice == 6:

            student_average_report()


        # -------------------------------------------------------------
        # OPTION 7: SUBJECT AVERAGES
        # -------------------------------------------------------------

        elif choice == 7:

            display_subject_averages()


        # -------------------------------------------------------------
        # OPTION 8: TOP STUDENT
        # -------------------------------------------------------------

        elif choice == 8:

            find_top_student()


        # -------------------------------------------------------------
        # OPTION 9: SORT STUDENTS
        # -------------------------------------------------------------

        elif choice == 9:

            sort_students()


        # -------------------------------------------------------------
        # OPTION 10: COMPLETE CLASS REPORT
        # -------------------------------------------------------------

        elif choice == 10:

            class_performance_report()


        # -------------------------------------------------------------
        # OPTION 11: EXIT
        # -------------------------------------------------------------

        elif choice == 11:

            print("\nThank you for using our application!")

            print("Student Performance System terminated.")

            break


        # -------------------------------------------------------------
        # INVALID MENU OPTION
        # -------------------------------------------------------------

        else:

            print("\nInvalid selection!")

            print("Please choose an option between 1 and 11.")


# =====================================================================
# SECTION 21: START THE APPLICATION
# =====================================================================

# This condition checks whether the file
# is being executed directly.
#
# It prevents main() from automatically running
# when this file is imported into another module.

if __name__ == "__main__":

    main()


# =====================================================================
# END OF DAY 015 - CHALLENGE.PY
# =====================================================================
