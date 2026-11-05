
# =====================================================================
# DAY 012 - PYTHON FOR LOOPS
#
# Bachelor's in Artificial Intelligence
# 90-Day Python Programming Journey
#
# MAIN TOPIC: ITERATION AND FOR LOOPS
#
# LEARNING OBJECTIVES:
# 1. Understand loops and iteration.
# 2. Understand for loop syntax.
# 3. Use the range() function.
# 4. Iterate through strings.
# 5. Iterate through lists and tuples.
# 6. Iterate through dictionaries and sets.
# 7. Understand nested for loops.
# 8. Use break and continue.
# 9. Use the else clause with loops.
# 10. Apply loops to mathematical problems.
# 11. Understand the applications of loops in AI.
#
# =====================================================================


# =====================================================================
# SECTION 1: INTRODUCTION TO LOOPS
# =====================================================================

# A loop repeats a block of code.
#
# Instead of writing the same instruction repeatedly,
# we can use a loop to execute it multiple times.
#
# Example:
#
# print("Hello")
# print("Hello")
# print("Hello")
#
# A loop makes this process easier.


print("\n" + "=" * 70)
print("SECTION 1: INTRODUCTION TO LOOPS")
print("=" * 70)


for number in range(1, 6):

    # The loop executes this statement five times.

    print("Hello Python!")

print("Loop completed.")


# =====================================================================
# SECTION 2: BASIC FOR LOOP
# =====================================================================

# The for loop processes each item in a sequence.
#
# The variable 'number' receives a new value
# during every iteration.
#
# Iteration means one complete execution of a loop.


print("\n" + "=" * 70)
print("SECTION 2: BASIC FOR LOOP")
print("=" * 70)


for number in range(1, 6):

    print(number)


# =====================================================================
# SECTION 3: UNDERSTANDING range()
# =====================================================================

# range() generates a sequence of integers.
#
# Syntax:
#
# range(start, stop, step)
#
# start = Starting value.
# stop  = Ending boundary, excluded.
# step  = Amount by which the value increases.
#
# The stop value is NOT included.


print("\n" + "=" * 70)
print("SECTION 3: UNDERSTANDING RANGE")
print("=" * 70)


# Example 1:
# Start at 0 and stop before 5.

for number in range(5):

    print(number)


# Example 2:
# Start at 1 and stop before 6.

for number in range(1, 6):

    print(number)


# Example 3:
# Start at 2 and increase by 2.

for number in range(2, 11, 2):

    print(number)


# Example 4:
# Count backwards from 5 to 1.

for number in range(5, 0, -1):

    print(number)


# =====================================================================
# SECTION 4: USING A FOR LOOP WITH STRINGS
# =====================================================================

# Strings are sequences of characters.
#
# A for loop can process each character individually.
#
# Example:
#
# word = "PYTHON"
#
# The loop processes P, Y, T, H, O and N.


print("\n" + "=" * 70)
print("SECTION 4: FOR LOOP WITH STRINGS")
print("=" * 70)


word = "PYTHON"

for character in word:

    print(character)


# =====================================================================
# SECTION 5: COUNTING CHARACTERS
# =====================================================================

# We can use a loop to count specific characters.
#
# Here we count the number of vowels.
#
# A vowel is one of:
# a, e, i, o, u
#
# We use a variable to keep track of the count.


print("\n" + "=" * 70)
print("SECTION 5: COUNTING VOWELS")
print("=" * 70)


word = "artificial intelligence"

vowel_count = 0

for character in word:

    if character in "aeiou":

        # Increase the counter by one.

        vowel_count += 1


print("Word:", word)

print("Number of vowels:", vowel_count)


# =====================================================================
# SECTION 6: FOR LOOP WITH LISTS
# =====================================================================

# A list stores multiple items.
#
# A for loop allows us to process each item.
#
# Lists are extremely important in Python.


print("\n" + "=" * 70)
print("SECTION 6: FOR LOOP WITH LISTS")
print("=" * 70)


subjects = [

    "Mathematics",

    "Python",

    "Statistics",

    "Machine Learning",

    "Computer Vision"

]


for subject in subjects:

    print("Subject:", subject)


# =====================================================================
# SECTION 7: CALCULATING THE SUM OF LIST ELEMENTS
# =====================================================================

# We can calculate the sum manually using a loop.
#
# total starts at zero.
#
# Each number is added to total.
#
# This technique is called accumulation.


print("\n" + "=" * 70)
print("SECTION 7: SUM OF LIST ELEMENTS")
print("=" * 70)


numbers = [10, 20, 30, 40, 50]

total = 0

for number in numbers:

    total = total + number

    # Equivalent shorter form:
    # total += number


print("Numbers:", numbers)

print("Total:", total)


