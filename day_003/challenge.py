
# ============================================================
# DAY 003 - CODING CHALLENGE
# AI STUDENT AND IMAGE CLASSIFICATION MANAGEMENT SYSTEM
# Bachelor's in Artificial Intelligence
# ============================================================


# ------------------------------------------------------------
# SECTION 1: PROGRAM INTRODUCTION
# ------------------------------------------------------------

print("=" * 65)
print("       AI STUDENT AND IMAGE CLASSIFICATION MANAGEMENT SYSTEM")
print("=" * 65)


# ------------------------------------------------------------
# SECTION 2: STUDENT PERSONAL INFORMATION
# ------------------------------------------------------------

student_name = "Abdulsamad Mohamed"
student_age = 23
student_country = "Kenya"
student_university = "Guilin University of Electronics Technology"
student_course = "Bachelor's in Artificial Intelligence"
is_student = True

print("\n" + "=" * 65)
print("                  STUDENT INFORMATION")
print("=" * 65)

print("Student Name:", student_name)
print("Age:", student_age)
print("Country:", student_country)
print("University:", student_university)
print("Course:", student_course)
print("Currently Studying:", is_student)


# ------------------------------------------------------------
# SECTION 3: STUDENT ACADEMIC RECORDS
# ------------------------------------------------------------

mathematics_marks = 85
physics_marks = 90
python_marks = 95
chemistry_marks = 88

total_marks = (
    mathematics_marks
    + physics_marks
    + python_marks
    + chemistry_marks
)

average_marks = total_marks / 4

print("\n" + "=" * 65)
print("                  ACADEMIC RECORDS")
print("=" * 65)

print("Mathematics:", mathematics_marks)
print("Physics:", physics_marks)
print("Python:", python_marks)
print("Chemistry:", chemistry_marks)

print("Total Marks:", total_marks)
print("Average Marks:", average_marks)


# ------------------------------------------------------------
# SECTION 4: STUDENT PROGRAMMING SKILLS
# ------------------------------------------------------------

programming_languages = [
    "Python",
    "Java",
    "C++",
    "JavaScript"
]

print("\n" + "=" * 65)
print("                  PROGRAMMING SKILLS")
print("=" * 65)

print("Programming Languages:", programming_languages)

print("First Language:", programming_languages[0])
print("Second Language:", programming_languages[1])

# Adding another programming language

programming_languages.append("R")

print("Updated Languages:", programming_languages)


# ------------------------------------------------------------
# SECTION 5: STUDENT COURSE REGISTRATION
# ------------------------------------------------------------

registered_courses = (
    "Python Programming",
    "Machine Learning",
    "Deep Learning",
    "Computer Vision"
)

print("\n" + "=" * 65)
print("                  REGISTERED COURSES")
print("=" * 65)

for course in registered_courses:
    print(course)

print("Total Registered Courses:", len(registered_courses))


# ------------------------------------------------------------
# SECTION 6: UNIQUE STUDENT IDENTIFICATION
# ------------------------------------------------------------

student_ids = {
    101,
    102,
    103,
    104,
    101,
    102,
    105
}

print("\n" + "=" * 65)
print("                  STUDENT IDENTIFICATION")
print("=" * 65)

print("Unique Student IDs:", student_ids)
print("Number of Unique Students:", len(student_ids))

student_ids.add(106)

print("After Adding New Student:", student_ids)


# ------------------------------------------------------------
# SECTION 7: STUDENT INFORMATION DICTIONARY
# ------------------------------------------------------------

student_information = {
    "name": student_name,
    "age": student_age,
    "country": student_country,
    "university": student_university,
    "course": student_course,
    "average_marks": average_marks,
    "is_student": is_student
}

print("\n" + "=" * 65)
print("                  STUDENT PROFILE")
print("=" * 65)

for key, value in student_information.items():
    print(key, ":", value)


# ------------------------------------------------------------
# SECTION 8: AI MODEL CONFIGURATION
# ------------------------------------------------------------

model_name = "Image Classification Model"
learning_rate = 0.001
number_of_epochs = 50
training_accuracy = 96.5
is_model_trained = True

image_dimensions = (224, 224, 3)

print("\n" + "=" * 65)
print("                  AI MODEL CONFIGURATION")
print("=" * 65)

print("Model Name:", model_name)
print("Learning Rate:", learning_rate)
print("Number of Epochs:", number_of_epochs)
print("Training Accuracy:", training_accuracy)
print("Model Trained:", is_model_trained)
print("Image Dimensions:", image_dimensions)


