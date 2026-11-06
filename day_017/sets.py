
# =====================================================================
# DAY 017 - PYTHON SETS
# Bachelor's in Artificial Intelligence
# 90-Day Python Programming Journey
#
# TOPIC: PYTHON SETS
#
# LEARNING OBJECTIVES:
# 1. Understand Python sets.
# 2. Create different types of sets.
# 3. Understand unordered collections.
# 4. Add and remove elements.
# 5. Perform mathematical set operations.
# 6. Understand subsets and supersets.
# 7. Learn frozen sets.
# 8. Learn set comprehensions.
# 9. Remove duplicate values.
# 10. Apply sets to statistics and AI.
# 11. Understand time complexity.
#
# =====================================================================


# =====================================================================
# SECTION 1: INTRODUCTION TO PYTHON SETS
# =====================================================================

# A set is a built-in Python data structure.
#
# A set stores UNIQUE elements.
#
# Main characteristics:
#
# 1. Unordered collection.
# 2. Mutable.
# 3. Does not allow duplicate elements.
# 4. Does not support indexing.
# 5. Elements must be hashable.
# 6. Supports mathematical set operations.
#
# Sets use curly brackets {}.
#
# IMPORTANT:
# An empty {} creates a dictionary, not a set.
#
# Use set() to create an empty set.

print("\n" + "=" * 65)
print("SECTION 1: INTRODUCTION TO PYTHON SETS")
print("=" * 65)

numbers = {10, 20, 30, 40, 50}

print("Numbers:", numbers)

print("Data type:", type(numbers))


# =====================================================================
# SECTION 2: CREATING SETS
# =====================================================================

print("\n" + "=" * 65)
print("SECTION 2: CREATING SETS")
print("=" * 65)

# Set containing integers.

numbers = {10, 20, 30, 40, 50}

print("Integer set:", numbers)


# Set containing strings.

names = {"Ali", "Ahmed", "John", "David"}

print("Names:", names)


# Set containing floating-point numbers.

measurements = {1.5, 2.5, 3.5, 4.5}

print("Measurements:", measurements)


# Mixed data types.

mixed = {"Python", 25, 3.14, True}

print("Mixed set:", mixed)


# Empty set.

empty_set = set()

print("Empty set:", empty_set)

print("Type:", type(empty_set))


# =====================================================================
# SECTION 3: DUPLICATE ELEMENTS
# =====================================================================

# Sets automatically remove duplicate elements.
#
# Only one occurrence of each equal element remains.
#
# IMPORTANT:
# Sets do not guarantee a particular display order.

print("\n" + "=" * 65)
print("SECTION 3: REMOVING DUPLICATES")
print("=" * 65)

numbers = {10, 20, 10, 30, 20, 40, 30}

print("Set:", numbers)

print("Number of unique elements:", len(numbers))


# =====================================================================
# SECTION 4: CONVERTING LISTS INTO SETS
# =====================================================================

# The set() constructor converts an iterable into a set.
#
# This is useful for removing duplicates from lists.

print("\n" + "=" * 65)
print("SECTION 4: LIST TO SET CONVERSION")
print("=" * 65)

numbers_list = [10, 20, 10, 30, 20, 40, 50]

numbers_set = set(numbers_list)

print("Original list:", numbers_list)

print("Converted set:", numbers_set)

print("Unique elements:", len(numbers_set))


# =====================================================================
# SECTION 5: ADDING ELEMENTS USING add()
# =====================================================================

# add() inserts one element into a set.
#
# If the element already exists,
# the set remains unchanged.

print("\n" + "=" * 65)
print("SECTION 5: ADD METHOD")
print("=" * 65)

fruits = {"Apple", "Banana", "Mango"}

print("Before:", fruits)

fruits.add("Orange")

print("After adding Orange:", fruits)

fruits.add("Apple")

print("After adding duplicate Apple:", fruits)


# =====================================================================
# SECTION 6: ADDING MULTIPLE ELEMENTS USING update()
# =====================================================================

# update() adds multiple elements from an iterable.
#
# It can accept lists, tuples, sets and other iterables.

