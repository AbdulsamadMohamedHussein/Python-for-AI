
# =================================================================
# DAY 010 - PYTHON CONDITIONAL STATEMENTS
#
# CHALLENGE PROJECT:
# STUDENT GRADING AND ACADEMIC PERFORMANCE MANAGEMENT SYSTEM
#
# Bachelor's in Artificial Intelligence
# 90-Day Python Programming Journey
#
# CONCEPTS USED:
# 1. Conditional Statements
# 2. if, elif and else
# 3. Comparison Operators
# 4. Logical Operators
# 5. Nested Conditions
# 6. Boolean Values
# 7. Functions
# 8. Loops
# 9. User Input
# 10. Exception Handling
# 11. Dictionaries
# 12. Lists
#
# =================================================================


# =================================================================
# SECTION 1: PROJECT INTRODUCTION
# =================================================================

print("\n" + "=" * 75)

print("       STUDENT ACADEMIC PERFORMANCE MANAGEMENT SYSTEM")

print("=" * 75)

print("Welcome to our Academic Performance Management System!")

print("This application evaluates student academic performance.")

print("=" * 75)


# =================================================================
# SECTION 2: CREATE A FUNCTION TO COLLECT STUDENT NAME
# =================================================================

# A function is a reusable block of code.
#
# This function collects the student's name.
#
# strip() removes unnecessary spaces.
# title() formats the name.
#
# We use a loop to prevent an empty name.

def get_student_name():

    while True:

        name = input("Enter student full name: ").strip()

        if name == "":

            print("Error: Name cannot be empty.")

        elif not all(character.isalpha() or character.isspace()
                     for character in name):

            print("Error: Use letters and spaces only.")

        else:

            return name.title()


# =================================================================
# SECTION 3: CREATE A FUNCTION TO COLLECT STUDENT AGE
# =================================================================

# int() converts numeric text into an integer.
#
# ValueError occurs if the user enters non-numeric text.
#
# try and except prevent the program from crashing.

def get_student_age():

    while True:

        try:

            age = int(input("Enter student age: "))

            if 1 <= age <= 120:

                return age

            else:

                print("Please enter an age between 1 and 120.")

        except ValueError:

            print("Invalid input. Please enter a whole number.")


# =================================================================
# SECTION 4: CREATE A FUNCTION TO COLLECT MARKS
# =================================================================

# Marks must be between 0 and 100.
#
# The function checks the input before accepting it.
#
# We return a number only when it is valid.

def get_marks(subject):

    while True:

        try:

            marks = float(input(f"Enter marks for {subject}: "))

            if 0 <= marks <= 100:

                return marks

            else:

                print("Marks must be between 0 and 100.")

        except ValueError:

            print("Invalid marks. Please enter a number.")


# =================================================================
# SECTION 5: CREATE A FUNCTION TO COLLECT ATTENDANCE
# =================================================================

# Attendance is measured as a percentage.
#
# It must be between 0 and 100.

def get_attendance():

    while True:

        try:

            attendance = float(input("Enter attendance percentage: "))

            if 0 <= attendance <= 100:

                return attendance

            else:

                print("Attendance must be between 0 and 100.")

        except ValueError:

            print("Please enter a valid percentage.")


# =================================================================
# SECTION 6: CREATE A FUNCTION TO CALCULATE TOTAL MARKS
# =================================================================

# We calculate the total marks from five subjects.
#
# sum() adds all numerical values in the list.
#
# len() counts the number of subjects.

def calculate_total(marks_list):

    return sum(marks_list)


# =================================================================
# SECTION 7: CREATE A FUNCTION TO CALCULATE AVERAGE
# =================================================================

# Average = Total Marks / Number of Subjects
#
# Example:
#
# Total = 400
# Subjects = 5
# Average = 80

def calculate_average(total, number_of_subjects):

    return total / number_of_subjects


# =================================================================
# SECTION 8: CREATE A FUNCTION TO ASSIGN GRADES
# =================================================================

# Grading system:
#
# 90-100 = A+
# 80-89  = A
# 70-79  = B
# 60-69  = C
# 50-59  = D
# Below 50 = F
#
# The conditions are checked from top to bottom.
#
# The first True condition determines the grade.

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


# =================================================================
# SECTION 9: CREATE A FUNCTION TO CHECK PASS OR FAIL
# =================================================================

