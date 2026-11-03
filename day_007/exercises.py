
# ================================================================
# DAY 007 - PYTHON FUNDAMENTALS REVISION
# SOLVED EXERCISES
#
# Bachelor's in Artificial Intelligence
# 90-Day Python Programming Journey
#
# Revision of Days 001-006
#
# Topics:
# Variables, Data Types, Type Conversion, Operators,
# Input, Output, F-Strings, Conditions and AI Applications.
# ================================================================


# ------------------------------------------------
# EXERCISE 1: STUDENT INFORMATION
# ------------------------------------------------

# QUESTION:
# Create variables containing student information.
# Display all information using print().

print("\n" + "=" * 65)
print("EXERCISE 1: STUDENT INFORMATION")
print("=" * 65)

# Store student information in variables.

name = "Abdulsamad Mohamed"

age = 23

country = "Pakistan"

course = "Artificial Intelligence"

university = "Guilin University of Electronics Technology"

# Display the stored information.

print("Name:", name)

print("Age:", age)

print("Country:", country)

print("Course:", course)

print("University:", university)


# ------------------------------------------------
# EXERCISE 2: IDENTIFY DATA TYPES
# ------------------------------------------------

# QUESTION:
# Create five variables using different data types.
# Display their values and data types.

print("\n" + "=" * 65)
print("EXERCISE 2: IDENTIFY DATA TYPES")
print("=" * 65)

# Create variables.

student_name = "Abdulsamad"

student_age = 23

student_height = 1.65

is_student = True

student_graduation = None

# Display values and their types.

print(student_name, type(student_name))

print(student_age, type(student_age))

print(student_height, type(student_height))

print(is_student, type(is_student))

print(student_graduation, type(student_graduation))


# ------------------------------------------------
# EXERCISE 3: TYPE CONVERSION
# ------------------------------------------------

# QUESTION:
# Convert a string into an integer.
# Convert a string into a float.
# Convert an integer into a string.

print("\n" + "=" * 65)
print("EXERCISE 3: TYPE CONVERSION")
print("=" * 65)

# Original string.

number_text = "150"

# Convert string into integer.

number_integer = int(number_text)

# Convert string into float.

number_float = float(number_text)

# Convert integer into string.

integer_text = str(number_integer)

# Display converted values.

print("Original:", number_text)

print("Integer:", number_integer)

print("Float:", number_float)

print("String:", integer_text)

print("Integer Type:", type(number_integer))

print("Float Type:", type(number_float))

print("String Type:", type(integer_text))


# ------------------------------------------------
# EXERCISE 4: BASIC CALCULATOR
# ------------------------------------------------

# QUESTION:
# Ask the user for two numbers.
# Perform addition, subtraction, multiplication and division.

print("\n" + "=" * 65)
print("EXERCISE 4: BASIC CALCULATOR")
print("=" * 65)

# Collect two numbers from the user.

first_number = float(input("Enter first number: "))

second_number = float(input("Enter second number: "))

# Perform mathematical calculations.

addition = first_number + second_number

subtraction = first_number - second_number

multiplication = first_number * second_number

# Display the results.

print("\nCALCULATOR RESULTS")

print("Addition:", addition)

print("Subtraction:", subtraction)

print("Multiplication:", multiplication)

# Check the denominator before division.

if second_number != 0:

    division = first_number / second_number

    print("Division:", division)

else:

    print("Division is impossible because the denominator is zero.")


# ------------------------------------------------
# EXERCISE 5: MATHEMATICAL OPERATORS
# ------------------------------------------------

# QUESTION:
# Demonstrate all basic arithmetic operators.

print("\n" + "=" * 65)
print("EXERCISE 5: MATHEMATICAL OPERATORS")
print("=" * 65)

a = 20

b = 6

print("Addition:", a + b)

print("Subtraction:", a - b)

print("Multiplication:", a * b)

print("Division:", a / b)

