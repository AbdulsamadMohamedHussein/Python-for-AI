
# =================================================================
# DAY 010 - PYTHON CONDITIONAL STATEMENTS
# SOLVED EXERCISES
#
# Bachelor's in Artificial Intelligence
# 90-Day Python Programming Journey
#
# TOTAL: 30 SOLVED EXERCISES
#
# TOPICS:
# 1. if statements
# 2. if-else statements
# 3. if-elif-else statements
# 4. Comparison operators
# 5. Logical operators
# 6. Nested conditions
# 7. Boolean values
# 8. Membership operators
# 9. Ternary expressions
# 10. User input
# 11. Practical decision-making programs
#
# =================================================================


# =================================================================
# EXERCISE 1: CHECK WHETHER A PERSON IS AN ADULT
# =================================================================

# QUESTION:
# Create a variable called age.
# If the age is 18 or above, display "You are an adult."

# EXPLANATION:
# The if statement executes its code only when
# the condition evaluates to True.
#
# >= means greater than or equal to.

print("\n" + "=" * 70)
print("EXERCISE 1: ADULT CHECK")
print("=" * 70)

age = 23

if age >= 18:

    print("You are an adult.")


# =================================================================
# EXERCISE 2: CHECK WHETHER A NUMBER IS POSITIVE
# =================================================================

# QUESTION:
# Check whether a number is greater than zero.
#
# EXPLANATION:
# A positive number is any number greater than zero.
# The condition number > 0 checks this.

print("\n" + "=" * 70)
print("EXERCISE 2: POSITIVE NUMBER")
print("=" * 70)

number = 15

if number > 0:

    print("The number is positive.")


# =================================================================
# EXERCISE 3: CHECK WHETHER A NUMBER IS NEGATIVE OR POSITIVE
# =================================================================

# QUESTION:
# Check whether a number is positive or negative.
#
# EXPLANATION:
# if checks the first condition.
# elif checks another condition if the first is False.
#
# Zero is neither positive nor negative.

print("\n" + "=" * 70)
print("EXERCISE 3: POSITIVE OR NEGATIVE")
print("=" * 70)

number = -12

if number > 0:

    print("Positive number.")

elif number < 0:

    print("Negative number.")

else:

    print("The number is zero.")


# =================================================================
# EXERCISE 4: CHECK EVEN OR ODD
# =================================================================

# QUESTION:
# Determine whether a number is even or odd.
#
# EXPLANATION:
# The modulo operator (%) calculates the remainder.
#
# If number % 2 equals zero, the number is even.
# Otherwise, it is odd.

print("\n" + "=" * 70)
print("EXERCISE 4: EVEN OR ODD")
print("=" * 70)

number = 17

if number % 2 == 0:

    print("The number is even.")

else:

    print("The number is odd.")


# =================================================================
# EXERCISE 5: CHECK WHETHER TWO NUMBERS ARE EQUAL
# =================================================================

# QUESTION:
# Compare two numbers and determine whether they are equal.
#
# EXPLANATION:
# == compares two values.
# It returns True if both values are equal.

print("\n" + "=" * 70)
print("EXERCISE 5: EQUALITY CHECK")
print("=" * 70)

first_number = 25

second_number = 25

if first_number == second_number:

    print("Both numbers are equal.")

else:

    print("The numbers are different.")


# =================================================================
# EXERCISE 6: FIND THE GREATER NUMBER
# =================================================================

# QUESTION:
# Compare two numbers and display the greater number.
#
# EXPLANATION:
# > means greater than.
# < means less than.
#
# We also handle the possibility that both numbers are equal.

print("\n" + "=" * 70)
print("EXERCISE 6: GREATER NUMBER")
print("=" * 70)

a = 45

b = 30

if a > b:

    print("Greater number:", a)

elif b > a:

    print("Greater number:", b)

else:

    print("Both numbers are equal.")


# =================================================================
# EXERCISE 7: FIND THE LARGEST OF THREE NUMBERS
# =================================================================

# QUESTION:
# Find the largest number among three numbers.
#
# EXPLANATION:
# We use the AND operator to compare one number
# against both other numbers.
#
# Both comparisons must be True.

print("\n" + "=" * 70)
print("EXERCISE 7: LARGEST OF THREE NUMBERS")
print("=" * 70)

a = 45

b = 80

c = 60

if a >= b and a >= c:

    print("Largest number:", a)