print("\n" + "=" * 65)
print("SECTION 6: UPDATE METHOD")
print("=" * 65)

numbers = {10, 20, 30}

print("Original:", numbers)

numbers.update([40, 50, 60])

print("After list update:", numbers)

numbers.update((70, 80))

print("After tuple update:", numbers)

numbers.update({90, 100})

print("After set update:", numbers)


# =====================================================================
# SECTION 7: REMOVING ELEMENTS USING remove()
# =====================================================================

# remove() deletes a specified element.
#
# If the element does not exist,
# Python raises a KeyError.

print("\n" + "=" * 65)
print("SECTION 7: REMOVE METHOD")
print("=" * 65)

numbers = {10, 20, 30, 40, 50}

print("Before:", numbers)

numbers.remove(30)

print("After removing 30:", numbers)


# =====================================================================
# SECTION 8: REMOVING ELEMENTS USING discard()
# =====================================================================

# discard() removes an element if it exists.
#
# If the element does not exist,
# discard() does not raise an error.

print("\n" + "=" * 65)
print("SECTION 8: DISCARD METHOD")
print("=" * 65)

numbers = {10, 20, 30, 40}

numbers.discard(20)

print("After removing 20:", numbers)

# This does not cause an error.

numbers.discard(100)

print("After discarding 100:", numbers)


# =====================================================================
# SECTION 9: REMOVING ELEMENTS USING pop()
# =====================================================================

# pop() removes and returns an arbitrary element.
#
# Because sets are unordered, we should not
# assume which element will be removed.

print("\n" + "=" * 65)
print("SECTION 9: POP METHOD")
print("=" * 65)

numbers = {10, 20, 30, 40}

removed = numbers.pop()

print("Removed element:", removed)

print("Remaining set:", numbers)


# =====================================================================
# SECTION 10: CLEARING A SET
# =====================================================================

# clear() removes all elements.

print("\n" + "=" * 65)
print("SECTION 10: CLEAR METHOD")
print("=" * 65)

fruits = {"Apple", "Banana", "Mango"}

print("Before:", fruits)

fruits.clear()

print("After clear:", fruits)


# =====================================================================
# SECTION 11: CHECKING ELEMENTS USING IN
# =====================================================================

# The in operator checks whether an element exists.
#
# It returns True or False.

print("\n" + "=" * 65)
print("SECTION 11: MEMBERSHIP OPERATORS")
print("=" * 65)

languages = {"Python", "Java", "C++", "JavaScript"}

print("Python exists:", "Python" in languages)

print("PHP exists:", "PHP" in languages)

print("PHP does not exist:", "PHP" not in languages)


# =====================================================================
# SECTION 12: SET LENGTH
# =====================================================================

# len() returns the number of unique elements.

print("\n" + "=" * 65)
print("SECTION 12: SET LENGTH")
print("=" * 65)

numbers = {10, 20, 30, 40, 50}

print("Set:", numbers)

print("Total elements:", len(numbers))


# =====================================================================
# SECTION 13: ITERATING THROUGH SETS
# =====================================================================

# A for loop processes every set element.
#
# Remember:
# The order of iteration is not guaranteed.

print("\n" + "=" * 65)
print("SECTION 13: SET ITERATION")
print("=" * 65)

fruits = {"Apple", "Banana", "Mango", "Orange"}

for fruit in fruits:

    print("Fruit:", fruit)


# =====================================================================
# SECTION 14: SET UNION
# =====================================================================

# Union combines elements from two sets.
#
# Duplicate elements appear only once.
#
# Mathematical symbol: A ∪ B
#
# Python operator: |
#
# Method: union()

print("\n" + "=" * 65)
print("SECTION 14: SET UNION")
print("=" * 65)

A = {1, 2, 3, 4}

B = {3, 4, 5, 6}

result = A | B

print("Set A:", A)

print("Set B:", B)

print("Union:", result)

print("Using method:", A.union(B))


# =====================================================================
# SECTION 15: SET INTERSECTION
# =====================================================================

# Intersection returns elements common to both sets.
#
# Mathematical symbol: A ∩ B
#
# Python operator: &
#
# Method: intersection()

