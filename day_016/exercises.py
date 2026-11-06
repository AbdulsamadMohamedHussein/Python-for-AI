
# =====================================================================
# DAY 016 - PYTHON TUPLES
# 30 FULLY SOLVED EXERCISES
#
# Bachelor's in Artificial Intelligence
# Python for AI - 90-Day Journey
#
# =====================================================================


# =====================================================================
# EXERCISE 1: CREATE A TUPLE
# =====================================================================

# QUESTION:
# Create a tuple containing five fruits.

print("\nEXERCISE 1: CREATE A TUPLE")

fruits = ("Apple", "Banana", "Mango", "Orange", "Grapes")

print("Fruits:", fruits)


# =====================================================================
# EXERCISE 2: CREATE A TUPLE OF NUMBERS
# =====================================================================

# QUESTION:
# Create a tuple containing ten numbers.

print("\nEXERCISE 2: NUMERICAL TUPLE")

numbers = (10, 20, 30, 40, 50, 60, 70, 80, 90, 100)

print("Numbers:", numbers)

print("Total elements:", len(numbers))


# =====================================================================
# EXERCISE 3: CREATE A MIXED TUPLE
# =====================================================================

# QUESTION:
# Create a tuple containing different data types.

print("\nEXERCISE 3: MIXED DATA TYPES")

mixed = ("Python", 25, 3.14, True)

print("Mixed tuple:", mixed)


# =====================================================================
# EXERCISE 4: CREATE AN EMPTY TUPLE
# =====================================================================

# QUESTION:
# Create an empty tuple.

print("\nEXERCISE 4: EMPTY TUPLE")

empty_tuple = ()

print("Empty tuple:", empty_tuple)

print("Length:", len(empty_tuple))


# =====================================================================
# EXERCISE 5: CREATE A SINGLE-ELEMENT TUPLE
# =====================================================================

# QUESTION:
# Create a tuple containing only one element.
#
# IMPORTANT:
# A comma is necessary to create a single-element tuple.

print("\nEXERCISE 5: SINGLE-ELEMENT TUPLE")

single = ("Python",)

print("Single tuple:", single)

print("Data type:", type(single))


# =====================================================================
# EXERCISE 6: ACCESS THE FIRST ELEMENT
# =====================================================================

# QUESTION:
# Access the first element using indexing.
#
# Python indexing starts from ZERO.

print("\nEXERCISE 6: FIRST ELEMENT")

numbers = (10, 20, 30, 40, 50)

print("First element:", numbers[0])


# =====================================================================
# EXERCISE 7: ACCESS THE LAST ELEMENT
# =====================================================================

# QUESTION:
# Access the last element using negative indexing.
#
# -1 represents the last element.

print("\nEXERCISE 7: LAST ELEMENT")

fruits = ("Apple", "Banana", "Mango", "Orange")

print("Last fruit:", fruits[-1])


# =====================================================================
# EXERCISE 8: ACCESS THE SECOND-LAST ELEMENT
# =====================================================================

# QUESTION:
# Access the second-last element.

print("\nEXERCISE 8: SECOND-LAST ELEMENT")

numbers = (10, 20, 30, 40, 50)

print("Second-last:", numbers[-2])


# =====================================================================
# EXERCISE 9: EXTRACT THE FIRST THREE ELEMENTS
# =====================================================================

# QUESTION:
# Extract the first three elements using slicing.
#
# The stop index is excluded.

print("\nEXERCISE 9: TUPLE SLICING")

numbers = (10, 20, 30, 40, 50, 60)

first_three = numbers[:3]

print("Original:", numbers)

print("First three:", first_three)


# =====================================================================
# EXERCISE 10: REVERSE A TUPLE
# =====================================================================

# QUESTION:
# Reverse a tuple using slicing.
#
# [::-1] traverses the sequence backwards.

print("\nEXERCISE 10: REVERSE TUPLE")

