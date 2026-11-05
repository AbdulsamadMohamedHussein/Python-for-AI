
# =====================================================================
# DAY 013 - PYTHON WHILE LOOPS
#
# Bachelor's in Artificial Intelligence
# 90-Day Python Programming Journey
#
# MAIN TOPIC: WHILE LOOPS AND ITERATION
#
# LEARNING OBJECTIVES:
# 1. Understand while loops.
# 2. Understand loop conditions.
# 3. Learn initialization and updating.
# 4. Understand infinite loops.
# 5. Use break and continue.
# 6. Use else with while loops.
# 7. Build counting systems.
# 8. Perform mathematical calculations.
# 9. Understand nested while loops.
# 10. Process data using while loops.
# 11. Apply while loops to AI-related problems.
#
# =====================================================================


# =====================================================================
# SECTION 1: INTRODUCTION TO WHILE LOOPS
# =====================================================================

# A while loop repeatedly executes code
# as long as its condition is True.
#
# Unlike a for loop, which commonly iterates
# over a sequence, a while loop is controlled
# by a Boolean condition.


print("\n" + "=" * 70)
print("SECTION 1: INTRODUCTION TO WHILE LOOPS")
print("=" * 70)


number = 1

while number <= 5:

    print("Hello Python!")

    # Increase number by one.
    # Without this update, the condition
    # would remain True forever.

    number += 1


# =====================================================================
# SECTION 2: BASIC WHILE LOOP
# =====================================================================

# We will print numbers from 1 to 10.
#
# Initialization:
# number = 1
#
# Condition:
# number <= 10
#
# Update:
# number += 1


print("\n" + "=" * 70)
print("SECTION 2: BASIC WHILE LOOP")
print("=" * 70)


number = 1

while number <= 10:

    print(number)

    number += 1


# =====================================================================
# SECTION 3: UNDERSTANDING INITIALIZATION
# =====================================================================

# Initialization means giving a variable
# its starting value before a loop begins.
#
# Here, we start counting from zero.


print("\n" + "=" * 70)
print("SECTION 3: INITIALIZATION")
print("=" * 70)


counter = 0

while counter < 5:

    print("Current counter:", counter)

    counter += 1


# =====================================================================
# SECTION 4: UNDERSTANDING THE LOOP CONDITION
# =====================================================================

# The condition determines whether the loop
# should execute.
#
# If the condition is True, the loop executes.
# If the condition is False, the loop stops.


print("\n" + "=" * 70)
print("SECTION 4: LOOP CONDITION")
print("=" * 70)


age = 15

while age < 20:

    print("Current age:", age)

    age += 1


# =====================================================================
# SECTION 5: COUNTING BACKWARDS
# =====================================================================

# We can also use a while loop to count backwards.
#
# Start at 10.
# Continue while the number is greater than zero.
# Decrease the number by one.


print("\n" + "=" * 70)
print("SECTION 5: COUNTING BACKWARDS")
print("=" * 70)


number = 10

while number >= 1:

    print(number)

    number -= 1


# =====================================================================
# SECTION 6: EVEN NUMBERS
# =====================================================================

# An even number is divisible by 2.
#
# The modulo operator (%) calculates the remainder.
#
# number % 2 == 0 means the number is even.


print("\n" + "=" * 70)
print("SECTION 6: EVEN NUMBERS")
print("=" * 70)


number = 1

while number <= 20:

    if number % 2 == 0:

        print(number)

    number += 1


# =====================================================================
# SECTION 7: ODD NUMBERS
# =====================================================================

# Odd numbers have a non-zero remainder
# when divided by two.


print("\n" + "=" * 70)
print("SECTION 7: ODD NUMBERS")
print("=" * 70)


number = 1

while number <= 20:

    if number % 2 != 0:

        print(number)

    number += 1


# =====================================================================
# SECTION 8: CALCULATING THE SUM OF NUMBERS
# =====================================================================

# We calculate:
#
# 1 + 2 + 3 + 4 + ... + 100
#
# total is an accumulator.
#
# An accumulator stores a running result.


print("\n" + "=" * 70)
print("SECTION 8: SUMMATION")
print("=" * 70)


