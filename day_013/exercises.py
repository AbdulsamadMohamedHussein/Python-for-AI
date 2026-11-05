
# =====================================================================
# DAY 013 - PYTHON WHILE LOOPS
# 30 FULLY SOLVED EXERCISES
#
# Bachelor's in Artificial Intelligence
# 90-Day Python Programming Journey
#
# TOPICS:
# 1. Basic while loops
# 2. Counting
# 3. Mathematical calculations
# 4. Strings
# 5. Lists
# 6. break and continue
# 7. Nested while loops
# 8. Number problems
# 9. Functions
# 10. Data processing
# 11. Machine Learning introduction
#
# =====================================================================


# =====================================================================
# EXERCISE 1: PRINT NUMBERS FROM 1 TO 10
# =====================================================================

# QUESTION:
# Use a while loop to print numbers from 1 to 10.
#
# EXPLANATION:
# First, initialize number at 1.
# The condition checks whether number is <= 10.
# After printing, increase number by one.
#
# IMPORTANT:
# Updating the counter prevents an infinite loop.

print("\n" + "=" * 70)
print("EXERCISE 1: PRINT NUMBERS")
print("=" * 70)

number = 1

while number <= 10:

    print(number)

    number += 1


# =====================================================================
# EXERCISE 2: PRINT NUMBERS FROM 10 TO 1
# =====================================================================

# QUESTION:
# Count backwards from 10 to 1.
#
# EXPLANATION:
# Start at 10.
# Continue while number is greater than zero.
# Subtract one during every iteration.

print("\n" + "=" * 70)
print("EXERCISE 2: COUNT BACKWARDS")
print("=" * 70)

number = 10

while number >= 1:

    print(number)

    number -= 1


# =====================================================================
# EXERCISE 3: PRINT EVEN NUMBERS FROM 1 TO 50
# =====================================================================

# QUESTION:
# Print all even numbers between 1 and 50.
#
# EXPLANATION:
# A number is even if its remainder after
# division by 2 is zero.
#
# The modulo operator (%) calculates the remainder.

print("\n" + "=" * 70)
print("EXERCISE 3: EVEN NUMBERS")
print("=" * 70)

number = 1

while number <= 50:

    if number % 2 == 0:

        print(number)

    number += 1


# =====================================================================
# EXERCISE 4: PRINT ODD NUMBERS FROM 1 TO 50
# =====================================================================

# QUESTION:
# Print all odd numbers between 1 and 50.
#
# EXPLANATION:
# Odd numbers have a remainder of 1
# when divided by 2.

print("\n" + "=" * 70)
print("EXERCISE 4: ODD NUMBERS")
print("=" * 70)

number = 1

while number <= 50:

    if number % 2 != 0:

        print(number)

    number += 1


# =====================================================================
# EXERCISE 5: SUM NUMBERS FROM 1 TO 100
# =====================================================================

# QUESTION:
# Calculate the sum of integers from 1 to 100.
#
# MATHEMATICAL FORMULA:
#
# S = 1 + 2 + 3 + ... + 100
#
# EXPLANATION:
# total is an accumulator.
# It stores the running sum.
#
# Every number is added to total.

print("\n" + "=" * 70)
print("EXERCISE 5: SUMMATION")
print("=" * 70)

number = 1

total = 0

while number <= 100:

    total += number

    number += 1

print("Total:", total)

# Expected output: 5050


# =====================================================================
# EXERCISE 6: MULTIPLICATION TABLE
# =====================================================================

# QUESTION:
# Generate the multiplication table of 8.
#
# EXPLANATION:
# multiplier begins at 1.
# Each iteration multiplies 8 by multiplier.
# The multiplier increases until it reaches 10.

print("\n" + "=" * 70)
print("EXERCISE 6: MULTIPLICATION TABLE")
print("=" * 70)

number = 8

multiplier = 1

while multiplier <= 10:

    result = number * multiplier

    print(number, "x", multiplier, "=", result)

    multiplier += 1


# =====================================================================
# EXERCISE 7: CALCULATE FACTORIAL
# =====================================================================

# QUESTION:
# Calculate the factorial of 6.
#
# MATHEMATICAL FORMULA:
#
# 6! = 6 x 5 x 4 x 3 x 2 x 1
#
# Result = 720
#
# EXPLANATION:
# factorial starts at 1.
# Each iteration multiplies it by counter.

