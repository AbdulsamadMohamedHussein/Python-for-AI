
# ==========================================
# DAY 018 - PYTHON DICTIONARY EXERCISES
# 10 SOLVED QUESTIONS
# Topic: Python Dictionaries
# ==========================================


# QUESTION 01
# Create a dictionary containing your personal information.

print("\n========== QUESTION 01 ==========")

person = {
    "name": "Alex",
    "age": 25,
    "country": "Japan",
    "profession": "Python Developer"
}

print("Personal Information:", person)


# QUESTION 02
# Access and print the name, age and profession.

print("\n========== QUESTION 02 ==========")

print("Name:", person["name"])
print("Age:", person["age"])
print("Profession:", person["profession"])


# QUESTION 03
# Add a new key called "language" to the dictionary.

print("\n========== QUESTION 03 ==========")

person["language"] = "Python"

print("Updated Dictionary:", person)


# QUESTION 04
# Change the person's age to 26.

print("\n========== QUESTION 04 ==========")

person["age"] = 26

print("Updated Age:", person["age"])
print("Updated Dictionary:", person)


# QUESTION 05
# Remove the country key from the dictionary.

print("\n========== QUESTION 05 ==========")

person.pop("country")

print("After Removing Country:", person)


# QUESTION 06
# Create a dictionary of five products and their prices.
# Print all products with their prices.

print("\n========== QUESTION 06 ==========")

products = {
    "Laptop": 800,
    "Mobile": 500,
    "Keyboard": 50,
    "Mouse": 25,
    "Headphones": 75
}

for product, price in products.items():
    print(product, "=", "$", price)


# QUESTION 07
# Find the total price of all products.

print("\n========== QUESTION 07 ==========")

total_price = sum(products.values())

print("Total Price: $", total_price)


# QUESTION 08
# Create a nested dictionary for three students.
# Display each student's name and marks.

print("\n========== QUESTION 08 ==========")

students = {
    "student1": {
        "name": "Ali",
        "marks": 85
    },

    "student2": {
        "name": "Ahmed",
        "marks": 90
    },

    "student3": {
        "name": "Sara",
        "marks": 95
    }
}

for student_id, details in students.items():
    print(
        "Name:", details["name"],
        "| Marks:", details["marks"]
    )


# QUESTION 09
# Find the student with the highest marks.

print("\n========== QUESTION 09 ==========")

highest_student = max(
    students.values(),
    key=lambda student: student["marks"]
)

print("Top Student:", highest_student["name"])
print("Highest Marks:", highest_student["marks"])


# QUESTION 10
# Create a dictionary using dictionary comprehension.
# Store numbers from 1 to 10 and their squares.

print("\n========== QUESTION 10 ==========")

squares = {
    number: number ** 2
    for number in range(1, 11)
}

print("Number and Square Dictionary:")

for number, square in squares.items():
    print(number, ":", square)


# ==========================================
# DAY 018 - ALL EXERCISES COMPLETED
# ==========================================

print("\n===================================")
print("CONGRATULATIONS!")
print("You have completed all 10 exercises.")
print("DAY 018 - PYTHON DICTIONARIES")
print("===================================")