# A student must:
#
# 1. Have an average of at least 50.
# 2. Pass every individual subject with at least 40.
#
# This is an example academic grading policy.

def check_pass_fail(average, marks_list):

    if average >= 50 and all(mark >= 40 for mark in marks_list):

        return "PASS"

    else:

        return "FAIL"


# =================================================================
# SECTION 10: CREATE A FUNCTION TO EVALUATE ATTENDANCE
# =================================================================

# Our example attendance requirement is 75%.
#
# >= means greater than or equal to.

def check_attendance(attendance):

    if attendance >= 75:

        return "Satisfactory"

    else:

        return "Insufficient"


# =================================================================
# SECTION 11: CREATE A FUNCTION FOR SCHOLARSHIP ELIGIBILITY
# =================================================================

# Example scholarship requirements:
#
# Average marks must be at least 85.
# Attendance must be at least 80%.
# Student must pass all subjects.
#
# All conditions must be True.
#
# We use the AND operator.

def check_scholarship(average, attendance, result):

    if average >= 85 and attendance >= 80 and result == "PASS":

        return "ELIGIBLE"

    else:

        return "NOT ELIGIBLE"


# =================================================================
# SECTION 12: CREATE A FUNCTION FOR PERFORMANCE CLASSIFICATION
# =================================================================

# Performance categories:
#
# 90 and above = Excellent
# 80-89 = Very Good
# 70-79 = Good
# 60-69 = Satisfactory
# 50-59 = Needs Improvement
# Below 50 = Poor

def classify_performance(average):

    if average >= 90:

        return "Excellent"

    elif average >= 80:

        return "Very Good"

    elif average >= 70:

        return "Good"

    elif average >= 60:

        return "Satisfactory"

    elif average >= 50:

        return "Needs Improvement"

    else:

        return "Poor"


# =================================================================
# SECTION 13: COLLECT STUDENT INFORMATION
# =================================================================

print("\n" + "=" * 75)

print("                 STUDENT INFORMATION")

print("=" * 75)

# Call the functions to collect information.

student_name = get_student_name()

student_age = get_student_age()

student_course = input("Enter course name: ").strip().title()

while student_course == "":

    print("Course cannot be empty.")

    student_course = input("Enter course name: ").strip().title()


# =================================================================
# SECTION 14: COLLECT SUBJECT MARKS
# =================================================================

print("\n" + "=" * 75)

print("                 SUBJECT MARKS")

print("=" * 75)

# We store five subjects in a list.
#
# A list allows us to store multiple values.
#
# A dictionary will connect each subject to its marks.

subjects = [

    "Mathematics",

    "Python Programming",

    "Statistics",

    "Computer Science",

    "Artificial Intelligence"

]

marks_list = []

subject_results = {}

# Loop through each subject.
#
# The user enters marks separately for each subject.

for subject in subjects:

    marks = get_marks(subject)

    # Add marks to the list.

    marks_list.append(marks)

    # Store subject and marks in the dictionary.

    subject_results[subject] = marks


# =================================================================
# SECTION 15: COLLECT ATTENDANCE
# =================================================================

print("\n" + "=" * 75)

print("                 ATTENDANCE INFORMATION")

print("=" * 75)

attendance = get_attendance()


# =================================================================
# SECTION 16: CALCULATE TOTAL AND AVERAGE
# =================================================================

# Calculate the sum of all subject marks.

total_marks = calculate_total(marks_list)

# Calculate the average.
#
# We use len(subjects) to determine the subject count.

average_marks = calculate_average(

    total_marks,

    len(subjects)

)


# =================================================================
# SECTION 17: DETERMINE STUDENT GRADE
# =================================================================

# Send the average to the grade function.

grade = calculate_grade(average_marks)


# =================================================================
# SECTION 18: DETERMINE PASS OR FAIL
# =================================================================

# A student must meet the average and individual
# subject requirements.

result = check_pass_fail(

    average_marks,

    marks_list

)


# =================================================================
# SECTION 19: EVALUATE ATTENDANCE
# =================================================================

attendance_status = check_attendance(attendance)


# =================================================================
# SECTION 20: CHECK SCHOLARSHIP ELIGIBILITY
# =================================================================

scholarship_status = check_scholarship(

    average_marks,

    attendance,

    result

)