print("\n" + "=" * 70)
print("EXERCISE 7: FACTORIAL")
print("=" * 70)

number = 6

counter = 1

factorial = 1

while counter <= number:

    factorial *= counter

    counter += 1

print("Factorial:", factorial)


# =====================================================================
# EXERCISE 8: COUNT THE DIGITS OF A NUMBER
# =====================================================================

# QUESTION:
# Count how many digits are in 987654.
#
# EXPLANATION:
# Integer division by 10 removes the last digit.
#
# 987654 // 10 = 98765
# 98765 // 10 = 9876
#
# We count every time a digit is removed.
#
# Special case:
# The number zero contains one digit.

print("\n" + "=" * 70)
print("EXERCISE 8: COUNT DIGITS")
print("=" * 70)

number = 987654

original_number = number

digit_count = 0

while number > 0:

    number //= 10

    digit_count += 1

if original_number == 0:

    digit_count = 1

print("Number:", original_number)

print("Digits:", digit_count)


# =====================================================================
# EXERCISE 9: REVERSE A NUMBER
# =====================================================================

# QUESTION:
# Reverse the number 12345.
#
# EXPLANATION:
# % 10 extracts the last digit.
# // 10 removes the last digit.
#
# We build the reversed number one digit at a time.

print("\n" + "=" * 70)
print("EXERCISE 9: REVERSE NUMBER")
print("=" * 70)

number = 12345

original_number = number

reversed_number = 0

while number > 0:

    digit = number % 10

    reversed_number = reversed_number * 10 + digit

    number //= 10

print("Original:", original_number)

print("Reversed:", reversed_number)


# =====================================================================
# EXERCISE 10: SUM OF DIGITS
# =====================================================================

# QUESTION:
# Calculate the sum of the digits of 4567.
#
# MATHEMATICAL EXPRESSION:
#
# 4 + 5 + 6 + 7 = 22
#
# EXPLANATION:
# Extract one digit at a time using % 10.
# Add it to digit_sum.
# Remove it using // 10.

print("\n" + "=" * 70)
print("EXERCISE 10: SUM OF DIGITS")
print("=" * 70)

number = 4567

original_number = number

digit_sum = 0

while number > 0:

    digit = number % 10

    digit_sum += digit

    number //= 10

print("Number:", original_number)

print("Digit sum:", digit_sum)


# =====================================================================
# EXERCISE 11: CHECK PALINDROME NUMBER
# =====================================================================

# QUESTION:
# Check whether 1221 is a palindrome.
#
# EXPLANATION:
# A palindrome reads the same forwards
# and backwards.
#
# We reverse the number and compare it
# with the original number.

print("\n" + "=" * 70)
print("EXERCISE 11: PALINDROME")
print("=" * 70)

number = 1221

original_number = number

reversed_number = 0

while number > 0:

    digit = number % 10

    reversed_number = reversed_number * 10 + digit

    number //= 10

if original_number == reversed_number:

    print(original_number, "is a palindrome.")

else:

    print(original_number, "is not a palindrome.")


# =====================================================================
# EXERCISE 12: GENERATE FIBONACCI SEQUENCE
# =====================================================================

# QUESTION:
# Generate the first 10 Fibonacci numbers.
#
# FORMULA:
#
# F(n) = F(n-1) + F(n-2)
#
# EXPLANATION:
# Every new number is the sum of
# the previous two numbers.

print("\n" + "=" * 70)
print("EXERCISE 12: FIBONACCI")
print("=" * 70)

first = 0

second = 1

count = 0

while count < 10:

    print(first, end=" ")

    next_number = first + second

    first = second

    second = next_number

    count += 1

print()


# =====================================================================
# EXERCISE 13: CHECK PRIME NUMBER
# =====================================================================

# QUESTION:
# Check whether 37 is prime.
#
# EXPLANATION:
# A prime number is greater than 1
# and has exactly two positive divisors.
#
# We test divisors up to the square root.
#
# If a divisor divides the number exactly,
# the number is not prime.

print("\n" + "=" * 70)
print("EXERCISE 13: PRIME NUMBER")
print("=" * 70)

number = 37

divisor = 2

is_prime = number > 1

while is_prime and divisor * divisor <= number:

    if number % divisor == 0:

        is_prime = False

    divisor += 1

if is_prime:

    print(number, "is prime.")

else:

    print(number, "is not prime.")


