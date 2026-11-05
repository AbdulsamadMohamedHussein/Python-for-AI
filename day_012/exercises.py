
# =====================================================================
# DAY 012 - PYTHON FOR LOOPS
# 30 COMPLETE SOLVED EXERCISES
#
# Bachelor's in Artificial Intelligence
# 90-Day Python Programming Journey
#
# TOPICS:
# 1. Basic for loops
# 2. range()
# 3. Strings
# 4. Lists and tuples
# 5. Dictionaries
# 6. enumerate()
# 7. break and continue
# 8. Nested loops
# 9. Mathematical calculations
# 10. Functions and data processing
# 11. Basic AI-related calculations
#
# =====================================================================


# =====================================================================
# EXERCISE 1: PRINT NUMBERS FROM 1 TO 10
# =====================================================================

# QUESTION:
# Use a for loop to print numbers from 1 to 10.
#
# EXPLANATION:
# range(1, 11) generates numbers starting at 1
# and stopping before 11.
#
# Therefore, the numbers 1 through 10 are printed.

print("\n" + "=" * 70)
print("EXERCISE 1: PRINT NUMBERS FROM 1 TO 10")
print("=" * 70)

for number in range(1, 11):

    print(number)


# =====================================================================
# EXERCISE 2: PRINT EVEN NUMBERS FROM 1 TO 20
# =====================================================================

# QUESTION:
# Print all even numbers between 1 and 20.
#
# EXPLANATION:
# An even number is divisible by 2.
#
# number % 2 == 0 checks whether the remainder
# after division by 2 is zero.
#
# If True, the number is even.

print("\n" + "=" * 70)
print("EXERCISE 2: EVEN NUMBERS")
print("=" * 70)

for number in range(1, 21):

    if number % 2 == 0:

        print(number)


# =====================================================================
# EXERCISE 3: PRINT ODD NUMBERS FROM 1 TO 20
# =====================================================================

# QUESTION:
# Print all odd numbers between 1 and 20.
#
# EXPLANATION:
# Odd numbers have a remainder of 1
# when divided by 2.

print("\n" + "=" * 70)
print("EXERCISE 3: ODD NUMBERS")
print("=" * 70)

for number in range(1, 21):

    if number % 2 != 0:

        print(number)


# =====================================================================
# EXERCISE 4: COUNT BACKWARDS FROM 10 TO 1
# =====================================================================

# QUESTION:
# Use a for loop to count backwards from 10 to 1.
#
# EXPLANATION:
# range(10, 0, -1)
#
# 10 = Starting number.
# 0 = Stopping boundary, excluded.
# -1 = Decrease by one during each iteration.

print("\n" + "=" * 70)
print("EXERCISE 4: COUNT BACKWARDS")
print("=" * 70)

for number in range(10, 0, -1):

    print(number)


# =====================================================================
# EXERCISE 5: MULTIPLICATION TABLE
# =====================================================================

# QUESTION:
# Generate the multiplication table of 5.
#
# EXPLANATION:
# The loop generates numbers from 1 to 10.
#
# Each number is multiplied by 5.
#
# The result is displayed during every iteration.

print("\n" + "=" * 70)
print("EXERCISE 5: MULTIPLICATION TABLE")
print("=" * 70)

number = 5

for multiplier in range(1, 11):

    result = number * multiplier

    print(number, "x", multiplier, "=", result)


# =====================================================================
# EXERCISE 6: CALCULATE THE SUM OF NUMBERS FROM 1 TO 100
# =====================================================================

# QUESTION:
# Calculate the sum of all integers from 1 to 100.
#
# EXPLANATION:
# total starts at zero.
#
# During each iteration, the current number
# is added to total.
#
# This is called accumulation.

print("\n" + "=" * 70)
print("EXERCISE 6: SUM OF NUMBERS")
print("=" * 70)

total = 0

for number in range(1, 101):

    total += number

print("Total sum:", total)

# Expected output:
# Total sum: 5050


# =====================================================================
# EXERCISE 7: CALCULATE THE FACTORIAL OF A NUMBER
# =====================================================================