numbers = (1, 2, 3, 4, 5)

reversed_tuple = numbers[::-1]

print("Original:", numbers)

print("Reversed:", reversed_tuple)


# =====================================================================
# EXERCISE 11: FIND THE LENGTH OF A TUPLE
# =====================================================================

# QUESTION:
# Find the number of elements in a tuple.
#
# len() returns the total number of elements.

print("\nEXERCISE 11: TUPLE LENGTH")

animals = ("Cat", "Dog", "Lion", "Tiger", "Elephant")

print("Animals:", animals)

print("Total animals:", len(animals))


# =====================================================================
# EXERCISE 12: COUNT DUPLICATE VALUES
# =====================================================================

# QUESTION:
# Count how many times a number appears.
#
# count() returns the occurrence count.

print("\nEXERCISE 12: COUNT METHOD")

numbers = (10, 20, 10, 30, 10, 40, 10)

print("Tuple:", numbers)

print("Occurrences of 10:", numbers.count(10))


# =====================================================================
# EXERCISE 13: FIND THE INDEX OF AN ELEMENT
# =====================================================================

# QUESTION:
# Find the position of Mango.
#
# index() returns the first matching position.

print("\nEXERCISE 13: INDEX METHOD")

fruits = ("Apple", "Banana", "Mango", "Orange")

position = fruits.index("Mango")

print("Fruits:", fruits)

print("Mango index:", position)


# =====================================================================
# EXERCISE 14: CHECK WHETHER AN ELEMENT EXISTS
# =====================================================================

# QUESTION:
# Check whether Python exists in a tuple.
#
# The in operator returns True or False.

print("\nEXERCISE 14: MEMBERSHIP OPERATOR")

languages = ("Python", "Java", "C++", "JavaScript")

print("Python exists:", "Python" in languages)

print("PHP exists:", "PHP" in languages)


# =====================================================================
# EXERCISE 15: FIND MINIMUM AND MAXIMUM
# =====================================================================

# QUESTION:
# Find the smallest and largest numbers.

print("\nEXERCISE 15: MINIMUM AND MAXIMUM")

numbers = (45, 12, 89, 23, 100, 67)

print("Numbers:", numbers)

print("Minimum:", min(numbers))

print("Maximum:", max(numbers))


# =====================================================================
# EXERCISE 16: CALCULATE THE SUM
# =====================================================================

# QUESTION:
# Calculate the sum of all numerical elements.
#
# sum() adds all elements.

print("\nEXERCISE 16: SUM OF ELEMENTS")

numbers = (10, 20, 30, 40, 50)

total = sum(numbers)

print("Numbers:", numbers)

print("Total:", total)


# =====================================================================
# EXERCISE 17: CALCULATE THE AVERAGE
# =====================================================================

# QUESTION:
# Calculate the arithmetic mean.
#
# Mean = Sum of observations / Number of observations.

print("\nEXERCISE 17: ARITHMETIC MEAN")

scores = (70, 80, 90, 85, 75)

total = sum(scores)

count = len(scores)

average = total / count

print("Scores:", scores)

print("Total:", total)

print("Average:", average)


# =====================================================================
# EXERCISE 18: CONCATENATE TWO TUPLES
# =====================================================================

# QUESTION:
# Combine two tuples using +.
#
# Concatenation creates a new tuple.

print("\nEXERCISE 18: TUPLE CONCATENATION")

first = (1, 2, 3)

second = (4, 5, 6)

combined = first + second

print("First:", first)

print("Second:", second)

print("Combined:", combined)


# =====================================================================
# EXERCISE 19: REPEAT A TUPLE
# =====================================================================

# QUESTION:
# Repeat a tuple three times.
#
# The * operator repeats sequence elements.

print("\nEXERCISE 19: TUPLE REPETITION")

numbers = (1, 2, 3)

repeated = numbers * 3

print("Original:", numbers)

print("Repeated:", repeated)


