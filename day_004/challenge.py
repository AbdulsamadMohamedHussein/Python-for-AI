
# ================================================================
# DAY 004 - PYTHON CODING CHALLENGE
# AI DATASET PREPROCESSING AND IMAGE DATA MANAGEMENT SYSTEM
#
# Bachelor's in Artificial Intelligence
# Python for AI - 90 Days Learning Journey
# ================================================================


# ---------------------------------------------------------------
# SECTION 1: PROGRAM INTRODUCTION
# ---------------------------------------------------------------

print("=" * 75)
print("          AI DATASET PREPROCESSING AND MANAGEMENT SYSTEM")
print("=" * 75)

print("\nProject: AI Data Preprocessing")
print("Student: Abdulsamad Mohamed")
print("Learning Day: 004")
print("Main Topic: Python Type Conversion")


# ---------------------------------------------------------------
# SECTION 2: CREATE A RAW DATASET
# ---------------------------------------------------------------

# Imagine that we have received student information from a CSV file.
#
# CSV files often store imported values as text.
# Therefore, numbers such as age and marks may initially
# be represented as strings.
#
# Each dictionary represents one student.
#
# Notice that age and marks are written inside quotation marks.
# This means they are strings, not numerical values.

raw_dataset = [

    {
        "name": "Abdulsamad",
        "age": "23",
        "mathematics": "85.5",
        "physics": "90.0",
        "python": "95.5"
    },

    {
        "name": "John",
        "age": "22",
        "mathematics": "80.0",
        "physics": "85.5",
        "python": "88.0"
    },

    {
        "name": "Mary",
        "age": "21",
        "mathematics": "92.0",
        "physics": "94.5",
        "python": "96.0"
    },

    {
        "name": "David",
        "age": "24",
        "mathematics": "75.0",
        "physics": "80.0",
        "python": "82.5"
    },

    {
        "name": "Sarah",
        "age": "20",
        "mathematics": "88.5",
        "physics": "91.0",
        "python": "93.5"
    }

]


print("\n" + "=" * 75)
print("                    ORIGINAL RAW DATASET")
print("=" * 75)

# Display the original dataset before conversion.

for student in raw_dataset:

    print(student)


# ---------------------------------------------------------------
# SECTION 3: INSPECT ORIGINAL DATA TYPES
# ---------------------------------------------------------------

# Before processing data, we should understand its original types.
#
# We inspect the first student's information.
#
# The name should be a string.
# The age should currently be a string.
# Mathematics marks should also currently be a string.

first_student = raw_dataset[0]

print("\n" + "=" * 75)
print("                    ORIGINAL DATA TYPES")
print("=" * 75)

print("Name Type:", type(first_student["name"]))

print("Age Type:", type(first_student["age"]))

print("Mathematics Type:", type(first_student["mathematics"]))

print("Physics Type:", type(first_student["physics"]))

print("Python Type:", type(first_student["python"]))


# ---------------------------------------------------------------
# SECTION 4: CONVERT RAW DATA INTO NUMERICAL DATA
# ---------------------------------------------------------------

# We create a new empty list.
#
# This list will store the cleaned and converted student records.
#
# We do not modify the original raw_dataset.
# Instead, we create new dictionaries containing converted values.

cleaned_dataset = []

# Process every student individually.

for student in raw_dataset:

    # The student's name is already a string.
    # We do not need to convert it.

    name = student["name"]

    try:

        # Convert age from string into integer.

        age = int(student["age"])

        # Convert examination marks from strings into floats.

        mathematics = float(student["mathematics"])

        physics = float(student["physics"])

        python_marks = float(student["python"])

        # Check that examination marks are within a valid range.
        #
        # The expression below checks all three marks.

        if not all(
            0 <= mark <= 100
            for mark in [mathematics, physics, python_marks]
        ):

            print("Invalid marks detected for:", name)

            continue

        # Check that age is positive.

        if age <= 0:

            print("Invalid age detected for:", name)

            continue

        # Calculate the student's average marks.

        average = (
            mathematics + physics + python_marks
        ) / 3

        # Create a new dictionary with converted numerical values.

        cleaned_student = {

            "name": name,

            "age": age,

            "mathematics": mathematics,

            "physics": physics,

            "python": python_marks,

            "average": average

        }

        # Add the cleaned student record to our new dataset.

        cleaned_dataset.append(cleaned_student)

    except ValueError:

        # If a value cannot be converted into a number,
        # Python raises a ValueError.
        #
        # We handle that error and continue processing
        # the remaining students.

        print("Invalid numerical data for:", name)