elif b >= a and b >= c:

    print("Largest number:", b)

else:

    print("Largest number:", c)


# =================================================================
# EXERCISE 8: STUDENT PASS OR FAIL
# =================================================================

# QUESTION:
# A student passes if marks are 50 or above.
#
# EXPLANATION:
# We compare the marks with the passing threshold.
# >= includes the value 50 itself.

print("\n" + "=" * 70)
print("EXERCISE 8: PASS OR FAIL")
print("=" * 70)

marks = 75

if marks >= 50:

    print("Congratulations! You passed.")

else:

    print("You failed. Keep practising.")


# =================================================================
# EXERCISE 9: STUDENT GRADE CALCULATOR
# =================================================================

# QUESTION:
# Assign grades based on examination marks.
#
# GRADING SYSTEM:
# 90-100 = A+
# 80-89  = A
# 70-79  = B
# 60-69  = C
# 50-59  = D
# Below 50 = F
#
# EXPLANATION:
# Conditions are checked from top to bottom.
# The first True condition executes.
#
# We validate the marks before assigning a grade.

print("\n" + "=" * 70)
print("EXERCISE 9: GRADE CALCULATOR")
print("=" * 70)

marks = 85

if marks < 0 or marks > 100:

    print("Invalid marks.")

elif marks >= 90:

    print("Grade: A+")

elif marks >= 80:

    print("Grade: A")

elif marks >= 70:

    print("Grade: B")

elif marks >= 60:

    print("Grade: C")

elif marks >= 50:

    print("Grade: D")

else:

    print("Grade: F")


# =================================================================
# EXERCISE 10: CHECK VOTING ELIGIBILITY
# =================================================================

# QUESTION:
# Check whether a person meets the age requirement
# for voting in a hypothetical system.
#
# EXPLANATION:
# We check whether the age is at least 18.
#
# Actual voting eligibility depends on local laws
# and other requirements.

print("\n" + "=" * 70)
print("EXERCISE 10: VOTING ELIGIBILITY")
print("=" * 70)

age = 20

if age >= 18:

    print("You meet the age requirement.")

else:

    print("You do not meet the age requirement.")


# =================================================================
# EXERCISE 11: LOGICAL AND OPERATOR
# =================================================================

# QUESTION:
# A student passes only if:
# Marks are at least 50 AND attendance is at least 75%.
#
# EXPLANATION:
# AND requires BOTH conditions to be True.
#
# If either condition is False, the student does not
# satisfy the combined requirement.

print("\n" + "=" * 70)
print("EXERCISE 11: LOGICAL AND")
print("=" * 70)

marks = 75

attendance = 85

if marks >= 50 and attendance >= 75:

    print("Student meets both requirements.")

else:

    print("Student does not meet both requirements.")


# =================================================================
# EXERCISE 12: LOGICAL OR OPERATOR
# =================================================================

# QUESTION:
# A student can access an example portal if they have
# either a registered email OR a registered phone number.
#
# EXPLANATION:
# OR requires at least ONE condition to be True.

print("\n" + "=" * 70)
print("EXERCISE 12: LOGICAL OR")
print("=" * 70)

has_email = False

has_phone = True

if has_email or has_phone:

    print("Contact information is available.")

else:

    print("No contact information is available.")


# =================================================================
# EXERCISE 13: LOGICAL NOT OPERATOR
# =================================================================

# QUESTION:
# Check whether a student is NOT absent.
#
# EXPLANATION:
# NOT reverses a Boolean value.
#
# not False becomes True.
# not True becomes False.

print("\n" + "=" * 70)
print("EXERCISE 13: LOGICAL NOT")
print("=" * 70)

is_absent = False

if not is_absent:

    print("The student is present.")

else:

    print("The student is absent.")


# =================================================================
# EXERCISE 14: NESTED IF STATEMENTS
# =================================================================

# QUESTION:
# Check age first.
# If the person is at least 18, check whether they have an ID.
#
# EXPLANATION:
# A nested if is an if statement inside another if statement.
#
# The inner condition is reached only if the outer
# condition is True.

print("\n" + "=" * 70)
print("EXERCISE 14: NESTED CONDITIONS")
print("=" * 70)

age = 23

has_id = True

if age >= 18:

    print("Age requirement satisfied.")

    if has_id:

        print("Identity verified.")

    else:

        print("Please provide identification.")

else:

    print("Age requirement not satisfied.")