number = 1

total = 0

while number <= 100:

    total += number

    number += 1


print("Sum from 1 to 100:", total)


# =====================================================================
# SECTION 9: MULTIPLICATION TABLE
# =====================================================================

# We generate the multiplication table of 7.
#
# The multiplier begins at 1.
# It increases after every calculation.


print("\n" + "=" * 70)
print("SECTION 9: MULTIPLICATION TABLE")
print("=" * 70)


number = 7

multiplier = 1

while multiplier <= 10:

    result = number * multiplier

    print(number, "x", multiplier, "=", result)

    multiplier += 1


# =====================================================================
# SECTION 10: FACTORIAL CALCULATION
# =====================================================================

# Factorial means multiplying positive integers
# from 1 up to the selected number.
#
# Example:
#
# 5! = 5 x 4 x 3 x 2 x 1 = 120
#
# We start factorial at 1.


print("\n" + "=" * 70)
print("SECTION 10: FACTORIAL")
print("=" * 70)


number = 5

counter = 1

factorial = 1

while counter <= number:

    factorial *= counter

    counter += 1


print("Factorial of", number, "is:", factorial)


# =====================================================================
# SECTION 11: COUNTING DIGITS
# =====================================================================

# We can count the digits of an integer
# using integer division.
#
# Example:
#
# 12345 // 10 = 1234
# 1234 // 10 = 123
# 123 // 10 = 12
# 12 // 10 = 1
# 1 // 10 = 0
#
# Every division removes the last digit.


print("\n" + "=" * 70)
print("SECTION 11: COUNTING DIGITS")
print("=" * 70)


number = 12345

original_number = number

digit_count = 0


while number > 0:

    number //= 10

    digit_count += 1


print("Number:", original_number)

print("Number of digits:", digit_count)


# =====================================================================
# SECTION 12: REVERSE A NUMBER
# =====================================================================

# We reverse an integer using modulo and
# integer division.
#
# Example:
#
# 1234 becomes 4321.
#
# number % 10 extracts the last digit.
# number // 10 removes the last digit.


print("\n" + "=" * 70)
print("SECTION 12: REVERSE A NUMBER")
print("=" * 70)


number = 1234

original_number = number

reversed_number = 0


while number > 0:

    digit = number % 10

    reversed_number = reversed_number * 10 + digit

    number //= 10


print("Original number:", original_number)

print("Reversed number:", reversed_number)


# =====================================================================
# SECTION 13: PALINDROME NUMBER
# =====================================================================

# A palindrome reads the same forwards and backwards.
#
# Examples:
# 121
# 1331
# 1221
#
# We reverse the number and compare it
# with the original number.


print("\n" + "=" * 70)
print("SECTION 13: PALINDROME NUMBER")
print("=" * 70)


number = 121

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
# SECTION 14: FIBONACCI SEQUENCE
# =====================================================================

# Fibonacci sequence:
#
# 0, 1, 1, 2, 3, 5, 8, 13, ...
#
# Each new number is the sum of the previous
# two numbers.


print("\n" + "=" * 70)
print("SECTION 14: FIBONACCI SEQUENCE")
print("=" * 70)


first = 0

second = 1

count = 0

while count < 10:

    print(first)

    next_number = first + second

    first = second

    second = next_number

    count += 1


# =====================================================================
# SECTION 15: BREAK STATEMENT
# =====================================================================

# break immediately terminates the nearest loop.
#
# Here we stop when number reaches 6.


print("\n" + "=" * 70)
print("SECTION 15: BREAK STATEMENT")
print("=" * 70)


number = 1

while number <= 10:

    if number == 6:

        print("Stopping the loop.")

        break

    print(number)

    number += 1


# =====================================================================
# SECTION 16: CONTINUE STATEMENT
# =====================================================================

# continue skips the current iteration.
#
# We skip number 5.
#
# IMPORTANT:
# We must update the counter before continue.
# Otherwise, the loop could become infinite.


print("\n" + "=" * 70)
print("SECTION 16: CONTINUE STATEMENT")
print("=" * 70)


number = 0

