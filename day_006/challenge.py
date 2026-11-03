
# ================================================================
# DAY 006 - PYTHON PROGRAMMING CHALLENGE
# AI STUDENT DATA ANALYZER
#
# Bachelor's in Artificial Intelligence
# 90-Day Python Programming Journey
#
# Concepts:
# input(), print(), int(), float(), f-strings,
# input validation, mathematical calculations,
# data normalization and formatted reports.
# ================================================================


# ------------------------------------------------
# SECTION 1: PROGRAM INTRODUCTION
# ------------------------------------------------

print("=" * 70)

print("              AI STUDENT DATA ANALYZER")

print("=" * 70)

print("Welcome to the AI Student Data Analyzer!")

print("This program collects and analyzes student information.")

print("=" * 70)


# ------------------------------------------------
# SECTION 2: COLLECT STUDENT INFORMATION
# ------------------------------------------------

print("\nSTUDENT INFORMATION")

# Collect the student's name.
# input() receives information as a string.

student_name = input("Enter your full name: ").strip()

# Collect the student's country.

country = input("Enter your country: ").strip()

# Collect the student's university.

university = input("Enter your university: ").strip()

# Collect the student's age.
# int() converts the input string into an integer.

student_age = int(input("Enter your age: "))

# Collect the student's course.

course = input("Enter your course: ").strip()


# ------------------------------------------------
# SECTION 3: COLLECT EXAMINATION MARKS
# ------------------------------------------------

print("\n" + "=" * 70)

print("              EXAMINATION MARKS")

print("=" * 70)

# Collect marks for three subjects.
# float() allows decimal values.

mathematics = float(input("Enter Mathematics marks (0-100): "))

physics = float(input("Enter Physics marks (0-100): "))

python_marks = float(input("Enter Python marks (0-100): "))


# ------------------------------------------------
# SECTION 4: VALIDATE STUDENT DATA
# ------------------------------------------------

print("\n" + "=" * 70)

print("              STUDENT DATA VALIDATION")

print("=" * 70)

# Check that the personal information is not empty.

if not student_name or not country or not university or not course:

    raise ValueError("Student information cannot be empty.")

# Check that the age is positive.

if student_age <= 0:

    raise ValueError("Age must be greater than zero.")

# Check that all marks are between 0 and 100.

if not (
    0 <= mathematics <= 100
    and 0 <= physics <= 100
    and 0 <= python_marks <= 100
):

    raise ValueError("Marks must be between 0 and 100.")

print("Student information: Valid")

print("Examination marks: Valid")


# ------------------------------------------------
# SECTION 5: CALCULATE TOTAL AND AVERAGE MARKS
# ------------------------------------------------

print("\n" + "=" * 70)

print("              ACADEMIC CALCULATIONS")

print("=" * 70)

# Calculate total marks using addition.

total_marks = mathematics + physics + python_marks

# There are three subjects.
# Divide the total marks by three to calculate the average.

average_marks = total_marks / 3

# Calculate the percentage.
# Each subject has a maximum of 100 marks.
# Therefore, the total maximum marks are 300.

percentage = (total_marks / 300) * 100

print(f"Total Marks: {total_marks:.2f}/300")

print(f"Average Marks: {average_marks:.2f}")

print(f"Percentage: {percentage:.2f}%")


# ------------------------------------------------
# SECTION 6: CLASSIFY STUDENT PERFORMANCE
# ------------------------------------------------

print("\n" + "=" * 70)

print("              STUDENT PERFORMANCE")

print("=" * 70)

# Use conditional statements to classify performance.

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

    performance = "Average"

elif average_marks >= 50:

    grade = "E"

    performance = "Pass"

else:

    grade = "F"

    performance = "Fail"

print("Student Grade:", grade)

print("Performance:", performance)


# ------------------------------------------------
# SECTION 7: NORMALIZE STUDENT MARKS
# ------------------------------------------------

print("\n" + "=" * 70)

print("              DATA NORMALIZATION")

print("=" * 70)

# Normalization converts values from a 0-100 range
# into a 0-1 range.
#
# Formula:
# Normalized Value = Original Value / 100
#
# This is an example of simple numerical preprocessing.
# It is not the only normalization technique used in AI.

normalized_math = mathematics / 100

normalized_physics = physics / 100

normalized_python = python_marks / 100

print(f"Normalized Mathematics: {normalized_math:.3f}")

print(f"Normalized Physics: {normalized_physics:.3f}")

print(f"Normalized Python: {normalized_python:.3f}")


# ------------------------------------------------
# SECTION 8: COLLECT AI MODEL INFORMATION
# ------------------------------------------------

print("\n" + "=" * 70)

