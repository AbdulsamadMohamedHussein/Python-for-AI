
# =====================================================================
# DAY 015 - PYTHON LISTS
#
# Bachelor's in Artificial Intelligence
# 90-Day Python Programming Journey
#
# MAIN TOPIC: PYTHON LISTS
#
# LEARNING OBJECTIVES:
# 1. Understand Python lists.
# 2. Create and access lists.
# 3. Understand indexing and slicing.
# 4. Modify list elements.
# 5. Add and remove elements.
# 6. Use important list methods.
# 7. Sort and reverse lists.
# 8. Iterate through lists.
# 9. Understand nested lists.
# 10. Learn list comprehensions.
# 11. Perform basic data analysis.
# 12. Understand lists in Artificial Intelligence.
#
# =====================================================================


# =====================================================================
# SECTION 1: INTRODUCTION TO LISTS
# =====================================================================

# A list is a collection of multiple elements
# stored inside one variable.
#
# Lists are:
#
# 1. Ordered.
# 2. Mutable (changeable).
# 3. Able to contain duplicate values.
# 4. Able to contain different data types.
#
# Lists are created using square brackets [].

print("\n" + "=" * 70)

print("SECTION 1: INTRODUCTION TO LISTS")

print("=" * 70)


# Creating a list of numbers.

numbers = [10, 20, 30, 40, 50]

print("Numbers:", numbers)


# Creating a list of names.

names = ["Ali", "Ahmed", "John", "David"]

print("Names:", names)


# Creating a list of strings.

fruits = ["Apple", "Banana", "Mango"]

print("Fruits:", fruits)


# Creating a list with different data types.

mixed_list = [10, "Python", 3.14, True]

print("Mixed list:", mixed_list)


# Creating an empty list.

empty_list = []

print("Empty list:", empty_list)


# =====================================================================
# SECTION 2: ACCESSING LIST ELEMENTS
# =====================================================================

# Every element in a list has an index.
#
# Python indexing starts from ZERO.
#
# Example:
#
# numbers = [10, 20, 30, 40, 50]
#
# Index:       0   1   2   3   4
# Elements:   10  20  30  40  50
#
# We use the index to access individual elements.

print("\n" + "=" * 70)

print("SECTION 2: LIST INDEXING")

print("=" * 70)


numbers = [10, 20, 30, 40, 50]

print("First element:", numbers[0])

print("Second element:", numbers[1])

print("Third element:", numbers[2])

print("Last element:", numbers[4])


# Negative indexing starts from the end.
#
# -1 means the last element.
# -2 means the second-last element.
# -3 means the third-last element.

print("Last element using negative index:", numbers[-1])

print("Second-last element:", numbers[-2])

print("Third-last element:", numbers[-3])


# =====================================================================
# SECTION 3: LIST LENGTH
# =====================================================================

# The len() function returns the number
# of elements inside a list.
#
# Syntax:
#
# len(list_name)

print("\n" + "=" * 70)

print("SECTION 3: LIST LENGTH")

print("=" * 70)


students = ["Ali", "Ahmed", "John", "David", "Michael"]

total_students = len(students)

print("Students:", students)

print("Total students:", total_students)


# The last valid index is always:
#
# len(list) - 1

print("Last valid index:", len(students) - 1)


# =====================================================================
# SECTION 4: LIST SLICING
# =====================================================================

# Slicing extracts a portion of a list.
#
# Syntax:
#
# list_name[start:stop:step]
#
# START:
# The index where extraction begins.
#
# STOP:
# The index where extraction ends.
# The stop index is excluded.
#
# STEP:
# The number of positions to move.

print("\n" + "=" * 70)

print("SECTION 4: LIST SLICING")

print("=" * 70)


numbers = [10, 20, 30, 40, 50, 60, 70]

print("Original list:", numbers)

# Extract elements from index 1 to 3.

print("Slice 1:4:", numbers[1:4])

# Extract the first three elements.

print("First three:", numbers[:3])

# Extract elements from index 3 to the end.

print("From index 3:", numbers[3:])

# Extract the complete list.

print("Complete list:", numbers[:])

# Extract every second element.

print("Step of 2:", numbers[::2])

# Reverse a list using slicing.

print("Reversed list:", numbers[::-1])


