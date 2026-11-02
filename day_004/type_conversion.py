
# ============================================================
# DAY 004: TYPE CONVERSION IN PYTHON
# Bachelor's in Artificial Intelligence
# Python for AI - 90 Days Learning Journey
# ============================================================

# Today's learning objectives:
# 1. Understand what type conversion means.
# 2. Understand implicit type conversion.
# 3. Understand explicit type conversion.
# 4. Convert between different Python data types.
# 5. Understand common conversion errors.
# 6. Understand how type conversion is used in AI.


# ------------------------------------------------------------
# SECTION 1: INTRODUCTION TO TYPE CONVERSION
# ------------------------------------------------------------

print("=" * 65)
print("              DAY 004: TYPE CONVERSION")
print("=" * 65)

# Type conversion means changing a value from one data type
# into another data type.

# Example:
# The value "100" is a string because it is inside quotation marks.

number_as_string = "100"

# We use int() to convert the string into an integer.

number_as_integer = int(number_as_string)

print("\nOriginal Value:", number_as_string)
print("Original Type:", type(number_as_string))

print("\nConverted Value:", number_as_integer)
print("Converted Type:", type(number_as_integer))


# ------------------------------------------------------------
# SECTION 2: IMPLICIT TYPE CONVERSION
# ------------------------------------------------------------

# Implicit conversion happens automatically.
# Python changes a value's numerical type when needed
# to perform an operation safely.

# Here, we have an integer and a float.

integer_number = 20
float_number = 5.5

# Python automatically converts the integer into a float
# before performing the addition.

result = integer_number + float_number

print("\n" + "=" * 65)
print("              IMPLICIT TYPE CONVERSION")
print("=" * 65)

print("Integer Number:", integer_number)
print("Float Number:", float_number)

print("Addition Result:", result)
print("Result Type:", type(result))

# Expected result:
# 25.5
# <class 'float'>


# Another example of implicit conversion.

number_a = 10
number_b = 2.0

result_b = number_a * number_b

print("\nMultiplication Result:", result_b)
print("Multiplication Type:", type(result_b))


# ------------------------------------------------------------
# SECTION 3: EXPLICIT TYPE CONVERSION
# ------------------------------------------------------------

# Explicit conversion means that WE manually tell Python
# which data type we want.

# Python provides built-in functions such as:
#
# int()    - Converts suitable values into integers.
# float()  - Converts suitable values into floats.
# str()    - Converts values into strings.
# bool()   - Converts values into Boolean values.
# list()   - Converts an iterable into a list.
# tuple()  - Converts an iterable into a tuple.
# set()    - Converts an iterable into a set.
# dict()   - Creates a dictionary from suitable key-value pairs.


# ------------------------------------------------------------
# SECTION 4: CONVERTING STRING INTO INTEGER
# ------------------------------------------------------------

# A number written inside quotation marks is a string.
# We cannot directly perform ordinary numerical addition
# between a string and an integer.

student_age = "23"

# Convert the string into an integer.

converted_age = int(student_age)

print("\n" + "=" * 65)
print("              STRING TO INTEGER")
print("=" * 65)

print("Original Age:", student_age)
print("Original Type:", type(student_age))

print("Converted Age:", converted_age)
print("Converted Type:", type(converted_age))

# Now we can perform mathematical operations.

next_year_age = converted_age + 1

print("Age Next Year:", next_year_age)


# ------------------------------------------------------------
# SECTION 5: CONVERTING STRING INTO FLOAT
# ------------------------------------------------------------

# Sometimes numerical information contains decimal values.
# For example, a user's height or a machine learning accuracy.

height_as_string = "1.75"
accuracy_as_string = "96.5"

# Convert these strings into floating-point numbers.

height = float(height_as_string)
accuracy = float(accuracy_as_string)

print("\n" + "=" * 65)
print("              STRING TO FLOAT")
print("=" * 65)

print("Height:", height)
print("Height Type:", type(height))

print("Accuracy:", accuracy)
print("Accuracy Type:", type(accuracy))

# We can now perform mathematical calculations.

improved_accuracy = accuracy + 1.5