print("\n" + "=" * 65)
print("SECTION 15: SET INTERSECTION")
print("=" * 65)

A = {1, 2, 3, 4}

B = {3, 4, 5, 6}

result = A & B

print("Set A:", A)

print("Set B:", B)

print("Intersection:", result)

print("Using method:", A.intersection(B))


# =====================================================================
# SECTION 16: SET DIFFERENCE
# =====================================================================

# Difference returns elements present in A
# but not present in B.
#
# Mathematical symbol: A - B
#
# Python operator: -
#
# Method: difference()

print("\n" + "=" * 65)
print("SECTION 16: SET DIFFERENCE")
print("=" * 65)

A = {1, 2, 3, 4, 5}

B = {3, 4, 5, 6, 7}

print("A - B:", A - B)

print("B - A:", B - A)

print("Using method:", A.difference(B))


# =====================================================================
# SECTION 17: SYMMETRIC DIFFERENCE
# =====================================================================

# Symmetric difference returns elements
# that exist in either set but not both.
#
# Mathematical symbol: A △ B
#
# Python operator: ^
#
# Method: symmetric_difference()

print("\n" + "=" * 65)
print("SECTION 17: SYMMETRIC DIFFERENCE")
print("=" * 65)

A = {1, 2, 3, 4}

B = {3, 4, 5, 6}

result = A ^ B

print("Set A:", A)

print("Set B:", B)

print("Symmetric difference:", result)

print("Using method:", A.symmetric_difference(B))


# =====================================================================
# SECTION 18: SUBSETS
# =====================================================================

# A is a subset of B if every element in A
# is also present in B.
#
# Mathematical symbol: A ⊆ B
#
# Python operator: <=
#
# Method: issubset()

print("\n" + "=" * 65)
print("SECTION 18: SUBSETS")
print("=" * 65)

A = {1, 2}

B = {1, 2, 3, 4, 5}

print("A is subset of B:", A <= B)

print("Using method:", A.issubset(B))


# =====================================================================
# SECTION 19: PROPER SUBSETS
# =====================================================================

# A is a proper subset of B if:
#
# 1. Every element of A belongs to B.
# 2. A and B are not equal.
#
# Python operator: <

print("\n" + "=" * 65)
print("SECTION 19: PROPER SUBSETS")
print("=" * 65)

A = {1, 2}

B = {1, 2, 3}

C = {1, 2}

print("A is proper subset of B:", A < B)

print("A is proper subset of C:", A < C)


# =====================================================================
# SECTION 20: SUPERSETS
# =====================================================================

# A is a superset of B if A contains
# every element of B.
#
# Mathematical symbol: A ⊇ B
#
# Python operator: >=
#
# Method: issuperset()

print("\n" + "=" * 65)
print("SECTION 20: SUPERSETS")
print("=" * 65)

A = {1, 2, 3, 4, 5}

B = {1, 2, 3}

print("A is superset of B:", A >= B)

print("Using method:", A.issuperset(B))


# =====================================================================
# SECTION 21: DISJOINT SETS
# =====================================================================

# Two sets are disjoint if they have
# no elements in common.
#
# Method: isdisjoint()

print("\n" + "=" * 65)
print("SECTION 21: DISJOINT SETS")
print("=" * 65)

A = {1, 2, 3}

B = {4, 5, 6}

C = {3, 4, 5}

print("A and B disjoint:", A.isdisjoint(B))

print("A and C disjoint:", A.isdisjoint(C))


# =====================================================================
# SECTION 22: FROZEN SETS
# =====================================================================

# A frozenset is an immutable version of a set.
#
# Its elements cannot be added or removed.
#
# Frozen sets can be used as dictionary keys
# if their elements are hashable.

print("\n" + "=" * 65)
print("SECTION 22: FROZEN SETS")
print("=" * 65)

numbers = frozenset([10, 20, 30, 40])

print("Frozen set:", numbers)

print("Data type:", type(numbers))

# This operation is invalid:
#
# numbers.add(50)
#
# It raises AttributeError.