# =====================================================================
# SECTION 5: MODIFYING LIST ELEMENTS
# =====================================================================

# Lists are mutable.
#
# Mutable means that we can change
# their elements after creating them.
#
# We use the index to update a value.

print("\n" + "=" * 70)

print("SECTION 5: MODIFYING LISTS")

print("=" * 70)


colors = ["Red", "Blue", "Green", "Yellow"]

print("Original colors:", colors)


# Change the element at index 1.

colors[1] = "Purple"

print("After modification:", colors)


# Change the last element.

colors[-1] = "Black"

print("After second modification:", colors)


# Modify multiple elements using slicing.

colors[0:2] = ["White", "Orange"]

print("After slice modification:", colors)


# =====================================================================
# SECTION 6: APPEND METHOD
# =====================================================================

# append() adds ONE element
# to the end of a list.
#
# Syntax:
#
# list_name.append(element)

print("\n" + "=" * 70)

print("SECTION 6: APPEND METHOD")

print("=" * 70)


fruits = ["Apple", "Banana"]

print("Before append:", fruits)


# Add Mango to the end.

fruits.append("Mango")

print("After append:", fruits)


# Add another fruit.

fruits.append("Orange")

print("After second append:", fruits)


# =====================================================================
# SECTION 7: INSERT METHOD
# =====================================================================

# insert() adds an element
# at a specified index.
#
# Syntax:
#
# list_name.insert(index, element)

print("\n" + "=" * 70)

print("SECTION 7: INSERT METHOD")

print("=" * 70)


fruits = ["Apple", "Banana", "Mango"]

print("Original list:", fruits)


# Insert Orange at index 1.

fruits.insert(1, "Orange")

print("After insertion:", fruits)


# Insert Grapes at index 0.

fruits.insert(0, "Grapes")

print("After second insertion:", fruits)


# =====================================================================
# SECTION 8: EXTEND METHOD
# =====================================================================

# extend() adds multiple elements
# from another iterable to the end of a list.
#
# Unlike append(), extend() adds elements
# individually rather than adding the iterable
# as one nested element.

print("\n" + "=" * 70)

print("SECTION 8: EXTEND METHOD")

print("=" * 70)


list_one = [1, 2, 3]

list_two = [4, 5, 6]

print("First list:", list_one)

print("Second list:", list_two)


# Add all elements from list_two.

list_one.extend(list_two)

print("Combined list:", list_one)


# =====================================================================
# SECTION 9: REMOVE METHOD
# =====================================================================

# remove() removes the FIRST occurrence
# of a specified value.
#
# Syntax:
#
# list_name.remove(value)

print("\n" + "=" * 70)

print("SECTION 9: REMOVE METHOD")

print("=" * 70)


fruits = ["Apple", "Banana", "Mango", "Orange"]

print("Before removal:", fruits)


# Remove Banana.

fruits.remove("Banana")

print("After removing Banana:", fruits)


# =====================================================================
# SECTION 10: POP METHOD
# =====================================================================

# pop() removes an element using its index.
#
# If no index is supplied,
# it removes the last element.
#
# It also RETURNS the removed element.

print("\n" + "=" * 70)

print("SECTION 10: POP METHOD")

print("=" * 70)


numbers = [10, 20, 30, 40, 50]

print("Original list:", numbers)


# Remove the last element.

removed_value = numbers.pop()

print("Removed value:", removed_value)

print("Updated list:", numbers)


# Remove element at index 1.

removed_value = numbers.pop(1)

print("Second removed value:", removed_value)

print("Final list:", numbers)


# =====================================================================
# SECTION 11: DEL STATEMENT
# =====================================================================

# del removes an element or a portion
# of a list using its index or slice.

print("\n" + "=" * 70)

print("SECTION 11: DEL STATEMENT")

print("=" * 70)


numbers = [10, 20, 30, 40, 50]

print("Original list:", numbers)


# Delete the element at index 2.

del numbers[2]

print("After deleting index 2:", numbers)


# Delete the first two elements.

del numbers[:2]

print("After deleting first two:", numbers)


# =====================================================================
# SECTION 12: CLEAR METHOD
# =====================================================================

# clear() removes every element
# from the list.
#
# The list still exists, but becomes empty.

