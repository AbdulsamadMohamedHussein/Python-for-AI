
# =====================================================================
# DAY 011 - PYTHON NESTED CONDITIONS
# COMPLETE SOLVED EXERCISES
#
# Bachelor's in Artificial Intelligence
# 90-Day Python Programming Journey
#
# TOTAL: 30 SOLVED EXERCISES
#
# TOPICS:
# 1. Basic nested if statements
# 2. Nested if-else statements
# 3. Multiple levels of conditions
# 4. Logical operators
# 5. Comparison operators
# 6. Boolean values
# 7. User input and validation
# 8. Nested conditions with loops
# 9. Nested conditions with functions
# 10. Practical decision-making systems
#
# =====================================================================


# =====================================================================
# EXERCISE 1: AGE AND IDENTITY VERIFICATION
# =====================================================================

# QUESTION:
# Check whether a person is at least 18 years old.
# If they are 18 or older, check whether they have an ID.
#
# EXPLANATION:
# The first condition checks the person's age.
# The second condition is nested inside the first.
# The second condition executes only if the age
# requirement is satisfied.

print("\n" + "=" * 70)
print("EXERCISE 1: AGE AND IDENTITY VERIFICATION")
print("=" * 70)

age = 23
has_id = True

if age >= 18:

    print("Age requirement satisfied.")

    if has_id:

        print("Identity verified.")
        print("Access granted.")

    else:

        print("Please provide your identity card.")

else:

    print("You are below 18.")
    print("Access denied.")


# =====================================================================
# EXERCISE 2: STUDENT PASS AND ATTENDANCE CHECK
# =====================================================================

# QUESTION:
# A student must score at least 50 marks.
# If the student passes, check whether attendance
# is at least 75%.
#
# EXPLANATION:
# The outer condition checks examination marks.
# The inner condition checks attendance.

print("\n" + "=" * 70)
print("EXERCISE 2: PASS AND ATTENDANCE")
print("=" * 70)

marks = 75
attendance = 85

if marks >= 50:

    print("Student passed.")

    if attendance >= 75:

        print("Attendance requirement satisfied.")
        print("Student is eligible.")

    else:

        print("Attendance is insufficient.")

else:

    print("Student failed.")


# =====================================================================
# EXERCISE 3: LOGIN SYSTEM
# =====================================================================

# QUESTION:
# Check username first.
# If username is correct, check the password.
#
# EXPLANATION:
# The password is checked only after
# the username has been verified.
#
# This is an educational example, not secure
# production authentication.

print("\n" + "=" * 70)
print("EXERCISE 3: LOGIN SYSTEM")
print("=" * 70)

correct_username = "student"
correct_password = "python123"

entered_username = "student"
entered_password = "python123"

if entered_username == correct_username:

    print("Username verified.")

    if entered_password == correct_password:

        print("Password verified.")
        print("Login successful.")

    else:

        print("Incorrect password.")

else:

    print("Incorrect username.")


# =====================================================================
# EXERCISE 4: POSITIVE NUMBER AND EVEN OR ODD
# =====================================================================

# QUESTION:
# First check whether a number is positive.
# If positive, determine whether it is even or odd.
#
# EXPLANATION:
# The modulo operator (%) returns the remainder.
# Even numbers have a remainder of zero when divided by 2.

print("\n" + "=" * 70)
print("EXERCISE 4: POSITIVE AND EVEN OR ODD")
print("=" * 70)

number = 24

if number > 0:

    print("Positive number.")

    if number % 2 == 0:

        print("Even number.")

    else:

        print("Odd number.")

else:

    if number == 0:

        print("Number is zero.")

    else:

        print("Negative number.")


# =====================================================================
# EXERCISE 5: LARGEST OF THREE NUMBERS USING NESTED CONDITIONS
# =====================================================================

# QUESTION:
# Find the largest number among three numbers.
#
# EXPLANATION:
# First compare the first number with the second.
# Then use a nested condition to compare the winner
# with the third number.
#
# This example also handles equal numbers.

print("\n" + "=" * 70)
print("EXERCISE 5: LARGEST OF THREE NUMBERS")
print("=" * 70)

a = 45
b = 80
c = 60

if a >= b:

    if a >= c:

        largest = a

    else:

        largest = c

else:

    if b >= c:

        largest = b

    else:

        largest = c

