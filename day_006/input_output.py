
# ================================================================
# DAY 006 - PYTHON INPUT AND OUTPUT
# BACHELOR'S IN ARTIFICIAL INTELLIGENCE
# 90-DAY PYTHON PROGRAMMING JOURNEY
#
# Main Topics:
# 1. print() function
# 2. input() function
# 3. User input
# 4. Type conversion
# 5. Multiple inputs
# 6. sep and end parameters
# 7. Escape characters
# 8. Formatted output (f-strings)
# 9. Interactive programs
# 10. Input and output in AI applications
# ================================================================


# ------------------------------------------------
# SECTION 1: PROGRAM INTRODUCTION
# ------------------------------------------------

# The print() function displays information
# on the computer screen or terminal.

print("=" * 70)

print("             DAY 006: PYTHON INPUT AND OUTPUT")

print("=" * 70)

print("Welcome to Day 006 of Python for AI!")

print("Today we are learning how Python communicates with users.")


# ------------------------------------------------
# SECTION 2: BASIC OUTPUT USING print()
# ------------------------------------------------

print("\n" + "=" * 70)

print("                    BASIC OUTPUT")

print("=" * 70)

# We can use print() to display text.

print("Hello World!")

print("Welcome to Python Programming.")

print("I am learning Artificial Intelligence.")

# We can also display numerical values.

print(100)

print(25.75)

# We can display Boolean values.

print(True)

print(False)

# We can display mathematical calculations.

print(10 + 20)

print(50 * 2)

print(100 / 4)


# ------------------------------------------------
# SECTION 3: PRINTING VARIABLES
# ------------------------------------------------

print("\n" + "=" * 70)

print("                 PRINTING VARIABLES")

print("=" * 70)

# Create some variables.

student_name = "Abdulsamad"

student_age = 23

student_course = "Artificial Intelligence"

student_cgpa = 3.6

# Display the variables using print().

print(student_name)

print(student_age)

print(student_course)

print(student_cgpa)

# We can also display a description alongside a variable.

print("Student Name:", student_name)

print("Student Age:", student_age)

print("Student Course:", student_course)

print("Student CGPA:", student_cgpa)


# ------------------------------------------------
# SECTION 4: UNDERSTANDING THE INPUT() FUNCTION
# ------------------------------------------------

print("\n" + "=" * 70)

print("                   USER INPUT")

print("=" * 70)

# The input() function allows the user to enter information.
#
# Python waits until the user enters information
# and presses the Enter key.
#
# IMPORTANT:
# input() always returns a string.

user_name = input("Please enter your name: ")

# Display the information entered by the user.

print("Welcome,", user_name)

print("Nice to meet you,", user_name)


# ------------------------------------------------
# SECTION 5: COLLECTING MULTIPLE USER INPUTS
# ------------------------------------------------

print("\n" + "=" * 70)

print("                MULTIPLE USER INPUTS")

print("=" * 70)

# We can collect several pieces of information
# from the user using separate input() statements.

name = input("Enter your full name: ")

country = input("Enter your country: ")

university = input("Enter your university: ")

course = input("Enter your course: ")

# Display all collected information.

print("\n========== STUDENT INFORMATION ==========")

print("Name:", name)

print("Country:", country)

print("University:", university)

print("Course:", course)


# ------------------------------------------------
# SECTION 6: INPUT AND TYPE CONVERSION
# ------------------------------------------------

print("\n" + "=" * 70)

print("                INPUT TYPE CONVERSION")

print("=" * 70)

# Remember:
# input() always returns a string.
#
# If we want to perform mathematical calculations,
# we must convert the input into a numerical data type.

# Collect age from the user and convert it into integer.

age = int(input("Enter your age: "))

# Collect height and convert it into float.

height = float(input("Enter your height in metres: "))

# Display the information.

print("\nYour Age:", age)

print("Your Height:", height)

# Check the data types.

print("Age Data Type:", type(age))

print("Height Data Type:", type(height))


# ------------------------------------------------
# SECTION 7: PERFORMING CALCULATIONS WITH INPUT
# ------------------------------------------------

print("\n" + "=" * 70)

print("              USER INPUT CALCULATIONS")

print("=" * 70)

# Ask the user to enter two numerical values.
#
# float() allows the user to enter whole numbers
# or decimal numbers.

number_1 = float(input("Enter the first number: "))

number_2 = float(input("Enter the second number: "))