print("\n" + "=" * 70)

print("SECTION 12: CLEAR METHOD")

print("=" * 70)


numbers = [10, 20, 30, 40]

print("Before clear:", numbers)


numbers.clear()

print("After clear:", numbers)


# =====================================================================
# SECTION 13: COUNT METHOD
# =====================================================================

# count() returns how many times
# a particular value appears in a list.

print("\n" + "=" * 70)

print("SECTION 13: COUNT METHOD")

print("=" * 70)


numbers = [10, 20, 10, 30, 10, 40, 50]

print("Numbers:", numbers)


count_ten = numbers.count(10)

print("Number of times 10 appears:", count_ten)


# =====================================================================
# SECTION 14: INDEX METHOD
# =====================================================================

# index() returns the index of the FIRST occurrence
# of a specified element.
#
# It raises ValueError if the value is not found.

print("\n" + "=" * 70)

print("SECTION 14: INDEX METHOD")

print("=" * 70)


fruits = ["Apple", "Banana", "Mango", "Orange"]

print("Fruits:", fruits)


position = fruits.index("Mango")

print("Mango index:", position)


# =====================================================================
# SECTION 15: SORT METHOD
# =====================================================================

# sort() arranges list elements in ascending order
# by default.
#
# It modifies the original list.

print("\n" + "=" * 70)

print("SECTION 15: SORT METHOD")

print("=" * 70)


numbers = [50, 10, 40, 20, 30]

print("Before sorting:", numbers)


numbers.sort()

print("Ascending order:", numbers)


# Sort in descending order.

numbers.sort(reverse=True)

print("Descending order:", numbers)


# =====================================================================
# SECTION 16: SORTED FUNCTION
# =====================================================================

# sorted() creates and returns a NEW sorted list.
#
# The original list remains unchanged.

print("\n" + "=" * 70)

print("SECTION 16: SORTED FUNCTION")

print("=" * 70)


numbers = [50, 10, 40, 20, 30]

print("Original list:", numbers)


sorted_numbers = sorted(numbers)

print("New sorted list:", sorted_numbers)

print("Original remains unchanged:", numbers)


# =====================================================================
# SECTION 17: REVERSE METHOD
# =====================================================================

# reverse() reverses the current order
# of elements in the original list.
#
# It does not sort the list.

print("\n" + "=" * 70)

print("SECTION 17: REVERSE METHOD")

print("=" * 70)


numbers = [10, 20, 30, 40, 50]

print("Before reverse:", numbers)


numbers.reverse()

print("After reverse:", numbers)


# =====================================================================
# SECTION 18: COPYING LISTS
# =====================================================================

# copy() creates a shallow copy of a list.
#
# A shallow copy creates a new outer list,
# but nested mutable objects are still shared.
#
# This example uses a simple list of integers.

print("\n" + "=" * 70)

print("SECTION 18: COPYING LISTS")

print("=" * 70)


original = [10, 20, 30]

copied = original.copy()

print("Original:", original)

print("Copied:", copied)


# Modify the copied list.

copied.append(40)

print("Updated copied list:", copied)

print("Original list:", original)


# =====================================================================
# SECTION 19: LIST MEMBERSHIP
# =====================================================================

# The in operator checks whether
# an element exists inside a list.
#
# It returns True or False.

print("\n" + "=" * 70)

print("SECTION 19: MEMBERSHIP OPERATORS")

print("=" * 70)


fruits = ["Apple", "Banana", "Mango"]

print("Is Apple present?", "Apple" in fruits)

print("Is Orange present?", "Orange" in fruits)


# The not in operator checks whether
# an element does NOT exist.

print("Is Orange absent?", "Orange" not in fruits)


# =====================================================================
# SECTION 20: ITERATING THROUGH A LIST
# =====================================================================

# A for loop can process every element
# inside a list.
#
# This is one of the most common ways
# to work with lists.

print("\n" + "=" * 70)

print("SECTION 20: FOR LOOP WITH LISTS")

print("=" * 70)


students = ["Ali", "Ahmed", "John", "David"]

for student in students:

    print("Student:", student)


# =====================================================================
# SECTION 21: WHILE LOOP WITH LISTS
# =====================================================================