# ------------------------------------------------------------
# SECTION 9: IMAGE CLASSIFICATION RESULTS
# ------------------------------------------------------------

image_labels = [
    "Cat",
    "Dog",
    "Car",
    "Bird",
    "Person"
]

predicted_label = "Cat"
prediction_confidence = 0.985
is_prediction_correct = True

print("\n" + "=" * 65)
print("                  IMAGE CLASSIFICATION")
print("=" * 65)

print("Available Labels:", image_labels)
print("Predicted Image:", predicted_label)
print("Prediction Confidence:", prediction_confidence)
print("Prediction Correct:", is_prediction_correct)


# ------------------------------------------------------------
# SECTION 10: AI MODEL INFORMATION DICTIONARY
# ------------------------------------------------------------

ai_model = {
    "model_name": model_name,
    "learning_rate": learning_rate,
    "epochs": number_of_epochs,
    "accuracy": training_accuracy,
    "trained": is_model_trained,
    "image_shape": image_dimensions,
    "prediction": predicted_label,
    "confidence": prediction_confidence
}

print("\n" + "=" * 65)
print("                  AI MODEL INFORMATION")
print("=" * 65)

for key, value in ai_model.items():
    print(key, ":", value)


# ------------------------------------------------------------
# SECTION 11: DATA TYPE IDENTIFICATION
# ------------------------------------------------------------

print("\n" + "=" * 65)
print("                  DATA TYPE IDENTIFICATION")
print("=" * 65)

data_examples = [
    student_name,
    student_age,
    average_marks,
    is_student,
    registered_courses,
    programming_languages,
    student_ids,
    student_information,
    learning_rate,
    image_dimensions,
    None,
    3 + 4j
]

for item in data_examples:

    print(
        "Value:",
        str(item),
        "| Data Type:",
        type(item).__name__
    )


# ------------------------------------------------------------
# SECTION 12: TYPE VALIDATION
# ------------------------------------------------------------

print("\n" + "=" * 65)
print("                  TYPE VALIDATION")
print("=" * 65)

print("Is Age an Integer?", isinstance(student_age, int))

print("Is Name a String?", isinstance(student_name, str))

print("Is Accuracy a Float?", isinstance(training_accuracy, float))

print("Is Student Status Boolean?", isinstance(is_student, bool))

print("Is Programming Languages a List?",
      isinstance(programming_languages, list))

print("Is Image Dimensions a Tuple?",
      isinstance(image_dimensions, tuple))


# ------------------------------------------------------------
# SECTION 13: MUTABLE DATA TYPE DEMONSTRATION
# ------------------------------------------------------------

print("\n" + "=" * 65)
print("                  MUTABLE DATA TYPES")
print("=" * 65)

original_marks = [80, 85, 90]

print("Original Marks:", original_marks)

original_marks[0] = 100

print("Updated Marks:", original_marks)


# ------------------------------------------------------------
# SECTION 14: IMMUTABLE DATA TYPE DEMONSTRATION
# ------------------------------------------------------------

print("\n" + "=" * 65)
print("                  IMMUTABLE DATA TYPES")
print("=" * 65)

original_course = "Python"

print("Original Course:", original_course)

original_course = original_course + " Programming"

print("New Course:", original_course)


# ------------------------------------------------------------
# SECTION 15: STUDENT ELIGIBILITY
# ------------------------------------------------------------

print("\n" + "=" * 65)
print("                  STUDENT ELIGIBILITY")
print("=" * 65)

minimum_marks = 50

has_passed = average_marks >= minimum_marks

print("Average Marks:", average_marks)
print("Minimum Required:", minimum_marks)
print("Has Passed:", has_passed)


# ------------------------------------------------------------
# SECTION 16: FINAL REPORT
# ------------------------------------------------------------

print("\n" + "=" * 65)
print("                  FINAL STUDENT REPORT")
print("=" * 65)

print(f"Student Name: {student_name}")
print(f"University: {student_university}")
print(f"Average Marks: {average_marks}")
print(f"Programming Languages: {programming_languages}")
print(f"AI Model: {model_name}")
print(f"Model Accuracy: {training_accuracy}%")
print(f"Image Prediction: {predicted_label}")
print(f"Prediction Confidence: {prediction_confidence * 100}%")
print(f"Student Passed: {has_passed}")

print("\n" + "=" * 65)
print("             DAY 003 CHALLENGE COMPLETED")
print("=" * 65)

# ============================================================
# END OF DAY 003 CODING CHALLENGE
# ============================================================
