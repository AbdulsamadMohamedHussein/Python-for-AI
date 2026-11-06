
# =====================================================================
# DAY 015 - PYTHON LISTS
# 30 FULLY SOLVED EXERCISES
#
# Bachelor's in Artificial Intelligence
# 90-Day Python Programming Journey
#
# TOPICS:
# 1. Creating lists
# 2. Accessing list elements
# 3. Positive and negative indexing
# 4. List slicing
# 5. Modifying lists
# 6. append()
# 7. insert()
# 8. extend()
# 9. remove()
# 10. pop()
# 11. Sorting
# 12. Reversing
# 13. Searching
# 14. List iteration
# 15. Nested lists
# 16. List comprehensions
# 17. Statistical calculations
# 18. Dataset processing
# 19. Machine Learning concepts
#
# =====================================================================


# =====================================================================
# EXERCISE 1: CREATE A LIST
# =====================================================================

# QUESTION:
# Create a list containing five different fruits.
#
# EXPLANATION:
# Lists store multiple elements inside one variable.
# We create lists using square brackets [].

print("\n" + "=" * 65)
print("EXERCISE 1: CREATE A LIST")
print("=" * 65)

fruits = ["Apple", "Banana", "Mango", "Orange", "Grapes"]

print("Fruits:", fruits)


# =====================================================================
# EXERCISE 2: CREATE A LIST OF NUMBERS
# =====================================================================

# QUESTION:
# Create a list containing ten numbers.
#
# EXPLANATION:
# Lists can store integers.
# These values can later be used for mathematical calculations.

print("\n" + "=" * 65)
print("EXERCISE 2: LIST OF NUMBERS")
print("=" * 65)

numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

print("Numbers:", numbers)

print("Total elements:", len(numbers))


# =====================================================================
# EXERCISE 3: CREATE A MIXED DATA TYPE LIST
# =====================================================================

# QUESTION:
# Create a list containing different data types.
#
# EXPLANATION:
# Python lists can contain integers, strings,
# floating-point numbers and Boolean values.

print("\n" + "=" * 65)
print("EXERCISE 3: MIXED DATA TYPES")
print("=" * 65)

mixed_list = [25, "Python", 3.14, True, "AI"]

print("Mixed list:", mixed_list)


# =====================================================================
# EXERCISE 4: ACCESS THE FIRST ELEMENT
# =====================================================================

# QUESTION:
# Access the first element of a list.
#
# EXPLANATION:
# Python indexing starts at ZERO.
#
# The first element is at index 0.

print("\n" + "=" * 65)
print("EXERCISE 4: FIRST ELEMENT")
print("=" * 65)

colors = ["Red", "Blue", "Green", "Yellow"]

first_color = colors[0]

print("First color:", first_color)


# =====================================================================
# EXERCISE 5: ACCESS THE LAST ELEMENT
# =====================================================================

# QUESTION:
# Access the last element using negative indexing.
#
# EXPLANATION:
# Negative indexing starts from the end.
#
# -1 means the last element.
# -2 means the second-last element.

print("\n" + "=" * 65)
print("EXERCISE 5: LAST ELEMENT")
print("=" * 65)

animals = ["Cat", "Dog", "Lion", "Tiger", "Elephant"]

last_animal = animals[-1]

print("Last animal:", last_animal)


# =====================================================================
# EXERCISE 6: ACCESS MULTIPLE ELEMENTS USING SLICING
# =====================================================================

# QUESTION:
# Extract the first three elements from a list.
#
# EXPLANATION:
# Slicing uses:
#
# list[start:stop]
#
# The stop index is excluded.

print("\n" + "=" * 65)
print("EXERCISE 6: LIST SLICING")
print("=" * 65)

numbers = [10, 20, 30, 40, 50, 60]

first_three = numbers[:3]

print("Original list:", numbers)

print("First three elements:", first_three)