# =====================================================================
# EXERCISE 14: COUNT VOWELS IN A STRING
# =====================================================================

# QUESTION:
# Count vowels in "Artificial Intelligence".
#
# EXPLANATION:
# Convert the text into lowercase.
# Check every character.
# If the character exists in "aeiou",
# increase vowel_count.

print("\n" + "=" * 70)
print("EXERCISE 14: COUNT VOWELS")
print("=" * 70)

sentence = "Artificial Intelligence"

index = 0

vowel_count = 0

while index < len(sentence):

    character = sentence[index].lower()

    if character in "aeiou":

        vowel_count += 1

    index += 1

print("Sentence:", sentence)

print("Vowels:", vowel_count)


# =====================================================================
# EXERCISE 15: REVERSE A STRING
# =====================================================================

# QUESTION:
# Reverse the word "PYTHON".
#
# EXPLANATION:
# Start from the last character.
# Move backwards through the string.
# Add each character to reversed_word.

print("\n" + "=" * 70)
print("EXERCISE 15: REVERSE STRING")
print("=" * 70)

word = "PYTHON"

index = len(word) - 1

reversed_word = ""

while index >= 0:

    reversed_word += word[index]

    index -= 1

print("Original:", word)

print("Reversed:", reversed_word)


# =====================================================================
# EXERCISE 16: ITERATE THROUGH A LIST
# =====================================================================

# QUESTION:
# Print all subjects stored in a list.
#
# EXPLANATION:
# Lists use zero-based indexing.
# Therefore, the first element is at index 0.
#
# len() gives the total number of elements.

print("\n" + "=" * 70)
print("EXERCISE 16: LIST ITERATION")
print("=" * 70)

subjects = [

    "Mathematics",

    "Python",

    "Statistics",

    "Machine Learning"

]

index = 0

while index < len(subjects):

    print(subjects[index])

    index += 1


# =====================================================================
# EXERCISE 17: CALCULATE LIST SUM
# =====================================================================

# QUESTION:
# Calculate the sum of all numbers in a list.
#
# EXPLANATION:
# Access each list element using its index.
# Add every value to total.

print("\n" + "=" * 70)
print("EXERCISE 17: LIST SUM")
print("=" * 70)

numbers = [10, 20, 30, 40, 50]

index = 0

total = 0

while index < len(numbers):

    total += numbers[index]

    index += 1

print("Total:", total)


# =====================================================================
# EXERCISE 18: CALCULATE LIST AVERAGE
# =====================================================================

# QUESTION:
# Calculate the average of examination marks.
#
# FORMULA:
#
# Average = Total / Number of observations
#
# EXPLANATION:
# First calculate the total.
# Then divide by the number of marks.

print("\n" + "=" * 70)
print("EXERCISE 18: LIST AVERAGE")
print("=" * 70)

marks = [80, 90, 75, 85, 95]

index = 0

total = 0

while index < len(marks):

    total += marks[index]

    index += 1

average = total / len(marks)

print("Total:", total)

print("Average:", average)


# =====================================================================
# EXERCISE 19: FIND LARGEST NUMBER
# =====================================================================

# QUESTION:
# Find the largest number in a list.
#
# EXPLANATION:
# Initially assume the first number is largest.
# Compare every remaining number.
# Update largest when a bigger value is found.

print("\n" + "=" * 70)
print("EXERCISE 19: LARGEST NUMBER")
print("=" * 70)

numbers = [45, 89, 12, 100, 67, 34]

largest = numbers[0]

index = 1

while index < len(numbers):

    if numbers[index] > largest:

        largest = numbers[index]

    index += 1

print("Largest:", largest)


# =====================================================================
# EXERCISE 20: FIND SMALLEST NUMBER
# =====================================================================

# QUESTION:
# Find the smallest number in a list.
#
# EXPLANATION:
# Initially assume the first number is smallest.
# Update smallest whenever a lower number appears.

print("\n" + "=" * 70)
print("EXERCISE 20: SMALLEST NUMBER")
print("=" * 70)

numbers = [45, 89, 12, 100, 67, 34]

smallest = numbers[0]

index = 1

while index < len(numbers):

    if numbers[index] < smallest:

        smallest = numbers[index]

    index += 1

print("Smallest:", smallest)


# =====================================================================
# EXERCISE 21: COUNT EVEN AND ODD NUMBERS
# =====================================================================

