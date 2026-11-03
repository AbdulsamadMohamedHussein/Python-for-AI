
# ================================================================
# DAY 005 - PYTHON OPERATORS
# BACHELOR'S IN ARTIFICIAL INTELLIGENCE
# 90-DAY PYTHON PROGRAMMING JOURNEY
#
# Topic: Understanding Python Operators
# ================================================================


# ---------------------------------------------------------------
# SECTION 1: INTRODUCTION TO OPERATORS
# ---------------------------------------------------------------

print("=" * 65)
print("              DAY 005: PYTHON OPERATORS")
print("=" * 65)

# An operator performs an operation on values.
# The values involved in the operation are called operands.

number_1 = 20
number_2 = 10

result = number_1 + number_2

print("\nFirst Number:", number_1)
print("Second Number:", number_2)
print("Addition Result:", result)


# ---------------------------------------------------------------
# SECTION 2: ARITHMETIC OPERATORS
# ---------------------------------------------------------------

print("\n" + "=" * 65)
print("                 ARITHMETIC OPERATORS")
print("=" * 65)

a = 20
b = 6

# Addition
addition = a + b

# Subtraction
subtraction = a - b

# Multiplication
multiplication = a * b

# Division
division = a / b

# Floor division
floor_division = a // b

# Modulus: returns the remainder
modulus = a % b

# Exponentiation
exponentiation = a ** 2

print("Addition:", addition)
print("Subtraction:", subtraction)
print("Multiplication:", multiplication)
print("Division:", division)
print("Floor Division:", floor_division)
print("Modulus:", modulus)
print("Exponentiation:", exponentiation)


# ---------------------------------------------------------------
# SECTION 3: ASSIGNMENT OPERATORS
# ---------------------------------------------------------------

print("\n" + "=" * 65)
print("                 ASSIGNMENT OPERATORS")
print("=" * 65)

# The equal sign assigns an initial value.

score = 100

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

# Floor division assignment.

score //= 3

print("After //= 3:", score)

# Modulus assignment.

score %= 5

print("After %= 5:", score)

# Exponentiation assignment.

score **= 2

print("After **= 2:", score)


# ---------------------------------------------------------------
# SECTION 4: COMPARISON OPERATORS
# ---------------------------------------------------------------

print("\n" + "=" * 65)
print("                 COMPARISON OPERATORS")
print("=" * 65)

student_marks = 85

# Comparison operators return True or False.

print("Marks Equal to 85:", student_marks == 85)

print("Marks Not Equal to 85:", student_marks != 85)

print("Marks Greater Than 50:", student_marks > 50)

print("Marks Less Than 50:", student_marks < 50)

print("Marks Greater or Equal to 85:", student_marks >= 85)

print("Marks Less or Equal to 100:", student_marks <= 100)


# ---------------------------------------------------------------
# SECTION 5: LOGICAL OPERATORS
# ---------------------------------------------------------------

print("\n" + "=" * 65)
print("                  LOGICAL OPERATORS")
print("=" * 65)

age = 23

marks = 85

# AND: both conditions must be True.

eligible = age >= 18 and marks >= 50

print("Eligible:", eligible)

# OR: at least one condition must be True.

qualified = marks >= 90 or age >= 18

print("Qualified:", qualified)

# NOT: reverses a Boolean value.

is_registered = True

print("Not Registered:", not is_registered)


# ---------------------------------------------------------------
# SECTION 6: BITWISE OPERATORS
# ---------------------------------------------------------------

print("\n" + "=" * 65)
print("                  BITWISE OPERATORS")
print("=" * 65)

x = 5

y = 3

# Binary representation of 5 is 0101.
# Binary representation of 3 is 0011.

print("Bitwise AND:", x & y)

print("Bitwise OR:", x | y)

print("Bitwise XOR:", x ^ y)

print("Bitwise NOT:", ~x)

print("Left Shift:", x << 1)

print("Right Shift:", x >> 1)


# ---------------------------------------------------------------
# SECTION 7: MEMBERSHIP OPERATORS
# ---------------------------------------------------------------

print("\n" + "=" * 65)
print("                 MEMBERSHIP OPERATORS")
print("=" * 65)

ai_topics = [
    "Python",
    "Machine Learning",
    "Deep Learning",
    "Computer Vision"
]

# Check whether a topic exists in the list.