# =====================================================================
# EXERCISE 20: TUPLE UNPACKING
# =====================================================================

# QUESTION:
# Assign tuple elements to separate variables.
#
# The number of variables must match
# the number of elements.

print("\nEXERCISE 20: TUPLE UNPACKING")

coordinates = (10, 20, 30)

x, y, z = coordinates

print("X:", x)

print("Y:", y)

print("Z:", z)


# =====================================================================
# EXERCISE 21: STARRED UNPACKING
# =====================================================================

# QUESTION:
# Extract the first, middle and last elements.
#
# The * operator collects remaining elements
# into a list.

print("\nEXERCISE 21: STARRED UNPACKING")

numbers = (10, 20, 30, 40, 50)

first, *middle, last = numbers

print("First:", first)

print("Middle:", middle)

print("Last:", last)


# =====================================================================
# EXERCISE 22: NESTED TUPLES
# =====================================================================

# QUESTION:
# Create a tuple containing other tuples.
#
# Nested tuples can represent structured data.

print("\nEXERCISE 22: NESTED TUPLES")

students = (

    ("Ali", 20, 90),

    ("Ahmed", 22, 85),

    ("John", 21, 95)

)

print("Student records:", students)

print("First student:", students[0])

print("First student's name:", students[0][0])

print("John's grade:", students[2][2])


# =====================================================================
# EXERCISE 23: LOOP THROUGH A TUPLE
# =====================================================================

# QUESTION:
# Display every element using a for loop.

print("\nEXERCISE 23: TUPLE ITERATION")

fruits = ("Apple", "Banana", "Mango", "Orange")

for fruit in fruits:

    print("Fruit:", fruit)


# =====================================================================
# EXERCISE 24: ENUMERATE A TUPLE
# =====================================================================

# QUESTION:
# Display each element with its index.
#
# enumerate() provides index and value.

print("\nEXERCISE 24: ENUMERATE")

students = ("Ali", "Ahmed", "John", "David")

for index, student in enumerate(students):

    print("Index:", index, "Student:", student)


# =====================================================================
# EXERCISE 25: SORT A TUPLE
# =====================================================================

# QUESTION:
# Sort tuple elements in ascending order.
#
# sorted() returns a LIST, not a tuple.
#
# We use tuple() to convert the result back.

print("\nEXERCISE 25: SORTING TUPLES")

numbers = (50, 10, 40, 20, 30)

sorted_list = sorted(numbers)

sorted_tuple = tuple(sorted_list)

print("Original tuple:", numbers)

print("Sorted list:", sorted_list)

print("Sorted tuple:", sorted_tuple)


# =====================================================================
# EXERCISE 26: SEPARATE EVEN AND ODD NUMBERS
# =====================================================================

# QUESTION:
# Separate even and odd values from a tuple.
#
# Even numbers have remainder zero
# when divided by two.

print("\nEXERCISE 26: EVEN AND ODD NUMBERS")

numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

even_numbers = []

odd_numbers = []

for number in numbers:

    if number % 2 == 0:

        even_numbers.append(number)

    else:

        odd_numbers.append(number)

# Convert the resulting lists into tuples.

even_tuple = tuple(even_numbers)

odd_tuple = tuple(odd_numbers)

print("Original:", numbers)

print("Even numbers:", even_tuple)

print("Odd numbers:", odd_tuple)


# =====================================================================
# EXERCISE 27: FIND THE MEDIAN
# =====================================================================

# QUESTION:
# Calculate the median of a numerical tuple.
#
# Median is the middle value after sorting.
#
# For even-sized datasets, take the average
# of the two middle values.

print("\nEXERCISE 27: MEDIAN")

data = (10, 50, 30, 20, 40, 60)

sorted_data = sorted(data)

count = len(sorted_data)

middle = count // 2

if count % 2 == 1:

    median = sorted_data[middle]