# =====================================================================
# EXERCISE 7: REVERSE A LIST USING SLICING
# =====================================================================

# QUESTION:
# Reverse a list using slicing.
#
# EXPLANATION:
# The slicing expression [::-1]
# traverses the list backwards.
#
# It creates a new reversed list.

print("\n" + "=" * 65)
print("EXERCISE 7: REVERSE USING SLICING")
print("=" * 65)

numbers = [1, 2, 3, 4, 5]

reversed_numbers = numbers[::-1]

print("Original:", numbers)

print("Reversed:", reversed_numbers)


# =====================================================================
# EXERCISE 8: MODIFY A LIST ELEMENT
# =====================================================================

# QUESTION:
# Change the second element of a list.
#
# EXPLANATION:
# Lists are mutable.
#
# Mutable means their values can be changed
# after the list has been created.

print("\n" + "=" * 65)
print("EXERCISE 8: MODIFY LIST ELEMENT")
print("=" * 65)

colors = ["Red", "Blue", "Green"]

print("Before:", colors)

colors[1] = "Purple"

print("After:", colors)


# =====================================================================
# EXERCISE 9: ADD AN ELEMENT USING APPEND
# =====================================================================

# QUESTION:
# Add a new element to the end of a list.
#
# EXPLANATION:
# append() adds one element to the end.

print("\n" + "=" * 65)
print("EXERCISE 9: APPEND METHOD")
print("=" * 65)

fruits = ["Apple", "Banana", "Mango"]

print("Before:", fruits)

fruits.append("Orange")

print("After:", fruits)


# =====================================================================
# EXERCISE 10: INSERT AN ELEMENT
# =====================================================================

# QUESTION:
# Insert an element at a specific position.
#
# EXPLANATION:
# insert(index, value) adds an element
# at the specified index.
#
# Existing elements shift to the right.

print("\n" + "=" * 65)
print("EXERCISE 10: INSERT METHOD")
print("=" * 65)

students = ["Ali", "Ahmed", "John"]

print("Before:", students)

students.insert(1, "David")

print("After:", students)


# =====================================================================
# EXERCISE 11: EXTEND A LIST
# =====================================================================

# QUESTION:
# Combine two lists using extend().
#
# EXPLANATION:
# extend() adds every element from another iterable.
#
# Unlike append(), it does not add the entire
# second list as one nested element.

print("\n" + "=" * 65)
print("EXERCISE 11: EXTEND METHOD")
print("=" * 65)

list_one = [1, 2, 3]

list_two = [4, 5, 6]

print("First list:", list_one)

print("Second list:", list_two)

list_one.extend(list_two)

print("Combined list:", list_one)


# =====================================================================
# EXERCISE 12: REMOVE AN ELEMENT
# =====================================================================

# QUESTION:
# Remove a particular value from a list.
#
# EXPLANATION:
# remove() deletes the first occurrence
# of the specified value.
#
# It raises ValueError if the value is absent.

print("\n" + "=" * 65)
print("EXERCISE 12: REMOVE METHOD")
print("=" * 65)

fruits = ["Apple", "Banana", "Mango", "Orange"]

print("Before:", fruits)

fruits.remove("Banana")

print("After:", fruits)


# =====================================================================
# EXERCISE 13: REMOVE AN ELEMENT USING POP
# =====================================================================

# QUESTION:
# Remove an element using its index.
#
# EXPLANATION:
# pop(index) removes and returns an element.
#
# If no index is provided, it removes the last element.

print("\n" + "=" * 65)
print("EXERCISE 13: POP METHOD")
print("=" * 65)

numbers = [10, 20, 30, 40, 50]

print("Before:", numbers)

removed_element = numbers.pop(2)

print("Removed element:", removed_element)

print("After:", numbers)


# =====================================================================
# EXERCISE 14: SORT A LIST
# =====================================================================

# QUESTION:
# Sort a list in ascending and descending order.
#
# EXPLANATION:
# sort() modifies the original list.
#
# reverse=True sorts in descending order.