# QUESTION:
# Calculate the factorial of 5.
#
# EXPLANATION:
# Factorial means multiplying all positive integers
# from 1 up to the selected number.
#
# 5! = 5 x 4 x 3 x 2 x 1 = 120
#
# We start factorial at 1 because multiplying
# by 1 does not change the result.

print("\n" + "=" * 70)
print("EXERCISE 7: FACTORIAL")
print("=" * 70)

number = 5

factorial = 1

for value in range(1, number + 1):

    factorial *= value

print("Factorial of", number, "is:", factorial)

# Expected output:
# Factorial of 5 is: 120


# =====================================================================
# EXERCISE 8: ITERATE THROUGH A STRING
# =====================================================================

# QUESTION:
# Print every character in the word PYTHON.
#
# EXPLANATION:
# A string is a sequence of characters.
#
# The for loop takes one character at a time
# and stores it in the variable character.

print("\n" + "=" * 70)
print("EXERCISE 8: STRING ITERATION")
print("=" * 70)

word = "PYTHON"

for character in word:

    print(character)


# =====================================================================
# EXERCISE 9: COUNT VOWELS IN A STRING
# =====================================================================

# QUESTION:
# Count how many vowels exist in a sentence.
#
# EXPLANATION:
# We use the vowels a, e, i, o and u.
#
# lower() converts the sentence into lowercase.
#
# The in operator checks whether a character
# exists inside the string "aeiou".
#
# vowel_count increases whenever a vowel is found.

print("\n" + "=" * 70)
print("EXERCISE 9: COUNT VOWELS")
print("=" * 70)

sentence = "Artificial Intelligence"

vowel_count = 0

for character in sentence.lower():

    if character in "aeiou":

        vowel_count += 1

print("Sentence:", sentence)

print("Number of vowels:", vowel_count)


# =====================================================================
# EXERCISE 10: CALCULATE THE SUM OF LIST ELEMENTS
# =====================================================================

# QUESTION:
# Calculate the sum of all numbers in a list.
#
# EXPLANATION:
# The loop processes each element.
#
# total accumulates the values.
#
# This is a common technique in data processing.

print("\n" + "=" * 70)
print("EXERCISE 10: SUM OF LIST ELEMENTS")
print("=" * 70)

numbers = [10, 20, 30, 40, 50]

total = 0

for number in numbers:

    total += number

print("Numbers:", numbers)

print("Total:", total)


# =====================================================================
# EXERCISE 11: CALCULATE THE AVERAGE OF LIST ELEMENTS
# =====================================================================

# QUESTION:
# Calculate the average of five examination marks.
#
# MATHEMATICAL FORMULA:
#
# Average = Total / Number of values
#
# EXPLANATION:
# First, calculate the total using a loop.
# Then divide by the number of elements.

print("\n" + "=" * 70)
print("EXERCISE 11: CALCULATE AVERAGE")
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
# EXERCISE 12: FIND THE LARGEST NUMBER IN A LIST
# =====================================================================

# QUESTION:
# Find the largest number in a list.
#
# EXPLANATION:
# We initially assume the first element
# is the largest.
#
# During every iteration, we compare the current
# number with the largest value found so far.
#
# If the current number is larger, we update largest.

print("\n" + "=" * 70)
print("EXERCISE 12: FIND LARGEST NUMBER")
print("=" * 70)

numbers = [45, 89, 12, 100, 67, 34]

largest = numbers[0]

for number in numbers:

    if number > largest:

        largest = number

print("Largest number:", largest)


# =====================================================================
# EXERCISE 13: FIND THE SMALLEST NUMBER IN A LIST
# =====================================================================

# QUESTION:
# Find the smallest number in a list.
#
# EXPLANATION:
# We initially assume the first element
# is the smallest.
#
# If a smaller number is found, update smallest.

print("\n" + "=" * 70)
print("EXERCISE 13: FIND SMALLEST NUMBER")
print("=" * 70)

numbers = [45, 89, 12, 100, 67, 34]

smallest = numbers[0]

for number in numbers:

    if number < smallest:

        smallest = number

print("Smallest number:", smallest)


# =====================================================================
# EXERCISE 14: COUNT EVEN AND ODD NUMBERS
# =====================================================================

