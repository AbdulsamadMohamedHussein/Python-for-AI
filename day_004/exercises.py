
# ==================================================
# EXERCISE 1: STRING TO INTEGER
# ==================================================

# The student's age is stored as text.
student_age = "23"

# Check the original data type.
print("Original Age:", student_age)
print("Original Type:", type(student_age))

# Convert the string into an integer.
age_integer = int(student_age)

# Calculate the age after five years.
future_age = age_integer + 5

# Display the converted information.
print("\nConverted Age:", age_integer)
print("Converted Type:", type(age_integer))

print("Age After Five Years:", future_age)


# ==================================================
# EXERCISE 2: STRING TO FLOAT
# ==================================================

# Model accuracy values are stored as strings.
old_accuracy = "85.5"
new_accuracy = "94.8"

# Convert both strings into floating-point numbers.
old_accuracy_float = float(old_accuracy)
new_accuracy_float = float(new_accuracy)

# Calculate the improvement in accuracy.
improvement = new_accuracy_float - old_accuracy_float

print("Old Accuracy:", old_accuracy_float)
print("New Accuracy:", new_accuracy_float)

print("Accuracy Improvement:", improvement)

# Display the data types.
print("Old Accuracy Type:", type(old_accuracy_float))
print("New Accuracy Type:", type(new_accuracy_float))


# ==================================================
# EXERCISE 3: INTEGER AND FLOAT CONVERSION
# ==================================================

# Original integer value.
mathematics_marks = 85

# Original floating-point value.
model_score = 96.75

# Convert integer into float.
mathematics_float = float(mathematics_marks)

# Convert float into integer.
model_score_integer = int(model_score)

print("Original Mathematics Marks:", mathematics_marks)
print("Converted Mathematics Marks:", mathematics_float)

print("\nOriginal Model Score:", model_score)
print("Converted Model Score:", model_score_integer)

print("\nData Types:")

print(type(mathematics_float))
print(type(model_score_integer))


# ==================================================
# EXERCISE 4: USER INPUT CONVERSION
# ==================================================

# Ask the user to enter their personal information.
student_name = input("Enter your name: ")

# IMPORTANT:
# input() always returns a string.
# Therefore, we use int() to convert the age.
student_age = int(input("Enter your age: "))

# Convert examination marks into a float.
student_marks = float(input("Enter your marks: "))

# Calculate improved marks.
improved_marks = student_marks + 5.0

# Display the student's information.
print("\n========== STUDENT REPORT ==========")

print("Student Name:", student_name)
print("Student Age:", student_age)
print("Original Marks:", student_marks)
print("Improved Marks:", improved_marks)

print("\n========== DATA TYPES ==========")

print("Name Type:", type(student_name))
print("Age Type:", type(student_age))
print("Marks Type:", type(student_marks))


# ==================================================
# EXERCISE 5: BOOLEAN CONVERSION
# ==================================================

# Original information.
registration_status = 1
fees_paid = 0

# Convert numerical values into Boolean values.
is_registered = bool(registration_status)
has_paid_fees = bool(fees_paid)

# Both conditions must be True.
exam_eligibility = is_registered and has_paid_fees

print("Registration Status:", is_registered)
print("Fees Paid:", has_paid_fees)

print("Eligible for Examination:", exam_eligibility)

print("Eligibility Data Type:", type(exam_eligibility))


# ==================================================
# EXERCISE 6: COLLECTION CONVERSION
# ==================================================

# Original list containing duplicate marks.
student_marks = [85, 90, 95, 85, 90, 100]

print("Original List:", student_marks)

# Convert the list into a tuple.
marks_tuple = tuple(student_marks)

# Convert the list into a set.
marks_set = set(student_marks)

# Convert the set back into a list.
unique_marks_list = list(marks_set)

print("\nConverted Tuple:", marks_tuple)

print("Converted Set:", marks_set)

print("Unique Marks List:", unique_marks_list)

# Compare the number of elements.
print("\nOriginal Elements:", len(student_marks))
print("Unique Elements:", len(marks_set))