# =================================================================
# EXERCISE 15: CHECK DIVISIBILITY BY 5 AND 3
# =================================================================

# QUESTION:
# Check whether a number is divisible by BOTH 5 and 3.
#
# EXPLANATION:
# A number is divisible by another number
# if its remainder is zero.
#
# We combine both checks using AND.

print("\n" + "=" * 70)
print("EXERCISE 15: DIVISIBILITY")
print("=" * 70)

number = 30

if number % 5 == 0 and number % 3 == 0:

    print("The number is divisible by both 5 and 3.")

else:

    print("The number is not divisible by both 5 and 3.")


# =================================================================
# EXERCISE 16: CHECK A LEAP YEAR
# =================================================================

# QUESTION:
# Determine whether a year is a leap year.
#
# RULE:
# A year is a leap year if:
#
# 1. It is divisible by 400.
#
# OR
#
# 2. It is divisible by 4 but NOT divisible by 100.
#
# EXPLANATION:
# We combine AND, OR and NOT operators.
#
# This is a useful real-world logical problem.

print("\n" + "=" * 70)
print("EXERCISE 16: LEAP YEAR")
print("=" * 70)

year = 2024

if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):

    print(year, "is a leap year.")

else:

    print(year, "is not a leap year.")


# =================================================================
# EXERCISE 17: SIMPLE LOGIN SYSTEM
# =================================================================

# QUESTION:
# Check whether the entered username and password
# match the stored example credentials.
#
# EXPLANATION:
# BOTH credentials must match.
#
# We use AND to combine the two conditions.
#
# This is a learning example, not secure authentication.

print("\n" + "=" * 70)
print("EXERCISE 17: LOGIN SYSTEM")
print("=" * 70)

correct_username = "student"

correct_password = "python123"

entered_username = "student"

entered_password = "python123"

if entered_username == correct_username and entered_password == correct_password:

    print("Login successful.")

else:

    print("Incorrect username or password.")


# =================================================================
# EXERCISE 18: CHECK WHETHER A WORD EXISTS IN A LIST
# =================================================================

# QUESTION:
# Check whether Python exists in the available courses.
#
# EXPLANATION:
# The in operator checks membership.
#
# It returns True if the item exists in the list.

print("\n" + "=" * 70)
print("EXERCISE 18: MEMBERSHIP OPERATOR")
print("=" * 70)

courses = ["Python", "Machine Learning", "Deep Learning"]

selected_course = "Python"

if selected_course in courses:

    print("Course is available.")

else:

    print("Course is not available.")


# =================================================================
# EXERCISE 19: CHECK WHETHER A WORD DOES NOT EXIST
# =================================================================

# QUESTION:
# Check whether Java is NOT included in the course list.
#
# EXPLANATION:
# not in returns True when the value is absent.

print("\n" + "=" * 70)
print("EXERCISE 19: NOT IN OPERATOR")
print("=" * 70)

courses = ["Python", "Machine Learning", "Deep Learning"]

selected_course = "Java"

if selected_course not in courses:

    print("Java is not available.")

else:

    print("Java is available.")


# =================================================================
# EXERCISE 20: TERNARY CONDITIONAL EXPRESSION
# =================================================================

# QUESTION:
# Check whether a number is even or odd using one line.
#
# EXPLANATION:
# A ternary expression has this structure:
#
# value_if_true if condition else value_if_false
#
# It is useful for simple decisions.

print("\n" + "=" * 70)
print("EXERCISE 20: TERNARY EXPRESSION")
print("=" * 70)

number = 12

result = "Even" if number % 2 == 0 else "Odd"

print("Number:", number)

print("Result:", result)


# =================================================================
# EXERCISE 21: TEMPERATURE CLASSIFICATION
# =================================================================

# QUESTION:
# Classify temperature into categories.
#
# BELOW 10 = Cold
# 10-24 = Moderate
# 25-34 = Warm
# 35 OR ABOVE = Hot
#
# EXPLANATION:
# elif allows us to check multiple possible ranges.

print("\n" + "=" * 70)
print("EXERCISE 21: TEMPERATURE CLASSIFICATION")
print("=" * 70)

temperature = 30

if temperature < 10:

    print("Cold weather.")

elif temperature < 25:

    print("Moderate weather.")

elif temperature < 35:

    print("Warm weather.")

else:

    print("Hot weather.")