# Perform different mathematical operations.

addition = number_1 + number_2

subtraction = number_1 - number_2

multiplication = number_1 * number_2

# Check that the second number is not zero.
# Division by zero is not allowed in Python.

if number_2 != 0:

    division = number_1 / number_2

else:

    division = "Cannot divide by zero"

# Display the results.

print("\n========== CALCULATION RESULTS ==========")

print("Addition:", addition)

print("Subtraction:", subtraction)

print("Multiplication:", multiplication)

print("Division:", division)


# ------------------------------------------------
# SECTION 8: PRINT() SEP PARAMETER
# ------------------------------------------------

print("\n" + "=" * 70)

print("                  SEP PARAMETER")

print("=" * 70)

# sep means separator.
#
# By default, print() separates multiple values
# using a single space.
#
# We can change the separator using sep.

print("Python", "Machine Learning", "Deep Learning")

# Separate values using commas.

print("Python", "Machine Learning", "Deep Learning", sep=", ")

# Separate values using hyphens.

print("2026", "11", "03", sep="-")

# Separate values using vertical bars.

print("Name", "Age", "Course", sep=" | ")


# ------------------------------------------------
# SECTION 9: PRINT() END PARAMETER
# ------------------------------------------------

print("\n" + "=" * 70)

print("                  END PARAMETER")

print("=" * 70)

# By default, print() moves to a new line
# after displaying its output.
#
# The end parameter changes what happens
# at the end of a print statement.

print("Hello")

print("World")

# Using end=" " keeps the next output on the same line.

print("Hello", end=" ")

print("World")

# Using end=" | " adds a separator instead of a new line.

print("Python", end=" | ")

print("Artificial Intelligence")


# ------------------------------------------------
# SECTION 10: ESCAPE CHARACTERS
# ------------------------------------------------

print("\n" + "=" * 70)

print("                 ESCAPE CHARACTERS")

print("=" * 70)

# Escape characters allow us to control
# the formatting of displayed text.

# \n creates a new line.

print("Hello\nWorld")

# \t creates a horizontal tab.

print("Name:\tAbdulsamad")

# \\ displays a backslash.

print("Python\\AI")

# \" displays double quotation marks inside text.

print("He said: \"Python is powerful.\"")

# \' displays a single quotation mark.

print('It\'s time to learn Python.')


# ------------------------------------------------
# SECTION 11: FORMATTED OUTPUT USING F-STRINGS
# ------------------------------------------------

print("\n" + "=" * 70)

print("                 PYTHON F-STRINGS")

print("=" * 70)

# An f-string allows us to insert variables
# and expressions directly inside a string.
#
# We place the letter f before the quotation marks.
#
# Variables are written inside curly brackets {}.

student = "Abdulsamad"

age = 23

marks = 95.5678

print(f"My name is {student}.")

print(f"I am {age} years old.")

print(f"My examination marks are {marks}.")

# We can also perform calculations inside f-strings.

print(f"Next year I will be {age + 1} years old.")

# We can control decimal places.
# :.2f displays a floating-point number
# with two digits after the decimal point.

print(f"My marks are {marks:.2f}.")


# ------------------------------------------------
# SECTION 12: COLLECTING MULTIPLE VALUES IN ONE INPUT
# ------------------------------------------------

print("\n" + "=" * 70)

print("               MULTIPLE VALUES IN ONE INPUT")

print("=" * 70)

# The split() method separates a string into parts.
#
# The user enters two values separated by a space.
#
# Example:
# 10 20
#
# split() produces:
# ["10", "20"]

first_value, second_value = input(
    "Enter two numbers separated by a space: "
).split()

# Convert both strings into integers.

first_value = int(first_value)

second_value = int(second_value)

# Perform addition.

total = first_value + second_value

print("First Number:", first_value)

print("Second Number:", second_value)

print("Total:", total)


# ------------------------------------------------
# SECTION 13: FORMATTING DECIMAL OUTPUT
# ------------------------------------------------

print("\n" + "=" * 70)

print("               DECIMAL FORMATTING")

print("=" * 70)

# Create a floating-point number.

accuracy = 95.678945

# Display the value using different decimal precision.

print(f"Original Accuracy: {accuracy}")

print(f"Two Decimal Places: {accuracy:.2f}")

print(f"One Decimal Place: {accuracy:.1f}")

print(f"Three Decimal Places: {accuracy:.3f}")