print("\n" + "=" * 65)
print("EXERCISE 14: SORT METHOD")
print("=" * 65)

numbers = [50, 10, 40, 20, 30]

print("Original:", numbers)

numbers.sort()

print("Ascending:", numbers)

numbers.sort(reverse=True)

print("Descending:", numbers)


# =====================================================================
# EXERCISE 15: COUNT DUPLICATE ELEMENTS
# =====================================================================

# QUESTION:
# Count how many times a value appears.
#
# EXPLANATION:
# count(value) returns the number
# of occurrences of that value.

print("\n" + "=" * 65)
print("EXERCISE 15: COUNT METHOD")
print("=" * 65)

numbers = [10, 20, 10, 30, 10, 40, 10]

total_tens = numbers.count(10)

print("Numbers:", numbers)

print("Number of occurrences of 10:", total_tens)


# =====================================================================
# EXERCISE 16: FIND THE INDEX OF AN ELEMENT
# =====================================================================

# QUESTION:
# Find the index of a specific element.
#
# EXPLANATION:
# index(value) returns the position
# of the first matching element.

print("\n" + "=" * 65)
print("EXERCISE 16: INDEX METHOD")
print("=" * 65)

fruits = ["Apple", "Banana", "Mango", "Orange"]

position = fruits.index("Mango")

print("Fruits:", fruits)

print("Mango position:", position)


# =====================================================================
# EXERCISE 17: FIND EVEN AND ODD NUMBERS
# =====================================================================

# QUESTION:
# Separate even and odd numbers into different lists.
#
# EXPLANATION:
# A number is even if:
#
# number % 2 == 0
#
# Otherwise, it is odd.

print("\n" + "=" * 65)
print("EXERCISE 17: EVEN AND ODD NUMBERS")
print("=" * 65)

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

even_numbers = []

odd_numbers = []

for number in numbers:

    if number % 2 == 0:

        even_numbers.append(number)

    else:

        odd_numbers.append(number)

print("Original:", numbers)

print("Even numbers:", even_numbers)

print("Odd numbers:", odd_numbers)


# =====================================================================
# EXERCISE 18: FIND THE SUM OF ALL ELEMENTS
# =====================================================================

# QUESTION:
# Calculate the sum of all numbers in a list.
#
# EXPLANATION:
# sum() adds all numerical elements.
#
# We can also calculate the sum manually
# using an accumulator.

print("\n" + "=" * 65)
print("EXERCISE 18: SUM OF ELEMENTS")
print("=" * 65)

numbers = [10, 20, 30, 40, 50]

total = 0

for number in numbers:

    total += number

print("Numbers:", numbers)

print("Total:", total)

# Verify using the built-in sum() function.

print("Built-in sum:", sum(numbers))


# =====================================================================
# EXERCISE 19: FIND THE LARGEST NUMBER
# =====================================================================

# QUESTION:
# Find the largest number without using max().
#
# EXPLANATION:
# Start by assuming the first element is largest.
#
# Compare every remaining element with it.
#
# Update largest whenever a greater value is found.

print("\n" + "=" * 65)
print("EXERCISE 19: FIND LARGEST NUMBER")
print("=" * 65)

numbers = [45, 12, 89, 23, 100, 67]

largest = numbers[0]

for number in numbers:

    if number > largest:

        largest = number

print("Numbers:", numbers)

print("Largest number:", largest)


# =====================================================================
# EXERCISE 20: FIND THE SMALLEST NUMBER
# =====================================================================

# QUESTION:
# Find the smallest number without using min().
#
# EXPLANATION:
# Start by assuming the first element is smallest.
#
# Compare every element and update
# the smallest value when necessary.

print("\n" + "=" * 65)
print("EXERCISE 20: FIND SMALLEST NUMBER")
print("=" * 65)

numbers = [45, 12, 89, 23, 100, 67]

smallest = numbers[0]

