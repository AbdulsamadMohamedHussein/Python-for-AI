
# EXERCISE 1: IDENTIFY DATA TYPES

student_name = "Abdulsamad"
student_age = 23
student_height = 1.75
is_student = True
student_result = None

print("Student Name:", student_name)
print("Name Type:", type(student_name))

print("Student Age:", student_age)
print("Age Type:", type(student_age))

print("Student Height:", student_height)
print("Height Type:", type(student_height))

print("Is Student:", is_student)
print("Boolean Type:", type(is_student))

print("Student Result:", student_result)
print("Result Type:", type(student_result))


# EXERCISE 2: INTEGER AND FLOAT

mathematics = 85
physics = 90
python = 95

total_marks = mathematics + physics + python

average_marks = total_marks / 3

print("Mathematics:", mathematics)
print("Physics:", physics)
print("Python:", python)

print("Total Marks:", total_marks)
print("Average Marks:", average_marks)

print("Total Type:", type(total_marks))
print("Average Type:", type(average_marks))


# EXERCISE 3: STRINGS

first_name = "Abdulsamad"
last_name = "Mohamed"
country = "Kenya"
course = "Artificial Intelligence"

full_name = first_name + " " + last_name

print("Full Name:", full_name)

introduction = (
    f"My name is {full_name}. "
    f"I am from {country}. "
    f"I am studying {course}."
)

print(introduction)

print("Name Length:", len(full_name))
print("Uppercase:", full_name.upper())
print("Lowercase:", full_name.lower())


# EXERCISE 4: BOOLEAN

student_age = 23
has_completed_registration = True

is_adult = student_age >= 18

print("Is Adult:", is_adult)
print("Registration Completed:", has_completed_registration)

eligible = is_adult and has_completed_registration

print("Eligible for Examination:", eligible)

print("Eligibility Type:", type(eligible))


# EXERCISE 5: LISTS

student_marks = [85, 90, 95, 88, 92]

print("Original Marks:", student_marks)

print("First Mark:", student_marks[0])
print("Second Mark:", student_marks[1])
print("Last Mark:", student_marks[-1])

# Update the first mark
student_marks[0] = 100

# Add another mark
student_marks.append(96)

print("Updated Marks:", student_marks)

print("Number of Marks:", len(student_marks))
print("Highest Mark:", max(student_marks))
print("Lowest Mark:", min(student_marks))
print("Total Marks:", sum(student_marks))

average = sum(student_marks) / len(student_marks)

print("Average Marks:", average)


# EXERCISE 6: TUPLES

image_dimensions = (224, 224, 3)

width = image_dimensions[0]
height = image_dimensions[1]
channels = image_dimensions[2]

print("Image Dimensions:", image_dimensions)

print("Width:", width)
print("Height:", height)
print("Channels:", channels)

print("Tuple Type:", type(image_dimensions))

# Display image information
print(
    f"The image has a width of {width}, "
    f"height of {height}, "
    f"and {channels} colour channels."
)


# EXERCISE 7: SETS

student_ids = {101, 102, 103, 104, 101, 102}

print("Student IDs:", student_ids)

print("Number of Unique IDs:", len(student_ids))

# Add a new ID
student_ids.add(105)

print("After Adding:", student_ids)

# Remove an ID
student_ids.remove(103)

print("After Removing:", student_ids)

# Check membership
print("Is 101 Available?", 101 in student_ids)
print("Is 200 Available?", 200 in student_ids)


# EXERCISE 8: DICTIONARIES

student = {
    "name": "Abdulsamad Mohamed",
    "age": 23,
    "country": "Kenya",
    "course": "Artificial Intelligence",
    "university": "Guilin University of Electronics Technology"
}

print("Student Information:", student)

print("Name:", student["name"])
print("Age:", student["age"])
print("Country:", student["country"])

# Add a new key-value pair
student["programming_level"] = "Beginner"

# Update an existing value
student["age"] = 24

print("\nUpdated Student Information:")

for key, value in student.items():
    print(key, ":", value)


# EXERCISE 9: MIXED DATA TYPES

student_record = [
    "Abdulsamad Mohamed",
    23,
    95.5,
    True,
    None
]

print("Student Record:", student_record)

print("Name:", student_record[0])
print("Age:", student_record[1])
print("Accuracy:", student_record[2])
print("Currently Studying:", student_record[3])
print("Final Result:", student_record[4])

print("\nChecking Individual Data Types:")

for item in student_record:
    print(item, "=", type(item))


# EXERCISE 10: AI MODEL INFORMATION

ai_model = {
    "model_name": "Image Classifier",
    "learning_rate": 0.001,
    "accuracy": 96.5,
    "epochs": 50,
    "image_dimensions": (224, 224, 3),
    "is_trained": True,
    "prediction_label": "Cat"
}

print("=" * 50)
print("           AI MODEL INFORMATION")
print("=" * 50)

print("Model Name:", ai_model["model_name"])
print("Learning Rate:", ai_model["learning_rate"])
print("Accuracy:", ai_model["accuracy"], "%")
print("Epochs:", ai_model["epochs"])
print("Image Dimensions:", ai_model["image_dimensions"])
print("Model Trained:", ai_model["is_trained"])
print("Prediction:", ai_model["prediction_label"])

print("\nDATA TYPES:")

for key, value in ai_model.items():
    print(key, ":", type(value).__name__)

print("=" * 50)