# =====================================================================
# SECTION 8: CALCULATING AVERAGE
# =====================================================================

# Average = Sum of values / Number of values.
#
# We use a loop to calculate the total.
# len() determines how many elements exist.


print("\n" + "=" * 70)
print("SECTION 8: CALCULATING AVERAGE")
print("=" * 70)


marks = [80, 90, 75, 85, 95]

total = 0

for mark in marks:

    total += mark


average = total / len(marks)


print("Marks:", marks)

print("Total:", total)

print("Average:", average)


# =====================================================================
# SECTION 9: FOR LOOP WITH TUPLES
# =====================================================================

# A tuple stores multiple items.
#
# Unlike lists, tuples cannot be modified after creation.
#
# We can still iterate through them using a for loop.


print("\n" + "=" * 70)
print("SECTION 9: FOR LOOP WITH TUPLES")
print("=" * 70)


coordinates = (10, 20, 30, 40)


for coordinate in coordinates:

    print("Coordinate:", coordinate)


# =====================================================================
# SECTION 10: FOR LOOP WITH SETS
# =====================================================================

# A set stores unique elements.
#
# Sets do not guarantee a particular iteration order.
#
# A for loop can process every element in a set.


print("\n" + "=" * 70)
print("SECTION 10: FOR LOOP WITH SETS")
print("=" * 70)


unique_numbers = {10, 20, 30, 40, 50}


for number in unique_numbers:

    print(number)


# =====================================================================
# SECTION 11: FOR LOOP WITH DICTIONARIES
# =====================================================================

# Dictionaries contain key-value pairs.
#
# We can iterate through:
#
# 1. Keys.
# 2. Values.
# 3. Both keys and values.


print("\n" + "=" * 70)
print("SECTION 11: FOR LOOP WITH DICTIONARIES")
print("=" * 70)


student = {

    "name": "Ali",

    "age": 22,

    "course": "Artificial Intelligence",

    "marks": 90

}


# Iterate through dictionary keys.

for key in student:

    print("Key:", key)


# Iterate through dictionary values.

for value in student.values():

    print("Value:", value)


# Iterate through both keys and values.

for key, value in student.items():

    print(key, ":", value)


# =====================================================================
# SECTION 12: USING enumerate()
# =====================================================================

# enumerate() provides both:
#
# 1. Index position.
# 2. Current element.
#
# This is useful when we need the position
# of an element while iterating.


print("\n" + "=" * 70)
print("SECTION 12: ENUMERATE")
print("=" * 70)


subjects = [

    "Mathematics",

    "Python",

    "Statistics",

    "Machine Learning"

]


for index, subject in enumerate(subjects):

    print(index, subject)


# We can start counting from 1 instead of 0.

for index, subject in enumerate(subjects, start=1):

    print(index, subject)


# =====================================================================
# SECTION 13: USING break
# =====================================================================

# break immediately terminates the nearest loop.
#
# Python stops processing further iterations.
#
# Example:
# Stop counting when the number reaches 5.


print("\n" + "=" * 70)
print("SECTION 13: BREAK STATEMENT")
print("=" * 70)


for number in range(1, 11):

    if number == 5:

        print("Stopping the loop.")

        break

    print(number)


# =====================================================================
# SECTION 14: USING continue
# =====================================================================

# continue skips the current iteration.
#
# The loop then moves to the next item.
#
# Example:
# Skip the number 5.


print("\n" + "=" * 70)
print("SECTION 14: CONTINUE STATEMENT")
print("=" * 70)


for number in range(1, 11):

    if number == 5:

        continue

    print(number)


# =====================================================================
# SECTION 15: USING ELSE WITH A FOR LOOP
# =====================================================================

# Python allows an else block after a for loop.
#
# The else block executes when the loop finishes
# normally without being terminated by break.


print("\n" + "=" * 70)
print("SECTION 15: ELSE WITH FOR LOOP")
print("=" * 70)


for number in range(1, 6):

    print(number)

else:

    print("Loop completed normally.")


# =====================================================================
# SECTION 16: NESTED FOR LOOPS
# =====================================================================

# A nested loop is a loop inside another loop.
#
# The inner loop completes all its iterations
# for each iteration of the outer loop.


print("\n" + "=" * 70)
print("SECTION 16: NESTED FOR LOOPS")
print("=" * 70)


for outer in range(1, 4):

    print("Outer loop:", outer)

    for inner in range(1, 4):

        print("   Inner loop:", inner)


# =====================================================================
# SECTION 17: MULTIPLICATION TABLE
# =====================================================================

# Nested loops are useful for generating tables.
#
# The outer loop chooses the number.
# The inner loop multiplies it by 1 through 10.


print("\n" + "=" * 70)
print("SECTION 17: MULTIPLICATION TABLE")
print("=" * 70)


