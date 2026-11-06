
# =====================================================================
# DAY 017 - PYTHON SETS CHALLENGE
#
# PROJECT:
# STUDENT ENROLLMENT AND COURSE ANALYSIS SYSTEM
#
# Bachelor's in Artificial Intelligence
# 90-Day Python Programming Journey
#
# MAIN TOPIC: PYTHON SETS
#
# CONCEPTS:
# 1. Sets
# 2. Set Operations
# 3. Union
# 4. Intersection
# 5. Difference
# 6. Symmetric Difference
# 7. Subsets
# 8. Frozen Sets
# 9. Set Comprehensions
# 10. Functions
# 11. Loops
# 12. Conditions
# 13. Statistics
# 14. Data Analysis
#
# =====================================================================


# =====================================================================
# SECTION 1: INITIAL DATABASE
# =====================================================================

# Each course contains a set of enrolled student names.
#
# Sets automatically prevent duplicate enrollments.

courses = {

    "Python": {

        "Ali",
        "Ahmed",
        "John",
        "David",
        "Michael"

    },

    "Mathematics": {

        "Ali",
        "John",
        "Sarah",
        "David",
        "Emma"

    },

    "Statistics": {

        "Ahmed",
        "John",
        "Michael",
        "Emma",
        "Daniel"

    },

    "Artificial Intelligence": {

        "Ali",
        "Michael",
        "Sarah",
        "Daniel"

    }

}


# =====================================================================
# SECTION 2: WELCOME SCREEN
# =====================================================================

def welcome():

    print("\n" + "=" * 70)

    print("       STUDENT ENROLLMENT AND COURSE ANALYSIS SYSTEM")

    print("=" * 70)

    print("Welcome to our Python Sets Project!")

    print("Manage students and analyze course enrollments.")

    print("=" * 70)


# =====================================================================
# SECTION 3: MAIN MENU
# =====================================================================

def display_menu():

    print("\n" + "=" * 65)

    print("                       MAIN MENU")

    print("=" * 65)

    print("1. Display All Courses")

    print("2. Register New Student")

    print("3. Enroll Student in Course")

    print("4. Remove Student from Course")

    print("5. Display Students in a Course")

    print("6. Find Common Students")

    print("7. Find Students in Any Course")

    print("8. Find Students Taking Only One Course")

    print("9. Compare Two Courses")

    print("10. Find Students Taking All Courses")

    print("11. Display Course Enrollment Statistics")

    print("12. Search Student")

    print("13. Generate Complete Academic Report")

    print("14. Display Set Theory Analysis")

    print("15. Exit")

    print("=" * 65)


# =====================================================================
# SECTION 4: INPUT VALIDATION
# =====================================================================

def get_integer(message):

    while True:

        try:

            return int(input(message))

        except ValueError:

            print("Invalid input! Enter a whole number.")


# =====================================================================
# SECTION 5: DISPLAY ALL COURSES
# =====================================================================

def display_courses():

    print("\nAVAILABLE COURSES")

    print("-" * 50)

    for number, course in enumerate(courses, start=1):

        print(f"{number}. {course}")

    print("-" * 50)


# =====================================================================
# SECTION 6: SELECT COURSE
# =====================================================================

def select_course():

    display_courses()

    course_name = input(
        "\nEnter course name: "
    ).strip()

    if course_name in courses:

        return course_name

    print("Course does not exist.")

    return None


# =====================================================================
# SECTION 7: REGISTER NEW STUDENT
# =====================================================================

# A separate set maintains all registered students.
#
# This ensures students remain registered
# even if they leave every course.

registered_students = set()

for enrolled_students in courses.values():

    registered_students.update(enrolled_students)


def register_student():

    print("\nREGISTER NEW STUDENT")

    name = input("Enter student name: ").strip()

    if not name:

        print("Student name cannot be empty.")

        return

    # Case-insensitive duplicate checking.

    existing_names = {

        student.casefold()

        for student in registered_students

    }

    if name.casefold() in existing_names:

        print("Student is already registered.")

        return

    registered_students.add(name)

    print(f"{name} registered successfully!")


# =====================================================================
# SECTION 8: ENROLL STUDENT IN COURSE
# =====================================================================

def enroll_student():

    print("\nENROLL STUDENT")

    name = input("Enter student name: ").strip()

    if not name:

        print("Student name cannot be empty.")

        return

    course_name = select_course()

    if course_name is None:

        return

    # Register the student if necessary.

    existing = {

        student.casefold(): student

        for student in registered_students

    }

    if name.casefold() not in existing:

        registered_students.add(name)

        student_name = name

        print("New student registered.")

    else:

        student_name = existing[name.casefold()]

    # Check whether already enrolled.

    if student_name in courses[course_name]:

        print("Student is already enrolled in this course.")

        return

    # Add student to the course set.

    courses[course_name].add(student_name)

    print(
        f"{student_name} successfully enrolled in {course_name}!"
    )