# =====================================================================
# SECTION 23: SET COMPREHENSIONS
# =====================================================================

# Set comprehensions create sets
# using a concise expression.
#
# Syntax:
#
# {expression for item in iterable}

print("\n" + "=" * 65)
print("SECTION 23: SET COMPREHENSIONS")
print("=" * 65)

squares = {

    number ** 2

    for number in range(1, 6)

}

print("Squares:", squares)


# =====================================================================
# SECTION 24: CONDITIONAL SET COMPREHENSIONS
# =====================================================================

# We can include a condition
# inside a set comprehension.

print("\n" + "=" * 65)
print("SECTION 24: CONDITIONAL SET COMPREHENSIONS")
print("=" * 65)

even_numbers = {

    number

    for number in range(1, 21)

    if number % 2 == 0

}

print("Even numbers:", even_numbers)


# =====================================================================
# SECTION 25: REMOVE DUPLICATES FROM STRINGS
# =====================================================================

# Sets can remove duplicate characters.
#
# IMPORTANT:
# Converting a set back into a string
# does not preserve the original character order.

print("\n" + "=" * 65)
print("SECTION 25: UNIQUE CHARACTERS")
print("=" * 65)

word = "programming"

unique_characters = set(word)

print("Original word:", word)

print("Unique characters:", unique_characters)

print("Number of unique characters:", len(unique_characters))


# =====================================================================
# SECTION 26: FIND COMMON ELEMENTS IN LISTS
# =====================================================================

# Convert lists into sets.
#
# Then use intersection to find common elements.

print("\n" + "=" * 65)
print("SECTION 26: COMMON ELEMENTS")
print("=" * 65)

list_1 = [10, 20, 30, 40, 50]

list_2 = [30, 40, 50, 60, 70]

common = set(list_1) & set(list_2)

print("First list:", list_1)

print("Second list:", list_2)

print("Common elements:", common)


# =====================================================================
# SECTION 27: FIND UNIQUE ELEMENTS
# =====================================================================

# Symmetric difference finds values
# that occur in one collection but not both.

print("\n" + "=" * 65)
print("SECTION 27: UNIQUE ELEMENTS")
print("=" * 65)

A = {10, 20, 30, 40}

B = {30, 40, 50, 60}

unique = A ^ B

print("Unique elements:", unique)


# =====================================================================
# SECTION 28: REMOVE DUPLICATES WHILE PRESERVING ORDER
# =====================================================================

# A normal set does not preserve the original
# sequence order.
#
# dict.fromkeys() removes duplicates
# while preserving insertion order.

print("\n" + "=" * 65)
print("SECTION 28: PRESERVE ORIGINAL ORDER")
print("=" * 65)

numbers = [10, 20, 10, 30, 20, 40, 50]

unique_numbers = list(dict.fromkeys(numbers))

print("Original list:", numbers)

print("Unique ordered list:", unique_numbers)


# =====================================================================
# SECTION 29: SET OPERATIONS IN STATISTICS
# =====================================================================

# Example:
#
# Students enrolled in Mathematics and Python.
#
# We can find:
# 1. Students taking at least one subject.
# 2. Students taking both subjects.
# 3. Students taking only Mathematics.
# 4. Students taking only Python.

print("\n" + "=" * 65)
print("SECTION 29: STATISTICAL SET ANALYSIS")
print("=" * 65)

mathematics_students = {

    "Ali",

    "Ahmed",

    "John",

    "David"

}

python_students = {

    "Ali",

    "John",

    "Michael",

    "Sarah"

}

all_students = mathematics_students | python_students

both_subjects = mathematics_students & python_students

only_mathematics = mathematics_students - python_students

only_python = python_students - mathematics_students

print("All students:", all_students)

print("Both subjects:", both_subjects)

print("Only Mathematics:", only_mathematics)

print("Only Python:", only_python)

print("Total unique students:", len(all_students))


# =====================================================================
# SECTION 30: SETS IN ARTIFICIAL INTELLIGENCE
# =====================================================================

# Sets can help process unique labels,
# categories and feature names.
#
# Example:
# A dataset containing repeated class labels.