print("Largest number:", largest)


# =====================================================================
# EXERCISE 6: UNIVERSITY ADMISSION SYSTEM
# =====================================================================

# QUESTION:
# A student must:
# 1. Be at least 18 years old.
# 2. Score at least 70 in the entrance examination.
# 3. Pass the interview.
#
# EXPLANATION:
# Each requirement is checked after
# the previous requirement is satisfied.

print("\n" + "=" * 70)
print("EXERCISE 6: UNIVERSITY ADMISSION")
print("=" * 70)

age = 21
entrance_marks = 85
interview_passed = True

if age >= 18:

    print("Age requirement satisfied.")

    if entrance_marks >= 70:

        print("Entrance examination passed.")

        if interview_passed:

            print("Interview passed.")
            print("University admission approved.")

        else:

            print("Interview failed.")

    else:

        print("Entrance examination requirement not met.")

else:

    print("Age requirement not met.")


# =====================================================================
# EXERCISE 7: SCHOLARSHIP ELIGIBILITY
# =====================================================================

# QUESTION:
# Check scholarship eligibility.
#
# Requirements:
# Average marks >= 85
# Attendance >= 80%
# All subjects passed
#
# EXPLANATION:
# We check each condition separately using nesting.

print("\n" + "=" * 70)
print("EXERCISE 7: SCHOLARSHIP ELIGIBILITY")
print("=" * 70)

average_marks = 90
attendance = 85
all_subjects_passed = True

if average_marks >= 85:

    print("Academic requirement satisfied.")

    if attendance >= 80:

        print("Attendance requirement satisfied.")

        if all_subjects_passed:

            print("Scholarship approved!")

        else:

            print("Scholarship rejected: Subject requirement failed.")

    else:

        print("Scholarship rejected: Attendance too low.")

else:

    print("Scholarship rejected: Average too low.")


# =====================================================================
# EXERCISE 8: BANK WITHDRAWAL SYSTEM
# =====================================================================

# QUESTION:
# Check whether a customer can withdraw money.
#
# Requirements:
# 1. Correct PIN.
# 2. Active account.
# 3. Positive withdrawal amount.
# 4. Sufficient balance.
#
# EXPLANATION:
# Each condition protects the next operation.
# We only subtract money after all checks pass.

print("\n" + "=" * 70)
print("EXERCISE 8: BANK WITHDRAWAL")
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

                print("Insufficient balance.")

        else:

            print("Invalid withdrawal amount.")

    else:

        print("Account is inactive.")

else:

    print("Incorrect PIN.")


# =====================================================================
# EXERCISE 9: TEMPERATURE CLASSIFICATION
# =====================================================================

# QUESTION:
# Check whether a temperature is within
# an acceptable example range.
# If valid, classify the temperature.
#
# EXPLANATION:
# First validate the reading.
# Then classify it using nested conditions.

print("\n" + "=" * 70)
print("EXERCISE 9: TEMPERATURE CLASSIFICATION")
print("=" * 70)

temperature = 32

if temperature >= -50:

    if temperature <= 60:

        print("Temperature reading is valid.")

        if temperature < 10:

            print("Cold.")

        elif temperature < 25:

            print("Moderate.")

        elif temperature < 35:

            print("Warm.")

        else:

            print("Hot.")

    else:

        print("Temperature is too high.")

else:

    print("Temperature is too low.")


# =====================================================================
# EXERCISE 10: TRIANGLE CLASSIFICATION
# =====================================================================

# QUESTION:
# Check whether three sides form a valid triangle.
# If valid, classify the triangle.
#
# EXPLANATION:
# Triangle inequality:
# a + b > c
# a + c > b
# b + c > a
#
# Equilateral: All sides equal.
# Isosceles: Two sides equal.
# Scalene: All sides different.

print("\n" + "=" * 70)
print("EXERCISE 10: TRIANGLE CLASSIFICATION")
print("=" * 70)

a = 5
b = 5
c = 8

if a > 0 and b > 0 and c > 0:

    if a + b > c and a + c > b and b + c > a:

        print("Valid triangle.")

        if a == b and b == c:

            print("Equilateral triangle.")

        elif a == b or a == c or b == c:

            print("Isosceles triangle.")

        else:

            print("Scalene triangle.")

    else:

        print("Invalid triangle.")

else:

    print("All sides must be positive.")