for number in range(1, 6):

    print("\nMultiplication table:", number)

    for multiplier in range(1, 11):

        result = number * multiplier

        print(number, "x", multiplier, "=", result)


# =====================================================================
# SECTION 18: MATHEMATICAL SUMMATION
# =====================================================================

# Calculate the sum of numbers from 1 to 100.
#
# Mathematical notation:
#
# 1 + 2 + 3 + ... + 100
#
# We use a loop to add every number.


print("\n" + "=" * 70)
print("SECTION 18: SUMMATION")
print("=" * 70)


total = 0

for number in range(1, 101):

    total += number


print("Sum from 1 to 100:", total)


# =====================================================================
# SECTION 19: FACTORIAL CALCULATION
# =====================================================================

# Factorial is the product of all positive integers
# from 1 up to a given number.
#
# Example:
#
# 5! = 5 x 4 x 3 x 2 x 1
#
# Result = 120


print("\n" + "=" * 70)
print("SECTION 19: FACTORIAL")
print("=" * 70)


number = 5

factorial = 1

for value in range(1, number + 1):

    factorial *= value


print("Number:", number)

print("Factorial:", factorial)


# =====================================================================
# SECTION 20: PRIME NUMBER CHECK
# =====================================================================

# A prime number is an integer greater than 1
# that has exactly two positive divisors:
# 1 and itself.
#
# We check whether any number from 2 up to
# the square root of the number divides it.
#
# The loop else block runs if no break occurs.


print("\n" + "=" * 70)
print("SECTION 20: PRIME NUMBER CHECK")
print("=" * 70)


number = 29

if number > 1:

    for divisor in range(2, int(number ** 0.5) + 1):

        if number % divisor == 0:

            print(number, "is not prime.")

            break

    else:

        print(number, "is prime.")

else:

    print(number, "is not prime.")


# =====================================================================
# SECTION 21: FIBONACCI SEQUENCE
# =====================================================================

# Fibonacci sequence:
#
# 0, 1, 1, 2, 3, 5, 8, 13, ...
#
# Every new term is the sum of the previous
# two terms.
#
# Formula:
#
# F(n) = F(n-1) + F(n-2)


print("\n" + "=" * 70)
print("SECTION 21: FIBONACCI SEQUENCE")
print("=" * 70)


first = 0

second = 1

for number in range(10):

    print(first)

    # Calculate the next Fibonacci number.

    next_number = first + second

    # Move the values forward.

    first = second

    second = next_number


# =====================================================================
# SECTION 22: COUNTING EVEN AND ODD NUMBERS
# =====================================================================

# We can use conditions inside a loop
# to classify numbers.
#
# Modulo operator:
# number % 2 == 0 means even.


print("\n" + "=" * 70)
print("SECTION 22: EVEN AND ODD COUNT")
print("=" * 70)


numbers = [10, 15, 20, 25, 30, 35, 40]

even_count = 0

odd_count = 0


for number in numbers:

    if number % 2 == 0:

        even_count += 1

    else:

        odd_count += 1


print("Even numbers:", even_count)

print("Odd numbers:", odd_count)


# =====================================================================
# SECTION 23: FINDING THE LARGEST NUMBER
# =====================================================================

# We use a loop to find the maximum value.
#
# We initially assume the first element is largest.
# Then we compare each following number.


print("\n" + "=" * 70)
print("SECTION 23: FINDING THE LARGEST NUMBER")
print("=" * 70)


numbers = [45, 89, 12, 100, 67, 34]

largest = numbers[0]


for number in numbers:

    if number > largest:

        largest = number


print("Largest number:", largest)


# =====================================================================
# SECTION 24: FINDING THE SMALLEST NUMBER
# =====================================================================

# This follows the same principle as finding
# the largest number.
#
# We initially assume the first number is smallest.


print("\n" + "=" * 70)
print("SECTION 24: FINDING THE SMALLEST NUMBER")
print("=" * 70)


numbers = [45, 89, 12, 100, 67, 34]

smallest = numbers[0]


for number in numbers:

    if number < smallest:

        smallest = number


print("Smallest number:", smallest)


# =====================================================================
# SECTION 25: USING zip()
# =====================================================================

# zip() combines corresponding elements
# from two or more sequences.
#
# Example:
# names[0] matches marks[0].
# names[1] matches marks[1].


print("\n" + "=" * 70)
print("SECTION 25: ZIP FUNCTION")
print("=" * 70)


names = ["Ali", "Ahmed", "Sara"]

marks = [85, 90, 95]


for name, mark in zip(names, marks):

    print(name, "scored", mark)


# =====================================================================
# SECTION 26: LIST COMPREHENSION
# =====================================================================

