
# =====================================================================
# DAY 011 - PYTHON NESTED CONDITIONS
# PRACTICAL PROGRAMMING CHALLENGE
#
# PROJECT:
# UNIVERSITY ADMISSION AND STUDENT ELIGIBILITY SYSTEM
#
# BACHELOR'S IN ARTIFICIAL INTELLIGENCE
# 90-DAY PYTHON PROGRAMMING JOURNEY
#
# CONCEPTS USED:
# 1. Variables
# 2. Data types
# 3. User input
# 4. Type conversion
# 5. Nested if statements
# 6. if-elif-else statements
# 7. Logical operators
# 8. Comparison operators
# 9. Boolean values
# 10. Functions
# 11. Lists
# 12. Input validation
# 13. String methods
#
# =====================================================================


# =====================================================================
# SECTION 1: PROJECT INTRODUCTION
# =====================================================================

print("=" * 70)

print("       UNIVERSITY ADMISSION MANAGEMENT SYSTEM")

print("=" * 70)

print("Welcome to the University Admission Portal.")

print("Please provide the requested information.")

print("=" * 70)


# =====================================================================
# SECTION 2: STUDENT INFORMATION
# =====================================================================

# input() collects information from the student.
#
# strip() removes unnecessary spaces.
#
# The student's name is stored as a string.

student_name = input("\nEnter your full name: ").strip()

# Collect the student's age.
#
# int() converts the input string into an integer.

try:

    student_age = int(input("Enter your age: "))

except ValueError:

    print("Invalid age. Please enter a whole number.")

    student_age = -1


# Collect the student's examination marks.
#
# float() allows decimal values such as 85.5.

try:

    entrance_marks = float(
        input("Enter your entrance examination marks: ")
    )

except ValueError:

    print("Invalid marks entered.")

    entrance_marks = -1


# Collect attendance percentage.

try:

    attendance = float(
        input("Enter your attendance percentage: ")
    )

except ValueError:

    print("Invalid attendance entered.")

    attendance = -1


# Collect interview result.
#
# lower() converts the answer into lowercase.
#
# Therefore YES, Yes and yes become yes.

interview_result = input(
    "Did you pass the interview? (yes/no): "
).strip().lower()


# Collect document verification status.

documents = input(
    "Have you submitted all required documents? (yes/no): "
).strip().lower()


# =====================================================================
# SECTION 3: INITIALIZE STUDENT STATUS
# =====================================================================

# We create Boolean variables to track each requirement.
#
# Initially, every requirement is False.
#
# If the student satisfies a requirement,
# we change the corresponding variable to True.

age_eligible = False

marks_eligible = False

attendance_eligible = False

interview_eligible = False

documents_eligible = False

admission_approved = False

scholarship_approved = False


# =====================================================================
# SECTION 4: INPUT VALIDATION
# =====================================================================

print("\n" + "=" * 70)

print("             INPUT VALIDATION")

print("=" * 70)


# Before evaluating admission requirements,
# we must check whether the information is valid.
#
# Age cannot be negative.
# Entrance marks must be between 0 and 100.
# Attendance must be between 0 and 100.

if student_name:

    print("Student name: Valid.")

    if student_age >= 0:

        print("Student age: Valid.")

        if 0 <= entrance_marks <= 100:

            print("Entrance marks: Valid.")

            if 0 <= attendance <= 100:

                print("Attendance: Valid.")

                if interview_result in ["yes", "no"]:

                    print("Interview response: Valid.")

                    if documents in ["yes", "no"]:

                        print("Document response: Valid.")

                        input_valid = True

                    else:

                        print("Invalid document response.")

                        input_valid = False

                else:

                    print("Invalid interview response.")

                    input_valid = False

            else:

                print("Attendance must be between 0 and 100.")

                input_valid = False

        else:

            print("Marks must be between 0 and 100.")

            input_valid = False

    else:

        print("Age cannot be negative.")

        input_valid = False

else:

    print("Student name cannot be empty.")

    input_valid = False


# =====================================================================
# SECTION 5: ADMISSION ELIGIBILITY EVALUATION
# =====================================================================

print("\n" + "=" * 70)

print("          ADMISSION ELIGIBILITY EVALUATION")

print("=" * 70)


# We only evaluate admission requirements
# when all collected information is valid.