# QUESTION:
# Count how many even and odd numbers
# exist in a list.
#
# EXPLANATION:
# We create two counters.
#
# If a number is divisible by 2,
# increase even_count.
#
# Otherwise, increase odd_count.

print("\n" + "=" * 70)
print("EXERCISE 14: COUNT EVEN AND ODD")
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
# EXERCISE 15: USE enumerate()
# =====================================================================

# QUESTION:
# Display the index and subject name
# for every subject in a list.
#
# EXPLANATION:
# enumerate() provides two values:
#
# 1. Index.
# 2. Current element.
#
# start=1 makes numbering begin at 1
# instead of the default 0.

print("\n" + "=" * 70)
print("EXERCISE 15: ENUMERATE")
print("=" * 70)

subjects = [

    "Mathematics",

    "Python",

    "Statistics",

    "Machine Learning"

]

for index, subject in enumerate(subjects, start=1):

    print(index, subject)


# =====================================================================
# EXERCISE 16: ITERATE THROUGH A DICTIONARY
# =====================================================================

# QUESTION:
# Display student information stored in a dictionary.
#
# EXPLANATION:
# items() provides both the key and its value.
#
# We unpack them into key and value.

print("\n" + "=" * 70)
print("EXERCISE 16: DICTIONARY ITERATION")
print("=" * 70)

student = {

    "name": "Ali",

    "age": 22,

    "course": "Artificial Intelligence",

    "marks": 90

}

for key, value in student.items():

    print(key, ":", value)


# =====================================================================
# EXERCISE 17: USE break TO STOP A LOOP
# =====================================================================

# QUESTION:
# Print numbers from 1 to 10,
# but stop when the number reaches 6.
#
# EXPLANATION:
# break immediately terminates the nearest loop.
#
# The number 6 is not printed because break
# executes before the print statement.

print("\n" + "=" * 70)
print("EXERCISE 17: BREAK STATEMENT")
print("=" * 70)

for number in range(1, 11):

    if number == 6:

        break

    print(number)


# =====================================================================
# EXERCISE 18: USE continue TO SKIP AN ITERATION
# =====================================================================

# QUESTION:
# Print numbers from 1 to 10,
# but skip number 5.
#
# EXPLANATION:
# continue skips the current iteration.
#
# The loop then continues with the next number.

print("\n" + "=" * 70)
print("EXERCISE 18: CONTINUE STATEMENT")
print("=" * 70)

for number in range(1, 11):

    if number == 5:

        continue

    print(number)


# =====================================================================
# EXERCISE 19: CHECK WHETHER A NUMBER IS PRIME
# =====================================================================

# QUESTION:
# Determine whether a number is prime.
#
# EXPLANATION:
# A prime number is greater than 1
# and has exactly two positive divisors:
# 1 and itself.
#
# We test divisors from 2 up to the square root.
#
# If any divisor divides the number exactly,
# it is not prime.
#
# The loop's else executes when no break occurs.

print("\n" + "=" * 70)
print("EXERCISE 19: PRIME NUMBER")
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
# EXERCISE 20: GENERATE FIBONACCI SEQUENCE
# =====================================================================

# QUESTION:
# Generate the first 10 Fibonacci numbers.
#
# EXPLANATION:
# Each new Fibonacci number is the sum
# of the previous two numbers.
#
# The sequence begins with 0 and 1.
#
# F(n) = F(n-1) + F(n-2)

print("\n" + "=" * 70)
print("EXERCISE 20: FIBONACCI SEQUENCE")
print("=" * 70)

first = 0

second = 1

for number in range(10):

    print(first, end=" ")

    next_number = first + second

    first = second

    second = next_number

print()


# =====================================================================
# EXERCISE 21: GENERATE A MULTIPLICATION TABLE
# =====================================================================

# QUESTION:
# Generate multiplication tables from 1 to 5.
#
# EXPLANATION:
# We use a nested for loop.
#
# The outer loop selects the table.
# The inner loop calculates multiples from 1 to 10.

print("\n" + "=" * 70)
print("EXERCISE 21: MULTIPLICATION TABLES")
print("=" * 70)

for number in range(1, 6):

    print("\nTable of", number)

    for multiplier in range(1, 11):

        result = number * multiplier

        print(number, "x", multiplier, "=", result)


