
# ================================================================
# DAY 007 - PYTHON FUNDAMENTALS REVISION PROJECT
#
# PROJECT: AI STUDENT PERFORMANCE ANALYZER
#
# Bachelor's in Artificial Intelligence
# 90-Day Python Programming Journey
#
# This project revises everything learned in Days 001-006.
#
# Topics:
# Variables, Data Types, Type Conversion, Operators,
# Input, Output, F-Strings, Conditions and Data Validation.
# ================================================================


# ================================================================
# SECTION 1: PROGRAM INTRODUCTION
# ================================================================

# print() displays information on the screen.
# The multiplication operator (*) repeats a string.
# Here, we repeat "=" 70 times to create a separator.

print("=" * 70)

print("             AI STUDENT PERFORMANCE ANALYZER")

print("=" * 70)

print("Welcome to the Python Fundamentals Revision Project!")

print("This application analyzes student academic performance.")

print("=" * 70)


# ================================================================
# SECTION 2: VARIABLES AND DATA STORAGE
# ================================================================

# A variable is a named location used to store information.
#
# Below, we create variables to store student information.
#
# String: Textual information.
# Integer: Whole numbers.
# Float: Decimal numbers.
# Boolean: True or False.

student_name = "Abdulsamad Mohamed"

student_age = 23

student_country = "Pakistan"

student_university = "Guilin University of Electronics Technology"

student_course = "Bachelor's in Artificial Intelligence"

is_ai_student = True

# Display the variables and their values.

print("\nSTUDENT INFORMATION")

print("-" * 70)

print("Name:", student_name)

print("Age:", student_age)

print("Country:", student_country)

print("University:", student_university)

print("Course:", student_course)

print("AI Student:", is_ai_student)


# ================================================================
# SECTION 3: CHECKING DATA TYPES
# ================================================================

# The type() function tells us the data type of a variable.
#
# This is important because Python handles different
# types of data differently.

print("\nCHECKING DATA TYPES")

print("-" * 70)

print("Name Data Type:", type(student_name))

print("Age Data Type:", type(student_age))

print("Country Data Type:", type(student_country))

print("AI Student Data Type:", type(is_ai_student))

# Create additional variables to understand data types.

temperature = 25.5

number_of_students = 120

university_open = True

print("Temperature Type:", type(temperature))

print("Student Count Type:", type(number_of_students))

print("University Status Type:", type(university_open))


# ================================================================
# SECTION 4: USER INPUT
# ================================================================

# The input() function collects information from users.
#
# Unlike the previous sections, we will now collect
# information directly from the person running the program.

print("\nENTER STUDENT INFORMATION")

print("-" * 70)

# Collect the student's name.
# strip() removes unnecessary spaces around the input.

user_name = input("Enter your name: ").strip()

# Collect the student's age.
# input() initially returns a string.
# int() converts it into an integer.

user_age = int(input("Enter your age: "))

# Collect the student's country.

user_country = input("Enter your country: ").strip()

# Collect the student's course.

user_course = input("Enter your course: ").strip()


# ================================================================
# SECTION 5: TYPE CONVERSION
# ================================================================

# Type conversion changes information from one data type
# into another.
#
# int() converts to integer.
# float() converts to decimal.
# str() converts to string.
#
# We demonstrate these conversions below.

print("\nTYPE CONVERSION DEMONSTRATION")

print("-" * 70)

# String to integer.

number_as_string = "100"

converted_integer = int(number_as_string)

print("Original Value:", number_as_string)

print("Converted Value:", converted_integer)

print("Original Type:", type(number_as_string))

print("Converted Type:", type(converted_integer))

# String to float.

decimal_as_string = "95.75"

converted_float = float(decimal_as_string)

print("\nOriginal Decimal:", decimal_as_string)

print("Converted Decimal:", converted_float)

print("Converted Type:", type(converted_float))

# Integer to string.

student_number = 23

student_number_text = str(student_number)

print("\nInteger to String:", student_number_text)

print("New Data Type:", type(student_number_text))


# ================================================================
# SECTION 6: MATHEMATICAL OPERATORS
# ================================================================

# Python supports several mathematical operators.
#
# + Addition
# - Subtraction
# * Multiplication
# / Division
# // Floor Division
# % Modulus
# ** Exponentiation

