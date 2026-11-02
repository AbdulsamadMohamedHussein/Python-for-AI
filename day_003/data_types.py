
# ============================================================
# DAY 003 - PYTHON DATA TYPES
# BACHELOR'S IN ARTIFICIAL INTELLIGENCE
# ============================================================

# ------------------------------------------------------------
# SECTION 1: INTRODUCTION TO DATA TYPES
# ------------------------------------------------------------

print("=" * 60)
print("             DAY 003 - PYTHON DATA TYPES")
print("=" * 60)

# A data type tells Python what kind of value is stored.


# ------------------------------------------------------------
# SECTION 2: INTEGER (int)
# ------------------------------------------------------------

# Integer means a whole number without a decimal point.

student_age = 23
mathematics_marks = 85
number_of_students = 120
negative_number = -15
zero_value = 0

print("\n========== INTEGER DATA TYPE ==========")

print("Student Age:", student_age)
print("Mathematics Marks:", mathematics_marks)
print("Number of Students:", number_of_students)
print("Negative Number:", negative_number)
print("Zero Value:", zero_value)

print("Age Data Type:", type(student_age))
print("Marks Data Type:", type(mathematics_marks))


# ------------------------------------------------------------
# SECTION 3: FLOAT (float)
# ------------------------------------------------------------

# Float represents a number containing a decimal point.

student_height = 1.75
learning_rate = 0.001
model_accuracy = 96.5
temperature = 36.8

print("\n========== FLOAT DATA TYPE ==========")

print("Student Height:", student_height)
print("Learning Rate:", learning_rate)
print("Model Accuracy:", model_accuracy)
print("Temperature:", temperature)

print("Height Data Type:", type(student_height))
print("Learning Rate Data Type:", type(learning_rate))


# ------------------------------------------------------------
# SECTION 4: STRING (str)
# ------------------------------------------------------------

# String represents text.
# Strings can be written using single or double quotes.

student_name = "Abdulsamad Mohamed"
country = 'Kenya'
university = "Guilin University of Electronics Technology"
course = "Artificial Intelligence"

print("\n========== STRING DATA TYPE ==========")

print("Student Name:", student_name)
print("Country:", country)
print("University:", university)
print("Course:", course)

print("Name Data Type:", type(student_name))
print("Country Data Type:", type(country))


# ------------------------------------------------------------
# SECTION 5: BOOLEAN (bool)
# ------------------------------------------------------------

# Boolean represents only two logical values:
# True or False.

is_student = True
has_completed_python = False
is_model_trained = True
has_errors = False

print("\n========== BOOLEAN DATA TYPE ==========")

print("Is Student:", is_student)
print("Completed Python:", has_completed_python)
print("Model Trained:", is_model_trained)
print("Has Errors:", has_errors)

print("Student Data Type:", type(is_student))
print("Model Data Type:", type(is_model_trained))


# ------------------------------------------------------------
# SECTION 6: NONE TYPE (NoneType)
# ------------------------------------------------------------

# None represents the absence of a value.
# It is not the same as zero or an empty string.

student_middle_name = None
model_result = None

print("\n========== NONE DATA TYPE ==========")

print("Middle Name:", student_middle_name)
print("Model Result:", model_result)

print("Middle Name Type:", type(student_middle_name))
print("Model Result Type:", type(model_result))


# ------------------------------------------------------------
# SECTION 7: COMPLEX NUMBERS
# ------------------------------------------------------------

# Complex numbers contain real and imaginary parts.
# Python uses j for the imaginary component.

complex_number = 3 + 4j
another_complex = 5 + 2j

print("\n========== COMPLEX DATA TYPE ==========")

print("First Complex Number:", complex_number)
print("Second Complex Number:", another_complex)

print("Complex Number Type:", type(complex_number))
print("Real Part:", complex_number.real)
print("Imaginary Part:", complex_number.imag)


# ------------------------------------------------------------
# SECTION 8: LIST (list)
# ------------------------------------------------------------

# A list stores multiple values in one variable.
# Lists are ordered and mutable.
# Mutable means their contents can be changed.

student_marks = [85, 90, 95, 88, 92]

programming_languages = [
    "Python",
    "Java",
    "C++",
    "JavaScript"
]

print("\n========== LIST DATA TYPE ==========")

print("Student Marks:", student_marks)
print("Programming Languages:", programming_languages)

print("First Mark:", student_marks[0])
print("Second Language:", programming_languages[1])

# Changing a list element
student_marks[0] = 99

print("Updated Student Marks:", student_marks)

print("List Data Type:", type(student_marks))


# ------------------------------------------------------------
# SECTION 9: TUPLE (tuple)
# ------------------------------------------------------------

# A tuple stores multiple values.
# Tuples are ordered but immutable.
# Immutable means their contents cannot be changed.

student_coordinates = (10, 20)
rgb_color = (255, 100, 50)

print("\n========== TUPLE DATA TYPE ==========")

print("Student Coordinates:", student_coordinates)
print("RGB Color:", rgb_color)

print("First Coordinate:", student_coordinates[0])
print("Second Coordinate:", student_coordinates[1])

print("Tuple Data Type:", type(student_coordinates))


# ------------------------------------------------------------
# SECTION 10: SET (set)
# ------------------------------------------------------------

# A set stores unique values.
# Sets do not guarantee a fixed display order.
# Duplicate values are automatically removed.

student_ids = {101, 102, 103, 104, 101}

programming_topics = {
    "Variables",
    "Loops",
    "Functions",
    "Variables"
}