while number < 10:

    number += 1

    if number == 5:

        continue

    print(number)


# =====================================================================
# SECTION 17: ELSE WITH WHILE LOOPS
# =====================================================================

# The else block executes when the while loop
# finishes normally because its condition becomes False.
#
# It does not execute when break terminates the loop.


print("\n" + "=" * 70)
print("SECTION 17: ELSE WITH WHILE LOOP")
print("=" * 70)


number = 1

while number <= 5:

    print(number)

    number += 1

else:

    print("Loop completed normally.")


# =====================================================================
# SECTION 18: USER INPUT WITH WHILE LOOPS
# =====================================================================

# A while loop can repeatedly request user input.
#
# This example keeps asking until the correct
# password is entered.
#
# This is only a demonstration, not a secure
# real-world authentication system.


print("\n" + "=" * 70)
print("SECTION 18: PASSWORD SYSTEM")
print("=" * 70)


correct_password = "python123"

entered_password = ""

attempts = 0

maximum_attempts = 3


while entered_password != correct_password and attempts < maximum_attempts:

    entered_password = input("Enter password: ")

    attempts += 1

    if entered_password == correct_password:

        print("Access granted!")

    else:

        print("Incorrect password.")

        print("Attempts remaining:", maximum_attempts - attempts)


if entered_password != correct_password:

    print("Account access denied.")


# =====================================================================
# SECTION 19: INPUT VALIDATION
# =====================================================================

# We can use a while loop to ensure that
# the user enters a valid number.
#
# The loop continues until valid input is received.
#
# try and except handle conversion errors.


print("\n" + "=" * 70)
print("SECTION 19: INPUT VALIDATION")
print("=" * 70)


valid_number = False

while not valid_number:

    try:

        age = int(input("Enter your age: "))

        if age >= 0:

            valid_number = True

            print("Valid age:", age)

        else:

            print("Age cannot be negative.")

    except ValueError:

        print("Please enter a whole number.")


# =====================================================================
# SECTION 20: NESTED WHILE LOOPS
# =====================================================================

# A nested while loop is a while loop
# placed inside another while loop.
#
# The inner loop completes its execution
# for every iteration of the outer loop.


print("\n" + "=" * 70)
print("SECTION 20: NESTED WHILE LOOPS")
print("=" * 70)


outer = 1

while outer <= 3:

    print("Outer:", outer)

    inner = 1

    while inner <= 3:

        print("   Inner:", inner)

        inner += 1

    outer += 1


# =====================================================================
# SECTION 21: STAR PATTERN
# =====================================================================

# Nested while loops can generate patterns.
#
# The outer loop controls rows.
# The inner loop controls stars in each row.


print("\n" + "=" * 70)
print("SECTION 21: STAR PATTERN")
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
# SECTION 22: SUM OF DIGITS
# =====================================================================

# We calculate the sum of digits of a number.
#
# Example:
#
# 1234 = 1 + 2 + 3 + 4 = 10
#
# Modulo extracts the final digit.
# Integer division removes the final digit.


print("\n" + "=" * 70)
print("SECTION 22: SUM OF DIGITS")
print("=" * 70)


number = 1234

original_number = number

digit_sum = 0


while number > 0:

    digit = number % 10

    digit_sum += digit

    number //= 10


print("Number:", original_number)

print("Sum of digits:", digit_sum)


# =====================================================================
# SECTION 23: CHECK PRIME NUMBER
# =====================================================================

# A prime number is an integer greater than 1
# with exactly two positive divisors.
#
# We check possible divisors up to its square root.
#
# If a divisor is found, the number is not prime.


print("\n" + "=" * 70)
print("SECTION 23: PRIME NUMBER")
print("=" * 70)


number = 29

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
# SECTION 24: LIST ITERATION USING WHILE
# =====================================================================

# A while loop can process a list
# using its index positions.
#
# Indexing begins at zero.
#
# len() provides the total number of elements.


print("\n" + "=" * 70)
print("SECTION 24: LIST ITERATION")
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
# SECTION 25: FIND THE LARGEST NUMBER
# =====================================================================

# We find the maximum number in a list.
#
# First, assume the first element is largest.
# Then compare each remaining element.


