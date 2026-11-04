
# =====================================================================
# DAY 011 - PYTHON NESTED CONDITIONS
#
# Bachelor's in Artificial Intelligence
# 90-Day Python Programming Journey
#
# MAIN TOPIC: NESTED CONDITIONAL STATEMENTS
#
# LEARNING OBJECTIVES:
# 1. Understand nested if statements.
# 2. Understand nested if-else statements.
# 3. Understand multiple levels of conditions.
# 4. Combine nested conditions with logical operators.
# 5. Use nested conditions with user input.
# 6. Validate information using nested conditions.
# 7. Build practical decision-making programs.
#
# =====================================================================


# =====================================================================
# SECTION 1: INTRODUCTION TO NESTED CONDITIONS
# =====================================================================

# A nested condition is a conditional statement
# written inside another conditional statement.
#
# The inner condition is checked only when Python
# reaches that particular section of the outer condition.
#
# Example:
#
# if condition_1:
#
#     if condition_2:
#
#         print("Both conditions satisfied.")
#
# The second if statement is INSIDE the first if statement.


print("\n" + "=" * 70)
print("SECTION 1: INTRODUCTION TO NESTED CONDITIONS")
print("=" * 70)


age = 23

has_id = True

# FIRST CONDITION:
# Check whether the person's age is at least 18.

if age >= 18:

    print("Age requirement satisfied.")

    # SECOND CONDITION:
    # This condition is inside the first condition.
    # Python checks it only if age >= 18 is True.

    if has_id:

        print("Identity verified.")

        print("Access granted.")

    else:

        # This else belongs to the INNER if statement.

        print("Identity verification failed.")

else:

    # This else belongs to the OUTER if statement.

    print("Age requirement not satisfied.")

    print("Access denied.")


# =====================================================================
# SECTION 2: NESTED IF-ELSE STATEMENTS
# =====================================================================

# We can use if-else inside another if-else structure.
#
# The outer condition makes the first decision.
# The inner condition makes a second decision.
#
# Each else belongs to the nearest unmatched if
# at the same indentation level.


print("\n" + "=" * 70)
print("SECTION 2: NESTED IF-ELSE")
print("=" * 70)


marks = 85

attendance = 90

# First, check examination marks.

if marks >= 50:

    print("Student passed the examination.")

    # If the student passes, check attendance.

    if attendance >= 75:

        print("Attendance requirement satisfied.")

        print("Student qualifies for the next stage.")

    else:

        print("Attendance requirement not satisfied.")

else:

    print("Student failed the examination.")

    print("Student does not qualify for the next stage.")


# =====================================================================
# SECTION 3: MULTIPLE LEVELS OF NESTED CONDITIONS
# =====================================================================

# Nested conditions can contain more than two levels.
#
# Each additional indentation level represents
# another level of decision-making.
#
# Here we check:
#
# 1. Age.
# 2. University entrance examination.
# 3. Interview performance.
#
# The next condition is checked only after
# satisfying the previous requirement.


print("\n" + "=" * 70)
print("SECTION 3: MULTIPLE LEVELS OF NESTED CONDITIONS")
print("=" * 70)


age = 22

entrance_marks = 85

interview_passed = True


# LEVEL 1: AGE REQUIREMENT

if age >= 18:

    print("Level 1: Age requirement satisfied.")

    # LEVEL 2: ENTRANCE EXAMINATION

    if entrance_marks >= 70:

        print("Level 2: Entrance examination passed.")

        # LEVEL 3: INTERVIEW

        if interview_passed:

            print("Level 3: Interview passed.")

            print("FINAL RESULT: University admission approved.")

        else:

            print("Interview failed.")

            print("Admission rejected.")

    else:

        print("Entrance examination failed.")

        print("Admission rejected.")

else:

    print("Age requirement not satisfied.")

    print("Admission rejected.")


# =====================================================================
# SECTION 4: NESTED CONDITIONS WITH AND OPERATOR
# =====================================================================

# The AND operator requires BOTH conditions to be True.
#
# We can also use AND inside nested conditions.
#
# Example:
#
# A student must pass mathematics AND physics.
# After passing both subjects, attendance is checked.


print("\n" + "=" * 70)
print("SECTION 4: NESTED CONDITIONS WITH AND")
print("=" * 70)


mathematics = 85

physics = 78

attendance = 90


