
# ================================================================
# DAY 005 - PYTHON PROGRAMMING CHALLENGE
# AI MODEL PERFORMANCE ANALYZER
#
# Bachelor's in Artificial Intelligence
# 90-Day Python Programming Journey
#
# Topics:
# Arithmetic, Assignment, Comparison, Logical,
# Membership, Identity and Operator Precedence
# ================================================================


# ------------------------------------------------
# SECTION 1: PROGRAM INTRODUCTION
# ------------------------------------------------

print("=" * 65)
print("              AI MODEL PERFORMANCE ANALYZER")
print("=" * 65)

# This program evaluates an imaginary AI image classifier.
# We will use Python operators to calculate and analyse
# the performance of our machine learning model.


# ------------------------------------------------
# SECTION 2: MODEL INFORMATION
# ------------------------------------------------

model_name = "Image Classification Model"

total_images = 1000

correct_predictions = 940

incorrect_predictions = 60

learning_rate = 0.01

training_epochs = 50

# Display model information

print("\nMODEL INFORMATION")

print("Model Name:", model_name)

print("Total Images:", total_images)

print("Correct Predictions:", correct_predictions)

print("Incorrect Predictions:", incorrect_predictions)

print("Learning Rate:", learning_rate)

print("Training Epochs:", training_epochs)


# ------------------------------------------------
# SECTION 3: ARITHMETIC OPERATORS
# ------------------------------------------------

print("\n" + "=" * 65)
print("              ARITHMETIC CALCULATIONS")
print("=" * 65)

# Calculate total predictions.
# Addition operator combines correct and incorrect predictions.

calculated_total = (
    correct_predictions + incorrect_predictions
)

# Calculate accuracy.
# Accuracy = Correct Predictions / Total Predictions * 100

accuracy = (
    correct_predictions / total_images
) * 100

# Calculate error percentage.

error_percentage = (
    incorrect_predictions / total_images
) * 100

# Calculate the difference between correct and incorrect predictions.

prediction_difference = (
    correct_predictions - incorrect_predictions
)

# Calculate the ratio of correct predictions to incorrect predictions.

prediction_ratio = (
    correct_predictions / incorrect_predictions
)

print("Calculated Total:", calculated_total)

print("Model Accuracy:", accuracy, "%")

print("Error Percentage:", error_percentage, "%")

print("Prediction Difference:", prediction_difference)

print("Prediction Ratio:", prediction_ratio)


# ------------------------------------------------
# SECTION 4: ASSIGNMENT OPERATORS
# ------------------------------------------------

print("\n" + "=" * 65)
print("              ASSIGNMENT OPERATORS")
print("=" * 65)

# Store the original learning rate.

print("Original Learning Rate:", learning_rate)

# Reduce the learning rate by 10 percent.
# Multiplication assignment updates the existing variable.

learning_rate *= 0.90

print("After First Update:", learning_rate)

# Reduce it by another 10 percent.

learning_rate *= 0.90

print("After Second Update:", learning_rate)

# Increase the training epoch counter.

training_epochs += 10

print("Updated Training Epochs:", training_epochs)


# ------------------------------------------------
# SECTION 5: COMPARISON OPERATORS
# ------------------------------------------------

print("\n" + "=" * 65)
print("              COMPARISON OPERATORS")
print("=" * 65)

# Check different performance conditions.

print("Accuracy Above 90:", accuracy > 90)

print("Accuracy Below 90:", accuracy < 90)

print("Accuracy Equals 94:", accuracy == 94)

print("Accuracy At Least 90:", accuracy >= 90)

print("Error Below 10:", error_percentage < 10)

print("Predictions Not Equal:", correct_predictions != incorrect_predictions)


# ------------------------------------------------
# SECTION 6: LOGICAL OPERATORS
# ------------------------------------------------

print("\n" + "=" * 65)
print("                LOGICAL OPERATORS")
print("=" * 65)

# A model is considered excellent if:
# Accuracy is at least 90 AND error is below 10.

excellent_model = (
    accuracy >= 90 and error_percentage < 10
)

# A model is considered acceptable if:
# Accuracy is at least 75 OR error is below 25.

acceptable_model = (
    accuracy >= 75 or error_percentage < 25
)

# Reverse the excellent_model Boolean value.

not_excellent = not excellent_model

print("Excellent Model:", excellent_model)

print("Acceptable Model:", acceptable_model)

print("Not Excellent:", not_excellent)