# =====================================================================
# EXERCISE 22: GENERATE A STAR PATTERN
# =====================================================================

# QUESTION:
# Generate a triangle pattern using stars.
#
# EXPLANATION:
# The outer loop controls the number of rows.
#
# The inner loop prints stars for each row.
#
# end="" keeps stars on the same line.
# print() moves to the next line after each row.

print("\n" + "=" * 70)
print("EXERCISE 22: STAR PATTERN")
print("=" * 70)

for row in range(1, 6):

    for column in range(row):

        print("*", end=" ")

    print()


# =====================================================================
# EXERCISE 23: CALCULATE THE SUM OF SQUARES
# =====================================================================

# QUESTION:
# Calculate the sum of squares from 1 to 5.
#
# MATHEMATICAL EXPRESSION:
#
# 1² + 2² + 3² + 4² + 5²
#
# EXPLANATION:
# The ** operator calculates powers.
#
# We add each squared number to total.

print("\n" + "=" * 70)
print("EXERCISE 23: SUM OF SQUARES")
print("=" * 70)

total = 0

for number in range(1, 6):

    square = number ** 2

    total += square

    print(number, "squared =", square)

print("Sum of squares:", total)

# Expected result: 55


# =====================================================================
# EXERCISE 24: MULTIPLY ALL NUMBERS IN A LIST
# =====================================================================

# QUESTION:
# Calculate the product of all numbers in a list.
#
# EXPLANATION:
# We initialize product with 1.
#
# Each number is multiplied into product.
#
# We use 1 because multiplying by 1
# does not change the result.

print("\n" + "=" * 70)
print("EXERCISE 24: PRODUCT OF LIST ELEMENTS")
print("=" * 70)

numbers = [2, 3, 4, 5]

product = 1

for number in numbers:

    product *= number

print("Numbers:", numbers)

print("Product:", product)


# =====================================================================
# EXERCISE 25: USE zip() WITH TWO LISTS
# =====================================================================

# QUESTION:
# Display student names alongside their marks.
#
# EXPLANATION:
# zip() combines corresponding elements.
#
# The first name is paired with the first mark.
# The second name is paired with the second mark.
#
# zip() stops when the shortest iterable is exhausted.

print("\n" + "=" * 70)
print("EXERCISE 25: ZIP FUNCTION")
print("=" * 70)

names = ["Ali", "Ahmed", "Sara", "John"]

marks = [85, 90, 95, 80]

for name, mark in zip(names, marks):

    print(name, "scored", mark)


# =====================================================================
# EXERCISE 26: USE LIST COMPREHENSION
# =====================================================================

# QUESTION:
# Create a list containing squares of numbers
# from 1 to 10.
#
# EXPLANATION:
# List comprehension creates a new list
# using a compact expression.
#
# It combines iteration and list creation.

print("\n" + "=" * 70)
print("EXERCISE 26: LIST COMPREHENSION")
print("=" * 70)

squares = [

    number ** 2

    for number in range(1, 11)

]

print("Squares:", squares)


# =====================================================================
# EXERCISE 27: PROCESS A TWO-DIMENSIONAL LIST
# =====================================================================

# QUESTION:
# Print every element of a matrix.
#
# EXPLANATION:
# A two-dimensional list contains smaller lists.
#
# The outer loop processes each row.
# The inner loop processes each value in that row.

print("\n" + "=" * 70)
print("EXERCISE 27: MATRIX ITERATION")
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
# EXERCISE 28: CALCULATE STUDENT PERFORMANCE
# =====================================================================

# QUESTION:
# Calculate the total and average marks
# of multiple students.
#
# EXPLANATION:
# The dictionary stores each student and their marks.
#
# The outer loop processes each student.
# The inner loop calculates their total marks.
#
# This is a simple example of structured data processing.

print("\n" + "=" * 70)
print("EXERCISE 28: STUDENT PERFORMANCE")
print("=" * 70)

students = {

    "Ali": [80, 90, 85],

    "Ahmed": [75, 80, 70],

    "Sara": [95, 90, 100]

}

for name, marks in students.items():

    total = 0

    for mark in marks:

        total += mark

    average = total / len(marks)

    print("\nStudent:", name)

    print("Total:", total)

    print("Average:", round(average, 2))


