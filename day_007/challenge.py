
# =================================================================
# DAY 007 - PYTHON FUNDAMENTALS CHALLENGE
#
# PROJECT: AI STUDENT MANAGEMENT AND PERFORMANCE SYSTEM
#
# Bachelor's in Artificial Intelligence
# 90-Day Python Programming Journey
#
# Revision of Days 001-006
#
# Concepts:
# Variables, Data Types, Type Conversion, Operators,
# Input, Output, F-Strings, Conditions, Validation,
# Mathematical Calculations and AI Data Normalization.
# =================================================================


# =================================================================
# SECTION 1: PROGRAM INTRODUCTION
# =================================================================

# Display the application heading.
# print() displays information in the terminal.
# Multiplying a string repeats it.

print("=" * 75)

print("          AI STUDENT MANAGEMENT AND PERFORMANCE SYSTEM")

print("=" * 75)

print("Welcome to the AI Student Management System!")

print("This application analyzes student academic performance.")

print("=" * 75)


# =================================================================
# SECTION 2: STUDENT REGISTRATION
# =================================================================

print("\nSECTION 1: STUDENT REGISTRATION")

print("-" * 75)

# Collect student information.
# input() returns a string.
# strip() removes spaces from the beginning and end.

student_name = input("Enter student full name: ").strip()

student_id = input("Enter student ID: ").strip()

country = input("Enter your country: ").strip()

university = input("Enter your university: ").strip()

course = input("Enter your course: ").strip()

# Convert age into an integer.

student_age = int(input("Enter your age: "))


# =================================================================
# SECTION 3: STUDENT INFORMATION VALIDATION
# =================================================================

print("\nSECTION 2: STUDENT VALIDATION")

print("-" * 75)

# Check that required information is not empty.

if not all([student_name, student_id, country, university, course]):

    raise ValueError("Student information cannot be empty.")

# Check that the student's age is positive.

if student_age <= 0:

    raise ValueError("Age must be greater than zero.")

print("Student registration information is valid.")


# =================================================================
# SECTION 4: COLLECT ACADEMIC MARKS
# =================================================================

print("\nSECTION 3: ACADEMIC INFORMATION")

print("-" * 75)

# Collect four examination marks.
# float() allows decimal values.

mathematics = float(input("Enter Mathematics marks (0-100): "))

physics = float(input("Enter Physics marks (0-100): "))

python_marks = float(input("Enter Python marks (0-100): "))

chemistry = float(input("Enter Chemistry marks (0-100): "))


# =================================================================
# SECTION 5: VALIDATE EXAMINATION MARKS
# =================================================================

print("\nSECTION 4: EXAMINATION VALIDATION")

print("-" * 75)

# Check whether every subject mark is between 0 and 100.
#
# The AND operator means every condition must be True.

valid_marks = (
    0 <= mathematics <= 100
    and 0 <= physics <= 100
    and 0 <= python_marks <= 100
    and 0 <= chemistry <= 100
)

if valid_marks:

    print("All examination marks are valid.")

else:

    raise ValueError("Marks must be between 0 and 100.")


# =================================================================
# SECTION 6: CALCULATE ACADEMIC RESULTS
# =================================================================

print("\nSECTION 5: ACADEMIC CALCULATIONS")

print("-" * 75)

# Calculate total marks.

total_marks = (
    mathematics
    + physics
    + python_marks
    + chemistry
)

# Four subjects, each with a maximum of 100 marks.

maximum_marks = 400

# Calculate average marks.

average_marks = total_marks / 4

# Calculate percentage.

percentage = (total_marks / maximum_marks) * 100

print(f"Total Marks: {total_marks:.2f}/400")

print(f"Average Marks: {average_marks:.2f}")

print(f"Percentage: {percentage:.2f}%")


# =================================================================
# SECTION 7: ACADEMIC GRADE CLASSIFICATION
# =================================================================

print("\nSECTION 6: GRADE CLASSIFICATION")

print("-" * 75)