# We can also access list elements
# using a while loop and their indexes.
#
# Python indexes begin at zero.
#
# len() returns the total number of elements.

print("\n" + "=" * 70)

print("SECTION 21: WHILE LOOP WITH LISTS")

print("=" * 70)


numbers = [10, 20, 30, 40, 50]

index = 0

while index < len(numbers):

    print("Element:", numbers[index])

    index += 1


# =====================================================================
# SECTION 22: SUM, MINIMUM AND MAXIMUM
# =====================================================================

# Python provides useful built-in functions
# for numerical lists.
#
# sum() calculates the total.
# min() returns the smallest element.
# max() returns the largest element.

print("\n" + "=" * 70)

print("SECTION 22: BASIC LIST STATISTICS")

print("=" * 70)


numbers = [10, 20, 30, 40, 50]

print("Numbers:", numbers)

print("Total:", sum(numbers))

print("Minimum:", min(numbers))

print("Maximum:", max(numbers))

print("Length:", len(numbers))


# =====================================================================
# SECTION 23: CALCULATING THE MEAN
# =====================================================================

# The arithmetic mean is calculated by:
#
# Mean = Sum of values / Number of values
#
# Formula:
#
# x_bar = (x1 + x2 + ... + xn) / n

print("\n" + "=" * 70)

print("SECTION 23: CALCULATING THE MEAN")

print("=" * 70)


scores = [70, 80, 90, 85, 75]

total = sum(scores)

number_of_scores = len(scores)

mean = total / number_of_scores

print("Scores:", scores)

print("Total:", total)

print("Mean:", mean)


# =====================================================================
# SECTION 24: FINDING EVEN AND ODD NUMBERS
# =====================================================================

# The modulo operator % calculates a remainder.
#
# Even numbers have remainder 0 after division by 2.
#
# Odd numbers have remainder 1 after division by 2.

print("\n" + "=" * 70)

print("SECTION 24: EVEN AND ODD NUMBERS")

print("=" * 70)


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

even_numbers = []

odd_numbers = []


for number in numbers:

    if number % 2 == 0:

        even_numbers.append(number)

    else:

        odd_numbers.append(number)


print("Original numbers:", numbers)

print("Even numbers:", even_numbers)

print("Odd numbers:", odd_numbers)


# =====================================================================
# SECTION 25: FILTERING NUMBERS
# =====================================================================

# Filtering means selecting elements
# that satisfy a particular condition.
#
# Here we select numbers greater than 50.

print("\n" + "=" * 70)

print("SECTION 25: FILTERING NUMBERS")

print("=" * 70)


numbers = [10, 25, 55, 70, 35, 90, 45, 100]

large_numbers = []


for number in numbers:

    if number > 50:

        large_numbers.append(number)


print("Original list:", numbers)

print("Numbers greater than 50:", large_numbers)


# =====================================================================
# SECTION 26: NESTED LISTS
# =====================================================================

# A nested list is a list that contains
# other lists as its elements.
#
# Nested lists can represent tables,
# matrices and structured data.

print("\n" + "=" * 70)

print("SECTION 26: NESTED LISTS")

print("=" * 70)


matrix = [

    [1, 2, 3],

    [4, 5, 6],

    [7, 8, 9]

]


print("Matrix:", matrix)


# Access the first row.

print("First row:", matrix[0])


# Access the second element of the first row.

print("Element:", matrix[0][1])


# Access the third row, third column.

print("Last element:", matrix[2][2])


# =====================================================================
# SECTION 27: ITERATING THROUGH A NESTED LIST
# =====================================================================

# Nested loops allow us to process
# every element in a nested list.

print("\n" + "=" * 70)

print("SECTION 27: NESTED LIST ITERATION")

print("=" * 70)


matrix = [

    [1, 2, 3],

    [4, 5, 6],

    [7, 8, 9]

]


for row in matrix:

    for element in row:

        print(element, end=" ")

    print()


# =====================================================================
# SECTION 28: LIST COMPREHENSIONS
# =====================================================================

# List comprehensions provide a concise way
# to create lists.
#
# General syntax:
#
# [expression for item in iterable]
#
# They can replace certain simple loops.

print("\n" + "=" * 70)

print("SECTION 28: LIST COMPREHENSIONS")

print("=" * 70)


# Create a list of squares.