print("\n" + "=" * 65)
print("SECTION 30: AI - UNIQUE CLASS LABELS")
print("=" * 65)

class_labels = [

    "Cat",

    "Dog",

    "Cat",

    "Bird",

    "Dog",

    "Cat",

    "Fish"

]

unique_labels = set(class_labels)

print("Original labels:", class_labels)

print("Unique labels:", unique_labels)

print("Number of classes:", len(unique_labels))


# =====================================================================
# SECTION 31: AI - FEATURE SELECTION
# =====================================================================

# Sets can compare feature names
# from two different feature groups.
#
# This is a simplified data-processing example.

print("\n" + "=" * 65)
print("SECTION 31: AI - FEATURE ANALYSIS")
print("=" * 65)

dataset_A_features = {

    "age",

    "height",

    "weight",

    "income"

}

dataset_B_features = {

    "age",

    "weight",

    "education",

    "experience"

}

common_features = dataset_A_features & dataset_B_features

all_features = dataset_A_features | dataset_B_features

unique_features = dataset_A_features ^ dataset_B_features

print("Common features:", common_features)

print("All features:", all_features)

print("Unique features:", unique_features)


# =====================================================================
# SECTION 32: SET TIME COMPLEXITY
# =====================================================================

# Sets are commonly implemented using hash tables.
#
# Typical average-case complexities:
#
# Add: O(1)
# Remove: O(1)
# Discard: O(1)
# Membership: O(1)
# Union: O(n + m)
# Intersection: O(min(n, m)) in common cases
# Difference: O(n) in common cases
# Iteration: O(n)
#
# Worst-case behavior can be slower,
# particularly when hash collisions occur.

print("\n" + "=" * 65)
print("SECTION 32: SET TIME COMPLEXITY")
print("=" * 65)

complexities = {

    "Add": "O(1) average",

    "Remove": "O(1) average",

    "Discard": "O(1) average",

    "Membership": "O(1) average",

    "Union": "O(n + m)",

    "Intersection": "O(min(n, m)) typical",

    "Difference": "O(n) typical",

    "Iteration": "O(n)"

}

for operation, complexity in complexities.items():

    print(operation, ":", complexity)


# =====================================================================
# SECTION 33: PRACTICAL MINI PROJECT
# =====================================================================

# Find unique words in a sentence.
#
# This demonstrates a simple text-processing task.

print("\n" + "=" * 65)
print("SECTION 33: UNIQUE WORD ANALYSIS")
print("=" * 65)

sentence = "python is useful and python is powerful"

words = sentence.lower().split()

unique_words = set(words)

print("Sentence:", sentence)

print("All words:", words)

print("Unique words:", unique_words)

print("Total words:", len(words))

print("Unique words count:", len(unique_words))


# =====================================================================
# FINAL REVISION
# =====================================================================

print("\n" + "=" * 65)

print("DAY 017 - PYTHON SETS")

print("=" * 65)

topics = [

    "Introduction to Sets",

    "Creating Sets",

    "Removing Duplicates",

    "List to Set Conversion",

    "add() Method",

    "update() Method",

    "remove() Method",

    "discard() Method",

    "pop() Method",

    "clear() Method",

    "Membership Operators",

    "Set Length",

    "Set Iteration",

    "Union",

    "Intersection",

    "Difference",

    "Symmetric Difference",

    "Subsets",

    "Proper Subsets",

    "Supersets",

    "Disjoint Sets",

    "Frozen Sets",

    "Set Comprehensions",

    "Conditional Comprehensions",

    "Unique Characters",

    "Common Elements",

    "Unique Elements",

    "Preserving Original Order",

    "Statistical Set Analysis",

    "AI Class Labels",

    "AI Feature Analysis",

    "Time Complexity",

    "Unique Word Analysis"

]

for index, topic in enumerate(topics, start=1):

    print(f"{index}. {topic} - Covered")


print("\nDAY 017 SETS LESSON COMPLETED!")

print("KEEP PRACTISING!")

print("=" * 65)


# =====================================================================
# END OF DAY 017 - SETS.PY
# =====================================================================