print("\n========== SET DATA TYPE ==========")

print("Student IDs:", student_ids)
print("Programming Topics:", programming_topics)

print("Set Data Type:", type(student_ids))


# ------------------------------------------------------------
# SECTION 11: DICTIONARY (dict)
# ------------------------------------------------------------

# A dictionary stores information using key-value pairs.
# Each key identifies its corresponding value.

student_information = {
    "name": "Abdulsamad Mohamed",
    "age": 23,
    "country": "Kenya",
    "course": "Artificial Intelligence"
}

ai_model = {
    "model_name": "Image Classifier",
    "learning_rate": 0.001,
    "epochs": 100,
    "accuracy": 96.5
}

print("\n========== DICTIONARY DATA TYPE ==========")

print("Student Information:", student_information)

print("Student Name:", student_information["name"])
print("Student Age:", student_information["age"])

print("AI Model Information:", ai_model)

print("Model Name:", ai_model["model_name"])
print("Model Accuracy:", ai_model["accuracy"])

print("Dictionary Data Type:", type(student_information))


# ------------------------------------------------------------
# SECTION 12: RANGE DATA TYPE
# ------------------------------------------------------------

# Range represents a sequence of integers.
# It is commonly used when working with loops.

numbers = range(1, 6)

print("\n========== RANGE DATA TYPE ==========")

print("Range Object:", numbers)
print("Numbers:", list(numbers))

print("Range Data Type:", type(numbers))


# ------------------------------------------------------------
# SECTION 13: BYTES DATA TYPE
# ------------------------------------------------------------

# Bytes represent a sequence of bytes.
# Bytes are immutable.
# They are useful when working with binary data.

binary_data = b"Python"

print("\n========== BYTES DATA TYPE ==========")

print("Binary Data:", binary_data)
print("Bytes Data Type:", type(binary_data))


# ------------------------------------------------------------
# SECTION 14: CHECKING DATA TYPES USING type()
# ------------------------------------------------------------

# type() tells us the type of an object.

print("\n========== CHECKING DATA TYPES ==========")

print(type(100))
print(type(25.5))
print(type("Artificial Intelligence"))
print(type(True))
print(type(None))
print(type([1, 2, 3]))
print(type((1, 2, 3)))
print(type({1, 2, 3}))
print(type({"name": "Ali"}))


# ------------------------------------------------------------
# SECTION 15: CHECKING TYPES USING isinstance()
# ------------------------------------------------------------

# isinstance() checks whether an object belongs
# to a particular type.
# It returns True or False.

age = 23
name = "Abdulsamad"
accuracy = 95.5

print("\n========== ISINSTANCE FUNCTION ==========")

print(isinstance(age, int))
print(isinstance(name, str))
print(isinstance(accuracy, float))
print(isinstance(age, str))


# ------------------------------------------------------------
# SECTION 16: MUTABLE AND IMMUTABLE DATA TYPES
# ------------------------------------------------------------

# Mutable objects can be changed after creation.
# Immutable objects cannot be changed after creation.

# Example of a mutable object: LIST

marks = [80, 85, 90]

print("\n========== MUTABLE AND IMMUTABLE ==========")

print("Original Marks:", marks)

marks[0] = 100

print("Updated Marks:", marks)

# Example of an immutable object: STRING

language = "Python"

print("Original Language:", language)

language = language + " Programming"

print("Updated Language:", language)

# Note: The original string was not modified.
# A new string object was created and assigned.


# ------------------------------------------------------------
# SECTION 17: MIXED DATA TYPES
# ------------------------------------------------------------

# Python collections can store different data types.

student_record = [
    "Abdulsamad",
    23,
    95.5,
    True
]

print("\n========== MIXED DATA TYPES ==========")

print("Student Record:", student_record)

print("Name:", student_record[0])
print("Age:", student_record[1])
print("Accuracy:", student_record[2])
print("Student Status:", student_record[3])


# ------------------------------------------------------------
# SECTION 18: DATA TYPES IN ARTIFICIAL INTELLIGENCE
# ------------------------------------------------------------

# Different AI tasks require different data types.

image_width = 224
image_height = 224
image_channels = 3

image_label = "Cat"
prediction_confidence = 0.985
is_prediction_correct = True

image_shape = (224, 224, 3)

image_metadata = {
    "label": image_label,
    "confidence": prediction_confidence,
    "correct": is_prediction_correct
}

print("\n========== DATA TYPES IN AI ==========")

print("Image Width:", image_width)
print("Image Height:", image_height)
print("Image Channels:", image_channels)

print("Image Label:", image_label)
print("Prediction Confidence:", prediction_confidence)
print("Prediction Correct:", is_prediction_correct)

print("Image Shape:", image_shape)
print("Image Metadata:", image_metadata)


# ------------------------------------------------------------
# SECTION 19: FINAL DATA TYPE REPORT
# ------------------------------------------------------------

print("\n" + "=" * 60)
print("             FINAL DATA TYPE REPORT")
print("=" * 60)

data_type_examples = [
    100,
    25.5,
    "Python",
    True,
    None,
    3 + 4j,
    [1, 2, 3],
    (1, 2, 3),
    {1, 2, 3},
    {"name": "Ali"},
    range(5),
    b"AI"
]

for item in data_type_examples:
    print(f"Value: {str(item):30} | Type: {type(item).__name__}")

print("=" * 60)
print("          END OF DAY 003 LESSON")
print("=" * 60)

# ============================================================
# END OF DAY 003 - DATA TYPES
# ============================================================