squares = [number ** 2 for number in range(1, 11)]

print("Squares:", squares)


# Create a list of even numbers.

even_numbers = [

    number

    for number in range(1, 21)

    if number % 2 == 0

]

print("Even numbers:", even_numbers)


# =====================================================================
# SECTION 29: LIST COMPREHENSION WITH CONDITIONS
# =====================================================================

# We can combine conditions with list comprehensions.
#
# This example selects numbers greater than 50.

print("\n" + "=" * 70)

print("SECTION 29: CONDITIONAL LIST COMPREHENSION")

print("=" * 70)


numbers = [10, 20, 55, 70, 35, 90, 45, 100]


large_numbers = [

    number

    for number in numbers

    if number > 50

]


print("Original numbers:", numbers)

print("Filtered numbers:", large_numbers)


# =====================================================================
# SECTION 30: LIST UNPACKING
# =====================================================================

# List unpacking assigns list elements
# to separate variables.
#
# The number of variables must match
# the number of elements unless starred
# unpacking is used.

print("\n" + "=" * 70)

print("SECTION 30: LIST UNPACKING")

print("=" * 70)


coordinates = [10, 20, 30]

x, y, z = coordinates

print("X:", x)

print("Y:", y)

print("Z:", z)


# Starred unpacking collects remaining elements.

numbers = [10, 20, 30, 40, 50]

first, *middle, last = numbers

print("First:", first)

print("Middle:", middle)

print("Last:", last)


# =====================================================================
# SECTION 31: LIST CONCATENATION
# =====================================================================

# The + operator combines two lists.
#
# It creates a new list.

print("\n" + "=" * 70)

print("SECTION 31: LIST CONCATENATION")

print("=" * 70)


list_one = [1, 2, 3]

list_two = [4, 5, 6]

combined = list_one + list_two

print("First list:", list_one)

print("Second list:", list_two)

print("Combined list:", combined)


# =====================================================================
# SECTION 32: LIST REPETITION
# =====================================================================

# The * operator repeats list elements.
#
# Example:
#
# [0] * 5
#
# Creates five zero values.

print("\n" + "=" * 70)

print("SECTION 32: LIST REPETITION")

print("=" * 70)


zeros = [0] * 5

print("Zeros:", zeros)


stars = ["*"] * 5

print("Stars:", stars)


# =====================================================================
# SECTION 33: AVOIDING COMMON LIST COPYING ERRORS
# =====================================================================

# Assigning one list variable to another
# does NOT create an independent copy.
#
# Both variables refer to the same list.

print("\n" + "=" * 70)

print("SECTION 33: LIST REFERENCES")

print("=" * 70)


original = [10, 20, 30]

reference = original

reference.append(40)

print("Original:", original)

print("Reference:", reference)


# To create a separate shallow copy,
# use copy() or slicing.

original = [10, 20, 30]

separate_copy = original[:]

separate_copy.append(40)

print("Original:", original)

print("Separate copy:", separate_copy)


# =====================================================================
# SECTION 34: BASIC DATASET PROCESSING
# =====================================================================

# Lists can store numerical observations.
#
# Here we calculate basic statistics
# from a small dataset.

print("\n" + "=" * 70)

print("SECTION 34: DATASET PROCESSING")

print("=" * 70)


dataset = [12, 15, 18, 20, 25, 30, 35, 40]


# Calculate the total.

total = sum(dataset)


# Calculate the number of observations.

count = len(dataset)


# Calculate the mean.

mean = total / count


# Find the smallest observation.

minimum = min(dataset)


# Find the largest observation.

maximum = max(dataset)


print("Dataset:", dataset)

print("Total:", total)

print("Observations:", count)

print("Mean:", mean)

print("Minimum:", minimum)

print("Maximum:", maximum)


# =====================================================================
# SECTION 35: CONNECTION TO ARTIFICIAL INTELLIGENCE
# =====================================================================

# AI systems process collections of data.
#
# Lists help us understand how data
# can be stored and processed.
#
# This is a conceptual example.
#
# Later we will learn NumPy arrays,
# which are better suited to large-scale
# numerical computation.

print("\n" + "=" * 70)

print("SECTION 35: AI DATA REPRESENTATION")

print("=" * 70)


# Example: Student performance dataset.