# QUESTION:
# Count even and odd numbers in a list.
#
# EXPLANATION:
# Use modulo to determine whether
# a number is even or odd.

print("\n" + "=" * 70)
print("EXERCISE 21: EVEN AND ODD COUNT")
print("=" * 70)

numbers = [10, 15, 20, 25, 30, 35, 40]

index = 0

even_count = 0

odd_count = 0

while index < len(numbers):

    if numbers[index] % 2 == 0:

        even_count += 1

    else:

        odd_count += 1

    index += 1

print("Even:", even_count)

print("Odd:", odd_count)


# =====================================================================
# EXERCISE 22: USE BREAK
# =====================================================================

# QUESTION:
# Print numbers from 1 to 10,
# but stop when number reaches 6.
#
# EXPLANATION:
# break terminates the nearest loop immediately.

print("\n" + "=" * 70)
print("EXERCISE 22: BREAK")
print("=" * 70)

number = 1

while number <= 10:

    if number == 6:

        break

    print(number)

    number += 1


# =====================================================================
# EXERCISE 23: USE CONTINUE
# =====================================================================

# QUESTION:
# Print numbers from 1 to 10,
# but skip number 5.
#
# EXPLANATION:
# continue skips the current iteration.
#
# We update number before continue
# to prevent an infinite loop.

print("\n" + "=" * 70)
print("EXERCISE 23: CONTINUE")
print("=" * 70)

number = 0

while number < 10:

    number += 1

    if number == 5:

        continue

    print(number)


# =====================================================================
# EXERCISE 24: NESTED WHILE LOOPS
# =====================================================================

# QUESTION:
# Display a multiplication grid from 1 to 5.
#
# EXPLANATION:
# The outer loop controls rows.
# The inner loop controls columns.
#
# The inner loop restarts for every outer iteration.

print("\n" + "=" * 70)
print("EXERCISE 24: NESTED WHILE LOOPS")
print("=" * 70)

row = 1

while row <= 5:

    column = 1

    while column <= 5:

        print(row * column, end="\t")

        column += 1

    print()

    row += 1


# =====================================================================
# EXERCISE 25: GENERATE STAR PATTERN
# =====================================================================

# QUESTION:
# Generate a triangle using five rows of stars.
#
# EXPLANATION:
# The outer loop controls the rows.
# The inner loop prints the stars in each row.

print("\n" + "=" * 70)
print("EXERCISE 25: STAR PATTERN")
print("=" * 70)

row = 1

while row <= 5:

    column = 1

    while column <= row:

        print("*", end=" ")

        column += 1

    print()

    row += 1


# =====================================================================
# EXERCISE 26: GENERATE MULTIPLICATION TABLES
# =====================================================================

# QUESTION:
# Generate multiplication tables from 1 to 5.
#
# EXPLANATION:
# Outer loop chooses the number.
# Inner loop generates its multiples.

print("\n" + "=" * 70)
print("EXERCISE 26: MULTIPLICATION TABLES")
print("=" * 70)

number = 1

while number <= 5:

    multiplier = 1

    print("\nTable of", number)

    while multiplier <= 10:

        print(number, "x", multiplier, "=", number * multiplier)

        multiplier += 1

    number += 1


# =====================================================================
# EXERCISE 27: CREATE A COUNTDOWN SYSTEM
# =====================================================================

# QUESTION:
# Create a countdown from 10 to 1.
#
# EXPLANATION:
# Decrease the counter by one during
# every iteration until it reaches zero.

print("\n" + "=" * 70)
print("EXERCISE 27: COUNTDOWN")
print("=" * 70)

countdown = 10

while countdown > 0:

    print(countdown)

    countdown -= 1

print("Countdown finished!")


# =====================================================================
# EXERCISE 28: STUDENT DATA PROCESSING
# =====================================================================

# QUESTION:
# Calculate student averages and grades.
#
# EXPLANATION:
# The dictionary contains student names and marks.
#
# We process each student's marks using indexes.
#
# We calculate their total and average,
# then assign an academic grade.

print("\n" + "=" * 70)
print("EXERCISE 28: STUDENT DATA PROCESSING")
print("=" * 70)

students = {

    "Ali": [80, 90, 85],

    "Ahmed": [70, 75, 80],

    "Sara": [95, 90, 100],

    "John": [40, 45, 35]

}

