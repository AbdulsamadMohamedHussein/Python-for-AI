
# ==========================================================
# DAY 002 - CHALLENGE
# PROJECT: AI STUDENT PROFILE SYSTEM
# ==========================================================

# ----------------------------------------------------------
# TASK 1: STUDENT INFORMATION
# ----------------------------------------------------------

student_name = "Abdulsamad Mohamed"
student_age = 23
student_country = "Kenya"
university = "Guilin University of Electronics Technology"
degree_program = "Bachelors in Artificial Intelligence"


# ----------------------------------------------------------
# TASK 2: ACADEMIC INFORMATION
# ----------------------------------------------------------

mathematics_marks = 85
python_marks = 95
physics_marks = 90

programming_language = "Python"


# ----------------------------------------------------------
# TASK 3: AI MODEL INFORMATION
# ----------------------------------------------------------

model_name = "Basic Model"

learning_rate = 0.001
epochs = 100
batch_size = 32
model_accuracy = 96.5


# ----------------------------------------------------------
# TASK 4: VARIABLE REASSIGNMENT
# ----------------------------------------------------------

print("\n========== MODEL REASSIGNMENT ==========")

print(f"Original Model: {model_name}")

# Updating the model name
model_name = "Neural Network"

print(f"Updated Model: {model_name}")


# ----------------------------------------------------------
# TASK 5: SWAPPING VARIABLES
# ----------------------------------------------------------

first_course = "Python"
second_course = "Machine Learning"

print("\n========== COURSE SWAPPING ==========")

print(f"Before Swapping:")
print(f"First Course: {first_course}")
print(f"Second Course: {second_course}")

# Swapping the two variables
first_course, second_course = second_course, first_course

print("\nAfter Swapping:")
print(f"First Course: {first_course}")
print(f"Second Course: {second_course}")


# ----------------------------------------------------------
# TASK 6: CHECKING VARIABLE TYPES
# ----------------------------------------------------------

print("\n========== VARIABLE DATA TYPES ==========")

print(f"Student Name Type: {type(student_name)}")

print(f"Student Age Type: {type(student_age)}")

print(f"Learning Rate Type: {type(learning_rate)}")

print(f"Model Accuracy Type: {type(model_accuracy)}")


# ----------------------------------------------------------
# TASK 7: FINAL AI STUDENT PROFILE REPORT
# ----------------------------------------------------------

print("\n")
print("=" * 55)
print("             AI STUDENT PROFILE REPORT")
print("=" * 55)


# STUDENT INFORMATION

print("\nSTUDENT INFORMATION")

print(f"Name: {student_name}")

print(f"Age: {student_age}")

print(f"Country: {student_country}")

print(f"University: {university}")

print(f"Degree: {degree_program}")


# ACADEMIC INFORMATION

print("\nACADEMIC INFORMATION")

print(f"Mathematics Marks: {mathematics_marks}")

print(f"Python Marks: {python_marks}")

print(f"Physics Marks: {physics_marks}")

print(f"Programming Language: {programming_language}")


# AI MODEL INFORMATION

print("\nAI MODEL INFORMATION")

print(f"Model Name: {model_name}")

print(f"Learning Rate: {learning_rate}")

print(f"Training Epochs: {epochs}")

print(f"Batch Size: {batch_size}")

print(f"Model Accuracy: {model_accuracy}%")


# COURSE SWAPPING INFORMATION

print("\nCOURSE SWAPPING")

print(f"First Course: {first_course}")

print(f"Second Course: {second_course}")


# FINAL MESSAGE

print("\n" + "=" * 55)

print("                 END OF REPORT")

print("=" * 55)


# ==========================================================
# END OF DAY 002 CHALLENGE
# ==========================================================