print("Improved Accuracy:", improved_accuracy)


# ------------------------------------------------------------
# SECTION 6: CONVERTING INTEGER INTO FLOAT
# ------------------------------------------------------------

# int() stores whole numbers.
# float() stores decimal numbers.

student_marks = 85

# Convert the integer into a float.

marks_as_float = float(student_marks)

print("\n" + "=" * 65)
print("              INTEGER TO FLOAT")
print("=" * 65)

print("Original Marks:", student_marks)
print("Original Type:", type(student_marks))

print("Converted Marks:", marks_as_float)
print("Converted Type:", type(marks_as_float))


# ------------------------------------------------------------
# SECTION 7: CONVERTING FLOAT INTO INTEGER
# ------------------------------------------------------------

# float() can be converted into an integer using int().
#
# IMPORTANT:
# int() removes the decimal part.
# It does NOT round the number to the nearest integer.

decimal_number = 95.85

whole_number = int(decimal_number)

print("\n" + "=" * 65)
print("              FLOAT TO INTEGER")
print("=" * 65)

print("Original Number:", decimal_number)
print("Converted Number:", whole_number)

# Example:
# int(95.85) produces 95.
# It does not produce 96.

print("Original Type:", type(decimal_number))
print("Converted Type:", type(whole_number))


# ------------------------------------------------------------
# SECTION 8: CONVERTING NUMBERS INTO STRINGS
# ------------------------------------------------------------

# str() converts suitable Python values into text.
#
# This is useful when we want to combine numerical values
# with other text in a message.

student_name = "Abdulsamad"
student_age = 23

# Convert the integer age into a string.

age_as_string = str(student_age)

# Now both values are strings and can be concatenated.

student_information = (
    "My name is " + student_name
    + " and I am " + age_as_string + " years old."
)

print("\n" + "=" * 65)
print("              NUMBER TO STRING")
print("=" * 65)

print(student_information)

print("Original Age Type:", type(student_age))
print("Converted Age Type:", type(age_as_string))


# ------------------------------------------------------------
# SECTION 9: CONVERTING VALUES INTO BOOLEAN
# ------------------------------------------------------------

# bool() converts values into True or False.
#
# Important:
# Python considers certain values as False:
#
# 0
# 0.0
# ""
# []
# ()
# {}
# set()
# None
#
# Most other values are considered True.

print("\n" + "=" * 65)
print("              BOOLEAN TYPE CONVERSION")
print("=" * 65)

print("Boolean of 1:", bool(1))
print("Boolean of 0:", bool(0))

print("Boolean of 100:", bool(100))
print("Boolean of -5:", bool(-5))

print("Boolean of 0.0:", bool(0.0))
print("Boolean of 3.5:", bool(3.5))

print("Boolean of Empty String:", bool(""))
print("Boolean of Python:", bool("Python"))

print("Boolean of Empty List:", bool([]))
print("Boolean of Nonempty List:", bool([1, 2, 3]))

print("Boolean of None:", bool(None))


# ------------------------------------------------------------
# SECTION 10: CONVERTING LIST INTO TUPLE
# ------------------------------------------------------------

# A list is mutable, meaning we can change its elements.
# A tuple is immutable, meaning its elements cannot be reassigned.
#
# tuple() converts an iterable into a tuple.

programming_languages = ["Python", "Java", "C++"]

languages_tuple = tuple(programming_languages)

print("\n" + "=" * 65)
print("              LIST TO TUPLE")
print("=" * 65)

print("Original List:", programming_languages)
print("Converted Tuple:", languages_tuple)

print("Original Type:", type(programming_languages))
print("Converted Type:", type(languages_tuple))


# ------------------------------------------------------------
# SECTION 11: CONVERTING TUPLE INTO LIST
# ------------------------------------------------------------

# list() converts an iterable into a list.
#
# This is useful when we need to modify information
# that is currently stored in a tuple.

fixed_courses = ("Python", "Machine Learning", "Deep Learning")

courses_list = list(fixed_courses)

print("\n" + "=" * 65)
print("              TUPLE TO LIST")
print("=" * 65)