# ==================================================
# EXERCISE 7: LIST TO DICTIONARY
# ==================================================

# Each pair contains a key and its corresponding value.
student_data = [
    ("name", "Abdulsamad"),
    ("age", 23),
    ("country", "Kenya"),
    ("course", "Artificial Intelligence"),
    ("marks", 95.5)
]

print("Original Student Data:")
print(student_data)

# Convert the list of pairs into a dictionary.
student_dictionary = dict(student_data)

print("\nConverted Dictionary:")
print(student_dictionary)

# Access individual dictionary values.
print("\nStudent Name:", student_dictionary["name"])
print("Student Age:", student_dictionary["age"])
print("Student Country:", student_dictionary["country"])
print("Student Marks:", student_dictionary["marks"])

# Check the resulting data type.
print("\nDictionary Type:", type(student_dictionary))


# ==================================================
# EXERCISE 8: ERROR HANDLING
# ==================================================

# Ask the user to enter their examination marks.
user_marks = input("Enter your examination marks: ")

# Attempt to convert the entered text into a float.
try:

    marks = float(user_marks)

    print("Your Marks:", marks)

    # Check whether the marks are within a valid range.
    if 0 <= marks <= 100:

        print("Valid examination marks.")

    else:

        print("Marks must be between 0 and 100.")

# This block runs if conversion fails.
except ValueError:

    print("ERROR: Please enter a valid numerical value.")

print("Program execution completed.")


# ==================================================
# EXERCISE 9: AI DATASET PREPROCESSING
# ==================================================

# Imagine these records were imported from a CSV file.
# Notice that the numerical information is stored as strings.

student_ages = ["20", "22", "23", "25", "21"]

student_marks = ["85.5", "90.0", "95.5", "80.0", "88.5"]

print("Original Ages:", student_ages)
print("Original Marks:", student_marks)

# Convert every age into an integer.
# The list comprehension processes each element.

ages_converted = [int(age) for age in student_ages]

# Convert every examination mark into a float.

marks_converted = [float(mark) for mark in student_marks]

print("\nConverted Ages:", ages_converted)
print("Converted Marks:", marks_converted)

# Calculate the total marks.
total_marks = sum(marks_converted)

# Calculate the average marks.
average_marks = total_marks / len(marks_converted)

# Calculate the average age.
average_age = sum(ages_converted) / len(ages_converted)

print("\n========== DATASET ANALYSIS ==========")

print("Total Students:", len(ages_converted))

print("Total Marks:", total_marks)

print("Average Marks:", average_marks)

print("Average Age:", average_age)

print("\n========== DATA TYPES ==========")

print("Age Type:", type(ages_converted[0]))

print("Marks Type:", type(marks_converted[0]))


# ==================================================
# EXERCISE 10: IMAGE PIXEL NORMALIZATION
# ==================================================

# Original image pixel values.
# In a standard 8-bit image, each channel has values
# ranging from 0 to 255.

pixel_values = [0, 128, 255]

print("Original Pixel Values:", pixel_values)

# Step 1:
# Convert each integer pixel value into a float.

pixel_values_float = [
    float(pixel) for pixel in pixel_values
]

print("\nFloat Pixel Values:", pixel_values_float)

# Step 2:
# Normalize the pixel values.
#
# Divide every pixel by 255.
#
# This transforms the original range of 0-255
# into a numerical range of 0-1.

normalized_pixels = [
    pixel / 255.0 for pixel in pixel_values_float
]

print("\nNormalized Pixel Values:", normalized_pixels)

# Step 3:
# Display the original and normalized values together.

print("\n========== IMAGE NORMALIZATION REPORT ==========")

for original, normalized in zip(
    pixel_values,
    normalized_pixels
):

    print(
        "Original Pixel:", original,
        "| Normalized Pixel:", round(normalized, 4)
    )

# Step 4:
# Display the data types.

print("\nOriginal Data Type:", type(pixel_values[0]))

print("Normalized Data Type:", type(normalized_pixels[0]))