for number in numbers:

    if number < smallest:

        smallest = number

print("Numbers:", numbers)

print("Smallest number:", smallest)


# =====================================================================
# EXERCISE 21: CREATE A LIST USING A LOOP
# =====================================================================

# QUESTION:
# Create a list containing squares of numbers
# from 1 to 10.
#
# EXPLANATION:
# A square is calculated by multiplying
# a number by itself.
#
# Formula:
#
# n^2 = n * n
#
# append() adds each calculated square.

print("\n" + "=" * 65)
print("EXERCISE 21: LIST OF SQUARES")
print("=" * 65)

squares = []

for number in range(1, 11):

    square = number ** 2

    squares.append(square)

print("Squares:", squares)


# =====================================================================
# EXERCISE 22: USE LIST COMPREHENSION
# =====================================================================

# QUESTION:
# Generate even numbers between 1 and 20.
#
# EXPLANATION:
# List comprehension creates a new list
# using a concise expression.
#
# General syntax:
#
# [expression for item in iterable if condition]

print("\n" + "=" * 65)
print("EXERCISE 22: LIST COMPREHENSION")
print("=" * 65)

even_numbers = [

    number

    for number in range(1, 21)

    if number % 2 == 0

]

print("Even numbers:", even_numbers)


# =====================================================================
# EXERCISE 23: CREATE A NESTED LIST
# =====================================================================

# QUESTION:
# Create a 3 x 3 matrix using nested lists.
#
# EXPLANATION:
# A nested list contains other lists.
#
# Each inner list represents one row.

print("\n" + "=" * 65)
print("EXERCISE 23: NESTED LIST")
print("=" * 65)

matrix = [

    [1, 2, 3],

    [4, 5, 6],

    [7, 8, 9]

]

print("Matrix:", matrix)

# Access a particular element.
#
# matrix[1][2]:
#
# First index 1 selects the second row.
# Second index 2 selects the third element.

print("Element at row 2, column 3:", matrix[1][2])


# =====================================================================
# EXERCISE 24: CALCULATE THE SUM OF A MATRIX
# =====================================================================

# QUESTION:
# Calculate the sum of every element
# in a nested list.
#
# EXPLANATION:
# We use two loops.
#
# The outer loop accesses each row.
# The inner loop accesses each element.

print("\n" + "=" * 65)
print("EXERCISE 24: MATRIX SUM")
print("=" * 65)

matrix = [

    [1, 2, 3],

    [4, 5, 6],

    [7, 8, 9]

]

total = 0

for row in matrix:

    for number in row:

        total += number

print("Matrix:", matrix)

print("Total matrix sum:", total)


# =====================================================================
# EXERCISE 25: FILTER NUMBERS GREATER THAN 50
# =====================================================================

# QUESTION:
# Create a new list containing only
# numbers greater than 50.
#
# EXPLANATION:
# Filtering selects elements that satisfy
# a particular condition.

print("\n" + "=" * 65)
print("EXERCISE 25: FILTERING")
print("=" * 65)

numbers = [10, 25, 55, 70, 35, 90, 45, 100]

filtered_numbers = []

for number in numbers:

    if number > 50:

        filtered_numbers.append(number)

print("Original list:", numbers)

print("Filtered list:", filtered_numbers)


# =====================================================================
# EXERCISE 26: CALCULATE THE MEAN
# =====================================================================

# QUESTION:
# Calculate the arithmetic mean of a dataset.
#
# EXPLANATION:
#
# Mean = Sum of observations / Number of observations
#
# Mathematical formula:
#
# x_bar = (x1 + x2 + ... + xn) / n

print("\n" + "=" * 65)
print("EXERCISE 26: ARITHMETIC MEAN")
print("=" * 65)

dataset = [10, 20, 30, 40, 50]

total = sum(dataset)

count = len(dataset)

mean = total / count

print("Dataset:", dataset)

print("Total:", total)