print("Original Tuple:", fixed_courses)
print("Converted List:", courses_list)

# We can now modify the list.

courses_list.append("Computer Vision")

print("Updated Courses:", courses_list)


# ------------------------------------------------------------
# SECTION 12: CONVERTING LIST INTO SET
# ------------------------------------------------------------

# set() converts an iterable into a set.
#
# A set automatically removes duplicate elements.
# Sets do not guarantee a fixed display order.

student_marks_list = [85, 90, 95, 85, 90, 100]

unique_marks = set(student_marks_list)

print("\n" + "=" * 65)
print("              LIST TO SET")
print("=" * 65)

print("Original List:", student_marks_list)
print("Converted Set:", unique_marks)

print("Original Length:", len(student_marks_list))
print("Unique Elements:", len(unique_marks))


# ------------------------------------------------------------
# SECTION 13: CONVERTING SET INTO LIST
# ------------------------------------------------------------

# list() can also convert a set into a list.
# The resulting order is not guaranteed to match the original.

unique_student_ids = {101, 102, 103, 104}

student_ids_list = list(unique_student_ids)

print("\n" + "=" * 65)
print("              SET TO LIST")
print("=" * 65)

print("Original Set:", unique_student_ids)
print("Converted List:", student_ids_list)

print("Converted Type:", type(student_ids_list))


# ------------------------------------------------------------
# SECTION 14: CONVERTING TUPLE INTO SET
# ------------------------------------------------------------

# set() can convert a tuple into a set.
# Duplicate values are removed.

numbers_tuple = (10, 20, 30, 20, 10, 40)

numbers_set = set(numbers_tuple)

print("\n" + "=" * 65)
print("              TUPLE TO SET")
print("=" * 65)

print("Original Tuple:", numbers_tuple)
print("Converted Set:", numbers_set)


# ------------------------------------------------------------
# SECTION 15: CONVERTING LIST OF PAIRS INTO DICTIONARY
# ------------------------------------------------------------

# dict() can create a dictionary from an iterable
# containing two-element key-value pairs.

student_data = [
    ("name", "Abdulsamad"),
    ("age", 23),
    ("country", "Kenya"),
    ("course", "Artificial Intelligence")
]

student_dictionary = dict(student_data)

print("\n" + "=" * 65)
print("              LIST TO DICTIONARY")
print("=" * 65)

print("Original Data:", student_data)
print("Converted Dictionary:", student_dictionary)

print("Student Name:", student_dictionary["name"])
print("Student Age:", student_dictionary["age"])


# ------------------------------------------------------------
# SECTION 16: CONVERTING DATA USING INPUT()
# ------------------------------------------------------------

# input() always returns the user's input as a string.
#
# Even if the user enters 25, Python initially stores it as "25".
#
# Therefore, we must convert the value when we want to
# perform mathematical operations.

print("\n" + "=" * 65)
print("              USER INPUT CONVERSION")
print("=" * 65)

# The int() function converts the entered text into an integer.

user_age = int(input("Enter your age: "))

# The float() function converts the entered text into a float.

user_height = float(input("Enter your height in metres: "))

print("\nYour Information:")

print("Age:", user_age)
print("Age Type:", type(user_age))

print("Height:", user_height)
print("Height Type:", type(user_height))

# Now Python can calculate with these values.

age_after_one_year = user_age + 1

print("Your Age Next Year:", age_after_one_year)


# ------------------------------------------------------------
# SECTION 17: CONVERSION ERRORS
# ------------------------------------------------------------

# Not every string can be converted into an integer.
#
# For example:
# int("Hello") is invalid.
#
# Python raises a ValueError because "Hello" is not
# a valid integer representation.

print("\n" + "=" * 65)
print("              UNDERSTANDING CONVERSION ERRORS")
print("=" * 65)

invalid_number = "Hello"

print("Invalid Number:", invalid_number)

# We use try and except to handle a possible conversion error.
# This prevents the program from stopping unexpectedly.

try:

    converted_number = int(invalid_number)

    print("Converted Number:", converted_number)

except ValueError:

    print("ERROR: This text cannot be converted into an integer.")