# ------------------------------------------------
# SECTION 7: MEMBERSHIP OPERATORS
# ------------------------------------------------

print("\n" + "=" * 65)
print("                MEMBERSHIP OPERATORS")
print("=" * 65)

ai_techniques = [
    "Machine Learning",
    "Deep Learning",
    "Computer Vision",
    "Natural Language Processing",
    "Neural Networks"
]

# Check whether particular techniques exist.

print(
    "Deep Learning Available:",
    "Deep Learning" in ai_techniques
)

print(
    "Robotics Available:",
    "Robotics" in ai_techniques
)

print(
    "Robotics Not Available:",
    "Robotics" not in ai_techniques
)


# ------------------------------------------------
# SECTION 8: IDENTITY OPERATORS
# ------------------------------------------------

print("\n" + "=" * 65)
print("                 IDENTITY OPERATORS")
print("=" * 65)

model_status = None

another_status = model_status

different_status = "Completed"

# None represents the absence of a value.

print("Model Status Is None:", model_status is None)

print("Same Status Object:", model_status is another_status)

print("Different Status Object:", model_status is not different_status)


# ------------------------------------------------
# SECTION 9: BITWISE OPERATORS
# ------------------------------------------------

print("\n" + "=" * 65)
print("                  BITWISE OPERATORS")
print("=" * 65)

number_a = 5

number_b = 3

# Binary representation:
# 5 = 0101
# 3 = 0011

print("Binary AND:", number_a & number_b)

print("Binary OR:", number_a | number_b)

print("Binary XOR:", number_a ^ number_b)

print("Left Shift:", number_a << 1)

print("Right Shift:", number_a >> 1)


# ------------------------------------------------
# SECTION 10: OPERATOR PRECEDENCE
# ------------------------------------------------

print("\n" + "=" * 65)
print("                OPERATOR PRECEDENCE")
print("=" * 65)

# Multiplication happens before addition.

result_1 = 10 + 5 * 2

# Parentheses change the calculation order.

result_2 = (10 + 5) * 2

# Exponentiation happens before multiplication.

result_3 = 2 + 3 ** 2 * 2

print("Result One:", result_1)

print("Result Two:", result_2)

print("Result Three:", result_3)


# ------------------------------------------------
# SECTION 11: MODEL PERFORMANCE EVALUATION
# ------------------------------------------------

print("\n" + "=" * 65)
print("                MODEL EVALUATION")
print("=" * 65)

# Use conditional statements and comparison operators
# to determine the model's performance category.

if accuracy >= 95:

    performance = "Outstanding"

elif accuracy >= 90:

    performance = "Excellent"

elif accuracy >= 75:

    performance = "Good"

elif accuracy >= 50:

    performance = "Average"

else:

    performance = "Poor"

print("Model Performance:", performance)


# ------------------------------------------------
# SECTION 12: FINAL AI MODEL REPORT
# ------------------------------------------------

print("\n" + "=" * 65)
print("                  FINAL MODEL REPORT")
print("=" * 65)

print("Model:", model_name)

print("Total Images:", total_images)

print("Correct Predictions:", correct_predictions)

print("Incorrect Predictions:", incorrect_predictions)

print("Accuracy:", accuracy, "%")

print("Error Percentage:", error_percentage, "%")

print("Performance:", performance)

print("Updated Learning Rate:", learning_rate)

print("Updated Training Epochs:", training_epochs)

print("Excellent Model:", excellent_model)

print("Acceptable Model:", acceptable_model)


# ------------------------------------------------
# SECTION 13: FINAL VALIDATION
# ------------------------------------------------

print("\n" + "=" * 65)
print("                  FINAL VALIDATION")
print("=" * 65)

# Confirm that our prediction counts are consistent.

if calculated_total == total_images:

    print("Prediction Counts: Correct")

else:

    print("Prediction Counts: Incorrect")

# Confirm that the learning rate is positive.

if learning_rate > 0:

    print("Learning Rate: Valid")

else:

    print("Learning Rate: Invalid")

# Confirm that the model has a performance category.

if performance is not None:

    print("Performance Evaluation: Completed")

else:

    print("Performance Evaluation: Missing")


# ------------------------------------------------
# SECTION 14: COMPLETION MESSAGE
# ------------------------------------------------

print("\n" + "=" * 65)

print("DAY 005 CHALLENGE COMPLETED SUCCESSFULLY!")

print("Python Operators Applied to an AI Project.")

print("=" * 65)


# ================================================================
# END OF DAY 005 CHALLENGE
# ================================================================