student_scores = [85, 90, 78, 92, 88]


# Example: Numerical features.

features = [1.5, 2.3, 4.1, 3.7]


# Example: Model predictions.

predictions = [0.85, 0.72, 0.91, 0.66]


# Example: Actual labels.

actual_labels = [1, 0, 1, 1]


print("Student scores:", student_scores)

print("Features:", features)

print("Predictions:", predictions)

print("Actual labels:", actual_labels)


# =====================================================================
# SECTION 36: CALCULATING MEAN ABSOLUTE ERROR
# =====================================================================

# Mean Absolute Error (MAE) measures
# the average absolute difference between
# actual and predicted numerical values.
#
# Formula:
#
# MAE = (1/n) * SUM(|actual - predicted|)
#
# This is an introductory Machine Learning
# evaluation metric.

print("\n" + "=" * 70)

print("SECTION 36: MEAN ABSOLUTE ERROR")

print("=" * 70)


actual = [100, 200, 300, 400]

predicted = [90, 210, 280, 390]


absolute_errors = []


for index in range(len(actual)):

    error = abs(actual[index] - predicted[index])

    absolute_errors.append(error)


mae = sum(absolute_errors) / len(absolute_errors)


print("Actual values:", actual)

print("Predicted values:", predicted)

print("Absolute errors:", absolute_errors)

print("Mean Absolute Error:", mae)


# =====================================================================
# SECTION 37: LIST PERFORMANCE AND TIME COMPLEXITY
# =====================================================================

# Time complexity describes how the amount
# of work grows as the input size increases.
#
# Common list operation complexities:
#
# Indexing: O(1)
# Append: O(1) amortized
# Inserting at the beginning: O(n)
# Searching: O(n)
# Removing by value: O(n)
# Sorting: O(n log n)
#
# These are typical average or amortized
# complexities for Python lists.

print("\n" + "=" * 70)

print("SECTION 37: LIST COMPLEXITY")

print("=" * 70)


complexities = [

    "Indexing: O(1)",

    "Append: O(1) amortized",

    "Insertion at beginning: O(n)",

    "Searching: O(n)",

    "Removing by value: O(n)",

    "Sorting: O(n log n)"

]


for operation in complexities:

    print(operation)


# =====================================================================
# SECTION 38: FINAL REVISION
# =====================================================================

# Display all important list methods.

print("\n" + "=" * 70)

print("SECTION 38: PYTHON LIST METHODS")

print("=" * 70)


methods = [

    "append() - Adds one element",

    "insert() - Adds at a specific index",

    "extend() - Adds multiple elements",

    "remove() - Removes the first matching value",

    "pop() - Removes and returns an element",

    "clear() - Removes all elements",

    "index() - Finds the first matching index",

    "count() - Counts occurrences",

    "sort() - Sorts the original list",

    "reverse() - Reverses the original list",

    "copy() - Creates a shallow copy"

]


for method in methods:

    print(method)


# =====================================================================
# FINAL LEARNING SUMMARY
# =====================================================================

print("\n" + "=" * 70)

print("DAY 015 - PYTHON LISTS")

print("=" * 70)


topics = [

    "Introduction to Lists",

    "Creating Lists",

    "Positive Indexing",

    "Negative Indexing",

    "List Length",

    "List Slicing",

    "Modifying Elements",

    "append()",

    "insert()",

    "extend()",

    "remove()",

    "pop()",

    "del Statement",

    "clear()",

    "count()",

    "index()",

    "sort()",

    "sorted()",

    "reverse()",

    "copy()",

    "Membership Operators",

    "For Loops with Lists",

    "While Loops with Lists",

    "Basic List Statistics",

    "Even and Odd Filtering",

    "Nested Lists",

    "List Comprehensions",

    "List Unpacking",

    "List Concatenation",

    "List Repetition",

    "List References",

    "Dataset Processing",

    "AI Data Representation",

    "Mean Absolute Error",

    "Time Complexity"

]


index = 0

while index < len(topics):

    print(index + 1, topics[index], "- Covered")

    index += 1


print("\nDAY 015 MAIN LESSON COMPLETED!")

print("=" * 70)


# =====================================================================
# END OF DAY 015 - LISTS.PY
# =====================================================================