print("Count:", count)

print("Mean:", mean)


# =====================================================================
# EXERCISE 27: CALCULATE THE MEDIAN
# =====================================================================

# QUESTION:
# Calculate the median of a numerical dataset.
#
# EXPLANATION:
# The median is the middle value
# after sorting the dataset.
#
# For an odd number of observations,
# the median is the middle element.
#
# For an even number of observations,
# the median is the mean of the two middle elements.

print("\n" + "=" * 65)
print("EXERCISE 27: MEDIAN")
print("=" * 65)

dataset = [10, 50, 30, 20, 40]

sorted_dataset = sorted(dataset)

count = len(sorted_dataset)

middle = count // 2

if count % 2 == 1:

    median = sorted_dataset[middle]

else:

    median = (

        sorted_dataset[middle - 1]

        + sorted_dataset[middle]

    ) / 2

print("Original dataset:", dataset)

print("Sorted dataset:", sorted_dataset)

print("Median:", median)


# =====================================================================
# EXERCISE 28: CALCULATE THE VARIANCE
# =====================================================================

# QUESTION:
# Calculate the population variance.
#
# EXPLANATION:
# Variance measures the average squared
# distance from the mean.
#
# Population variance formula:
#
# sigma^2 = SUM((x - mean)^2) / n
#
# We calculate squared differences
# and then find their average.

print("\n" + "=" * 65)
print("EXERCISE 28: POPULATION VARIANCE")
print("=" * 65)

dataset = [10, 20, 30, 40, 50]

mean = sum(dataset) / len(dataset)

squared_differences = []

for value in dataset:

    difference = value - mean

    squared_difference = difference ** 2

    squared_differences.append(squared_difference)

variance = sum(squared_differences) / len(dataset)

print("Dataset:", dataset)

print("Mean:", mean)

print("Squared differences:", squared_differences)

print("Population variance:", variance)


# =====================================================================
# EXERCISE 29: CALCULATE MEAN ABSOLUTE ERROR
# =====================================================================

# QUESTION:
# Calculate Mean Absolute Error (MAE)
# using actual and predicted values.
#
# EXPLANATION:
# MAE measures the average absolute difference
# between actual and predicted numerical values.
#
# Formula:
#
# MAE = SUM(|actual - predicted|) / n
#
# This is an important introductory
# Machine Learning evaluation metric.

print("\n" + "=" * 65)
print("EXERCISE 29: MEAN ABSOLUTE ERROR")
print("=" * 65)

actual = [100, 200, 300, 400]

predicted = [90, 210, 280, 390]

absolute_errors = []

for index in range(len(actual)):

    error = abs(actual[index] - predicted[index])

    absolute_errors.append(error)

mae = sum(absolute_errors) / len(actual)

print("Actual values:", actual)

print("Predicted values:", predicted)

print("Absolute errors:", absolute_errors)

print("Mean Absolute Error:", mae)


# =====================================================================
# EXERCISE 30: COMPLETE DATASET ANALYSIS
# =====================================================================

# QUESTION:
# Build a basic numerical dataset analysis program.
#
# Calculate:
#
# 1. Total observations.
# 2. Sum.
# 3. Mean.
# 4. Median.
# 5. Minimum.
# 6. Maximum.
# 7. Even values.
# 8. Odd values.
# 9. Population variance.
# 10. Population standard deviation.
#
# EXPLANATION:
# This combines Python lists with
# fundamental descriptive statistics.
#
# IMPORTANT:
# We calculate population variance and
# population standard deviation here.

print("\n" + "=" * 65)
print("EXERCISE 30: COMPLETE DATASET ANALYSIS")
print("=" * 65)


# Our sample numerical dataset.

dataset = [12, 15, 18, 20, 25, 30, 35, 40, 45, 50]


# -------------------------------------------------------------
# STEP 1: COUNT OBSERVATIONS
# -------------------------------------------------------------

# len() returns the number of elements.