# =====================================================================
# EXERCISE 11: EMPLOYEE BONUS SYSTEM
# =====================================================================

# QUESTION:
# An employee must have at least one year of service.
# If eligible, check their performance rating.
#
# EXPLANATION:
# The inner condition determines the bonus
# only after the service requirement is met.

print("\n" + "=" * 70)
print("EXERCISE 11: EMPLOYEE BONUS")
print("=" * 70)

years_of_service = 3
performance_rating = 9

if years_of_service >= 1:

    print("Service requirement satisfied.")

    if performance_rating >= 8:

        bonus = 1000
        print("Excellent performance.")
        print("Bonus:", bonus)

    else:

        bonus = 500
        print("Standard performance.")
        print("Bonus:", bonus)

else:

    print("Not eligible for a bonus.")


# =====================================================================
# EXERCISE 12: PASSWORD STRENGTH CHECK
# =====================================================================

# QUESTION:
# Check whether a password has at least 8 characters.
# If it does, check whether it contains a digit.
#
# EXPLANATION:
# len() calculates string length.
# isdigit() checks whether a character is numeric.
#
# This is a basic educational password check.

print("\n" + "=" * 70)
print("EXERCISE 12: PASSWORD CHECK")
print("=" * 70)

password = "Python123"

if len(password) >= 8:

    print("Password length accepted.")

    if any(character.isdigit() for character in password):

        print("Password contains a digit.")
        print("Basic password requirements satisfied.")

    else:

        print("Password must contain a digit.")

else:

    print("Password must contain at least 8 characters.")


# =====================================================================
# EXERCISE 13: VOTING ELIGIBILITY
# =====================================================================

# QUESTION:
# Check whether a person is at least 18 years old.
# If yes, check whether they are registered.
#
# EXPLANATION:
# Both conditions are necessary in this example.
# Actual voting rules depend on local laws.

print("\n" + "=" * 70)
print("EXERCISE 13: VOTING ELIGIBILITY")
print("=" * 70)

age = 25
registered = True

if age >= 18:

    print("Age requirement satisfied.")

    if registered:

        print("Registration confirmed.")
        print("Voting requirements satisfied.")

    else:

        print("Please register first.")

else:

    print("You do not meet the age requirement.")


# =====================================================================
# EXERCISE 14: COURSE ENROLLMENT SYSTEM
# =====================================================================

# QUESTION:
# Check whether a course exists.
# If available, check whether the student has enrolled.

print("\n" + "=" * 70)
print("EXERCISE 14: COURSE ENROLLMENT")
print("=" * 70)

courses = ["Python", "Machine Learning", "Deep Learning"]

selected_course = "Python"
enrolled = True

if selected_course in courses:

    print("Course is available.")

    if enrolled:

        print("Student is enrolled.")
        print("Course access granted.")

    else:

        print("Please enroll first.")

else:

    print("Course is unavailable.")


# =====================================================================
# EXERCISE 15: WEATHER DECISION SYSTEM
# =====================================================================

# QUESTION:
# Check whether it is raining.
# If it is not raining, check the temperature.
#
# EXPLANATION:
# The inner decision depends on the weather condition.

print("\n" + "=" * 70)
print("EXERCISE 15: WEATHER DECISION")
print("=" * 70)

is_raining = False
temperature = 25

if is_raining:

    print("It is raining.")
    print("Take an umbrella.")

else:

    print("It is not raining.")

    if temperature >= 30:

        print("It is hot. Wear light clothing.")

    else:

        print("Weather is suitable for going outside.")


# =====================================================================
# EXERCISE 16: NESTED CONDITIONS WITH A FOR LOOP
# =====================================================================

# QUESTION:
# Classify the marks of multiple students.
#
# EXPLANATION:
# The for loop processes each mark.
# The nested if statement classifies each result.

print("\n" + "=" * 70)
print("EXERCISE 16: MULTIPLE STUDENT RESULTS")
print("=" * 70)

student_marks = [95, 82, 65, 45, 30]

for marks in student_marks:

    print("\nStudent marks:", marks)

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
# EXERCISE 17: NESTED CONDITIONS WITH A FUNCTION
# =====================================================================

# QUESTION:
# Create a function that checks a student's eligibility.
#
# EXPLANATION:
# Functions allow us to reuse decision-making logic.
# return sends the result back to the calling code.