print("\nMATHEMATICAL OPERATORS")

print("-" * 70)

number_1 = 20

number_2 = 6

print("First Number:", number_1)

print("Second Number:", number_2)

print("Addition:", number_1 + number_2)

print("Subtraction:", number_1 - number_2)

print("Multiplication:", number_1 * number_2)

print("Division:", number_1 / number_2)

print("Floor Division:", number_1 // number_2)

print("Modulus:", number_1 % number_2)

print("Exponentiation:", number_1 ** number_2)


# ================================================================
# SECTION 7: COLLECT ACADEMIC MARKS
# ================================================================

# Now we collect academic marks from the user.
#
# float() allows the user to enter decimal marks.
#
# Each subject has a maximum score of 100.

print("\nACADEMIC INFORMATION")

print("-" * 70)

mathematics = float(input("Enter Mathematics marks: "))

physics = float(input("Enter Physics marks: "))

python_marks = float(input("Enter Python marks: "))

chemistry = float(input("Enter Chemistry marks: "))


# ================================================================
# SECTION 8: DATA VALIDATION
# ================================================================

# Before performing calculations, we must check
# whether the entered information is valid.
#
# Marks cannot be below 0 or above 100.
#
# The and operator requires all conditions
# to be True.

print("\nVALIDATING ACADEMIC INFORMATION")

print("-" * 70)

valid_marks = (
    0 <= mathematics <= 100
    and 0 <= physics <= 100
    and 0 <= python_marks <= 100
    and 0 <= chemistry <= 100
)

if valid_marks:

    print("All examination marks are valid.")

else:

    raise ValueError("Invalid marks! Enter values between 0 and 100.")


# ================================================================
# SECTION 9: ARITHMETIC CALCULATIONS
# ================================================================

# We calculate the total marks.
#
# There are four subjects.
# Each subject has a maximum of 100 marks.
#
# Maximum possible marks = 400.

print("\nACADEMIC CALCULATIONS")

print("-" * 70)

total_marks = (
    mathematics
    + physics
    + python_marks
    + chemistry
)

maximum_marks = 400

average_marks = total_marks / 4

percentage = (total_marks / maximum_marks) * 100

print("Total Marks:", total_marks)

print("Maximum Marks:", maximum_marks)

print(f"Average Marks: {average_marks:.2f}")

print(f"Percentage: {percentage:.2f}%")


# ================================================================
# SECTION 10: COMPARISON OPERATORS
# ================================================================

# Comparison operators compare two values.
#
# == Equal to
# != Not equal to
# > Greater than
# < Less than
# >= Greater than or equal to
# <= Less than or equal to
#
# Their results are Boolean values: True or False.

print("\nCOMPARISON OPERATORS")

print("-" * 70)

print("Is Mathematics greater than Physics?")

print(mathematics > physics)

print("Is Python marks equal to Chemistry marks?")

print(python_marks == chemistry)

print("Is Average greater than or equal to 50?")

print(average_marks >= 50)

print("Is Mathematics different from Physics?")

print(mathematics != physics)


# ================================================================
# SECTION 11: LOGICAL OPERATORS
# ================================================================

# Logical operators combine multiple conditions.
#
# and: All conditions must be True.
# or: At least one condition must be True.
# not: Reverses a Boolean value.

print("\nLOGICAL OPERATORS")

print("-" * 70)

# A student passes if their average is at least 50
# and their Python marks are at least 40.

passed = (
    average_marks >= 50
    and python_marks >= 40
)

print("Student Passed:", passed)

# Check whether the student has achieved
# a particularly strong average or Python score.

high_performance = (
    average_marks >= 85
    or python_marks >= 90
)

print("High Performance:", high_performance)

# Reverse the pass result.

not_passed = not passed

print("Student Did Not Pass:", not_passed)


# ================================================================
# SECTION 12: CONDITIONAL STATEMENTS
# ================================================================

# Conditional statements allow Python to make decisions.
#
# if: Executes when a condition is True.
# elif: Checks another condition.
# else: Executes when none of the previous conditions is True.

print("\nSTUDENT GRADE CLASSIFICATION")

print("-" * 70)

if average_marks >= 90:

    grade = "A"

    performance = "Outstanding"

elif average_marks >= 80:

    grade = "B"

    performance = "Excellent"

elif average_marks >= 70:

    grade = "C"

    performance = "Good"

elif average_marks >= 60:

    grade = "D"

    performance = "Satisfactory"

elif average_marks >= 50:

    grade = "E"

    performance = "Pass"

else:

    grade = "F"

    performance = "Fail"

print("Grade:", grade)

print("Performance:", performance)


# ================================================================
# SECTION 13: AUGMENTED ASSIGNMENT OPERATORS
# ================================================================

# Augmented assignment operators update variables.
#
# += Addition and assignment.
# -= Subtraction and assignment.
# *= Multiplication and assignment.
# /= Division and assignment.

print("\nAUGMENTED ASSIGNMENT OPERATORS")

print("-" * 70)

bonus_marks = 10

print("Original Bonus:", bonus_marks)

bonus_marks += 5

print("After Adding 5:", bonus_marks)

bonus_marks -= 3

print("After Subtracting 3:", bonus_marks)

bonus_marks *= 2

print("After Multiplying by 2:", bonus_marks)


# ================================================================
# SECTION 14: AI DATA NORMALIZATION
# ================================================================

# In Artificial Intelligence, numerical data
# sometimes needs to be scaled before training.
#
# Here we demonstrate simple normalization.
#
# Formula:
#
# Normalized Value = Original Value / 100
#
# Our marks have a range of 0 to 100.
# Therefore, this converts them into a range of 0 to 1.

print("\nAI DATA NORMALIZATION")

print("-" * 70)

normalized_math = mathematics / 100

normalized_physics = physics / 100

normalized_python = python_marks / 100

normalized_chemistry = chemistry / 100

print(f"Normalized Mathematics: {normalized_math:.3f}")

print(f"Normalized Physics: {normalized_physics:.3f}")

print(f"Normalized Python: {normalized_python:.3f}")

print(f"Normalized Chemistry: {normalized_chemistry:.3f}")


# ================================================================
# SECTION 15: STRING FORMATTING
# ================================================================

# F-strings make it easier to display variables
# and calculations inside text.
#
# :.2f displays two decimal places.
#
# sep changes the separator.
# end changes what print() displays at the end.

print("\nSTRING FORMATTING")

print("-" * 70)

print(f"Student: {user_name}")

print(f"Age: {user_age}")

print(f"Country: {user_country}")

print(f"Course: {user_course}")

print("Python", "NumPy", "Pandas", sep=" | ")

print("Learning Python", end=" -> ")

print("Learning Artificial Intelligence")


# ================================================================
# SECTION 16: FINAL STUDENT REPORT
# ================================================================

# We now combine our collected information
# and calculated results into one report.

print("\n" + "=" * 70)

print("                 FINAL STUDENT REPORT")

print("=" * 70)

print(f"Student Name: {user_name}")

print(f"Student Age: {user_age}")

print(f"Country: {user_country}")

print(f"Course: {user_course}")

print("-" * 70)

print("ACADEMIC PERFORMANCE")

print("-" * 70)

print(f"Mathematics: {mathematics:.2f}/100")

print(f"Physics: {physics:.2f}/100")

print(f"Python: {python_marks:.2f}/100")

print(f"Chemistry: {chemistry:.2f}/100")

print("-" * 70)

print(f"Total Marks: {total_marks:.2f}/400")

print(f"Average Marks: {average_marks:.2f}")

print(f"Percentage: {percentage:.2f}%")

print(f"Grade: {grade}")

print(f"Performance: {performance}")

print("=" * 70)


# ================================================================
# SECTION 17: FINAL LEARNING SUMMARY
# ================================================================

print("\nDAY 007 PROJECT SUMMARY")

print("-" * 70)

print("Variables and Data Storage: Practised")

print("Python Data Types: Practised")

print("Type Conversion: Practised")

print("Mathematical Operators: Practised")

print("User Input and Output: Practised")

print("Comparison Operators: Practised")

print("Logical Operators: Practised")

print("Conditional Statements: Practised")

print("F-Strings and Formatting: Practised")

print("Basic AI Data Normalization: Practised")

print("\nDAY 007 REVISION PROJECT COMPLETED!")

print("=" * 70)


# ================================================================
# END OF DAY 007 - REVISION_PROJECT.PY
# ================================================================