print("\n" + "=" * 70)
print("SECTION 25: LARGEST NUMBER")
print("=" * 70)


numbers = [45, 89, 12, 100, 67, 34]

index = 1

largest = numbers[0]


while index < len(numbers):

    if numbers[index] > largest:

        largest = numbers[index]

    index += 1


print("Largest number:", largest)


# =====================================================================
# SECTION 26: CALCULATE LIST AVERAGE
# =====================================================================

# We calculate the average of all numbers
# in a list using a while loop.
#
# Average = Total / Number of observations.


print("\n" + "=" * 70)
print("SECTION 26: LIST AVERAGE")
print("=" * 70)


marks = [80, 90, 75, 85, 95]

index = 0

total = 0


while index < len(marks):

    total += marks[index]

    index += 1


average = total / len(marks)


print("Average:", average)


# =====================================================================
# SECTION 27: SIMPLE COUNTDOWN TIMER
# =====================================================================

# A countdown repeatedly decreases a value.
#
# This is a simple demonstration of
# loop-based countdown logic.


print("\n" + "=" * 70)
print("SECTION 27: COUNTDOWN")
print("=" * 70)


countdown = 5

while countdown > 0:

    print(countdown)

    countdown -= 1


print("Countdown completed!")


# =====================================================================
# SECTION 28: DATASET PROCESSING
# =====================================================================

# We calculate the total and average
# of a numerical dataset.
#
# This introduces the basic logic
# used in data processing.


print("\n" + "=" * 70)
print("SECTION 28: DATASET PROCESSING")
print("=" * 70)


dataset = [10, 20, 30, 40, 50, 60]

index = 0

total = 0


while index < len(dataset):

    total += dataset[index]

    index += 1


average = total / len(dataset)


print("Dataset:", dataset)

print("Total:", total)

print("Average:", average)


# =====================================================================
# SECTION 29: BASIC AI PREDICTION ERROR
# =====================================================================

# Actual values represent real observations.
# Predicted values represent model predictions.
#
# Absolute Error = |Actual - Predicted|
#
# MAE = Total Absolute Error / Number of observations.


print("\n" + "=" * 70)
print("SECTION 29: AI PREDICTION ERROR")
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


# =====================================================================
# SECTION 30: FUNCTIONS WITH WHILE LOOPS
# =====================================================================

# Functions allow us to organize reusable code.
#
# This function calculates the sum of integers
# from 1 up to the given number using a while loop.


print("\n" + "=" * 70)
print("SECTION 30: FUNCTION WITH WHILE LOOP")
print("=" * 70)


def calculate_sum(number):

    total = 0

    counter = 1

    while counter <= number:

        total += counter

        counter += 1

    return total


result = calculate_sum(100)


print("Sum from 1 to 100:", result)


# =====================================================================
# FINAL LESSON SUMMARY
# =====================================================================


print("\n" + "=" * 70)

print("DAY 013 - PYTHON WHILE LOOPS")

print("=" * 70)


topics = [

    "Introduction to While Loops",

    "Basic While Loops",

    "Initialization",

    "Loop Conditions",

    "Counting Backwards",

    "Even Numbers",

    "Odd Numbers",

    "Summation",

    "Multiplication Tables",

    "Factorial",

    "Digit Counting",

    "Number Reversal",

    "Palindrome Checking",

    "Fibonacci Sequence",

    "Break Statement",

    "Continue Statement",

    "Else with While Loops",

    "Password System",

    "Input Validation",

    "Nested While Loops",

    "Star Patterns",

    "Sum of Digits",

    "Prime Number Checking",

    "List Iteration",

    "Finding Largest Values",

    "Average Calculation",

    "Countdown",

    "Dataset Processing",

    "AI Prediction Error",

    "Functions with While Loops"

]


index = 0

while index < len(topics):

    print(index + 1, topics[index], "- Completed")

    index += 1


print("\nALL DAY 013 LESSON EXAMPLES COMPLETED!")

print("=" * 70)


# =====================================================================
# END OF DAY 013 - WHILE_LOOPS.PY
# =====================================================================
