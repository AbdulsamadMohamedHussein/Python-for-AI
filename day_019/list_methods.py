
# ==========================================
# PYTHON FOR AI - DAY 019
# TOPIC: PYTHON LIST METHODS
# ==========================================

# 1. Creating a list
students = ["Abdulsamad", "Ali", "John", "Mary"]

print("Original list:", students)


# 2. append() - Add one element at the end
students.append("Ahmed")
print("After append:", students)


# 3. extend() - Add multiple elements
students.extend(["Peter", "Grace"])
print("After extend:", students)


# 4. insert() - Insert at a specific position
students.insert(1, "Hassan")
print("After insert:", students)


# 5. remove() - Remove a specific value
students.remove("John")
print("After remove:", students)


# 6. pop() - Remove an element using its index
removed_student = students.pop(2)

print("Removed student:", removed_student)
print("After pop:", students)


# 7. clear() - Remove all elements
temporary_list = [10, 20, 30]
temporary_list.clear()

print("Cleared list:", temporary_list)


# 8. sort() - Sort elements in ascending order
numbers = [45, 12, 89, 3, 27, 10]

numbers.sort()
print("Ascending order:", numbers)


# Sort in descending order
numbers.sort(reverse=True)
print("Descending order:", numbers)


# 9. reverse() - Reverse the list
scores = [50, 60, 70, 80, 90]

scores.reverse()
print("Reversed scores:", scores)


# 10. index() - Find the position of an element
subjects = ["Python", "Mathematics", "Machine Learning"]

position = subjects.index("Machine Learning")
print("Machine Learning position:", position)


# 11. count() - Count occurrences
marks = [80, 90, 80, 70, 80, 60]

frequency = marks.count(80)
print("Number of students scoring 80:", frequency)


# 12. copy() - Create a shallow copy
original = [10, 20, 30, 40]

copied = original.copy()
copied.append(50)

print("Original:", original)
print("Copied:", copied)


# ==========================================
# PRACTICAL AI EXAMPLE
# ==========================================

# Imagine these are model prediction scores.

prediction_scores = [0.85, 0.92, 0.78, 0.95, 0.88]

# Add another prediction
prediction_scores.append(0.97)

# Sort predictions
prediction_scores.sort()

# Calculate how many predictions are above 0.90
high_predictions = []

for score in prediction_scores:
    if score > 0.90:
        high_predictions.append(score)

print("All predictions:", prediction_scores)
print("High predictions:", high_predictions)

# ==========================================
# END OF DAY 019
# ==========================================