else:

    median = (
        sorted_data[middle - 1]
        + sorted_data[middle]
    ) / 2

print("Original:", data)

print("Sorted:", sorted_data)

print("Median:", median)


# =====================================================================
# EXERCISE 28: CALCULATE POPULATION VARIANCE
# =====================================================================

# QUESTION:
# Calculate the population variance.
#
# Formula:
#
# sigma^2 = SUM((x - mean)^2) / n

print("\nEXERCISE 28: POPULATION VARIANCE")

data = (10, 20, 30, 40, 50)

mean = sum(data) / len(data)

squared_differences = []

for value in data:

    difference = value - mean

    squared_difference = difference ** 2

    squared_differences.append(squared_difference)

variance = sum(squared_differences) / len(data)

print("Dataset:", data)

print("Mean:", mean)

print("Squared differences:", squared_differences)

print("Population variance:", variance)


# =====================================================================
# EXERCISE 29: CALCULATE STANDARD DEVIATION
# =====================================================================

# QUESTION:
# Calculate population standard deviation.
#
# Formula:
#
# sigma = sqrt(variance)
#
# In Python, ** 0.5 calculates the square root.

print("\nEXERCISE 29: STANDARD DEVIATION")

data = (10, 20, 30, 40, 50)

mean = sum(data) / len(data)

variance = sum(
    (value - mean) ** 2 for value in data
) / len(data)

standard_deviation = variance ** 0.5

print("Dataset:", data)

print("Mean:", mean)

print("Variance:", variance)

print("Standard deviation:", standard_deviation)


# =====================================================================
# EXERCISE 30: TUPLES IN ARTIFICIAL INTELLIGENCE
# =====================================================================

# QUESTION:
# Represent a small machine learning dataset
# using tuples.
#
# Each observation contains:
#
# (feature_1, feature_2, actual_label)
#
# This is an introductory representation.
# Real ML pipelines usually use NumPy arrays
# or other specialized data structures.

print("\nEXERCISE 30: AI DATA REPRESENTATION")

dataset = (

    (1.5, 2.3, 1),

    (2.1, 3.4, 0),

    (3.2, 4.5, 1),

    (4.1, 5.2, 1),

    (5.3, 6.1, 0)

)

print("Machine learning dataset:")

for observation in dataset:

    print(observation)


# Extract feature values.

features = tuple(
    (observation[0], observation[1])
    for observation in dataset
)

# Extract actual labels.

labels = tuple(
    observation[2]
    for observation in dataset
)

print("Features:", features)

print("Labels:", labels)

print("Total observations:", len(dataset))


# =====================================================================
# FINAL EXERCISE SUMMARY
# =====================================================================

exercise_names = [

    "Create a Tuple",

    "Numerical Tuple",

    "Mixed Data Types",

    "Empty Tuple",

    "Single-Element Tuple",

    "First Element",

    "Last Element",

    "Second-Last Element",

    "Tuple Slicing",

    "Reverse Tuple",

    "Tuple Length",

    "Count Method",

    "Index Method",

    "Membership Operator",

    "Minimum and Maximum",

    "Sum of Elements",

    "Arithmetic Mean",

    "Tuple Concatenation",

    "Tuple Repetition",

    "Tuple Unpacking",

    "Starred Unpacking",

    "Nested Tuples",

    "Tuple Iteration",

    "Enumerate",

    "Tuple Sorting",

    "Even and Odd Numbers",

    "Median",

    "Population Variance",

    "Standard Deviation",

    "AI Data Representation"

]

print("\n" + "=" * 65)

print("DAY 016 - EXERCISE SUMMARY")

print("=" * 65)

for index, exercise in enumerate(exercise_names, start=1):

    print(index, exercise, "- COMPLETED")

print("\nALL 30 EXERCISES COMPLETED!")

print("=" * 65)


# =====================================================================
# END OF DAY 016 - EXERCISES.PY
# =====================================================================
