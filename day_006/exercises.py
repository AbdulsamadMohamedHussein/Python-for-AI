
# ================================================================
# DAY 006 - PYTHON INPUT AND OUTPUT
# SOLVED PRACTICAL EXERCISES
#
# Bachelor's in Artificial Intelligence
# 90-Day Python Programming Journey
#
# Topics:
# print(), input(), type conversion, f-strings,
# sep, end, split(), escape characters,
# input validation and AI applications.
# ================================================================


# ------------------------------------------------
# EXERCISE 1: BASIC OUTPUT
# ------------------------------------------------

# QUESTION:
# Display your name, age, country and AI course
# using the print() function.

print("=" * 65)
print("EXERCISE 1: BASIC OUTPUT")
print("=" * 65)

# Store student information in variables.

student_name = "Abdulsamad"
student_age = 23
country = "Pakistan"
course = "Artificial Intelligence"

# Display the information.

print("Student Name:", student_name)
print("Age:", student_age)
print("Country:", country)
print("Course:", course)


# ------------------------------------------------
# EXERCISE 2: COLLECTING USER INPUT
# ------------------------------------------------

# QUESTION:
# Ask the user to enter their name and country.
# Display a welcome message.

print("\n" + "=" * 65)
print("EXERCISE 2: USER INPUT")
print("=" * 65)

# input() collects information from the user.
# The entered information is stored as a string.

name = input("Enter your name: ")

user_country = input("Enter your country: ")

# Display the collected information.

print("\nWelcome,", name)

print("Your country is:", user_country)

print("Welcome to Python for AI!")


# ------------------------------------------------
# EXERCISE 3: INTEGER AND FLOAT INPUT
# ------------------------------------------------

# QUESTION:
# Ask the user to enter their age and height.
# Convert age into an integer and height into a float.
# Display their data types.

print("\n" + "=" * 65)
print("EXERCISE 3: TYPE CONVERSION")
print("=" * 65)

# Convert the user's age into an integer.

age = int(input("Enter your age: "))

# Convert the user's height into a decimal number.

height = float(input("Enter your height in metres: "))

# Display the values.

print("Your Age:", age)

print("Your Height:", height)

# Check the data types.

print("Age Type:", type(age))

print("Height Type:", type(height))


# ------------------------------------------------
# EXERCISE 4: SIMPLE CALCULATOR
# ------------------------------------------------

# QUESTION:
# Ask the user to enter two numbers.
# Calculate addition, subtraction, multiplication
# and division.

print("\n" + "=" * 65)
print("EXERCISE 4: SIMPLE CALCULATOR")
print("=" * 65)

# Collect two numbers.
# float() allows decimal input.

number_1 = float(input("Enter first number: "))

number_2 = float(input("Enter second number: "))

# Perform mathematical calculations.

addition = number_1 + number_2

subtraction = number_1 - number_2

multiplication = number_1 * number_2

# Check for division by zero.

if number_2 != 0:

    division = number_1 / number_2

else:

    division = "Cannot divide by zero"

# Display the results.

print("\nCALCULATOR RESULTS")

print("Addition:", addition)

print("Subtraction:", subtraction)

print("Multiplication:", multiplication)

print("Division:", division)


# ------------------------------------------------
# EXERCISE 5: USING SEP AND END
# ------------------------------------------------

# QUESTION:
# Display information using different separators.
# Use end to print multiple values on the same line.

print("\n" + "=" * 65)
print("EXERCISE 5: SEP AND END")
print("=" * 65)

# sep changes the separator between values.

print("Python", "NumPy", "Pandas", sep=" | ")

print("2026", "11", "03", sep="-")

# end changes what print() displays at the end.
# Normally, print() moves to a new line.
# Here, we use a space instead.

print("Artificial", end=" ")

print("Intelligence")

# We can also use a custom ending.

print("Machine Learning", end=" -> ")

print("Deep Learning")


# ------------------------------------------------
# EXERCISE 6: ESCAPE CHARACTERS
# ------------------------------------------------

# QUESTION:
# Display information using new lines, tabs
# and quotation marks.

print("\n" + "=" * 65)
print("EXERCISE 6: ESCAPE CHARACTERS")
print("=" * 65)

# \n creates a new line.

print("Welcome to Python\nWelcome to AI")

# \t creates a horizontal tab.

print("Name:\tAbdulsamad")

print("Course:\tArtificial Intelligence")

# \\ displays a backslash.

print("Python\\AI")

# \" displays quotation marks inside a string.

print("He said: \"Python is powerful.\"")


# ------------------------------------------------
# EXERCISE 7: F-STRINGS
# ------------------------------------------------

# QUESTION:
# Collect student information and display it
# using formatted strings.

print("\n" + "=" * 65)
print("EXERCISE 7: F-STRINGS")
print("=" * 65)

# Collect information.

student = input("Enter student name: ")

student_age = int(input("Enter student age: "))

student_marks = float(input("Enter student marks: "))

# Display information using f-strings.
# Variables are placed inside curly brackets.

print("\nSTUDENT INFORMATION")

print(f"Student Name: {student}")

print(f"Student Age: {student_age}")

print(f"Student Marks: {student_marks:.2f}")

# We can perform calculations inside f-strings.

print(f"Next year your age will be {student_age + 1}.")


# ------------------------------------------------
# EXERCISE 8: MULTIPLE INPUTS USING SPLIT()
# ------------------------------------------------

# QUESTION:
# Ask the user to enter three numbers in one line.
# Separate the numbers and calculate their average.

print("\n" + "=" * 65)
print("EXERCISE 8: MULTIPLE INPUTS USING SPLIT")
print("=" * 65)

# The user enters three values separated by spaces.
#
# Example:
# 80 90 100
#
# split() separates the string into three parts.