for student_name, marks in students.items():

    index = 0

    total = 0

    while index < len(marks):

        total += marks[index]

        index += 1

    average = total / len(marks)

    if average >= 90:

        grade = "A+"

    elif average >= 80:

        grade = "A"

    elif average >= 70:

        grade = "B"

    elif average >= 50:

        grade = "C"

    else:

        grade = "F"

    print("\nStudent:", student_name)

    print("Total:", total)

    print("Average:", round(average, 2))

    print("Grade:", grade)


# =====================================================================
# EXERCISE 29: CALCULATE MEAN ABSOLUTE ERROR
# =====================================================================

# QUESTION:
# Calculate Mean Absolute Error (MAE).
#
# AI CONNECTION:
# MAE measures the average absolute difference
# between actual values and model predictions.
#
# FORMULA:
#
# MAE = (1/n) * SUM(|actual - predicted|)
#
# EXPLANATION:
# 1. Process corresponding values.
# 2. Calculate absolute error.
# 3. Accumulate errors.
# 4. Divide by the number of observations.

print("\n" + "=" * 70)
print("EXERCISE 29: MEAN ABSOLUTE ERROR")
print("=" * 70)

actual_values = [100, 200, 300, 400]

predicted_values = [90, 210, 280, 390]

index = 0

total_error = 0

while index < len(actual_values):

    error = abs(
        actual_values[index] - predicted_values[index]
    )

    total_error += error

    print("Actual:", actual_values[index])

    print("Predicted:", predicted_values[index])

    print("Absolute error:", error)

    index += 1

mae = total_error / len(actual_values)

print("Mean Absolute Error:", mae)

# Expected output: 12.5


# =====================================================================
# EXERCISE 30: COMPLETE DATASET ANALYSIS
# =====================================================================

# QUESTION:
# Process a numerical dataset.
#
# Calculate:
# 1. Total.
# 2. Average.
# 3. Maximum.
# 4. Minimum.
# 5. Even count.
# 6. Odd count.
#
# AI CONNECTION:
# Data analysis is a fundamental part
# of Machine Learning.
#
# This exercise combines several concepts
# learned during our Python journey.

print("\n" + "=" * 70)
print("EXERCISE 30: COMPLETE DATASET ANALYSIS")
print("=" * 70)

dataset = [12, 25, 38, 41, 56, 63, 72, 89, 90, 105]

index = 0

total = 0

even_count = 0

odd_count = 0

largest = dataset[0]

smallest = dataset[0]


while index < len(dataset):

    value = dataset[index]

    # Calculate total.

    total += value

    # Count even and odd values.

    if value % 2 == 0:

        even_count += 1

    else:

        odd_count += 1

    # Find maximum.

    if value > largest:

        largest = value

    # Find minimum.

    if value < smallest:

        smallest = value

    index += 1


# Calculate average after processing the dataset.

average = total / len(dataset)


# Display the final report.

print("Dataset:", dataset)

print("Number of observations:", len(dataset))

print("Total:", total)

print("Average:", average)

print("Largest:", largest)

print("Smallest:", smallest)

print("Even count:", even_count)

print("Odd count:", odd_count)


# =====================================================================
# FINAL EXERCISE SUMMARY
# =====================================================================

print("\n" + "=" * 70)

print("DAY 013 - EXERCISES SUMMARY")

print("=" * 70)


exercise_names = [

    "Print Numbers",

    "Count Backwards",

    "Even Numbers",

    "Odd Numbers",

    "Summation",

    "Multiplication Table",

    "Factorial",

    "Count Digits",

    "Reverse Number",

    "Sum of Digits",

    "Palindrome",

    "Fibonacci",

    "Prime Number",

    "Count Vowels",

    "Reverse String",

    "List Iteration",

    "List Sum",

    "List Average",

    "Largest Number",

    "Smallest Number",

    "Even and Odd Count",

    "Break Statement",

    "Continue Statement",

    "Nested While Loops",

    "Star Pattern",

    "Multiplication Tables",

    "Countdown",

    "Student Data Processing",

    "Mean Absolute Error",

    "Complete Dataset Analysis"

]


index = 0

while index < len(exercise_names):

    print(index + 1, exercise_names[index], "- Completed")

    index += 1


print("\nALL 30 EXERCISES COMPLETED!")

print("=" * 70)


# =====================================================================
# END OF DAY 013 - EXERCISES.PY
# =====================================================================