# ---------------------------------------------------------------
# SECTION 5: DISPLAY CLEANED DATASET
# ---------------------------------------------------------------

print("\n" + "=" * 75)
print("                    CLEANED DATASET")
print("=" * 75)

# Display each converted student record.

for student in cleaned_dataset:

    print("\nStudent Name:", student["name"])

    print("Age:", student["age"])

    print("Mathematics:", student["mathematics"])

    print("Physics:", student["physics"])

    print("Python:", student["python"])

    print("Average Marks:", round(student["average"], 2))


# ---------------------------------------------------------------
# SECTION 6: VERIFY CONVERTED DATA TYPES
# ---------------------------------------------------------------

# We now check whether the conversion was successful.
#
# Age should now be an integer.
#
# Examination marks and average should now be floats.

print("\n" + "=" * 75)
print("                    CONVERTED DATA TYPES")
print("=" * 75)

if len(cleaned_dataset) > 0:

    student = cleaned_dataset[0]

    print("Name Type:", type(student["name"]))

    print("Age Type:", type(student["age"]))

    print("Mathematics Type:", type(student["mathematics"]))

    print("Physics Type:", type(student["physics"]))

    print("Python Type:", type(student["python"]))

    print("Average Type:", type(student["average"]))


# ---------------------------------------------------------------
# SECTION 7: DATASET STATISTICS
# ---------------------------------------------------------------

# We now perform calculations using the cleaned numerical data.
#
# This is possible because we converted the original strings
# into appropriate numerical values.

print("\n" + "=" * 75)
print("                    DATASET STATISTICS")
print("=" * 75)

# Count the number of successfully processed students.

total_students = len(cleaned_dataset)

print("Total Valid Students:", total_students)

# Create a list containing every student's average marks.

student_averages = [
    student["average"]
    for student in cleaned_dataset
]

# Calculate the average performance of all students.

if total_students > 0:

    overall_average = sum(student_averages) / total_students

    highest_average = max(student_averages)

    lowest_average = min(student_averages)

    print("Overall Average:", round(overall_average, 2))

    print("Highest Student Average:", round(highest_average, 2))

    print("Lowest Student Average:", round(lowest_average, 2))


# ---------------------------------------------------------------
# SECTION 8: CONVERTING DATA INTO BOOLEAN VALUES
# ---------------------------------------------------------------

# We now demonstrate Boolean conversion.
#
# Suppose the university uses 50 as the minimum average
# required to pass the examination.

print("\n" + "=" * 75)
print("                    STUDENT ELIGIBILITY")
print("=" * 75)

for student in cleaned_dataset:

    # This comparison produces either True or False.

    passed_condition = student["average"] >= 50

    # Convert the result into a Boolean value explicitly.

    passed = bool(passed_condition)

    print("\nStudent:", student["name"])

    print("Average:", round(student["average"], 2))

    print("Passed:", passed)

    print("Status Type:", type(passed))


# ---------------------------------------------------------------
# SECTION 9: IMAGE PIXEL DATA
# ---------------------------------------------------------------

# We now move into Computer Vision.
#
# An ordinary 8-bit image stores pixel channel values
# between 0 and 255.
#
# These values are commonly represented as integers.
#
# Here we use a small artificial example containing
# nine pixel values.
#
# These are demonstration values, not an actual photograph.

image_pixels = [
    0, 50, 100,
    128, 150, 200,
    220, 240, 255
]

print("\n" + "=" * 75)
print("                    ORIGINAL IMAGE PIXELS")
print("=" * 75)

print("Original Pixel Values:", image_pixels)

print("Pixel Data Type:", type(image_pixels[0]))


# ---------------------------------------------------------------
# SECTION 10: CONVERT IMAGE PIXELS INTO FLOATS
# ---------------------------------------------------------------

# Machine learning applications commonly use floating-point
# representations for numerical calculations.
#
# We convert every integer pixel into a float.
#
# This is done using a list comprehension.