# The program continues after handling the error.


# ------------------------------------------------------------
# SECTION 18: SAFE NUMERICAL CONVERSION
# ------------------------------------------------------------

# Here we demonstrate a valid conversion.
# We use a numeric string containing decimal values.

user_score = "95.5"

try:

    converted_score = float(user_score)

    print("\nOriginal Score:", user_score)
    print("Converted Score:", converted_score)
    print("Converted Type:", type(converted_score))

except ValueError:

    print("Invalid score. Please enter a valid number.")


# ------------------------------------------------------------
# SECTION 19: TYPE CONVERSION IN AI
# ------------------------------------------------------------

# AI applications process numerical information.
# Sometimes data collected from users or files is stored as text.
#
# We must convert suitable values into numerical types
# before performing mathematical operations.

print("\n" + "=" * 65)
print("              TYPE CONVERSION IN AI")
print("=" * 65)

# Imagine we receive model information from a dataset.

model_accuracy = "96.5"
learning_rate = "0.001"
number_of_epochs = "50"

# Convert the numerical strings into suitable numerical types.

accuracy_value = float(model_accuracy)
learning_rate_value = float(learning_rate)
epochs_value = int(number_of_epochs)

print("Model Accuracy:", accuracy_value)
print("Learning Rate:", learning_rate_value)
print("Number of Epochs:", epochs_value)

print("\nChecking Data Types:")

print(type(accuracy_value))
print(type(learning_rate_value))
print(type(epochs_value))

# We can now perform numerical calculations.

improved_accuracy = accuracy_value + 1.0

print("\nImproved Accuracy:", improved_accuracy)


# ------------------------------------------------------------
# SECTION 20: IMAGE DATA CONVERSION EXAMPLE
# ------------------------------------------------------------

# In computer vision, image pixel values are often represented
# as integers between 0 and 255.
#
# Here we demonstrate converting pixel values into floats.
#
# This is a simplified numerical example, not actual image processing.

pixel_values = [0, 128, 255]

# Convert every pixel value into a float.

pixel_values_float = [float(pixel) for pixel in pixel_values]

print("\n" + "=" * 65)
print("              IMAGE PIXEL CONVERSION")
print("=" * 65)

print("Original Pixel Values:", pixel_values)
print("Converted Pixel Values:", pixel_values_float)

print("Original Type:", type(pixel_values[0]))
print("Converted Type:", type(pixel_values_float[0]))


# ------------------------------------------------------------
# SECTION 21: CONVERTING PIXEL VALUES INTO A 0-1 RANGE
# ------------------------------------------------------------

# Image pixels are commonly represented using values from 0 to 255.
#
# Dividing by 255 converts them into a range from 0 to 1.
#
# This is a common preprocessing technique in computer vision.

normalized_pixels = [pixel / 255 for pixel in pixel_values]

print("\nOriginal Pixels:", pixel_values)
print("Normalized Pixels:", normalized_pixels)

# Example:
# 0   / 255 = 0.0
# 128 / 255 = approximately 0.502
# 255 / 255 = 1.0


# ------------------------------------------------------------
# SECTION 22: FINAL SUMMARY
# ------------------------------------------------------------

print("\n" + "=" * 65)
print("              DAY 004 LEARNING SUMMARY")
print("=" * 65)

print("1. Learned implicit type conversion.")
print("2. Learned explicit type conversion.")
print("3. Converted strings into integers.")
print("4. Converted strings into floats.")
print("5. Converted integers into floats.")
print("6. Converted floats into integers.")
print("7. Converted numbers into strings.")
print("8. Converted values into Boolean types.")
print("9. Converted lists, tuples and sets.")
print("10. Created dictionaries using dict().")
print("11. Learned input conversion.")
print("12. Understood conversion errors.")
print("13. Explored type conversion in AI.")
print("14. Learned basic image pixel normalization.")

print("\n" + "=" * 65)
print("             DAY 004 MAIN LESSON COMPLETED")
print("=" * 65)

# ============================================================
# END OF DAY 004: TYPE CONVERSION IN PYTHON
# ============================================================
