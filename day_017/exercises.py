
# =====================================================================
# DAY 017 - PYTHON SETS
# 30 FULLY SOLVED EXERCISES
#
# Bachelor's in Artificial Intelligence
# 90-Day Python Programming Journey
#
# MAIN TOPIC: PYTHON SETS
#
# =====================================================================


# =====================================================================
# EXERCISE 1: CREATE A SET
# =====================================================================

# QUESTION:
# Create a set containing five different fruits.

print("\nEXERCISE 1: CREATE A SET")

fruits = {"Apple", "Banana", "Mango", "Orange", "Grapes"}

print("Fruits:", fruits)

print("Data type:", type(fruits))


# =====================================================================
# EXERCISE 2: CREATE A NUMERICAL SET
# =====================================================================

# QUESTION:
# Create a set containing ten numbers.

print("\nEXERCISE 2: NUMERICAL SET")

numbers = {10, 20, 30, 40, 50, 60, 70, 80, 90, 100}

print("Numbers:", numbers)

print("Total elements:", len(numbers))


# =====================================================================
# EXERCISE 3: CREATE A MIXED SET
# =====================================================================

# QUESTION:
# Create a set containing different data types.

print("\nEXERCISE 3: MIXED SET")

mixed = {"Python", 25, 3.14, True}

print("Mixed set:", mixed)


# =====================================================================
# EXERCISE 4: CREATE AN EMPTY SET
# =====================================================================

# QUESTION:
# Create an empty set.
#
# IMPORTANT:
# {} creates an empty dictionary.
# set() creates an empty set.

print("\nEXERCISE 4: EMPTY SET")

empty_set = set()

print("Empty set:", empty_set)

print("Data type:", type(empty_set))


# =====================================================================
# EXERCISE 5: REMOVE DUPLICATE VALUES
# =====================================================================

# QUESTION:
# Create a set from a list containing duplicates.
#
# Sets automatically retain only unique values.

print("\nEXERCISE 5: REMOVE DUPLICATES")

numbers = [10, 20, 10, 30, 20, 40, 30, 50]

unique_numbers = set(numbers)

print("Original list:", numbers)

print("Unique values:", unique_numbers)

print("Number of unique values:", len(unique_numbers))


# =====================================================================
# EXERCISE 6: ADD ONE ELEMENT
# =====================================================================

# QUESTION:
# Add a new fruit using add().

print("\nEXERCISE 6: ADD METHOD")

fruits = {"Apple", "Banana", "Mango"}

print("Before:", fruits)

fruits.add("Orange")

print("After:", fruits)


# =====================================================================
# EXERCISE 7: ADD MULTIPLE ELEMENTS
# =====================================================================

# QUESTION:
# Add multiple numbers using update().

print("\nEXERCISE 7: UPDATE METHOD")

numbers = {10, 20, 30}

numbers.update([40, 50, 60])

print("Updated set:", numbers)


# =====================================================================
# EXERCISE 8: REMOVE AN ELEMENT USING remove()
# =====================================================================

# QUESTION:
# Remove the number 30.
#
# remove() raises KeyError if the element is missing.

print("\nEXERCISE 8: REMOVE METHOD")

numbers = {10, 20, 30, 40, 50}

numbers.remove(30)

print("After removing 30:", numbers)


# =====================================================================
# EXERCISE 9: REMOVE AN ELEMENT USING discard()
# =====================================================================

# QUESTION:
# Remove an element using discard().
#
# discard() does not raise an error
# if the element does not exist.

print("\nEXERCISE 9: DISCARD METHOD")

numbers = {10, 20, 30, 40}

numbers.discard(20)

numbers.discard(100)

print("Updated set:", numbers)


# =====================================================================
# EXERCISE 10: CHECK WHETHER AN ELEMENT EXISTS
# =====================================================================

# QUESTION:
# Check whether Python exists in a set.

print("\nEXERCISE 10: MEMBERSHIP OPERATOR")

languages = {"Python", "Java", "C++", "JavaScript"}

print("Python exists:", "Python" in languages)

print("PHP exists:", "PHP" in languages)

print("PHP does not exist:", "PHP" not in languages)


# =====================================================================
# EXERCISE 11: SET UNION
# =====================================================================

# QUESTION:
# Combine two sets using union.
#
# Union combines all unique elements.
#
# Mathematical symbol: A ∪ B
# Python operator: |

print("\nEXERCISE 11: UNION")

A = {1, 2, 3, 4}

B = {3, 4, 5, 6}

result = A | B

print("Set A:", A)

print("Set B:", B)

print("Union:", result)


# =====================================================================
# EXERCISE 12: SET INTERSECTION
# =====================================================================

# QUESTION:
# Find common elements between two sets.
#
# Mathematical symbol: A ∩ B
# Python operator: &

print("\nEXERCISE 12: INTERSECTION")

A = {1, 2, 3, 4}

B = {3, 4, 5, 6}

result = A & B

print("Common elements:", result)


# =====================================================================
# EXERCISE 13: SET DIFFERENCE
# =====================================================================

# QUESTION:
# Find elements present in A but not in B.
#
# Mathematical expression: A - B