print("Floor Division:", a // b)

print("Modulus:", a % b)

print("Exponentiation:", a ** b)

# Floor division returns the whole-number quotient.
# Modulus returns the remainder.
# Exponentiation calculates powers.


# ------------------------------------------------
# EXERCISE 6: COMPARISON OPERATORS
# ------------------------------------------------

# QUESTION:
# Compare two numbers using comparison operators.

print("\n" + "=" * 65)
print("EXERCISE 6: COMPARISON OPERATORS")
print("=" * 65)

x = 85

y = 90

print("x == y:", x == y)

print("x != y:", x != y)

print("x > y:", x > y)

print("x < y:", x < y)

print("x >= y:", x >= y)

print("x <= y:", x <= y)

# Comparison operators always return Boolean values:
# True or False.


# ------------------------------------------------
# EXERCISE 7: LOGICAL OPERATORS
# ------------------------------------------------

# QUESTION:
# Demonstrate AND, OR and NOT operators.

print("\n" + "=" * 65)
print("EXERCISE 7: LOGICAL OPERATORS")
print("=" * 65)

mathematics = 85

python_marks = 90

# AND: Both conditions must be True.

passed = mathematics >= 50 and python_marks >= 50

# OR: At least one condition must be True.

excellent = mathematics >= 90 or python_marks >= 90

# NOT: Reverses a Boolean value.

not_passed = not passed

print("Student Passed:", passed)

print("Excellent Performance:", excellent)

print("Student Did Not Pass:", not_passed)


# ------------------------------------------------
# EXERCISE 8: USER INPUT AND F-STRINGS
# ------------------------------------------------

# QUESTION:
# Collect student information and display
# it using formatted strings.

print("\n" + "=" * 65)
print("EXERCISE 8: USER INPUT AND F-STRINGS")
print("=" * 65)

# Collect information.

student = input("Enter your name: ")

student_age = int(input("Enter your age: "))

student_country = input("Enter your country: ")

# Display using f-strings.

print("\nSTUDENT PROFILE")

print(f"My name is {student}.")

print(f"I am {student_age} years old.")

print(f"I am from {student_country}.")

print(f"Next year I will be {student_age + 1} years old.")


# ------------------------------------------------
# EXERCISE 9: ACADEMIC PERFORMANCE CALCULATOR
# ------------------------------------------------

# QUESTION:
# Collect marks from four subjects.
# Calculate total, average and percentage.

print("\n" + "=" * 65)
print("EXERCISE 9: ACADEMIC PERFORMANCE")
print("=" * 65)

# Collect examination marks.

maths = float(input("Enter Mathematics marks: "))

physics = float(input("Enter Physics marks: "))

python_score = float(input("Enter Python marks: "))

chemistry = float(input("Enter Chemistry marks: "))

# Validate marks.

if all(0 <= mark <= 100 for mark in [
    maths, physics, python_score, chemistry
]):

    # Calculate total marks.

    total = maths + physics + python_score + chemistry

    # Calculate average.

    average = total / 4

    # Calculate percentage.

    percentage = (total / 400) * 100

    print("\nACADEMIC REPORT")

    print(f"Total Marks: {total:.2f}/400")

    print(f"Average: {average:.2f}")

    print(f"Percentage: {percentage:.2f}%")

else:

    print("Invalid marks! All marks must be between 0 and 100.")


# ------------------------------------------------
# EXERCISE 10: GRADE CLASSIFICATION
# ------------------------------------------------

# QUESTION:
# Ask the user for average marks.
# Classify performance using if, elif and else.

print("\n" + "=" * 65)
print("EXERCISE 10: GRADE CLASSIFICATION")
print("=" * 65)

average_marks = float(input("Enter your average marks: "))

# Check that the average is within the valid range.

if not 0 <= average_marks <= 100:

    print("Invalid marks! Enter a value between 0 and 100.")

elif average_marks >= 90:

    print("Grade A: Outstanding")

elif average_marks >= 80:

    print("Grade B: Excellent")

elif average_marks >= 70:

    print("Grade C: Good")

elif average_marks >= 60:

    print("Grade D: Satisfactory")

elif average_marks >= 50:

    print("Grade E: Pass")

else:

    print("Grade F: Fail")


# ------------------------------------------------
# EXERCISE 11: AUGMENTED ASSIGNMENT OPERATORS
# ------------------------------------------------

# QUESTION:
# Demonstrate augmented assignment operators.

print("\n" + "=" * 65)
print("EXERCISE 11: AUGMENTED ASSIGNMENT")
print("=" * 65)

score = 50

print("Original Score:", score)

# Add 10 to the existing score.

score += 10

print("After += 10:", score)

# Subtract 5.

score -= 5

print("After -= 5:", score)

# Multiply by 2.

score *= 2

print("After *= 2:", score)

# Divide by 2.

score /= 2

print("After /= 2:", score)


# ------------------------------------------------
# EXERCISE 12: STRING FORMATTING
# ------------------------------------------------

# QUESTION:
# Demonstrate sep, end and decimal formatting.

print("\n" + "=" * 65)
print("EXERCISE 12: STRING FORMATTING")
print("=" * 65)

# sep changes the separator between values.

print("Python", "NumPy", "Pandas", sep=" | ")

# end changes the ending of print().

print("Artificial Intelligence", end=" -> ")

print("Machine Learning")

# Decimal formatting.

accuracy = 95.678945

print(f"Accuracy: {accuracy:.2f}%")

print(f"Precise Accuracy: {accuracy:.4f}%")


# ------------------------------------------------
# EXERCISE 13: MULTIPLE INPUTS USING SPLIT()
# ------------------------------------------------

# QUESTION:
# Ask the user to enter three numbers in one line.
# Calculate their average.

print("\n" + "=" * 65)
print("EXERCISE 13: MULTIPLE INPUTS")
print("=" * 65)

# split() separates the entered string into three parts.

value_1, value_2, value_3 = input(
    "Enter three numbers separated by spaces: "
).split()

# Convert the strings into floats.

value_1 = float(value_1)

value_2 = float(value_2)

value_3 = float(value_3)

# Calculate average.

average = (value_1 + value_2 + value_3) / 3

print(f"Average: {average:.2f}")


# ------------------------------------------------
# EXERCISE 14: INPUT VALIDATION
# ------------------------------------------------

# QUESTION:
# Collect an age from the user.
# Handle invalid numerical input using try and except.

print("\n" + "=" * 65)
print("EXERCISE 14: INPUT VALIDATION")
print("=" * 65)

age_input = input("Enter your age: ")

try:

    # Attempt to convert the input into an integer.

    validated_age = int(age_input)

    if validated_age > 0:

        print("Valid Age:", validated_age)

    else:

        print("Age must be greater than zero.")

except ValueError:

    # This block executes if the input
    # cannot be converted into an integer.

    print("Invalid input! Please enter a whole number.")


# ------------------------------------------------
# EXERCISE 15: AI DATA NORMALIZATION
# ------------------------------------------------

# QUESTION:
# Collect an examination score.
# Normalize it from a 0-100 range to a 0-1 range.

print("\n" + "=" * 65)
print("EXERCISE 15: AI DATA NORMALIZATION")
print("=" * 65)

# Collect a numerical score.

original_score = float(input("Enter score between 0 and 100: "))

# Validate the score.

if 0 <= original_score <= 100:

    # Normalize the score.

    normalized_score = original_score / 100

    print("Original Score:", original_score)

    print(f"Normalized Score: {normalized_score:.3f}")

else:

    print("Invalid score! Enter a value between 0 and 100.")


# ------------------------------------------------
# FINAL EXERCISE SUMMARY
# ------------------------------------------------

print("\n" + "=" * 65)

print("             DAY 007 EXERCISE SUMMARY")

print("=" * 65)

print("1. Student Information - Completed")

print("2. Data Types - Completed")

print("3. Type Conversion - Completed")

print("4. Basic Calculator - Completed")

print("5. Mathematical Operators - Completed")

print("6. Comparison Operators - Completed")

print("7. Logical Operators - Completed")

print("8. User Input and F-Strings - Completed")

print("9. Academic Performance - Completed")

print("10. Grade Classification - Completed")

print("11. Augmented Assignment - Completed")

print("12. String Formatting - Completed")

print("13. Multiple Inputs - Completed")

print("14. Input Validation - Completed")

print("15. AI Data Normalization - Completed")

print("\nALL DAY 007 EXERCISES COMPLETED!")

print("=" * 65)


# ================================================================
# END OF DAY 007 - EXERCISES.PY
# ================================================================