# OUTER CONDITION:
# Both mathematics and physics must be passed.

if mathematics >= 50 and physics >= 50:

    print("Both subjects passed.")

    # INNER CONDITION:
    # Now check attendance.

    if attendance >= 75:

        print("Attendance requirement satisfied.")

        print("Student meets all academic requirements.")

    else:

        print("Attendance requirement not satisfied.")

else:

    print("Student failed at least one subject.")


# =====================================================================
# SECTION 5: NESTED CONDITIONS WITH OR OPERATOR
# =====================================================================

# OR returns True when at least one condition is True.
#
# Here a user can verify identity using:
#
# 1. Registered email.
# 2. Registered phone number.
#
# If either is available, we perform another check.


print("\n" + "=" * 70)
print("SECTION 5: NESTED CONDITIONS WITH OR")
print("=" * 70)


has_email = False

has_phone = True

otp_verified = True


# OUTER CONDITION:
# At least one contact method must be available.

if has_email or has_phone:

    print("Contact information available.")

    # INNER CONDITION:
    # Verify the one-time password.

    if otp_verified:

        print("OTP verification successful.")

        print("Account verification completed.")

    else:

        print("OTP verification failed.")

else:

    print("No contact information available.")

    print("Verification cannot continue.")


# =====================================================================
# SECTION 6: NESTED CONDITIONS WITH NOT OPERATOR
# =====================================================================

# NOT reverses a Boolean value.
#
# not True = False
# not False = True
#
# We use NOT to check whether an account is NOT blocked.


print("\n" + "=" * 70)
print("SECTION 6: NESTED CONDITIONS WITH NOT")
print("=" * 70)


account_blocked = False

password_correct = True


if not account_blocked:

    print("Account is active.")

    if password_correct:

        print("Password is correct.")

        print("Login successful.")

    else:

        print("Incorrect password.")

else:

    print("Account is blocked.")

    print("Please contact support.")


# =====================================================================
# SECTION 7: NESTED CONDITIONS WITH USER INPUT
# =====================================================================

# input() allows users to provide information.
#
# int() converts numerical text into an integer.
#
# try-except prevents the program from crashing
# when the user enters an invalid numerical value.


print("\n" + "=" * 70)
print("SECTION 7: NESTED CONDITIONS WITH USER INPUT")
print("=" * 70)


try:

    age = int(input("Enter your age: "))

    if age >= 18:

        print("You meet the age requirement.")

        has_id = input("Do you have an identity card? (yes/no): ")

        # strip() removes surrounding spaces.
        # lower() converts text into lowercase.

        has_id = has_id.strip().lower()

        if has_id == "yes":

            print("Identity card confirmed.")

            print("You may proceed.")

        elif has_id == "no":

            print("Identity card required.")

        else:

            print("Invalid identity card response.")

    elif age >= 0:

        print("You are below 18.")

    else:

        print("Age cannot be negative.")

except ValueError:

    print("Invalid input. Enter your age as a whole number.")


# =====================================================================
# SECTION 8: NESTED CONDITIONS FOR STUDENT GRADING
# =====================================================================

# This example evaluates academic performance.
#
# First, the program checks whether marks are valid.
# Then it determines whether the student passed.
# Finally, it assigns an academic grade.
#
# This demonstrates how one decision can lead
# to another decision.


print("\n" + "=" * 70)
print("SECTION 8: NESTED STUDENT GRADING SYSTEM")
print("=" * 70)


marks = 87


if marks >= 0 and marks <= 100:

    print("Marks are valid.")

    if marks >= 50:

        print("Student passed.")

        if marks >= 90:

            grade = "A+"

        elif marks >= 80:

            grade = "A"

        elif marks >= 70:

            grade = "B"

        elif marks >= 60:

            grade = "C"

        else:

            grade = "D"

        print("Student grade:", grade)

    else:

        print("Student failed.")

        grade = "F"

        print("Student grade:", grade)

else:

    print("Invalid marks. Marks must be between 0 and 100.")


# =====================================================================
# SECTION 9: NESTED CONDITIONS FOR A BANK ATM
# =====================================================================

# Imagine a simplified ATM system.
#
# The user must:
#
# 1. Enter the correct PIN.
# 2. Have an active account.
# 3. Have sufficient balance.
#
# Each condition depends on the previous condition.
#
# This is an example of nested decision-making.