# =====================================================================
# SECTION 9: REMOVE STUDENT FROM COURSE
# =====================================================================

def remove_enrollment():

    print("\nREMOVE COURSE ENROLLMENT")

    name = input("Enter student name: ").strip()

    course_name = select_course()

    if course_name is None:

        return

    if name not in courses[course_name]:

        print("Student is not enrolled in this course.")

        return

    # discard() safely removes the element.

    courses[course_name].discard(name)

    print("Enrollment successfully removed.")

    # The student remains registered in the database.


# =====================================================================
# SECTION 10: DISPLAY STUDENTS IN A COURSE
# =====================================================================

def display_course_students():

    print("\nCOURSE STUDENT LIST")

    course_name = select_course()

    if course_name is None:

        return

    students = courses[course_name]

    print("\nCourse:", course_name)

    if not students:

        print("No enrolled students.")

        return

    for number, student in enumerate(
        sorted(students),
        start=1
    ):

        print(f"{number}. {student}")

    print("Total students:", len(students))


# =====================================================================
# SECTION 11: FIND COMMON STUDENTS
# =====================================================================

# Intersection:
#
# A & B
#
# Returns students enrolled in BOTH courses.

def find_common_students():

    print("\nCOMMON STUDENT ANALYSIS")

    course_A = select_course()

    if course_A is None:

        return

    course_B = select_course()

    if course_B is None:

        return

    common = courses[course_A] & courses[course_B]

    print("\nCourse A:", course_A)

    print("Course B:", course_B)

    print("Common students:", sorted(common))

    print("Total common students:", len(common))


# =====================================================================
# SECTION 12: FIND STUDENTS IN ANY COURSE
# =====================================================================

# Union:
#
# A | B
#
# Returns all unique students enrolled
# in at least one course.

def find_students_in_any_course():

    print("\nALL ENROLLED STUDENTS")

    all_enrolled = set()

    for students in courses.values():

        all_enrolled = all_enrolled | students

    print("All students:", sorted(all_enrolled))

    print("Total unique enrolled students:", len(all_enrolled))


# =====================================================================
# SECTION 13: STUDENTS TAKING ONLY ONE COURSE
# =====================================================================

# A student taking only one course appears
# in exactly one course set.

def find_single_course_students():

    print("\nSTUDENTS TAKING ONLY ONE COURSE")

    enrollment_count = {}

    for course_name, students in courses.items():

        for student in students:

            enrollment_count[student] = (

                enrollment_count.get(student, 0) + 1

            )

    single_course_students = {

        student

        for student, count in enrollment_count.items()

        if count == 1

    }

    print(
        "Students taking exactly one course:",
        sorted(single_course_students)
    )

    print("Total:", len(single_course_students))


# =====================================================================
# SECTION 14: COMPARE TWO COURSES
# =====================================================================

# We calculate:
#
# Union: A | B
# Intersection: A & B
# Difference: A - B
# Symmetric difference: A ^ B

def compare_courses():

    print("\nCOURSE COMPARISON")

    course_A = select_course()

    if course_A is None:

        return

    course_B = select_course()

    if course_B is None:

        return

    A = courses[course_A]

    B = courses[course_B]

    print("\nCOURSE A:", course_A)

    print("COURSE B:", course_B)

    print("\nUnion:", sorted(A | B))

    print("Intersection:", sorted(A & B))

    print("Only in A:", sorted(A - B))

    print("Only in B:", sorted(B - A))

    print("Symmetric difference:", sorted(A ^ B))


# =====================================================================
# SECTION 15: STUDENTS TAKING ALL COURSES
# =====================================================================

# Intersection across every course finds
# students enrolled in ALL courses.

def find_students_in_all_courses():

    print("\nSTUDENTS TAKING ALL COURSES")

    all_courses = list(courses.values())

    if not all_courses:

        print("No courses available.")

        return

    common_students = set.intersection(*all_courses)

    print("Students taking every course:")

    print(sorted(common_students))

    print("Total:", len(common_students))


# =====================================================================
# SECTION 16: COURSE ENROLLMENT STATISTICS
# =====================================================================

def enrollment_statistics():

    print("\nCOURSE ENROLLMENT STATISTICS")

    total_enrollments = 0

    for course_name, students in courses.items():

        count = len(students)

        total_enrollments += count

        print(
            f"{course_name}: {count} students"
        )

    total_courses = len(courses)

    unique_enrolled = set.union(*courses.values())

    print("\nTotal courses:", total_courses)

    print("Total enrollments:", total_enrollments)

    print("Unique enrolled students:", len(unique_enrolled))

    if total_courses > 0:

        average = total_enrollments / total_courses

        print("Average enrollment per course:", round(average, 2))