print("Python Exists:", "Python" in ai_topics)

print("Robotics Exists:", "Robotics" in ai_topics)

print("Robotics Does Not Exist:", "Robotics" not in ai_topics)


# ---------------------------------------------------------------
# SECTION 8: IDENTITY OPERATORS
# ---------------------------------------------------------------

print("\n" + "=" * 65)
print("                  IDENTITY OPERATORS")
print("=" * 65)

list_1 = [10, 20, 30]

# Both variables reference the same object.

list_2 = list_1

# This is a separate list containing equal values.

list_3 = [10, 20, 30]

print("list_1 is list_2:", list_1 is list_2)

print("list_1 is list_3:", list_1 is list_3)

print("list_1 == list_3:", list_1 == list_3)


# ---------------------------------------------------------------
# SECTION 9: OPERATOR PRECEDENCE
# ---------------------------------------------------------------

print("\n" + "=" * 65)
print("                 OPERATOR PRECEDENCE")
print("=" * 65)

# Multiplication happens before addition.

result_1 = 10 + 5 * 2

print("Without Parentheses:", result_1)

# Parentheses change the order of calculations.

result_2 = (10 + 5) * 2

print("With Parentheses:", result_2)

# Exponentiation is performed before multiplication.

result_3 = 2 + 3 ** 2 * 2

print("Complex Expression:", result_3)


# ---------------------------------------------------------------
# SECTION 10: AI APPLICATION - MODEL ACCURACY
# ---------------------------------------------------------------

print("\n" + "=" * 65)
print("                AI MODEL ACCURACY")
print("=" * 65)

correct_predictions = 950

total_predictions = 1000

# Accuracy is calculated by dividing correct predictions
# by total predictions and multiplying by 100.

accuracy = (
    correct_predictions / total_predictions
) * 100

print("Correct Predictions:", correct_predictions)

print("Total Predictions:", total_predictions)

print("Model Accuracy:", accuracy, "%")


# ---------------------------------------------------------------
# SECTION 11: AI APPLICATION - PREDICTION ERROR
# ---------------------------------------------------------------

print("\n" + "=" * 65)
print("                AI PREDICTION ERROR")
print("=" * 65)

actual_value = 100

predicted_value = 92

# Calculate the difference between actual and predicted values.

prediction_error = actual_value - predicted_value

# Absolute error removes the negative sign if present.

absolute_error = abs(prediction_error)

print("Actual Value:", actual_value)

print("Predicted Value:", predicted_value)

print("Prediction Error:", prediction_error)

print("Absolute Error:", absolute_error)


# ---------------------------------------------------------------
# SECTION 12: AI APPLICATION - LEARNING RATE
# ---------------------------------------------------------------

print("\n" + "=" * 65)
print("                AI LEARNING RATE")
print("=" * 65)

learning_rate = 0.01

print("Original Learning Rate:", learning_rate)

# Reduce the learning rate by 10 percent.
# Multiplying by 0.9 retains 90 percent of the old value.

learning_rate *= 0.9

print("Updated Learning Rate:", learning_rate)


# ---------------------------------------------------------------
# SECTION 13: AI APPLICATION - PERFORMANCE CHECK
# ---------------------------------------------------------------

print("\n" + "=" * 65)
print("                AI PERFORMANCE CHECK")
print("=" * 65)

model_accuracy = 95.5

# Use a comparison operator to check model performance.

if model_accuracy >= 90:

    print("Excellent Model Performance")

elif model_accuracy >= 75:

    print("Good Model Performance")

else:

    print("Model Needs Improvement")


# ---------------------------------------------------------------
# SECTION 14: FINAL REPORT
# ---------------------------------------------------------------

print("\n" + "=" * 65)
print("                  DAY 005 FINAL REPORT")
print("=" * 65)

print("Topic: Python Operators")

print("Arithmetic Operators: Completed")

print("Assignment Operators: Completed")

print("Comparison Operators: Completed")

print("Logical Operators: Completed")

print("Bitwise Operators: Completed")

print("Membership Operators: Completed")

print("Identity Operators: Completed")

print("Operator Precedence: Completed")

print("AI Mathematical Applications: Completed")

print("\nDAY 005 LESSON CODE EXECUTED SUCCESSFULLY!")

print("=" * 65)

# ================================================================
# END OF DAY 005 - PYTHON OPERATORS
# ================================================================