print("\n" + "=" * 70)
print("EXERCISE 17: STUDENT ELIGIBILITY FUNCTION")
print("=" * 70)


def check_eligibility(age, marks, attendance):

    if age >= 18:

        if marks >= 50:

            if attendance >= 75:

                return "Eligible"

            else:

                return "Insufficient attendance"

        else:

            return "Failed examination"

    else:

        return "Age requirement not met"


result = check_eligibility(22, 85, 90)

print("Eligibility result:", result)


# =====================================================================
# EXERCISE 18: NESTED CONDITIONS WITH BOOLEAN VARIABLES
# =====================================================================

# QUESTION:
# Check internet, server and application status.
#
# EXPLANATION:
# Boolean variables store True or False.
# Each condition is checked only after
# the previous requirement is satisfied.

print("\n" + "=" * 70)
print("EXERCISE 18: SYSTEM STATUS")
print("=" * 70)

internet_available = True
server_available = True
application_running = False

if internet_available:

    print("Internet available.")

    if server_available:

        print("Server available.")

        if application_running:

            print("Application running.")

        else:

            print("Application needs to start.")

    else:

        print("Server unavailable.")

else:

    print("Internet connection unavailable.")


# =====================================================================
# EXERCISE 19: CHECK LEAP YEAR WITH NESTED CONDITIONS
# =====================================================================

# QUESTION:
# Determine whether a year is a leap year.
#
# RULE:
# A year divisible by 400 is a leap year.
# Otherwise, a year divisible by 100 is not.
# Otherwise, a year divisible by 4 is a leap year.
#
# EXPLANATION:
# The order of these nested checks is important.

print("\n" + "=" * 70)
print("EXERCISE 19: LEAP YEAR")
print("=" * 70)

year = 2024

if year % 400 == 0:

    print("Leap year.")

else:

    if year % 100 == 0:

        print("Not a leap year.")

    else:

        if year % 4 == 0:

            print("Leap year.")

        else:

            print("Not a leap year.")


# =====================================================================
# EXERCISE 20: SIMPLE RESTAURANT ORDER SYSTEM
# =====================================================================

# QUESTION:
# Check whether an item is available.
# If available, check whether payment is completed.

print("\n" + "=" * 70)
print("EXERCISE 20: RESTAURANT ORDER")
print("=" * 70)

menu = ["Pizza", "Burger", "Pasta"]

selected_item = "Pizza"
payment_completed = True

if selected_item in menu:

    print("Item is available.")

    if payment_completed:

        print("Payment successful.")
        print("Order confirmed.")

    else:

        print("Please complete payment.")

else:

    print("Selected item is unavailable.")


# =====================================================================
# EXERCISE 21: NESTED CONDITIONS WITH INPUT VALIDATION
# =====================================================================

# QUESTION:
# Ask the user for a number.
# Check whether it is valid and then classify it.
#
# EXPLANATION:
# try-except handles invalid numerical conversion.
# Nested conditions classify the valid number.

print("\n" + "=" * 70)
print("EXERCISE 21: NUMBER VALIDATION")
print("=" * 70)

try:

    number = int(input("Enter an integer: "))

    if number >= 0:

        print("Non-negative number.")

        if number == 0:

            print("The number is zero.")

        else:

            if number % 2 == 0:

                print("Positive even number.")

            else:

                print("Positive odd number.")

    else:

        print("Negative number.")

except ValueError:

    print("Please enter a valid integer.")


# =====================================================================
# EXERCISE 22: ELECTRICITY BILL DISCOUNT SYSTEM
# =====================================================================

# QUESTION:
# Give a discount based on customer type and usage.
#
# EXAMPLE RULES:
# Premium customer:
#   Usage >= 100 units: 15% discount
#   Otherwise: 10% discount
#
# Regular customer:
#   Usage >= 100 units: 5% discount
#   Otherwise: No discount
#
# EXPLANATION:
# The outer condition checks customer type.
# The inner condition checks electricity usage.

print("\n" + "=" * 70)
print("EXERCISE 22: ELECTRICITY DISCOUNT")
print("=" * 70)

customer_type = "premium"
units = 150

if customer_type == "premium":

    if units >= 100:

        discount = 15

    else:

        discount = 10

else:

    if units >= 100:

        discount = 5

    else:

        discount = 0