# Use conditional statements to classify performance.
#
# if checks the first condition.
# elif checks additional conditions.
# else executes if none of the conditions is True.

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

print("Student Grade:", grade)

print("Performance:", performance)


# =================================================================
# SECTION 8: SUBJECT PERFORMANCE ANALYSIS
# =================================================================

print("\nSECTION 7: SUBJECT PERFORMANCE ANALYSIS")

print("-" * 75)

# Compare the four subjects to identify the highest score.

highest_score = max(
    mathematics,
    physics,
    python_marks,
    chemistry
)

lowest_score = min(
    mathematics,
    physics,
    python_marks,
    chemistry
)

# Identify the subject with the highest score.

if highest_score == mathematics:

    best_subject = "Mathematics"

elif highest_score == physics:

    best_subject = "Physics"

elif highest_score == python_marks:

    best_subject = "Python"

else:

    best_subject = "Chemistry"

# Identify the subject with the lowest score.

if lowest_score == mathematics:

    weakest_subject = "Mathematics"

elif lowest_score == physics:

    weakest_subject = "Physics"

elif lowest_score == python_marks:

    weakest_subject = "Python"

else:

    weakest_subject = "Chemistry"

print("Highest Score:", highest_score)

print("Best Subject:", best_subject)

print("Lowest Score:", lowest_score)

print("Subject Requiring Improvement:", weakest_subject)


# =================================================================
# SECTION 9: COMPARISON AND LOGICAL OPERATORS
# =================================================================

print("\nSECTION 8: LOGICAL PERFORMANCE ANALYSIS")

print("-" * 75)

# A student passes when the average is at least 50
# and Python marks are at least 40.

passed = (
    average_marks >= 50
    and python_marks >= 40
)

# Check whether the student has excellent performance
# in either overall average or Python marks.

excellent_performance = (
    average_marks >= 85
    or python_marks >= 90
)

# not reverses the Boolean result.

failed = not passed

print("Student Passed:", passed)

print("Excellent Performance:", excellent_performance)

print("Student Failed:", failed)


# =================================================================
# SECTION 10: AI DATA NORMALIZATION
# =================================================================

print("\nSECTION 9: AI DATA NORMALIZATION")

print("-" * 75)

# Normalization scales the marks from 0-100 into 0-1.
#
# Formula:
#
# Normalized Value = Original Value / 100
#
# This is an example of numerical preprocessing.

normalized_math = mathematics / 100

normalized_physics = physics / 100

normalized_python = python_marks / 100

normalized_chemistry = chemistry / 100

print(f"Normalized Mathematics: {normalized_math:.3f}")

print(f"Normalized Physics: {normalized_physics:.3f}")

print(f"Normalized Python: {normalized_python:.3f}")

print(f"Normalized Chemistry: {normalized_chemistry:.3f}")


# =================================================================
# SECTION 11: AI MODEL REGISTRATION
# =================================================================

print("\nSECTION 10: AI MODEL INFORMATION")

print("-" * 75)

# Collect information about an imaginary AI model.

model_name = input("Enter AI model name: ").strip()

model_accuracy = float(
    input("Enter model accuracy (0-100): ")
)

training_epochs = int(
    input("Enter number of training epochs: ")
)

learning_rate = float(
    input("Enter learning rate: ")
)


# =================================================================
# SECTION 12: AI MODEL VALIDATION
# =================================================================

print("\nSECTION 11: AI MODEL VALIDATION")

print("-" * 75)

# Validate model information.

if not model_name:

    raise ValueError("Model name cannot be empty.")

if not 0 <= model_accuracy <= 100:

    raise ValueError("Model accuracy must be between 0 and 100.")

if training_epochs <= 0:

    raise ValueError("Training epochs must be positive.")

if learning_rate <= 0:

    raise ValueError("Learning rate must be positive.")

print("AI model information is valid.")


# =================================================================
# SECTION 13: AI MODEL PERFORMANCE
# =================================================================

print("\nSECTION 12: MODEL PERFORMANCE ANALYSIS")

print("-" * 75)