print("\nEXERCISE 13: DIFFERENCE")

A = {1, 2, 3, 4, 5}

B = {3, 4, 5, 6, 7}

result = A - B

print("A - B:", result)

print("B - A:", B - A)


# =====================================================================
# EXERCISE 14: SYMMETRIC DIFFERENCE
# =====================================================================

# QUESTION:
# Find elements that exist in either set,
# but not in both sets.
#
# Mathematical symbol: A △ B
# Python operator: ^

print("\nEXERCISE 14: SYMMETRIC DIFFERENCE")

A = {1, 2, 3, 4}

B = {3, 4, 5, 6}

result = A ^ B

print("Symmetric difference:", result)


# =====================================================================
# EXERCISE 15: CHECK SUBSET
# =====================================================================

# QUESTION:
# Check whether A is a subset of B.
#
# Every element in A must also exist in B.

print("\nEXERCISE 15: SUBSET")

A = {1, 2}

B = {1, 2, 3, 4, 5}

print("A is a subset of B:", A.issubset(B))

print("Using operator:", A <= B)


# =====================================================================
# EXERCISE 16: CHECK PROPER SUBSET
# =====================================================================

# QUESTION:
# Check whether A is a proper subset of B.
#
# A must be a subset of B and A must not equal B.

print("\nEXERCISE 16: PROPER SUBSET")

A = {1, 2}

B = {1, 2, 3}

C = {1, 2}

print("A is proper subset of B:", A < B)

print("A is proper subset of C:", A < C)


# =====================================================================
# EXERCISE 17: CHECK SUPERSET
# =====================================================================

# QUESTION:
# Check whether A is a superset of B.

print("\nEXERCISE 17: SUPERSET")

A = {1, 2, 3, 4, 5}

B = {1, 2, 3}

print("A is a superset of B:", A.issuperset(B))

print("Using operator:", A >= B)


# =====================================================================
# EXERCISE 18: CHECK DISJOINT SETS
# =====================================================================

# QUESTION:
# Check whether two sets have no common elements.

print("\nEXERCISE 18: DISJOINT SETS")

A = {1, 2, 3}

B = {4, 5, 6}

C = {3, 4, 5}

print("A and B are disjoint:", A.isdisjoint(B))

print("A and C are disjoint:", A.isdisjoint(C))


# =====================================================================
# EXERCISE 19: CREATE A FROZEN SET
# =====================================================================

# QUESTION:
# Create an immutable set using frozenset().

print("\nEXERCISE 19: FROZEN SET")

numbers = frozenset([10, 20, 30, 40, 50])

print("Frozen set:", numbers)

print("Data type:", type(numbers))

# Frozen sets cannot use add() or remove().


# =====================================================================
# EXERCISE 20: SET COMPREHENSION
# =====================================================================

# QUESTION:
# Create a set containing squares from 1 to 10.
#
# Formula:
# Square = n ** 2

print("\nEXERCISE 20: SET COMPREHENSION")

squares = {

    number ** 2

    for number in range(1, 11)

}

print("Squares:", squares)


# =====================================================================
# EXERCISE 21: EVEN NUMBERS USING SET COMPREHENSION
# =====================================================================

# QUESTION:
# Create a set containing even numbers from 1 to 20.
#
# A number is even if:
#
# number % 2 == 0

print("\nEXERCISE 21: EVEN NUMBERS")

even_numbers = {

    number

    for number in range(1, 21)

    if number % 2 == 0

}

print("Even numbers:", even_numbers)


# =====================================================================
# EXERCISE 22: UNIQUE CHARACTERS IN A WORD
# =====================================================================

# QUESTION:
# Find unique characters in the word programming.

print("\nEXERCISE 22: UNIQUE CHARACTERS")

word = "programming"

unique_characters = set(word)

print("Word:", word)

print("Unique characters:", unique_characters)

print("Number of unique characters:", len(unique_characters))


# =====================================================================
# EXERCISE 23: COMMON ELEMENTS BETWEEN TWO LISTS
# =====================================================================

# QUESTION:
# Find common numbers between two lists.

print("\nEXERCISE 23: COMMON LIST ELEMENTS")

list_1 = [10, 20, 30, 40, 50]

list_2 = [30, 40, 50, 60, 70]

common = set(list_1).intersection(set(list_2))

print("List 1:", list_1)

print("List 2:", list_2)

print("Common elements:", common)


# =====================================================================
# EXERCISE 24: PRESERVE ORDER WHILE REMOVING DUPLICATES
# =====================================================================

# QUESTION:
# Remove duplicates without changing original order.
#
# A normal set does not preserve sequence order.
#
# dict.fromkeys() preserves insertion order.

print("\nEXERCISE 24: PRESERVE ORDER")

numbers = [10, 20, 10, 30, 20, 40, 50]

unique_numbers = list(dict.fromkeys(numbers))

print("Original:", numbers)

print("Unique ordered values:", unique_numbers)


# =====================================================================
# EXERCISE 25: COUNT UNIQUE STUDENTS
# =====================================================================

# QUESTION:
# Find the number of unique students
# who registered for a course.