# =====================================================================
# EXERCISE 29: CALCULATE MEAN ABSOLUTE ERROR
# =====================================================================

# QUESTION:
# Calculate Mean Absolute Error (MAE)
# using actual and predicted values.
#
# AI CONNECTION:
# MAE is an evaluation metric used in regression.
#
# FORMULA:
#
# MAE = (1/n) * SUM(|actual - predicted|)
#
# EXPLANATION:
# 1. Compare each actual value with its prediction.
# 2. Calculate the absolute error.
# 3. Add all errors.
# 4. Divide by the number of observations.

print("\n" + "=" * 70)
print("EXERCISE 29: MEAN ABSOLUTE ERROR")
print("=" * 70)

actual_values = [100, 200, 300, 400]

predicted_values = [90, 210, 280, 390]

total_error = 0

# zip() pairs corresponding actual and predicted values.

for actual, predicted in zip(actual_values, predicted_values):

    error = actual - predicted

    # abs() removes the negative sign if necessary.

    absolute_error = abs(error)

    total_error += absolute_error

    print("Actual:", actual)

    print("Predicted:", predicted)

    print("Absolute error:", absolute_error)

mae = total_error / len(actual_values)

print("\nMean Absolute Error:", mae)

# Expected result: 12.5


# =====================================================================
# EXERCISE 30: BASIC DATASET PROCESSING SYSTEM
# =====================================================================

# QUESTION:
# Process a dataset containing numerical values.
#
# Calculate:
# 1. Total.
# 2. Average.
# 3. Largest value.
# 4. Smallest value.
# 5. Number of even values.
# 6. Number of odd values.
#
# AI CONNECTION:
# Processing numerical datasets is a fundamental
# part of Data Science and Machine Learning.
#
# We will eventually use libraries such as NumPy
# and Pandas for larger datasets.

print("\n" + "=" * 70)
print("EXERCISE 30: DATASET PROCESSING")
print("=" * 70)

dataset = [12, 25, 38, 41, 56, 63, 72, 89, 90, 105]

total = 0

even_count = 0

odd_count = 0

largest = dataset[0]

smallest = dataset[0]


# Process each numerical value.

for value in dataset:

    # Calculate total.

    total += value

    # Count even and odd numbers.

    if value % 2 == 0:

        even_count += 1

    else:

        odd_count += 1

    # Find the largest value.

    if value > largest:

        largest = value

    # Find the smallest value.

    if value < smallest:

        smallest = value


# Calculate average after processing the dataset.

average = total / len(dataset)


# Display the final report.

print("Dataset:", dataset)

print("Number of observations:", len(dataset))

print("Total:", total)

print("Average:", average)

print("Largest value:", largest)

print("Smallest value:", smallest)

print("Even numbers:", even_count)

print("Odd numbers:", odd_count)


# =====================================================================
# FINAL EXERCISE SUMMARY
# =====================================================================

print("\n" + "=" * 70)

print("DAY 012 - PYTHON FOR LOOPS")

print("=" * 70)


exercise_titles = [

    "Print Numbers from 1 to 10",

    "Print Even Numbers",

    "Print Odd Numbers",

    "Count Backwards",

    "Multiplication Table",

    "Sum of Numbers",

    "Factorial Calculation",

    "String Iteration",

    "Count Vowels",

    "Sum of List Elements",

    "Calculate Average",

    "Find Largest Number",

    "Find Smallest Number",

    "Count Even and Odd",

    "Enumerate Function",

    "Dictionary Iteration",

    "Break Statement",

    "Continue Statement",

    "Prime Number Checking",

    "Fibonacci Sequence",

    "Multiplication Tables",

    "Star Pattern",

    "Sum of Squares",

    "Product of List Elements",

    "Zip Function",

    "List Comprehension",

    "Matrix Iteration",

    "Student Performance Processing",

    "Mean Absolute Error",

    "Dataset Processing System"

]


for number, title in enumerate(exercise_titles, start=1):

    print(f"{number}. {title} - Completed")


print("\nALL 30 EXERCISES COMPLETED!")

print("=" * 70)


# =====================================================================
# END OF DAY 012 - EXERCISES.PY
# =====================================================================