value_1, value_2, value_3 = input(
    "Enter three marks separated by spaces: "
).split()

# Convert the strings into floating-point numbers.

mark_1 = float(value_1)

mark_2 = float(value_2)

mark_3 = float(value_3)

# Calculate the average.

average = (mark_1 + mark_2 + mark_3) / 3

# Display the results.

print("\nMARKS REPORT")

print("First Mark:", mark_1)

print("Second Mark:", mark_2)

print("Third Mark:", mark_3)

print(f"Average Marks: {average:.2f}")


# ------------------------------------------------
# EXERCISE 9: DECIMAL FORMATTING
# ------------------------------------------------

# QUESTION:
# Display a numerical value using different
# decimal precision.

print("\n" + "=" * 65)
print("EXERCISE 9: DECIMAL FORMATTING")
print("=" * 65)

# Create a decimal value.

model_accuracy = 95.678945

# Display the original value.

print("Original Accuracy:", model_accuracy)

# Display two decimal places.

print(f"Two Decimal Places: {model_accuracy:.2f}")

# Display three decimal places.

print(f"Three Decimal Places: {model_accuracy:.3f}")

# Display one decimal place.

print(f"One Decimal Place: {model_accuracy:.1f}")


# ------------------------------------------------
# EXERCISE 10: INPUT VALIDATION
# ------------------------------------------------

# QUESTION:
# Ask the user to enter their age.
# Handle invalid input using try and except.

print("\n" + "=" * 65)
print("EXERCISE 10: INPUT VALIDATION")
print("=" * 65)

# Collect input as a string.

user_age = input("Enter your age: ")

try:

    # Attempt to convert the input into an integer.

    converted_age = int(user_age)

    print("Your Age:", converted_age)

    print("Age Data Type:", type(converted_age))

except ValueError:

    # This block executes when the input
    # cannot be converted into an integer.

    print("Invalid input!")

    print("Please enter a valid whole number.")


# ------------------------------------------------
# EXERCISE 11: AI MODEL INFORMATION COLLECTION
# ------------------------------------------------

# QUESTION:
# Create a program that collects AI model information.
# Ask for model name, accuracy, epochs and learning rate.
# Display a formatted report.

print("\n" + "=" * 65)
print("EXERCISE 11: AI MODEL INFORMATION")
print("=" * 65)

# Collect the model information.

model_name = input("Enter model name: ")

accuracy = float(input("Enter model accuracy percentage: "))

epochs = int(input("Enter training epochs: "))

learning_rate = float(input("Enter learning rate: "))

# Display the information in a clean report.

print("\n========== AI MODEL REPORT ==========")

print(f"Model Name: {model_name}")

print(f"Model Accuracy: {accuracy:.2f}%")

print(f"Training Epochs: {epochs}")

print(f"Learning Rate: {learning_rate:.5f}")

print("=" * 65)


# ------------------------------------------------
# EXERCISE 12: COMPUTER VISION PIXEL DATA
# ------------------------------------------------

# QUESTION:
# Collect three pixel values from the user.
# Calculate their average and normalize them.
#
# Standard 8-bit image pixel values range from 0 to 255.
#
# Normalization formula:
# Normalized Pixel = Pixel Value / 255

print("\n" + "=" * 65)
print("EXERCISE 12: COMPUTER VISION PIXELS")
print("=" * 65)

# Collect pixel values.

pixel_1 = int(input("Enter first pixel value (0-255): "))

pixel_2 = int(input("Enter second pixel value (0-255): "))

pixel_3 = int(input("Enter third pixel value (0-255): "))

# Validate that all pixel values are within the
# permitted 8-bit range.

if (
    0 <= pixel_1 <= 255
    and 0 <= pixel_2 <= 255
    and 0 <= pixel_3 <= 255
):

    # Calculate the average pixel value.

    average_pixel = (
        pixel_1 + pixel_2 + pixel_3
    ) / 3

    # Normalize each pixel into the range 0 to 1.

    normalized_1 = pixel_1 / 255

    normalized_2 = pixel_2 / 255

    normalized_3 = pixel_3 / 255

    # Display the results.

    print("\nPIXEL ANALYSIS REPORT")

    print("Pixel 1:", pixel_1)

    print("Pixel 2:", pixel_2)

    print("Pixel 3:", pixel_3)

    print(f"Average Pixel: {average_pixel:.2f}")

    print(f"Normalized Pixel 1: {normalized_1:.4f}")

    print(f"Normalized Pixel 2: {normalized_2:.4f}")

    print(f"Normalized Pixel 3: {normalized_3:.4f}")

else:

    print("Invalid pixel value!")

    print("Pixel values must be between 0 and 255.")


# ------------------------------------------------
# FINAL EXERCISE SUMMARY
# ------------------------------------------------

print("\n" + "=" * 65)

print("              DAY 006 EXERCISES SUMMARY")

print("=" * 65)

print("Exercise 1: Basic Output - Completed")

print("Exercise 2: User Input - Completed")

print("Exercise 3: Type Conversion - Completed")

print("Exercise 4: Simple Calculator - Completed")

print("Exercise 5: SEP and END - Completed")

print("Exercise 6: Escape Characters - Completed")

print("Exercise 7: F-Strings - Completed")

print("Exercise 8: Multiple Inputs - Completed")

print("Exercise 9: Decimal Formatting - Completed")

print("Exercise 10: Input Validation - Completed")

print("Exercise 11: AI Model Information - Completed")

print("Exercise 12: Computer Vision Pixels - Completed")

print("\nALL DAY 006 EXERCISES COMPLETED!")

print("=" * 65)


# ================================================================
# END OF DAY 006 - EXERCISES.PY
# ================================================================