# =================================================================
# EXERCISE 22: CHECK PASSWORD LENGTH
# =================================================================

# QUESTION:
# Check whether a password contains at least 8 characters.
#
# EXPLANATION:
# len() counts the characters in a string.
#
# >= 8 checks whether the length is at least 8.
#
# This is only a basic length check.

print("\n" + "=" * 70)
print("EXERCISE 22: PASSWORD LENGTH")
print("=" * 70)

password = "Python123"

if len(password) >= 8:

    print("Password length accepted.")

else:

    print("Password is too short.")


# =================================================================
# EXERCISE 23: CHECK WHETHER A NAME IS EMPTY
# =================================================================

# QUESTION:
# Check whether a name contains meaningful text.
#
# EXPLANATION:
# strip() removes surrounding whitespace.
#
# An empty string evaluates to False in a condition.
#
# This prevents a user from submitting only spaces.

print("\n" + "=" * 70)
print("EXERCISE 23: EMPTY NAME CHECK")
print("=" * 70)

name = "   Abdulsamad   "

clean_name = name.strip()

if clean_name:

    print("Valid name:", clean_name.title())

else:

    print("Name cannot be empty.")


# =================================================================
# EXERCISE 24: FIND THE SMALLEST OF THREE NUMBERS
# =================================================================

# QUESTION:
# Find the smallest of three numbers.
#
# EXPLANATION:
# We compare each number with the other two.
#
# <= allows equal values to be handled correctly.

print("\n" + "=" * 70)
print("EXERCISE 24: SMALLEST OF THREE")
print("=" * 70)

a = 15

b = 8

c = 25

if a <= b and a <= c:

    print("Smallest number:", a)

elif b <= a and b <= c:

    print("Smallest number:", b)

else:

    print("Smallest number:", c)


# =================================================================
# EXERCISE 25: CHECK TRIANGLE TYPE
# =================================================================

# QUESTION:
# Classify a triangle using its three side lengths.
#
# RULES:
# Equilateral: All three sides are equal.
# Isosceles: Exactly two sides are equal.
# Scalene: All three sides are different.
#
# IMPORTANT:
# First, check whether the sides can form a triangle.
#
# The sum of any two sides must be greater than
# the remaining side.

print("\n" + "=" * 70)
print("EXERCISE 25: TRIANGLE CLASSIFICATION")
print("=" * 70)

a = 5

b = 5

c = 5

if a <= 0 or b <= 0 or c <= 0:

    print("Invalid triangle sides.")

elif a + b <= c or a + c <= b or b + c <= a:

    print("These sides cannot form a triangle.")

elif a == b and b == c:

    print("Equilateral triangle.")

elif a == b or a == c or b == c:

    print("Isosceles triangle.")

else:

    print("Scalene triangle.")


# =================================================================
# EXERCISE 26: SIMPLE CALCULATOR
# =================================================================

# QUESTION:
# Perform arithmetic operations depending
# on the selected operator.
#
# EXPLANATION:
# We use if-elif-else to identify the operation.
#
# We also check for division by zero.

print("\n" + "=" * 70)
print("EXERCISE 26: SIMPLE CALCULATOR")
print("=" * 70)

first_number = 20

second_number = 5

operator = "/"

if operator == "+":

    result = first_number + second_number

    print("Addition:", result)

elif operator == "-":

    result = first_number - second_number

    print("Subtraction:", result)

elif operator == "*":

    result = first_number * second_number

    print("Multiplication:", result)

elif operator == "/":

    if second_number != 0:

        result = first_number / second_number

        print("Division:", result)

    else:

        print("Cannot divide by zero.")

else:

    print("Invalid operator.")


# =================================================================
# EXERCISE 27: STUDENT SCHOLARSHIP ELIGIBILITY
# =================================================================

# QUESTION:
# A student qualifies for this example scholarship if:
#
# Marks are at least 85 AND attendance is at least 80%.
#
# EXPLANATION:
# We use AND because both conditions must be satisfied.
#
# This is an illustrative scholarship rule.

print("\n" + "=" * 70)
print("EXERCISE 27: SCHOLARSHIP ELIGIBILITY")
print("=" * 70)

marks = 90

attendance = 85

if marks >= 85 and attendance >= 80:

    print("Student qualifies for the example scholarship.")

else:

    print("Student does not qualify.")


# =================================================================
# EXERCISE 28: CHECK THE DAY OF THE WEEK
# =================================================================