image_pixels_float = [

    float(pixel)

    for pixel in image_pixels

]

print("\n" + "=" * 75)
print("                    FLOAT IMAGE PIXELS")
print("=" * 75)

print("Converted Pixels:", image_pixels_float)

print("Converted Pixel Type:", type(image_pixels_float[0]))


# ---------------------------------------------------------------
# SECTION 11: NORMALIZE IMAGE PIXEL VALUES
# ---------------------------------------------------------------

# Normalization is an important preprocessing technique.
#
# The original image values range from 0 to 255.
#
# We divide every pixel value by 255.
#
# Mathematical formula:
#
# Normalized Pixel = Original Pixel / 255
#
# This transforms the pixel values into a range between 0 and 1.

normalized_pixels = [

    pixel / 255.0

    for pixel in image_pixels_float

]

print("\n" + "=" * 75)
print("                    NORMALIZED IMAGE PIXELS")
print("=" * 75)

print("Normalized Pixels:", normalized_pixels)

# Display each original pixel alongside its normalized value.

for original, normalized in zip(
    image_pixels,
    normalized_pixels
):

    print(
        "Original:", original,
        "| Normalized:", round(normalized, 4)
    )


# ---------------------------------------------------------------
# SECTION 12: CREATE AI MODEL CONFIGURATION
# ---------------------------------------------------------------

# An AI model needs several configuration values.
#
# We create a dictionary to store the model information.
#
# Notice the different data types:
#
# Model name       = String
# Learning rate    = Float
# Epochs           = Integer
# Accuracy         = Float
# Training status  = Boolean
# Image dimensions = Tuple

ai_model = {

    "model_name": "Image Classification Model",

    "learning_rate": 0.001,

    "epochs": 50,

    "accuracy": 96.5,

    "is_trained": True,

    "image_dimensions": (224, 224, 3)

}

print("\n" + "=" * 75)
print("                    AI MODEL CONFIGURATION")
print("=" * 75)

# Display all model information.

for key, value in ai_model.items():

    print(key, ":", value)


# ---------------------------------------------------------------
# SECTION 13: VERIFY AI MODEL DATA TYPES
# ---------------------------------------------------------------

# We use isinstance() to check whether the model configuration
# contains the expected data types.

print("\n" + "=" * 75)
print("                    AI MODEL TYPE VALIDATION")
print("=" * 75)

print(
    "Model Name Is String:",
    isinstance(ai_model["model_name"], str)
)

print(
    "Learning Rate Is Float:",
    isinstance(ai_model["learning_rate"], float)
)

print(
    "Epochs Is Integer:",
    isinstance(ai_model["epochs"], int)
)

print(
    "Accuracy Is Float:",
    isinstance(ai_model["accuracy"], float)
)

print(
    "Training Status Is Boolean:",
    isinstance(ai_model["is_trained"], bool)
)

print(
    "Image Dimensions Is Tuple:",
    isinstance(ai_model["image_dimensions"], tuple)
)


# ---------------------------------------------------------------
# SECTION 14: FINAL PREPROCESSING REPORT
# ---------------------------------------------------------------

print("\n" + "=" * 75)
print("             FINAL AI DATA PREPROCESSING REPORT")
print("=" * 75)

print("Project: AI Dataset Preprocessing")

print("Original Dataset Records:", len(raw_dataset))

print("Successfully Processed Records:", len(cleaned_dataset))

print("Rejected Records:", len(raw_dataset) - len(cleaned_dataset))

if len(cleaned_dataset) > 0:

    print("Dataset Average:", round(overall_average, 2))

print("Image Pixel Count:", len(image_pixels))

print("Image Pixel Original Type:", type(image_pixels[0]).__name__)

print("Image Pixel Converted Type:", type(image_pixels_float[0]).__name__)

print("Normalized Pixel Type:", type(normalized_pixels[0]).__name__)

print("AI Model:", ai_model["model_name"])

print("AI Model Accuracy:", ai_model["accuracy"], "%")

print("AI Model Learning Rate:", ai_model["learning_rate"])

print("AI Model Epochs:", ai_model["epochs"])

print("\n" + "=" * 75)
print("             DAY 004 CHALLENGE COMPLETED")
print("=" * 75)

# ================================================================
# END OF DAY 004 CODING CHALLENGE
# ================================================================