count = len(dataset)


# -------------------------------------------------------------
# STEP 2: CALCULATE TOTAL
# -------------------------------------------------------------

# sum() adds every observation.

total = sum(dataset)


# -------------------------------------------------------------
# STEP 3: CALCULATE MEAN
# -------------------------------------------------------------

# Mean = Total / Number of observations.

mean = total / count


# -------------------------------------------------------------
# STEP 4: SORT DATASET
# -------------------------------------------------------------

# Sorting helps us calculate the median.

sorted_dataset = sorted(dataset)


# -------------------------------------------------------------
# STEP 5: CALCULATE MEDIAN
# -------------------------------------------------------------

middle = count // 2

if count % 2 == 1:

    median = sorted_dataset[middle]

else:

    median = (

        sorted_dataset[middle - 1]

        + sorted_dataset[middle]

    ) / 2


# -------------------------------------------------------------
# STEP 6: FIND MINIMUM AND MAXIMUM
# -------------------------------------------------------------

minimum = min(dataset)

maximum = max(dataset)


# -------------------------------------------------------------
# STEP 7: SEPARATE EVEN AND ODD VALUES
# -------------------------------------------------------------

even_numbers = []

odd_numbers = []

for number in dataset:

    if number % 2 == 0:

        even_numbers.append(number)

    else:

        odd_numbers.append(number)


# -------------------------------------------------------------
# STEP 8: CALCULATE POPULATION VARIANCE
# -------------------------------------------------------------

# Population variance:
#
# sigma^2 = SUM((x - mean)^2) / n

squared_differences = []

for number in dataset:

    difference = number - mean

    squared_difference = difference ** 2

    squared_differences.append(squared_difference)

variance = sum(squared_differences) / count


# -------------------------------------------------------------
# STEP 9: CALCULATE POPULATION STANDARD DEVIATION
# -------------------------------------------------------------

# Standard deviation is the square root
# of population variance.

standard_deviation = variance ** 0.5


# -------------------------------------------------------------
# STEP 10: DISPLAY FINAL REPORT
# -------------------------------------------------------------

print("\nDATASET ANALYSIS REPORT")

print("-" * 45)

print("Original dataset:", dataset)

print("Sorted dataset:", sorted_dataset)

print("Total observations:", count)

print("Sum:", total)

print("Mean:", round(mean, 2))

print("Median:", median)

print("Minimum:", minimum)

print("Maximum:", maximum)

print("Even numbers:", even_numbers)

print("Odd numbers:", odd_numbers)

print("Population variance:", round(variance, 2))

print("Population standard deviation:",
      round(standard_deviation, 2))

print("-" * 45)


# =====================================================================
# FINAL EXERCISE SUMMARY
# =====================================================================

exercise_names = [

    "Create a List",

    "List of Numbers",

    "Mixed Data Types",

    "Access First Element",

    "Access Last Element",

    "List Slicing",

    "Reverse Using Slicing",

    "Modify List Element",

    "Append Method",

    "Insert Method",

    "Extend Method",

    "Remove Method",

    "Pop Method",

    "Sort Method",

    "Count Method",

    "Index Method",

    "Even and Odd Numbers",

    "Sum of Elements",

    "Find Largest Number",

    "Find Smallest Number",

    "List of Squares",

    "List Comprehension",

    "Nested Lists",

    "Matrix Sum",

    "Filtering",

    "Arithmetic Mean",

    "Median",

    "Population Variance",

    "Mean Absolute Error",

    "Complete Dataset Analysis"

]

print("\n" + "=" * 65)

print("DAY 015 - EXERCISE SUMMARY")

print("=" * 65)

for index, exercise in enumerate(exercise_names, start=1):

    print(index, exercise, "- COMPLETED")

print("\nALL 30 EXERCISES COMPLETED!")

print("=" * 65)


# =====================================================================
# END OF DAY 015 - EXERCISES.PY
# =====================================================================