# =====================================================================
# SECTION 17: SEARCH STUDENT
# =====================================================================

def search_student():

    print("\nSEARCH STUDENT")

    name = input("Enter student name: ").strip()

    existing = {

        student.casefold(): student

        for student in registered_students

    }

    student_name = existing.get(name.casefold())

    if student_name is None:

        print("Student not found.")

        return

    print("\nStudent:", student_name)

    print("Registration status: Registered")

    enrolled_courses = [

        course_name

        for course_name, students in courses.items()

        if student_name in students

    ]

    if enrolled_courses:

        print("Enrolled courses:")

        for course in enrolled_courses:

            print("-", course)

    else:

        print("Currently not enrolled in any course.")


# =====================================================================
# SECTION 18: COMPLETE ACADEMIC REPORT
# =====================================================================

def complete_academic_report():

    print("\n" + "=" * 70)

    print("             COMPLETE ACADEMIC REPORT")

    print("=" * 70)

    print("\nREGISTERED STUDENTS:", len(registered_students))

    print("REGISTERED STUDENT LIST:")

    for student in sorted(registered_students):

        print("-", student)

    print("\nCOURSE REPORT")

    for course_name, students in courses.items():

        print("\nCourse:", course_name)

        print("Enrolled students:", len(students))

        print("Students:", sorted(students))

    print("\nENROLLMENT STATISTICS")

    enrollment_statistics()

    print("\nCROSS-COURSE ANALYSIS")

    all_enrolled = set.union(*courses.values())

    print("Unique enrolled students:", len(all_enrolled))

    print(
        "Registered but not enrolled:",
        sorted(registered_students - all_enrolled)
    )

    print("\nREPORT COMPLETED!")

    print("=" * 70)


# =====================================================================
# SECTION 19: SET THEORY ANALYSIS
# =====================================================================

# Demonstrate mathematical set relationships.

def set_theory_analysis():

    print("\nMATHEMATICAL SET THEORY ANALYSIS")

    A = {1, 2, 3, 4}

    B = {3, 4, 5, 6}

    C = {1, 2}

    print("A:", A)

    print("B:", B)

    print("C:", C)

    print("\nA union B:", A | B)

    print("A intersection B:", A & B)

    print("A difference B:", A - B)

    print("A symmetric difference B:", A ^ B)

    print("C is subset of A:", C <= A)

    print("A is superset of C:", A >= C)

    print("A and B are disjoint:", A.isdisjoint(B))


# =====================================================================
# SECTION 20: APPLICATION OF SETS IN AI
# =====================================================================

# Sets can be used to identify unique
# labels and compare feature groups.
#
# This is a simplified data-processing example.

def ai_data_analysis():

    print("\nAI DATA ANALYSIS")

    dataset_A_labels = {

        "Cat",

        "Dog",

        "Bird",

        "Cat"

    }

    dataset_B_labels = {

        "Dog",

        "Fish",

        "Bird"

    }

    print("Dataset A labels:", dataset_A_labels)

    print("Dataset B labels:", dataset_B_labels)

    print(
        "All unique labels:",
        dataset_A_labels | dataset_B_labels
    )

    print(
        "Common labels:",
        dataset_A_labels & dataset_B_labels
    )

    print(
        "Labels unique to A:",
        dataset_A_labels - dataset_B_labels
    )

    print(
        "Labels unique to B:",
        dataset_B_labels - dataset_A_labels
    )


# =====================================================================
# SECTION 21: MAIN APPLICATION
# =====================================================================

def main():

    welcome()

    while True:

        display_menu()

        choice = get_integer(
            "\nSelect an option (1-15): "
        )

        if choice == 1:

            display_courses()

        elif choice == 2:

            register_student()

        elif choice == 3:

            enroll_student()

        elif choice == 4:

            remove_enrollment()

        elif choice == 5:

            display_course_students()

        elif choice == 6:

            find_common_students()

        elif choice == 7:

            find_students_in_any_course()

        elif choice == 8:

            find_single_course_students()

        elif choice == 9:

            compare_courses()

        elif choice == 10:

            find_students_in_all_courses()

        elif choice == 11:

            enrollment_statistics()

        elif choice == 12:

            search_student()

        elif choice == 13:

            complete_academic_report()

        elif choice == 14:

            set_theory_analysis()

            ai_data_analysis()

        elif choice == 15:

            print("\nThank you for using our system!")

            print("DAY 017 CHALLENGE COMPLETED!")

            break

        else:

            print("Invalid choice. Select 1-15.")


# =====================================================================
# SECTION 22: START APPLICATION
# =====================================================================

if __name__ == "__main__":

    main()


# =====================================================================
# END OF DAY 017 - CHALLENGE.PY
# =====================================================================