# =================================================================
# SECTION 21: CLASSIFY ACADEMIC PERFORMANCE
# =================================================================

performance = classify_performance(average_marks)


# =================================================================
# SECTION 22: STORE STUDENT INFORMATION
# =================================================================

# Dictionaries store information as key-value pairs.
#
# This makes it easier to organize and retrieve
# the student's information.

student_information = {

    "Student Name": student_name,

    "Age": student_age,

    "Course": student_course,

    "Total Marks": total_marks,

    "Average Marks": average_marks,

    "Grade": grade,

    "Result": result,

    "Attendance": attendance,

    "Attendance Status": attendance_status,

    "Performance": performance,

    "Scholarship": scholarship_status

}


# =================================================================
# SECTION 23: DISPLAY INDIVIDUAL SUBJECT RESULTS
# =================================================================

print("\n" + "=" * 75)

print("                 SUBJECT PERFORMANCE REPORT")

print("=" * 75)

# Display each subject and its corresponding marks.

for subject, marks in subject_results.items():

    print(f"{subject}: {marks:.2f}/100")

    # Nested conditions classify each subject.

    if marks >= 90:

        print("   Subject Grade: Excellent")

    elif marks >= 80:

        print("   Subject Grade: Very Good")

    elif marks >= 70:

        print("   Subject Grade: Good")

    elif marks >= 60:

        print("   Subject Grade: Satisfactory")

    elif marks >= 40:

        print("   Subject Grade: Pass")

    else:

        print("   Subject Grade: Fail")


# =================================================================
# SECTION 24: DISPLAY FINAL ACADEMIC REPORT
# =================================================================

print("\n" + "=" * 75)

print("              FINAL ACADEMIC PERFORMANCE REPORT")

print("=" * 75)

# Loop through the student dictionary.
#
# items() gives us each key and its value.

for key, value in student_information.items():

    # Format average and attendance to two decimal places.

    if isinstance(value, float):

        print(f"{key}: {value:.2f}")

    else:

        print(f"{key}: {value}")


# =================================================================
# SECTION 25: DISPLAY SCHOLARSHIP DECISION
# =================================================================

print("\n" + "=" * 75)

print("                 SCHOLARSHIP EVALUATION")

print("=" * 75)

# We use a condition to explain the result.

if scholarship_status == "ELIGIBLE":

    print("Congratulations!")

    print("The student meets all example scholarship requirements.")

else:

    print("The student does not meet all scholarship requirements.")

    # Nested conditions help explain why.

    if average_marks < 85:

        print("Reason: Average marks are below 85.")

    if attendance < 80:

        print("Reason: Attendance is below 80%.")

    if result == "FAIL":

        print("Reason: The student did not pass all subjects.")


# =================================================================
# SECTION 26: DISPLAY ACADEMIC ADVICE
# =================================================================

print("\n" + "=" * 75)

print("                 ACADEMIC ADVICE")

print("=" * 75)

# Give the student advice based on performance.

if performance == "Excellent":

    print("Excellent work! Keep maintaining your performance.")

elif performance == "Very Good":

    print("Very good! Continue improving your academic skills.")

elif performance == "Good":

    print("Good performance. Aim for a higher grade.")

elif performance == "Satisfactory":

    print("You are progressing. More practice is recommended.")

elif performance == "Needs Improvement":

    print("Increase your study time and revise difficult topics.")

else:

    print("Develop a study plan and seek academic support.")


# =================================================================
# SECTION 27: FINAL PROJECT SUMMARY
# =================================================================

print("\n" + "=" * 75)

print("       STUDENT ACADEMIC MANAGEMENT SYSTEM COMPLETED")

print("=" * 75)

print("Student Information Collection: Completed")

print("Input Validation: Completed")

print("Subject Marks Collection: Completed")

print("Total Marks Calculation: Completed")

print("Average Calculation: Completed")

print("Grade Calculation: Completed")

print("Pass/Fail Evaluation: Completed")

print("Attendance Evaluation: Completed")

print("Scholarship Evaluation: Completed")

print("Performance Classification: Completed")

print("Academic Report Generation: Completed")

print("\nTHANK YOU FOR USING OUR SYSTEM!")

print("=" * 75)


# =================================================================
# END OF DAY 010 - CHALLENGE.PY
# =================================================================