print("Customer type:", customer_type)
print("Electricity units:", units)
print("Discount:", discount, "%")


# =====================================================================
# EXERCISE 23: PRODUCT STOCK AND PURCHASE SYSTEM
# =====================================================================

# QUESTION:
# Check whether a product is available in stock.
# If available, check whether the customer can afford it.

print("\n" + "=" * 70)
print("EXERCISE 23: PRODUCT PURCHASE")
print("=" * 70)

stock = 10
price = 2500
customer_money = 3000

if stock > 0:

    print("Product is in stock.")

    if customer_money >= price:

        stock -= 1

        print("Purchase successful.")
        print("Remaining stock:", stock)

    else:

        print("Insufficient money.")

else:

    print("Product is out of stock.")


# =====================================================================
# EXERCISE 24: CHECK A PERSON'S AGE CATEGORY
# =====================================================================

# QUESTION:
# Check whether an age is valid.
# If valid, classify the person.
#
# EXAMPLE CATEGORIES:
# Below 13: Child
# 13-17: Teenager
# 18-59: Adult
# 60+: Senior

print("\n" + "=" * 70)
print("EXERCISE 24: AGE CLASSIFICATION")
print("=" * 70)

age = 30

if age >= 0:

    if age < 13:

        print("Child.")

    elif age < 18:

        print("Teenager.")

    elif age < 60:

        print("Adult.")

    else:

        print("Senior.")

else:

    print("Invalid age.")


# =====================================================================
# EXERCISE 25: NESTED CONDITIONS WITH STRING METHODS
# =====================================================================

# QUESTION:
# Check whether a username is empty.
# If not empty, check whether it matches the required name.
#
# EXPLANATION:
# strip() removes surrounding whitespace.
# lower() makes comparison case-insensitive.

print("\n" + "=" * 70)
print("EXERCISE 25: USERNAME VALIDATION")
print("=" * 70)

username = "  STUDENT  "

username = username.strip().lower()

if username:

    print("Username is not empty.")

    if username == "student":

        print("Username accepted.")

    else:

        print("Username is not recognized.")

else:

    print("Username cannot be empty.")


# =====================================================================
# EXERCISE 26: NESTED CONDITIONS FOR A SIMPLE CALCULATOR
# =====================================================================

# QUESTION:
# Check the selected operator.
# If division is selected, check for division by zero.
#
# EXPLANATION:
# The inner condition protects the division operation.

print("\n" + "=" * 70)
print("EXERCISE 26: CALCULATOR")
print("=" * 70)

a = 20
b = 0
operator = "/"

if operator == "+":

    result = a + b
    print("Result:", result)

elif operator == "-":

    result = a - b
    print("Result:", result)

elif operator == "*":

    result = a * b
    print("Result:", result)

elif operator == "/":

    if b != 0:

        result = a / b
        print("Result:", result)

    else:

        print("Error: Division by zero is not allowed.")

else:

    print("Invalid operator.")


# =====================================================================
# EXERCISE 27: NESTED CONDITIONS WITH A LIST
# =====================================================================

# QUESTION:
# Check whether a requested subject exists.
# If it exists, check whether the student passed it.
#
# EXPLANATION:
# We use a dictionary to store subject marks.
# The in operator checks whether a subject exists.

print("\n" + "=" * 70)
print("EXERCISE 27: SUBJECT PERFORMANCE")
print("=" * 70)

subject_marks = {

    "Mathematics": 85,

    "Python": 90,

    "Statistics": 45

}

selected_subject = "Python"

if selected_subject in subject_marks:

    print("Subject found.")

    marks = subject_marks[selected_subject]

    if marks >= 50:

        print("Student passed:", selected_subject)

    else:

        print("Student failed:", selected_subject)

else:

    print("Subject not found.")


# =====================================================================
# EXERCISE 28: NESTED CONDITIONS FOR MACHINE LEARNING DATA
# =====================================================================

# QUESTION:
# Create a basic data-quality decision system.
#
# Check whether a sample value is available.
# If available, check whether it falls within
# an acceptable example range.
#
# EXPLANATION:
# Data validation is important before training
# Machine Learning models.
#
# This is only a basic rule-based validation example.

print("\n" + "=" * 70)
print("EXERCISE 28: DATA VALIDATION")
print("=" * 70)