print("\n" + "=" * 70)
print("SECTION 9: BANK ATM SYSTEM")
print("=" * 70)


correct_pin = "1234"

entered_pin = "1234"

account_active = True

balance = 5000

withdrawal = 2000


if entered_pin == correct_pin:

    print("PIN verified.")

    if account_active:

        print("Account is active.")

        if withdrawal > 0:

            print("Withdrawal amount is valid.")

            if withdrawal <= balance:

                balance = balance - withdrawal

                print("Withdrawal successful.")

                print("Remaining balance:", balance)

            else:

                print("Insufficient account balance.")

        else:

            print("Invalid withdrawal amount.")

    else:

        print("Your account is inactive.")

else:

    print("Incorrect PIN.")

    print("Transaction cancelled.")


# =====================================================================
# SECTION 10: NESTED CONDITIONS FOR TRIANGLE CLASSIFICATION
# =====================================================================

# Three sides must satisfy the triangle inequality.
#
# The sum of any two sides must be greater
# than the third side.
#
# After checking validity, we classify the triangle.
#
# Equilateral: Three equal sides.
# Isosceles: Exactly two equal sides.
# Scalene: Three different sides.


print("\n" + "=" * 70)
print("SECTION 10: TRIANGLE CLASSIFICATION")
print("=" * 70)


a = 5

b = 5

c = 8


# FIRST: CHECK THAT ALL SIDES ARE POSITIVE.

if a > 0 and b > 0 and c > 0:

    print("All sides are positive.")

    # SECOND: CHECK THE TRIANGLE INEQUALITY.

    if a + b > c and a + c > b and b + c > a:

        print("Valid triangle.")

        # THIRD: CLASSIFY THE TRIANGLE.

        if a == b and b == c:

            print("Equilateral triangle.")

        elif a == b or a == c or b == c:

            print("Isosceles triangle.")

        else:

            print("Scalene triangle.")

    else:

        print("These sides cannot form a triangle.")

else:

    print("Invalid side lengths.")


# =====================================================================
# SECTION 11: NESTED CONDITIONS FOR TEMPERATURE CLASSIFICATION
# =====================================================================

# The program checks whether the temperature is valid.
#
# If it is valid, it determines the temperature category.
#
# This example demonstrates a validation condition
# followed by another decision-making structure.


print("\n" + "=" * 70)
print("SECTION 11: TEMPERATURE CLASSIFICATION")
print("=" * 70)


temperature = 32


if temperature >= -50 and temperature <= 60:

    print("Temperature reading is valid.")

    if temperature < 10:

        print("Cold temperature.")

    elif temperature < 25:

        print("Moderate temperature.")

    elif temperature < 35:

        print("Warm temperature.")

    else:

        print("Hot temperature.")

else:

    print("Temperature reading is outside the example range.")


# =====================================================================
# SECTION 12: NESTED CONDITIONS FOR SCHOLARSHIP ELIGIBILITY
# =====================================================================

# Example scholarship requirements:
#
# 1. Average marks must be at least 85.
# 2. Attendance must be at least 80%.
# 3. The student must pass all subjects.
#
# We check each requirement separately.
#
# These are illustrative eligibility rules.


print("\n" + "=" * 70)
print("SECTION 12: SCHOLARSHIP ELIGIBILITY")
print("=" * 70)


average_marks = 90

attendance = 85

all_subjects_passed = True


if average_marks >= 85:

    print("Academic requirement satisfied.")

    if attendance >= 80:

        print("Attendance requirement satisfied.")

        if all_subjects_passed:

            print("All subjects passed.")

            print("SCHOLARSHIP APPROVED!")

        else:

            print("Scholarship rejected: Subject requirement failed.")

    else:

        print("Scholarship rejected: Attendance is insufficient.")

else:

    print("Scholarship rejected: Academic average is insufficient.")


# =====================================================================
# SECTION 13: NESTED CONDITIONS WITH FOR LOOPS
# =====================================================================

# A loop can contain conditional statements.
#
# This example checks each student's marks.
#
# The for loop processes each student's marks.
# The nested if statement classifies the result.


print("\n" + "=" * 70)
print("SECTION 13: NESTED CONDITIONS WITH FOR LOOPS")
print("=" * 70)


student_marks = [95, 82, 65, 42, 30]


