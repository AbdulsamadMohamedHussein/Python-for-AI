
# ==========================================
# DAY 018 - PYTHON DICTIONARIES
# Author: Your Name
# Topic: Python Dictionary
# ==========================================


# 1. Creating a Dictionary

student = {
    "name": "Alex",
    "age": 22,
    "course": "Python Programming",
    "grade": "A"
}

print("1. Student Information:")
print(student)


# 2. Accessing Dictionary Values

print("\n2. Accessing Values:")

print("Name:", student["name"])
print("Age:", student["age"])
print("Course:", student["course"])


# 3. Using get() Method

print("\n3. Using get() Method:")

print(student.get("name"))
print(student.get("city", "City not found"))


# 4. Adding New Items

print("\n4. Adding New Items:")

student["city"] = "Tokyo"
student["email"] = "alex@example.com"

print(student)


# 5. Updating Existing Items

print("\n5. Updating Values:")

student["age"] = 23
student["grade"] = "A+"

print(student)


# 6. Removing Items

print("\n6. Removing Items:")

student.pop("email")

print("After pop():", student)

del student["city"]

print("After del:", student)


# 7. Dictionary Length

print("\n7. Dictionary Length:")

print("Total items:", len(student))


# 8. Dictionary Keys, Values and Items

print("\n8. Dictionary Methods:")

print("Keys:", student.keys())
print("Values:", student.values())
print("Items:", student.items())


# 9. Looping Through a Dictionary

print("\n9. Looping Through Dictionary:")

for key, value in student.items():
    print(key, ":", value)


# 10. Checking if a Key Exists

print("\n10. Checking Keys:")

if "name" in student:
    print("Name exists in dictionary.")
else:
    print("Name does not exist.")


# 11. Nested Dictionaries

print("\n11. Nested Dictionaries:")

students = {
    "student1": {
        "name": "Ali",
        "age": 21,
        "grade": "A"
    },

    "student2": {
        "name": "Ahmed",
        "age": 23,
        "grade": "B"
    },

    "student3": {
        "name": "Sara",
        "age": 22,
        "grade": "A+"
    }
}

print(students)

print("Student 1 Name:", students["student1"]["name"])
print("Student 2 Grade:", students["student2"]["grade"])


# 12. Looping Through Nested Dictionaries

print("\n12. Nested Dictionary Loop:")

for student_id, details in students.items():
    print("\nStudent ID:", student_id)

    for key, value in details.items():
        print(key, ":", value)


# 13. Dictionary Comprehension

print("\n13. Dictionary Comprehension:")

numbers = [1, 2, 3, 4, 5]

squares = {number: number ** 2 for number in numbers}

print("Square Dictionary:", squares)


# 14. Copying a Dictionary

print("\n14. Copying Dictionary:")

student_copy = student.copy()

print("Original:", student)
print("Copy:", student_copy)


# 15. Clearing a Dictionary

print("\n15. Clearing Dictionary:")

temporary = {"name": "John", "age": 25}

temporary.clear()

print("After clear():", temporary)


# ==========================================
# DAY 018 COMPLETED
# ==========================================

print("\nCongratulations! Day 018 Completed!")
print("You have learned Python Dictionaries.")