# QUESTION:
# Identify whether a day is a weekday or weekend.
#
# EXPLANATION:
# We use membership operators to check whether
# the entered day belongs to a particular list.
#
# lower() makes the comparison case-insensitive.

print("\n" + "=" * 70)
print("EXERCISE 28: WEEKDAY OR WEEKEND")
print("=" * 70)

day = "Sunday"

day = day.strip().lower()

weekend = ["saturday", "sunday"]

weekdays = [
    "monday",
    "tuesday",
    "wednesday",
    "thursday",
    "friday"
]

if day in weekend:

    print("It is a weekend.")

elif day in weekdays:

    print("It is a weekday.")

else:

    print("Invalid day name.")


# =================================================================
# EXERCISE 29: SIMPLE SHIPPING COST CALCULATOR
# =================================================================

# QUESTION:
# Calculate shipping cost based on package weight.
#
# EXAMPLE RULES:
# Up to 1 kg: 100
# Above 1 kg and up to 5 kg: 250
# Above 5 kg: 500
#
# EXPLANATION:
# We use multiple conditions to select the correct
# shipping category.
#
# The example currency is not specified.

print("\n" + "=" * 70)
print("EXERCISE 29: SHIPPING COST")
print("=" * 70)

weight = 3.5

if weight <= 0:

    print("Invalid package weight.")

elif weight <= 1:

    shipping_cost = 100

    print("Shipping Cost:", shipping_cost)

elif weight <= 5:

    shipping_cost = 250

    print("Shipping Cost:", shipping_cost)

else:

    shipping_cost = 500

    print("Shipping Cost:", shipping_cost)


# =================================================================
# EXERCISE 30: SIMPLE AI DECISION SYSTEM
# =================================================================

# QUESTION:
# Create a basic rule-based decision system.
#
# The system evaluates a student's performance.
#
# RULES:
# Marks >= 80 AND attendance >= 75:
# Excellent performance.
#
# Marks >= 50 AND attendance >= 60:
# Satisfactory performance.
#
# Otherwise:
# Needs improvement.
#
# EXPLANATION:
# This exercise combines:
# - Multiple conditions.
# - AND operator.
# - elif.
# - else.
#
# IMPORTANT:
# This is a rule-based Python program,
# NOT a trained Artificial Intelligence model.

print("\n" + "=" * 70)
print("EXERCISE 30: RULE-BASED STUDENT DECISION SYSTEM")
print("=" * 70)

marks = 88

attendance = 90

if marks >= 80 and attendance >= 75:

    performance = "Excellent"

elif marks >= 50 and attendance >= 60:

    performance = "Satisfactory"

else:

    performance = "Needs Improvement"

print("Student Marks:", marks)

print("Attendance:", attendance)

print("Performance:", performance)


# =================================================================
# FINAL EXERCISE SUMMARY
# =================================================================

print("\n" + "=" * 70)

print("DAY 010 - SOLVED EXERCISES SUMMARY")

print("=" * 70)

print("1. Adult Check - Completed")

print("2. Positive Number - Completed")

print("3. Positive or Negative - Completed")

print("4. Even or Odd - Completed")

print("5. Equality Check - Completed")

print("6. Greater Number - Completed")

print("7. Largest of Three Numbers - Completed")

print("8. Pass or Fail - Completed")

print("9. Grade Calculator - Completed")

print("10. Voting Eligibility - Completed")

print("11. Logical AND - Completed")

print("12. Logical OR - Completed")

print("13. Logical NOT - Completed")

print("14. Nested Conditions - Completed")

print("15. Divisibility - Completed")

print("16. Leap Year - Completed")

print("17. Login System - Completed")

print("18. Membership Operator - Completed")

print("19. NOT IN Operator - Completed")

print("20. Ternary Expression - Completed")

print("21. Temperature Classification - Completed")

print("22. Password Length - Completed")

print("23. Empty Name Check - Completed")

print("24. Smallest of Three - Completed")

print("25. Triangle Classification - Completed")

print("26. Simple Calculator - Completed")

print("27. Scholarship Eligibility - Completed")

print("28. Weekday or Weekend - Completed")

print("29. Shipping Cost - Completed")

print("30. Rule-Based AI Decision System - Completed")

print("\nALL 30 EXERCISES COMPLETED!")

print("=" * 70)


# =================================================================
# END OF DAY 010 - EXERCISES.PY
# =================================================================