# ------------------------------------------------
# SECTION 14: INPUT VALIDATION USING TRY AND EXCEPT
# ------------------------------------------------

print("\n" + "=" * 70)

print("                 INPUT VALIDATION")

print("=" * 70)

# Sometimes users enter incorrect information.
#
# For example, a user might enter "Hello"
# instead of a numerical age.
#
# int("Hello") causes a ValueError.
#
# We use try and except to handle this problem.

user_age = input("Enter your age: ")

try:

    # Attempt to convert the input into an integer.

    converted_age = int(user_age)

    print("Your Age:", converted_age)

except ValueError:

    # This block executes if the conversion fails.

    print("Invalid input! Please enter a whole number.")


# ------------------------------------------------
# SECTION 15: AI APPLICATION - STUDENT DATA INPUT
# ------------------------------------------------

print("\n" + "=" * 70)

print("             AI STUDENT DATA COLLECTION")

print("=" * 70)

# AI and data science projects frequently collect
# numerical and categorical information.
#
# Here we simulate collecting student information.

student_name = input("Enter student name: ")

mathematics = float(input("Enter Mathematics marks: "))

physics = float(input("Enter Physics marks: "))

python_marks = float(input("Enter Python marks: "))

# Calculate the average marks.

average_marks = (
    mathematics + physics + python_marks
) / 3

# Display a formatted report.

print("\n========== STUDENT PERFORMANCE REPORT ==========")

print(f"Student Name: {student_name}")

print(f"Mathematics: {mathematics:.2f}")

print(f"Physics: {physics:.2f}")

print(f"Python: {python_marks:.2f}")

print(f"Average Marks: {average_marks:.2f}")


# ------------------------------------------------
# SECTION 16: AI APPLICATION - MODEL INFORMATION INPUT
# ------------------------------------------------

print("\n" + "=" * 70)

print("               AI MODEL INFORMATION")

print("=" * 70)

# Imagine that a developer wants to collect
# information about a machine learning model.

model_name = input("Enter your AI model name: ")

model_accuracy = float(
    input("Enter model accuracy percentage: ")
)

training_epochs = int(
    input("Enter number of training epochs: ")
)

learning_rate = float(
    input("Enter learning rate: ")
)

# Display the collected model information.

print("\n========== AI MODEL REPORT ==========")

print(f"Model Name: {model_name}")

print(f"Accuracy: {model_accuracy:.2f}%")

print(f"Training Epochs: {training_epochs}")

print(f"Learning Rate: {learning_rate:.5f}")


# ------------------------------------------------
# SECTION 17: AI APPLICATION - IMAGE DATA INPUT
# ------------------------------------------------

print("\n" + "=" * 70)

print("                IMAGE DATA INPUT")

print("=" * 70)

# Imagine that we are collecting pixel information
# from a small example image.
#
# Standard 8-bit image channel values range
# from 0 to 255.

pixel_1 = int(input("Enter first pixel value (0-255): "))

pixel_2 = int(input("Enter second pixel value (0-255): "))

pixel_3 = int(input("Enter third pixel value (0-255): "))

# Calculate the average of the three pixel values.

average_pixel = (
    pixel_1 + pixel_2 + pixel_3
) / 3

# Display the results.

print("\n========== IMAGE PIXEL REPORT ==========")

print("First Pixel:", pixel_1)

print("Second Pixel:", pixel_2)

print("Third Pixel:", pixel_3)

print(f"Average Pixel Value: {average_pixel:.2f}")


# ------------------------------------------------
# SECTION 18: FINAL PROGRAM SUMMARY
# ------------------------------------------------

print("\n" + "=" * 70)

print("                DAY 006 FINAL REPORT")

print("=" * 70)

print("Basic Output: Completed")

print("User Input: Completed")

print("Multiple Inputs: Completed")

print("Type Conversion: Completed")

print("Mathematical Calculations: Completed")

print("SEP Parameter: Completed")

print("END Parameter: Completed")

print("Escape Characters: Completed")

print("F-Strings: Completed")

print("String Splitting: Completed")

print("Decimal Formatting: Completed")

print("Input Validation: Completed")

print("AI Data Collection Examples: Completed")

print("\nDAY 006 MAIN LESSON COMPLETED SUCCESSFULLY!")

print("=" * 70)


# ================================================================
# END OF DAY 006 - PYTHON INPUT AND OUTPUT
# ================================================================