print("\nEXERCISE 25: UNIQUE STUDENTS")

registered_students = [

    "Ali",

    "Ahmed",

    "Ali",

    "John",

    "Ahmed",

    "David",

    "Michael"

]

unique_students = set(registered_students)

print("All registrations:", registered_students)

print("Unique students:", unique_students)

print("Total unique students:", len(unique_students))


# =====================================================================
# EXERCISE 26: FIND CLASS ATTENDANCE
# =====================================================================

# QUESTION:
# Find students who attended both Monday and Tuesday.
#
# Use intersection.

print("\nEXERCISE 26: CLASS ATTENDANCE")

monday = {

    "Ali",

    "Ahmed",

    "John",

    "David"

}

tuesday = {

    "Ali",

    "John",

    "Michael",

    "Sarah"

}

both_days = monday & tuesday

print("Monday attendance:", monday)

print("Tuesday attendance:", tuesday)

print("Attended both days:", both_days)


# =====================================================================
# EXERCISE 27: CALCULATE SET STATISTICS
# =====================================================================

# QUESTION:
# Calculate the number of unique numerical observations.
#
# Also calculate their minimum, maximum and average.

print("\nEXERCISE 27: SET STATISTICS")

numbers = {10, 20, 30, 40, 50, 20, 30}

total = sum(numbers)

count = len(numbers)

average = total / count

print("Unique observations:", numbers)

print("Count:", count)

print("Minimum:", min(numbers))

print("Maximum:", max(numbers))

print("Sum:", total)

print("Average:", average)


# =====================================================================
# EXERCISE 28: POPULATION VARIANCE OF A SET
# =====================================================================

# QUESTION:
# Calculate population variance.
#
# Formula:
#
# Population Variance = SUM((x - mean)^2) / n
#
# IMPORTANT:
# A set removes duplicates.
# This calculation therefore treats unique values
# as the observations in the population.

print("\nEXERCISE 28: POPULATION VARIANCE")

data = {10, 20, 30, 40, 50}

mean = sum(data) / len(data)

squared_differences = [

    (value - mean) ** 2

    for value in data

]

variance = sum(squared_differences) / len(data)

print("Data:", data)

print("Mean:", mean)

print("Squared differences:", squared_differences)

print("Population variance:", variance)


# =====================================================================
# EXERCISE 29: AI - UNIQUE CLASS LABELS
# =====================================================================

# QUESTION:
# Find all unique class labels in a dataset.
#
# This is a simple example of data preprocessing.
#
# Machine learning datasets can contain repeated labels.

print("\nEXERCISE 29: AI CLASSIFICATION LABELS")

labels = [

    "Cat",

    "Dog",

    "Cat",

    "Bird",

    "Dog",

    "Cat",

    "Fish",

    "Bird"

]

unique_labels = set(labels)

print("Original labels:", labels)

print("Unique classes:", unique_labels)

print("Number of classes:", len(unique_labels))


# =====================================================================
# EXERCISE 30: AI - FEATURE COMPARISON
# =====================================================================

# QUESTION:
# Compare feature names from two datasets.
#
# Find:
# 1. Common features.
# 2. All features.
# 3. Features unique to Dataset A.
# 4. Features unique to Dataset B.
#
# This is a simplified data-processing example.

print("\nEXERCISE 30: AI FEATURE COMPARISON")

dataset_A = {

    "age",

    "height",

    "weight",

    "income",

    "education"

}

dataset_B = {

    "age",

    "weight",

    "experience",

    "education",

    "location"

}

common_features = dataset_A & dataset_B

all_features = dataset_A | dataset_B

only_A = dataset_A - dataset_B

only_B = dataset_B - dataset_A

print("Dataset A:", dataset_A)

print("Dataset B:", dataset_B)

print("Common features:", common_features)

print("All features:", all_features)

print("Only Dataset A:", only_A)

print("Only Dataset B:", only_B)


# =====================================================================
# FINAL EXERCISE SUMMARY
# =====================================================================

exercise_names = [

    "Create a Set",

    "Numerical Set",

    "Mixed Set",

    "Empty Set",

    "Remove Duplicates",

    "Add Method",

    "Update Method",

    "Remove Method",

    "Discard Method",

    "Membership Operator",

    "Set Union",

    "Set Intersection",

    "Set Difference",

    "Symmetric Difference",

    "Subset",

    "Proper Subset",

    "Superset",

    "Disjoint Sets",

    "Frozen Set",

    "Set Comprehension",

    "Even Numbers",

    "Unique Characters",

    "Common List Elements",

    "Preserve Original Order",

    "Unique Students",

    "Class Attendance",

    "Set Statistics",

    "Population Variance",

    "AI Class Labels",

    "AI Feature Comparison"

]

print("\n" + "=" * 65)

print("DAY 017 - EXERCISE SUMMARY")

print("=" * 65)

for index, exercise in enumerate(exercise_names, start=1):

    print(f"{index}. {exercise} - COMPLETED")


print("\nALL 30 EXERCISES COMPLETED!")

print("=" * 65)


# =====================================================================
# END OF DAY 017 - EXERCISES.PY
# =====================================================================