# List comprehension is a concise way to create lists.
#
# It can replace certain simple for loops.
#
# Example:
# Generate squares of numbers from 1 to 5.


print("\n" + "=" * 70)
print("SECTION 26: LIST COMPREHENSION")
print("=" * 70)


squares = []


for number in range(1, 6):

    squares.append(number ** 2)


print("Using a normal loop:", squares)


# Equivalent list comprehension:

squares = [number ** 2 for number in range(1, 6)]


print("Using list comprehension:", squares)


# =====================================================================
# SECTION 27: NESTED LOOPS WITH PATTERNS
# =====================================================================

# Nested loops can generate patterns.
#
# The outer loop controls the rows.
# The inner loop controls the symbols in each row.


print("\n" + "=" * 70)
print("SECTION 27: STAR PATTERN")
print("=" * 70)


for row in range(1, 6):

    for column in range(row):

        print("*", end=" ")

    print()


# =====================================================================
# SECTION 28: NESTED LOOPS WITH TWO-DIMENSIONAL LISTS
# =====================================================================

# A two-dimensional list contains lists inside a list.
#
# It can represent rows and columns in a table
# or a matrix.


print("\n" + "=" * 70)
print("SECTION 28: TWO-DIMENSIONAL LIST")
print("=" * 70)


matrix = [

    [1, 2, 3],

    [4, 5, 6],

    [7, 8, 9]

]


for row in matrix:

    for value in row:

        print(value, end=" ")

    print()


# =====================================================================
# SECTION 29: BASIC DATA PROCESSING
# =====================================================================

# Loops are commonly used to process datasets.
#
# Here we calculate the average of a collection
# of student marks.
#
# This is an introductory example of data processing.


print("\n" + "=" * 70)
print("SECTION 29: DATA PROCESSING")
print("=" * 70)


student_marks = [78, 85, 92, 67, 88, 95, 73]

total = 0

for mark in student_marks:

    total += mark


average = total / len(student_marks)


print("Student marks:", student_marks)

print("Total marks:", total)

print("Average marks:", round(average, 2))


# =====================================================================
# SECTION 30: FOR LOOPS IN ARTIFICIAL INTELLIGENCE
# =====================================================================

# Loops are important in Artificial Intelligence.
#
# Examples:
#
# 1. Processing datasets.
# 2. Training Machine Learning models.
# 3. Calculating errors.
# 4. Processing image pixels.
# 5. Evaluating predictions.
#
# This example calculates prediction errors.
#
# Error = Actual value - Predicted value
#
# Absolute error = Absolute value of the difference.


print("\n" + "=" * 70)
print("SECTION 30: AI DATA PROCESSING")
print("=" * 70)


actual_values = [100, 200, 300, 400]

predicted_values = [90, 210, 280, 390]

total_error = 0


for actual, predicted in zip(actual_values, predicted_values):

    error = actual - predicted

    absolute_error = abs(error)

    total_error += absolute_error

    print("Actual:", actual)

    print("Predicted:", predicted)

    print("Absolute error:", absolute_error)

    print("-" * 30)


mean_absolute_error = total_error / len(actual_values)


print("Mean Absolute Error:", mean_absolute_error)


# =====================================================================
# FINAL LESSON SUMMARY
# =====================================================================


print("\n" + "=" * 70)

print("DAY 012 - PYTHON FOR LOOPS")

print("=" * 70)

print("1. Introduction to Loops - Completed")

print("2. Basic For Loop - Completed")

print("3. Range Function - Completed")

print("4. String Iteration - Completed")

print("5. Counting Vowels - Completed")

print("6. Lists - Completed")

print("7. Summation - Completed")

print("8. Average Calculation - Completed")

print("9. Tuples - Completed")

print("10. Sets - Completed")

print("11. Dictionaries - Completed")

print("12. Enumerate - Completed")

print("13. Break - Completed")

print("14. Continue - Completed")

print("15. Loop Else - Completed")

print("16. Nested For Loops - Completed")

print("17. Multiplication Tables - Completed")

print("18. Mathematical Summation - Completed")

print("19. Factorial - Completed")

print("20. Prime Number Checking - Completed")

print("21. Fibonacci Sequence - Completed")

print("22. Even and Odd Counting - Completed")

print("23. Finding Maximum - Completed")

print("24. Finding Minimum - Completed")

print("25. Zip Function - Completed")

print("26. List Comprehension - Completed")

print("27. Pattern Generation - Completed")

print("28. Two-Dimensional Lists - Completed")

print("29. Dataset Processing - Completed")

print("30. AI Data Processing - Completed")


print("\nALL DAY 012 LESSON EXAMPLES COMPLETED!")

print("=" * 70)


# =====================================================================
# END OF DAY 012 - FOR_LOOP.PY
# =====================================================================