for marks in student_marks:

    print("\nChecking student marks:", marks)

    if marks >= 50:

        print("Result: PASS")

        if marks >= 90:

            print("Performance: Excellent")

        elif marks >= 80:

            print("Performance: Very Good")

        elif marks >= 70:

            print("Performance: Good")

        else:

            print("Performance: Satisfactory")

    else:

        print("Result: FAIL")

        print("Performance: Needs Improvement")


# =====================================================================
# SECTION 14: NESTED CONDITIONS FOR USER ACCOUNT VERIFICATION
# =====================================================================

# A simplified account verification example.
#
# First check whether the username exists.
# Then check the password.
# Then check whether the account is active.
#
# Each decision depends on the previous one.


print("\n" + "=" * 70)
print("SECTION 14: ACCOUNT VERIFICATION")
print("=" * 70)


stored_username = "student"

stored_password = "python123"

entered_username = "student"

entered_password = "python123"

account_active = True


if entered_username == stored_username:

    print("Username recognized.")

    if entered_password == stored_password:

        print("Password accepted.")

        if account_active:

            print("Account is active.")

            print("Welcome to the system.")

        else:

            print("Account is inactive.")

    else:

        print("Incorrect password.")

else:

    print("Username not found.")


# IMPORTANT:
# This is a basic educational example.
# Real systems should never store plaintext passwords.


# =====================================================================
# SECTION 15: NESTED CONDITIONS WITH MEMBERSHIP OPERATORS
# =====================================================================

# The IN operator checks whether a value
# exists inside a sequence.
#
# We first check whether the requested course exists.
# Then we check whether the student is enrolled.


print("\n" + "=" * 70)
print("SECTION 15: MEMBERSHIP WITH NESTED CONDITIONS")
print("=" * 70)


available_courses = [

    "Python",

    "Machine Learning",

    "Deep Learning",

    "Computer Vision"

]

selected_course = "Machine Learning"

enrolled = True


if selected_course in available_courses:

    print("Course is available.")

    if enrolled:

        print("Student is enrolled.")

        print("Course access granted.")

    else:

        print("Student must enroll first.")

else:

    print("Selected course is unavailable.")


# =====================================================================
# SECTION 16: NESTED CONDITIONS WITH FUNCTIONS
# =====================================================================

# Functions allow us to organize our decision-making logic.
#
# This function checks a student's eligibility.
#
# It returns a result rather than printing
# every decision inside the function.


print("\n" + "=" * 70)
print("SECTION 16: NESTED CONDITIONS WITH FUNCTIONS")
print("=" * 70)


def check_student_eligibility(age, marks, attendance):

    # FIRST CONDITION: AGE

    if age >= 18:

        # SECOND CONDITION: MARKS

        if marks >= 50:

            # THIRD CONDITION: ATTENDANCE

            if attendance >= 75:

                return "Eligible"

            else:

                return "Attendance requirement not met."

        else:

            return "Academic requirement not met."

    else:

        return "Age requirement not met."


student_result = check_student_eligibility(

    age=22,

    marks=85,

    attendance=90

)

print("Student eligibility:", student_result)


# =====================================================================
# SECTION 17: NESTED CONDITIONS AND INPUT VALIDATION
# =====================================================================

# A good program should validate information.
#
# We first check whether a number is positive.
# If it is positive, we check whether it is even or odd.
#
# Notice how we avoid performing the inner check
# when the outer requirement is not satisfied.


print("\n" + "=" * 70)
print("SECTION 17: INPUT VALIDATION")
print("=" * 70)


number = 24


if number > 0:

    print("Number is positive.")

    if number % 2 == 0:

        print("Number is even.")

    else:

        print("Number is odd.")

else:

    if number == 0:

        print("Number is zero.")

    else:

        print("Number is negative.")


# =====================================================================
# SECTION 18: NESTED CONDITIONS FOR AN AI RULE-BASED SYSTEM
# =====================================================================

# IMPORTANT AI CONNECTION:
#
# This example represents a simple rule-based decision system.
#
# It evaluates a student's performance using predefined rules.
#
# It is NOT a trained Machine Learning model.
#
# Machine Learning models learn patterns from data.
# Rule-based systems follow manually defined conditions.


print("\n" + "=" * 70)
print("SECTION 18: RULE-BASED DECISION SYSTEM")
print("=" * 70)


marks = 88

attendance = 90

assignment_completed = True


