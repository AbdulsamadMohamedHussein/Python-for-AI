student_name="John"
student_age=20
country="USA"
print("The student's name is:",student_name)
print(student_age)
print(country)

#========================================
# DAY 002: VARIABLES IN PYTHON
#student: Python for AI Learning
#purpose:Understanding variables and assignment

#------------------------------------------------
#SECTION 1:CREATING VARIABLES
#------------------------------------------------

# A variables stores a values under a name.
student_name="Abdulsamad Mohamed"
student_age= 23
student_country="Kenya"

print("The student's name is: ",student_name)
print("The student's age is: ",student_age)
print("The student's country is: ",student_country)


# --------------------------------------------------
# SECTION 2: PRINTING VARIABLES
# --------------------------------------------------
# print() displays the value of a variable.
name="Abdulsamad Mohamed"
age=23
university="Guilin University of Electronics Technology"
print("Name: ",name)
print("Age: ",age)
print("University: ",university)

#printing multiple variables together
print(name,age,university)

# --------------------------------------------------
# SECTION 3: VARIABLES WITH DIFFERENT VALUES
# --------------------------------------------------

# Variables can hold different kinds of values.
# We will study these value types in Day 003.
full_name="Abdulsamad Mohamed"
marks=85
height=1.75
is_student=True
print("Full Name: ",full_name)
print("Marks: ",marks)
print("Height: ",height)
print("Is Student: ",is_student)

# --------------------------------------------------
# SECTION 4: CHANGING VARIABLE VALUES
# --------------------------------------------------

# A variable can be assigned a new value.
city="Nairobi"
print(city)
city="Mombasa"
print(city)
city="Kisumu"
print(city)

# --------------------------------------------------
# SECTION 7: ASSIGNING THE SAME VALUE
# --------------------------------------------------

# Multiple variables can share the same value.

x = y = z = 100

print(x)
print(y)
print(z)

#----------------------------------------------
#SECTION 8: SWAPPING VARIABLE VALUES
#----------------------------------------------
#PYTHON ALLOWS US TO EXCHANGE VARIABLE VALUES

first="Apple"
second="Mango"

print("Before swapping:")
print(first)
print(second)
first, second = second, first
print("After swapping:")
print(first)
print(second)

# --------------------------------------------------
# SECTION 9: UNDERSTANDING VARIABLE NAMES
# --------------------------------------------------

# Good variable names explain their purpose.

student_marks = 90
student_email = "abdulsamadmohamed09@example.com"
student_address = "Guilin City, Guangxi, China"

print(student_marks)
print(student_email)
print(student_address)

# --------------------------------------------------
# SECTION 10: VARIABLE NAMING RULES
# --------------------------------------------------

# Valid variable names.
student_name = "Abdulsamad Mohamed"
student_age = 21
_marks =80
marks2=90
student1="John"
print(student_name)
print(student_age)
print(_marks)
print(marks2)
print(student1)

# --------------------------------------------------
# SECTION 11: INVALID VARIABLE NAMES
# --------------------------------------------------

# These are examples of INVALID names.
# Do not remove the comments (#).
# Otherwise, Python will produce syntax errors.

# 2student = "Ali"
# student-name = "Ali"
# student name = "Ali"
# class = "AI"
# --------------------------------------------------
# SECTION 12: PYTHON IS CASE-SENSITIVE
# --------------------------------------------------

# These are three different variables.

name = "Ali"
Name = "Ahmed"
NAME = "John"

print(name)
print(Name)
print(NAME)

#---------------------------------------------------
# SECTION 13: CHECKING VARIABLE TYPES
#---------------------------------------------------
person_name ="Abdulsamad Mohamed Hussein"
person_age=23
person_height=1.81
person_is_student=True

print(type(person_name))
print(type(person_age))
print(type(person_height))
print(type(person_is_student))

# --------------------------------------------------
# SECTION 14: USING VARIABLES INSIDE MESSAGES
# --------------------------------------------------

# print() can display text and variables together.

my_name = "Abdulsamad Mohamed"
my_age = 23
my_country = "Nigeria"

print("My name is", my_name)
print("My age is", my_age, "years old")
print("My country is", my_country)

# --------------------------------------------------
# SECTION 15: USING F-STRINGS
# --------------------------------------------------

# An f-string allows us to insert variables
# directly inside a string.

name = "Ahmed"
age = 22

print(f"My name is {name}")
print(f"I am {age} years old")

print(f"My name is {name} and my age is {age}")

#---------------------------------------------------
#SECTION 16: USING VARIABLES IN CALCULATIONS
#---------------------------------------------------    
#the same variable can receive a new value based on its previous value.
course="Python for AI"
print( "First course: course}")
course="Machine Learning"
print("Second Course: course}")
course="Deep learning"
print("Third Course: ", course)

# --------------------------------------------------
# SECTION 17: CONSTANTS
# --------------------------------------------------

# Python does not enforce constants.
# Uppercase naming is a convention for values
# that should not normally be changed.

PI = 3.14159
MAX_STUDENTS = 100
UNIVERSITY_NAME = "Guilin University of Electronics Technology"

print(PI)
print(MAX_STUDENTS)
print(UNIVERSITY_NAME)


# --------------------------------------------------
# SECTION 18: VARIABLES IN AN AI CONTEXT
# --------------------------------------------------

# Imagine we are storing information
# about a Machine Learning model.

model_name = "Image Classifier"
training_accuracy = 95.5
number_of_epochs = 50
learning_rate = 0.001

print("Model:", model_name)
print("Accuracy:", training_accuracy)
print("Epochs:", number_of_epochs)
print("Learning Rate:", learning_rate)

# --------------------------------------------------
# SECTION 19: A STUDENT INFORMATION PROGRAM
# --------------------------------------------------
student_name = "Abdulsamad Mohamed"
student_age=23
student_country="Kenya"
student_course="Bachelors in Artificial Intelligence"
student_university="Guilin University of Electronics Technology"

print("\n================STUDENT INFORMATION================\n")
print(f"Name: {student_name}")
print(f"Age: {student_age}")
print(f"Country: {student_country}")
print(f"Course: {student_course}")
print(f"University: {student_university}")

print("\n===================================================\n")

# --------------------------------------------------
# SECTION 20: END OF DAY 002
# --------------------------------------------------

print("\nCongratulations!")
print("You have completed the Variables lesson.")
print("Keep practising Python every day.")