if input_valid:

    print("Evaluating student eligibility...\n")

    # ---------------------------------------------------------------
    # LEVEL 1: AGE REQUIREMENT
    # ---------------------------------------------------------------

    # The university requires students to be
    # at least 18 years old.

    if student_age >= 18:

        age_eligible = True

        print("AGE REQUIREMENT: PASSED")

        # -----------------------------------------------------------
        # LEVEL 2: ENTRANCE EXAMINATION
        # -----------------------------------------------------------

        # The student must score at least 60%.

        if entrance_marks >= 60:

            marks_eligible = True

            print("ENTRANCE EXAMINATION: PASSED")

            # -------------------------------------------------------
            # LEVEL 3: ATTENDANCE REQUIREMENT
            # -------------------------------------------------------

            # Minimum required attendance is 75%.

            if attendance >= 75:

                attendance_eligible = True

                print("ATTENDANCE REQUIREMENT: PASSED")

                # ---------------------------------------------------
                # LEVEL 4: INTERVIEW
                # ---------------------------------------------------

                if interview_result == "yes":

                    interview_eligible = True

                    print("INTERVIEW: PASSED")

                    # -----------------------------------------------
                    # LEVEL 5: DOCUMENT VERIFICATION
                    # -----------------------------------------------

                    if documents == "yes":

                        documents_eligible = True

                        admission_approved = True

                        print("DOCUMENT VERIFICATION: PASSED")

                        print("\nADMISSION APPROVED!")

                    else:

                        print("DOCUMENT VERIFICATION: FAILED")

                        print("Please submit missing documents.")

                else:

                    print("INTERVIEW: FAILED")

                    print("Admission requirements not satisfied.")

            else:

                print("ATTENDANCE REQUIREMENT: FAILED")

                print("Minimum attendance is 75%.")

        else:

            print("ENTRANCE EXAMINATION: FAILED")

            print("Minimum entrance marks are 60%.")

    else:

        print("AGE REQUIREMENT: FAILED")

        print("Minimum age requirement is 18 years.")

else:

    print("Admission evaluation stopped.")

    print("Please correct the invalid information.")


# =====================================================================
# SECTION 6: SCHOLARSHIP EVALUATION
# =====================================================================

print("\n" + "=" * 70)

print("             SCHOLARSHIP EVALUATION")

print("=" * 70)


# Scholarship requirements:
#
# 1. Admission must be approved.
# 2. Marks must be at least 85%.
# 3. Attendance must be at least 90%.
#
# These are illustrative university rules.

if admission_approved:

    print("Student has received admission.")

    if entrance_marks >= 85:

        print("Academic scholarship requirement passed.")

        if attendance >= 90:

            scholarship_approved = True

            print("Attendance scholarship requirement passed.")

            print("\nSCHOLARSHIP APPROVED!")

        else:

            print("Scholarship rejected: Attendance below 90%.")

    else:

        print("Scholarship rejected: Marks below 85%.")

else:

    print("Scholarship evaluation unavailable.")

    print("Student must first qualify for admission.")


# =====================================================================
# SECTION 7: ACADEMIC GRADE CLASSIFICATION
# =====================================================================

print("\n" + "=" * 70)

print("             ACADEMIC GRADE")

print("=" * 70)


# We classify marks only when the input is valid.
#
# This grade scale is an illustrative example.

if input_valid:

    if entrance_marks >= 90:

        grade = "A+"

    elif entrance_marks >= 80:

        grade = "A"

    elif entrance_marks >= 70:

        grade = "B"

    elif entrance_marks >= 60:

        grade = "C"

    else:

        grade = "F"

    print("Entrance examination grade:", grade)

else:

    grade = "Not available"

    print("Grade cannot be calculated.")


# =====================================================================
# SECTION 8: STUDENT FINAL REPORT
# =====================================================================

print("\n" + "=" * 70)

print("               FINAL STUDENT REPORT")

print("=" * 70)


# A list stores the student's information.
#
# Lists allow us to organize multiple values
# under one variable.

student_information = [

    student_name,

    student_age,

    entrance_marks,

    attendance,

    grade

]


# Print the student information.

if input_valid:

    print("Student Name:", student_information[0])

    print("Student Age:", student_information[1])

    print("Entrance Marks:", student_information[2])

    print("Attendance:", student_information[3], "%")

    print("Academic Grade:", student_information[4])

    print("-" * 70)

    # Final admission status.

    if admission_approved:

        print("Admission Status: APPROVED")

    else:

        print("Admission Status: NOT APPROVED")

    # Final scholarship status.

    if scholarship_approved:

        print("Scholarship Status: APPROVED")

    else:

        print("Scholarship Status: NOT APPROVED")

else:

    print("Student report cannot be generated.")

    print("Please provide valid information.")


# =====================================================================
# SECTION 9: REQUIREMENT CHECKLIST
# =====================================================================

print("\n" + "=" * 70)

print("              REQUIREMENT CHECKLIST")

print("=" * 70)


# We store requirement names and their Boolean results.
#
# True means the requirement was satisfied.
# False means it was not satisfied.

requirements = [

    ("Age Requirement", age_eligible),

    ("Entrance Marks", marks_eligible),

    ("Attendance", attendance_eligible),

    ("Interview", interview_eligible),

    ("Documents", documents_eligible)

]


# The loop displays each requirement.
#
# This avoids writing five separate print statements.

if input_valid:

    for requirement, status in requirements:

        if status:

            print(requirement, ": PASSED")

        else:

            print(requirement, ": NOT PASSED")

else:

    print("Checklist unavailable because input was invalid.")


# =====================================================================
# SECTION 10: FINAL PROJECT SUMMARY
# =====================================================================

print("\n" + "=" * 70)

print("             PROJECT COMPLETED")

print("=" * 70)


if admission_approved and scholarship_approved:

    print("Congratulations!")

    print("You have received admission and a scholarship.")

elif admission_approved:

    print("Congratulations!")

    print("You have received university admission.")

    print("You do not qualify for the example scholarship.")

else:

    print("Admission was not approved.")

    print("Please review the admission requirements.")


print("\nThank you for using the University Admission System.")

print("=" * 70)


# =====================================================================
# END OF DAY 011 - CHALLENGE.PY
# =====================================================================