if marks >= 50:

    print("Examination passed.")

    if attendance >= 75:

        print("Attendance requirement satisfied.")

        if assignment_completed:

            print("Assignment completed.")

            if marks >= 85:

                print("FINAL CLASSIFICATION: HIGH PERFORMANCE")

            else:

                print("FINAL CLASSIFICATION: SATISFACTORY PERFORMANCE")

        else:

            print("Assignment is incomplete.")

    else:

        print("Attendance requirement not satisfied.")

else:

    print("FINAL CLASSIFICATION: ACADEMIC SUPPORT REQUIRED")


# =====================================================================
# SECTION 19: NESTED CONDITIONS WITH BOOLEAN VARIABLES
# =====================================================================

# Boolean variables store True or False.
#
# They are useful for representing states
# such as whether something is available or completed.


print("\n" + "=" * 70)
print("SECTION 19: BOOLEAN VARIABLES")
print("=" * 70)


internet_available = True

server_available = True

application_running = False


if internet_available:

    print("Internet connection available.")

    if server_available:

        print("Server is available.")

        if application_running:

            print("Application is running.")

        else:

            print("Application needs to be started.")

    else:

        print("Server is unavailable.")

else:

    print("No internet connection.")


# =====================================================================
# SECTION 20: NESTED CONDITIONS AND COMPARISON OPERATORS
# =====================================================================

# We can use all comparison operators inside nested
# conditional structures.
#
# This example determines whether a person
# falls within a particular example age category.


print("\n" + "=" * 70)
print("SECTION 20: COMPARISON OPERATORS")
print("=" * 70)


age = 25


if age >= 0:

    if age < 18:

        print("Minor.")

    elif age >= 18 and age <= 59:

        print("Adult.")

    else:

        print("Senior adult.")

else:

    print("Invalid age.")


# =====================================================================
# SECTION 21: FINAL REVISION EXAMPLE
# =====================================================================

# This example combines the most important
# concepts from today's lesson.
#
# It uses:
#
# 1. Nested if statements.
# 2. if-elif-else.
# 3. AND operator.
# 4. OR operator.
# 5. Boolean variables.
# 6. Comparison operators.
#
# This is a complete rule-based decision example.


print("\n" + "=" * 70)
print("SECTION 21: FINAL REVISION")
print("=" * 70)


age = 21

marks = 92

attendance = 88

has_identity_card = True


if age >= 18:

    print("Age requirement satisfied.")

    if has_identity_card:

        print("Identity verified.")

        if marks >= 50 and attendance >= 75:

            print("Academic requirements satisfied.")

            if marks >= 90:

                print("Academic grade: A+")

            elif marks >= 80:

                print("Academic grade: A")

            elif marks >= 70:

                print("Academic grade: B")

            else:

                print("Academic grade: C or D")

            print("FINAL RESULT: APPROVED")

        else:

            print("Academic requirements not satisfied.")

    else:

        print("Identity card is required.")

else:

    print("Age requirement not satisfied.")


# =====================================================================
# FINAL LESSON SUMMARY
# =====================================================================


print("\n" + "=" * 70)

print("DAY 011 - PYTHON NESTED CONDITIONS")

print("=" * 70)

print("1. Introduction to Nested Conditions - Completed")

print("2. Nested If-Else Statements - Completed")

print("3. Multiple Levels of Conditions - Completed")

print("4. Nested Conditions with AND - Completed")

print("5. Nested Conditions with OR - Completed")

print("6. Nested Conditions with NOT - Completed")

print("7. Nested Conditions with User Input - Completed")

print("8. Nested Student Grading System - Completed")

print("9. Bank ATM Decision System - Completed")

print("10. Triangle Classification - Completed")

print("11. Temperature Classification - Completed")

print("12. Scholarship Eligibility - Completed")

print("13. Nested Conditions with Loops - Completed")

print("14. Account Verification - Completed")

print("15. Membership Operators - Completed")

print("16. Nested Conditions with Functions - Completed")

print("17. Input Validation - Completed")

print("18. Rule-Based Decision System - Completed")

print("19. Boolean Variables - Completed")

print("20. Comparison Operators - Completed")

print("21. Final Revision - Completed")


print("\nALL DAY 011 LESSON EXAMPLES COMPLETED!")

print("=" * 70)


# =====================================================================
# END OF DAY 011 - NESTED_CONDITIONS.PY
# =====================================================================