print("              AI MODEL INFORMATION")

print("=" * 70)

# Collect the name of an AI model.

model_name = input("Enter AI model name: ").strip()

# Collect model accuracy.

model_accuracy = float(
    input("Enter model accuracy percentage: ")
)

# Collect training epochs.

training_epochs = int(
    input("Enter number of training epochs: ")
)

# Collect learning rate.

learning_rate = float(
    input("Enter learning rate: ")
)


# ------------------------------------------------
# SECTION 9: VALIDATE AI MODEL INFORMATION
# ------------------------------------------------

print("\n" + "=" * 70)

print("              AI MODEL VALIDATION")

print("=" * 70)

# Check that model name is not empty.

if not model_name:

    raise ValueError("Model name cannot be empty.")

# Accuracy must be between 0 and 100.

if not 0 <= model_accuracy <= 100:

    raise ValueError("Model accuracy must be between 0 and 100.")

# Training epochs must be positive.

if training_epochs <= 0:

    raise ValueError("Training epochs must be greater than zero.")

# Learning rate must be positive.

if learning_rate <= 0:

    raise ValueError("Learning rate must be greater than zero.")

print("AI model information: Valid")


# ------------------------------------------------
# SECTION 10: CLASSIFY AI MODEL PERFORMANCE
# ------------------------------------------------

print("\n" + "=" * 70)

print("              AI MODEL PERFORMANCE")

print("=" * 70)

# Classify the AI model using its accuracy.

if model_accuracy >= 95:

    model_performance = "Outstanding"

elif model_accuracy >= 90:

    model_performance = "Excellent"

elif model_accuracy >= 80:

    model_performance = "Good"

elif model_accuracy >= 70:

    model_performance = "Average"

else:

    model_performance = "Needs Improvement"

print("Model Name:", model_name)

print(f"Model Accuracy: {model_accuracy:.2f}%")

print("Model Performance:", model_performance)


# ------------------------------------------------
# SECTION 11: LEARNING RATE INFORMATION
# ------------------------------------------------

print("\n" + "=" * 70)

print("              LEARNING RATE ANALYSIS")

print("=" * 70)

# Reduce the learning rate by 10 percent.
# This demonstrates a simple numerical update.

updated_learning_rate = learning_rate * 0.90

print(f"Original Learning Rate: {learning_rate:.6f}")

print(f"Updated Learning Rate: {updated_learning_rate:.6f}")

print("Training Epochs:", training_epochs)


# ------------------------------------------------
# SECTION 12: GENERATE STUDENT REPORT
# ------------------------------------------------

print("\n" + "=" * 70)

print("              FINAL STUDENT REPORT")

print("=" * 70)

# Display all student information using f-strings.

print(f"Student Name: {student_name}")

print(f"Age: {student_age}")

print(f"Country: {country}")

print(f"University: {university}")

print(f"Course: {course}")

print("-" * 70)

print("ACADEMIC RESULTS")

print(f"Mathematics: {mathematics:.2f}")

print(f"Physics: {physics:.2f}")

print(f"Python: {python_marks:.2f}")

print(f"Total Marks: {total_marks:.2f}/300")

print(f"Average Marks: {average_marks:.2f}")

print(f"Percentage: {percentage:.2f}%")

print(f"Grade: {grade}")

print(f"Performance: {performance}")


# ------------------------------------------------
# SECTION 13: GENERATE AI MODEL REPORT
# ------------------------------------------------

print("\n" + "=" * 70)

print("              FINAL AI MODEL REPORT")

print("=" * 70)

print(f"Model Name: {model_name}")

print(f"Accuracy: {model_accuracy:.2f}%")

print(f"Performance: {model_performance}")

print(f"Training Epochs: {training_epochs}")

print(f"Original Learning Rate: {learning_rate:.6f}")

print(f"Updated Learning Rate: {updated_learning_rate:.6f}")


# ------------------------------------------------
# SECTION 14: FINAL PROGRAM SUMMARY
# ------------------------------------------------

print("\n" + "=" * 70)

print("              PROGRAM SUMMARY")

print("=" * 70)

print("Student Data Collection: Completed")

print("Input Type Conversion: Completed")

print("Input Validation: Completed")

print("Academic Calculations: Completed")

print("Student Performance Classification: Completed")

print("Data Normalization: Completed")

print("AI Model Information Collection: Completed")

print("AI Model Performance Analysis: Completed")

print("Formatted Report Generation: Completed")

print("\nDAY 006 CHALLENGE COMPLETED SUCCESSFULLY!")

print("=" * 70)


# ================================================================
# END OF DAY 006 - AI STUDENT DATA ANALYZER
# ================================================================