# Classify the model using its accuracy.

if model_accuracy >= 95:

    model_status = "Outstanding"

elif model_accuracy >= 90:

    model_status = "Excellent"

elif model_accuracy >= 80:

    model_status = "Good"

elif model_accuracy >= 70:

    model_status = "Average"

else:

    model_status = "Needs Improvement"

print("Model Name:", model_name)

print(f"Model Accuracy: {model_accuracy:.2f}%")

print("Model Status:", model_status)


# =================================================================
# SECTION 14: LEARNING RATE CALCULATION
# =================================================================

print("\nSECTION 13: LEARNING RATE CALCULATION")

print("-" * 75)

# Demonstrate reducing a learning rate by 10 percent.
#
# This is a numerical example, not an actual
# machine learning optimization procedure.

updated_learning_rate = learning_rate * 0.90

print(f"Original Learning Rate: {learning_rate:.6f}")

print(f"Updated Learning Rate: {updated_learning_rate:.6f}")

print("Training Epochs:", training_epochs)


# =================================================================
# SECTION 15: STRING FORMATTING
# =================================================================

print("\nSECTION 14: STRING FORMATTING")

print("-" * 75)

# f-strings insert variables into text.
# :.2f displays two decimal places.

print(f"Student: {student_name}")

print(f"Course: {course}")

print(f"Academic Average: {average_marks:.2f}")

print(f"AI Accuracy: {model_accuracy:.2f}%")

# sep changes the separator between values.

print("Python", "NumPy", "Pandas", sep=" | ")

# end changes what print() displays at the end.

print("Artificial Intelligence", end=" -> ")

print("Machine Learning")


# =================================================================
# SECTION 16: FINAL STUDENT REPORT
# =================================================================

print("\n" + "=" * 75)

print("                    FINAL STUDENT REPORT")

print("=" * 75)

print(f"Student Name: {student_name}")

print(f"Student ID: {student_id}")

print(f"Age: {student_age}")

print(f"Country: {country}")

print(f"University: {university}")

print(f"Course: {course}")

print("-" * 75)

print("ACADEMIC RESULTS")

print("-" * 75)

print(f"Mathematics: {mathematics:.2f}/100")

print(f"Physics: {physics:.2f}/100")

print(f"Python: {python_marks:.2f}/100")

print(f"Chemistry: {chemistry:.2f}/100")

print(f"Total Marks: {total_marks:.2f}/400")

print(f"Average Marks: {average_marks:.2f}")

print(f"Percentage: {percentage:.2f}%")

print(f"Grade: {grade}")

print(f"Performance: {performance}")

print(f"Best Subject: {best_subject}")

print(f"Subject Requiring Improvement: {weakest_subject}")


# =================================================================
# SECTION 17: FINAL AI MODEL REPORT
# =================================================================

print("\n" + "=" * 75)

print("                     AI MODEL REPORT")

print("=" * 75)

print(f"Model Name: {model_name}")

print(f"Model Accuracy: {model_accuracy:.2f}%")

print(f"Model Status: {model_status}")

print(f"Training Epochs: {training_epochs}")

print(f"Original Learning Rate: {learning_rate:.6f}")

print(f"Updated Learning Rate: {updated_learning_rate:.6f}")


# =================================================================
# SECTION 18: PROGRAM COMPLETION
# =================================================================

print("\n" + "=" * 75)

print("                  DAY 007 CHALLENGE SUMMARY")

print("=" * 75)

print("Student Registration: Completed")

print("Data Type Handling: Completed")

print("Type Conversion: Completed")

print("Mathematical Calculations: Completed")

print("Academic Analysis: Completed")

print("Logical Decision Making: Completed")

print("Data Normalization: Completed")

print("AI Model Registration: Completed")

print("AI Model Analysis: Completed")

print("Professional Report Generation: Completed")

print("\nDAY 007 CHALLENGE COMPLETED SUCCESSFULLY!")

print("=" * 75)


# =================================================================
# END OF DAY 007 - CHALLENGE.PY
# =================================================================