sample_value = 75

sample_available = True

if sample_available:

    print("Sample is available.")

    if 0 <= sample_value <= 100:

        print("Sample value is within the example range.")

        if sample_value >= 50:

            print("Sample classification: HIGH")

        else:

            print("Sample classification: LOW")

    else:

        print("Sample value is outside the allowed range.")

else:

    print("Sample is missing.")


# =====================================================================
# EXERCISE 29: RULE-BASED STUDENT DECISION SYSTEM
# =====================================================================

# QUESTION:
# Evaluate student performance using multiple requirements.
#
# Requirements:
# 1. Marks must be valid.
# 2. Student must pass.
# 3. Attendance must be sufficient.
# 4. Assignment must be completed.
#
# EXPLANATION:
# This exercise combines multiple levels of nesting.
#
# This is a rule-based system, not a trained AI model.

print("\n" + "=" * 70)
print("EXERCISE 29: RULE-BASED STUDENT SYSTEM")
print("=" * 70)

marks = 88
attendance = 90
assignment_completed = True

if 0 <= marks <= 100:

    print("Marks are valid.")

    if marks >= 50:

        print("Examination passed.")

        if attendance >= 75:

            print("Attendance requirement satisfied.")

            if assignment_completed:

                print("Assignment completed.")
                print("FINAL RESULT: APPROVED")

            else:

                print("FINAL RESULT: ASSIGNMENT INCOMPLETE")

        else:

            print("FINAL RESULT: INSUFFICIENT ATTENDANCE")

    else:

        print("FINAL RESULT: FAILED")

else:

    print("FINAL RESULT: INVALID MARKS")


# =====================================================================
# EXERCISE 30: COMPREHENSIVE UNIVERSITY DECISION SYSTEM
# =====================================================================

# QUESTION:
# Build a decision-making system for a university.
#
# Requirements:
#
# 1. Age must be at least 18.
# 2. Entrance marks must be at least 60.
# 3. Interview must be passed.
# 4. Required documents must be submitted.
#
# EXPLANATION:
# This final exercise combines:
#
# - Nested conditions
# - Boolean variables
# - Comparison operators
# - Multiple decision levels
#
# This is our most comprehensive exercise today.

print("\n" + "=" * 70)
print("EXERCISE 30: UNIVERSITY DECISION SYSTEM")
print("=" * 70)

age = 22
entrance_marks = 85
interview_passed = True
documents_submitted = True

if age >= 18:

    print("Age requirement: PASSED")

    if entrance_marks >= 60:

        print("Entrance examination: PASSED")

        if interview_passed:

            print("Interview: PASSED")

            if documents_submitted:

                print("Documents: VERIFIED")

                print("\nFINAL DECISION: ADMISSION APPROVED!")

            else:

                print("Admission pending: Documents missing.")

        else:

            print("Admission rejected: Interview failed.")

    else:

        print("Admission rejected: Entrance marks insufficient.")

else:

    print("Admission rejected: Age requirement not met.")


# =====================================================================
# FINAL EXERCISE SUMMARY
# =====================================================================

print("\n" + "=" * 70)

print("DAY 011 - SOLVED EXERCISES SUMMARY")

print("=" * 70)

exercise_titles = [

    "Age and Identity Verification",

    "Student Pass and Attendance",

    "Login System",

    "Positive and Even or Odd",

    "Largest of Three Numbers",

    "University Admission",

    "Scholarship Eligibility",

    "Bank Withdrawal",

    "Temperature Classification",

    "Triangle Classification",

    "Employee Bonus",

    "Password Check",

    "Voting Eligibility",

    "Course Enrollment",

    "Weather Decision",

    "Multiple Student Results",

    "Student Eligibility Function",

    "System Status",

    "Leap Year",

    "Restaurant Order",

    "Number Validation",

    "Electricity Discount",

    "Product Purchase",

    "Age Classification",

    "Username Validation",

    "Calculator",

    "Subject Performance",

    "Machine Learning Data Validation",

    "Rule-Based Student System",

    "University Decision System"

]

for number, title in enumerate(exercise_titles, start=1):

    print(f"{number}. {title} - Completed")


print("\nALL 30 SOLVED EXERCISES COMPLETED!")

print("=" * 70)


# =====================================================================
# END OF DAY 011 - EXERCISES.PY
# =====================================================================
