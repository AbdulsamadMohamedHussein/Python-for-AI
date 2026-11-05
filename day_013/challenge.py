
# =====================================================================
# DAY 013 - PYTHON WHILE LOOPS
#
# PRACTICAL PROJECT:
# INTERACTIVE MATHEMATICAL AND DATA ANALYSIS SYSTEM
#
# Bachelor's in Artificial Intelligence
# 90-Day Python Programming Journey
#
# PROGRAMMING CONCEPTS:
# 1. While loops
# 2. Nested while loops
# 3. Functions
# 4. Conditional statements
# 5. User input
# 6. Input validation
# 7. Lists
# 8. Mathematical calculations
# 9. Data processing
# 10. Statistical analysis
# 11. Menu-driven applications
#
# =====================================================================


# =====================================================================
# SECTION 1: PROJECT INTRODUCTION
# =====================================================================

print("\n" + "=" * 75)

print("       INTERACTIVE MATHEMATICAL AND DATA ANALYSIS SYSTEM")

print("=" * 75)

print("Welcome to our Python programming application!")

print("This application performs mathematical calculations")

print("and basic numerical data analysis.")

print("=" * 75)


# =====================================================================
# SECTION 2: INPUT VALIDATION FUNCTION
# =====================================================================

# WHY DO WE NEED INPUT VALIDATION?
#
# When users enter information, they may accidentally
# enter letters instead of numbers.
#
# For example:
#
# int("hello")
#
# This produces a ValueError.
#
# We use try and except to handle this problem.
#
# The while loop keeps asking until valid input is received.
#
# This function also supports optional minimum values.


def get_integer(message, minimum=None):

    while True:

        try:

            value = int(input(message))

            # Check whether the value satisfies
            # the minimum requirement.

            if minimum is not None and value < minimum:

                print("Please enter a number greater than or equal to", minimum)

                continue

            return value

        except ValueError:

            print("Invalid input! Please enter a whole number.")


# =====================================================================
# SECTION 3: ADDITION CALCULATOR
# =====================================================================

# QUESTION:
# Create an addition calculator.
#
# EXPLANATION:
# We request two integers from the user.
# Then we add both values.
#
# The function returns the result.


def addition_calculator():

    print("\nADDITION CALCULATOR")

    first_number = get_integer("Enter first number: ")

    second_number = get_integer("Enter second number: ")

    result = first_number + second_number

    print("Result:", result)


# =====================================================================
# SECTION 4: MULTIPLICATION CALCULATOR
# =====================================================================

# QUESTION:
# Multiply two numbers.
#
# EXPLANATION:
# The multiplication operator (*) calculates
# the product of two numbers.


def multiplication_calculator():

    print("\nMULTIPLICATION CALCULATOR")

    first_number = get_integer("Enter first number: ")

    second_number = get_integer("Enter second number: ")

    result = first_number * second_number

    print("Product:", result)


# =====================================================================
# SECTION 5: FACTORIAL CALCULATOR
# =====================================================================

# QUESTION:
# Calculate the factorial of a number.
#
# MATHEMATICAL FORMULA:
#
# n! = n x (n-1) x (n-2) x ... x 1
#
# Example:
#
# 5! = 5 x 4 x 3 x 2 x 1 = 120
#
# EXPLANATION:
# We initialize factorial at 1.
#
# The while loop multiplies the counter
# into factorial until the counter exceeds
# the selected number.
#
# IMPORTANT:
# 0! = 1.


def factorial_calculator():

    print("\nFACTORIAL CALCULATOR")

    number = get_integer("Enter a non-negative number: ", minimum=0)

    factorial = 1

    counter = 1

    while counter <= number:

        factorial *= counter

        counter += 1

    print("Factorial of", number, "is:", factorial)


# =====================================================================
# SECTION 6: PRIME NUMBER DETECTOR
# =====================================================================

# QUESTION:
# Determine whether a number is prime.
#
# DEFINITION:
# A prime number is greater than 1 and has
# exactly two positive divisors:
# 1 and itself.
#
# Examples:
# 2, 3, 5, 7, 11, 13.
#
# EXPLANATION:
# We test possible divisors starting from 2.
#
# We only need to check up to the square root.
#
# If a divisor divides the number exactly,
# the number is not prime.


def prime_number_checker():

    print("\nPRIME NUMBER DETECTOR")

    number = get_integer("Enter a number: ")

    if number <= 1:

        print(number, "is not a prime number.")

        return

    divisor = 2

    is_prime = True

    while divisor * divisor <= number:

        if number % divisor == 0:

            is_prime = False

            break

        divisor += 1

    if is_prime:

        print(number, "is a prime number.")

    else:

        print(number, "is not a prime number.")


# =====================================================================
# SECTION 7: FIBONACCI GENERATOR
# =====================================================================

# QUESTION:
# Generate a Fibonacci sequence.
#
# MATHEMATICAL FORMULA:
#
# F(n) = F(n-1) + F(n-2)
#
# EXPLANATION:
# Each new Fibonacci number is obtained
# by adding the previous two numbers.
#
# Example:
#
# 0, 1, 1, 2, 3, 5, 8, 13, 21...
#
# The user decides how many numbers to generate.


def fibonacci_generator():

    print("\nFIBONACCI GENERATOR")

    count = get_integer("How many Fibonacci numbers? ", minimum=0)

    first = 0

    second = 1

    counter = 0

    print("Fibonacci sequence:")

    while counter < count:

        print(first, end=" ")

        next_number = first + second

        first = second

        second = next_number

        counter += 1

    print()


# =====================================================================
# SECTION 8: NUMBER REVERSAL
# =====================================================================

# QUESTION:
# Reverse an integer.
#
# Example:
#
# Original: 12345
# Reversed: 54321
#
# EXPLANATION:
# The modulo operator (%) extracts the last digit.
#
# Integer division (//) removes the last digit.
#
# We repeatedly extract digits and construct
# a new reversed number.


def number_reversal():

    print("\nNUMBER REVERSAL")

    number = get_integer("Enter a non-negative integer: ", minimum=0)

    original_number = number

    reversed_number = 0

    while number > 0:

        digit = number % 10

        reversed_number = reversed_number * 10 + digit

        number //= 10

    print("Original number:", original_number)

    print("Reversed number:", reversed_number)


# =====================================================================
# SECTION 9: SUM OF DIGITS
# =====================================================================

# QUESTION:
# Calculate the sum of all digits in an integer.
#
# Example:
#
# 1234 = 1 + 2 + 3 + 4 = 10
#
# EXPLANATION:
# Extract the last digit using % 10.
# Add it to digit_sum.
# Remove it using // 10.
#
# Repeat until the number becomes zero.


def sum_of_digits():

    print("\nSUM OF DIGITS")

    number = get_integer("Enter a non-negative integer: ", minimum=0)

    original_number = number

    digit_sum = 0

    while number > 0:

        digit = number % 10

        digit_sum += digit

        number //= 10

    print("Original number:", original_number)

    print("Sum of digits:", digit_sum)


# =====================================================================
# SECTION 10: PALINDROME DETECTOR
# =====================================================================

# QUESTION:
# Determine whether a number is a palindrome.
#
# DEFINITION:
# A palindrome reads the same forwards
# and backwards.
#
# Examples:
# 121
# 1331
# 1221
#
# EXPLANATION:
# We reverse the number and compare
# it with the original number.


def palindrome_detector():

    print("\nPALINDROME DETECTOR")

    number = get_integer("Enter a non-negative integer: ", minimum=0)

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
# SECTION 11: DATASET ANALYSIS
# =====================================================================

# QUESTION:
# Analyze a numerical dataset.
#
# CALCULATIONS:
#
# 1. Total.
# 2. Average.
# 3. Maximum.
# 4. Minimum.
# 5. Even number count.
# 6. Odd number count.
#
# EXPLANATION:
# We use a list to store numerical values.
#
# The while loop processes each observation
# using its index.
#
# This is a simple introduction to data analysis.


def dataset_analysis():

    print("\nDATASET ANALYSIS")

    numbers = []

    count = get_integer("How many numbers will you enter? ", minimum=1)

    # Collect numerical observations.

    index = 0

    while index < count:

        value = get_integer("Enter number " + str(index + 1) + ": ")

        numbers.append(value)

        index += 1

    # Initialize statistical variables.

    index = 0

    total = 0

    even_count = 0

    odd_count = 0

    largest = numbers[0]

    smallest = numbers[0]

    # Process each observation.

    while index < len(numbers):

        value = numbers[index]

        # Calculate total.

        total += value

        # Count even and odd numbers.

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

    # Calculate arithmetic mean.

    average = total / len(numbers)

    # Display report.

    print("\nDATASET REPORT")

    print("-" * 40)

    print("Dataset:", numbers)

    print("Observations:", len(numbers))

    print("Total:", total)

    print("Average:", round(average, 2))

    print("Largest:", largest)

    print("Smallest:", smallest)

    print("Even numbers:", even_count)

    print("Odd numbers:", odd_count)

    print("-" * 40)


# =====================================================================
# SECTION 12: MEAN ABSOLUTE ERROR
# =====================================================================

# QUESTION:
# Calculate Mean Absolute Error (MAE).
#
# AI CONNECTION:
# MAE is used to evaluate regression models.
#
# FORMULA:
#
# MAE = (1/n) * SUM(|actual - predicted|)
#
# EXPLANATION:
# Actual values are real observations.
# Predicted values are model predictions.
#
# We calculate the absolute difference
# between corresponding observations.
#
# Finally, we divide the total error
# by the number of observations.


def mean_absolute_error():

    print("\nMEAN ABSOLUTE ERROR CALCULATOR")

    actual_values = []

    predicted_values = []

    count = get_integer("Enter number of observations: ", minimum=1)

    index = 0

    # Collect actual values.

    while index < count:

        actual = get_integer("Enter actual value: ")

        actual_values.append(actual)

        index += 1

    index = 0

    # Collect predicted values.

    while index < count:

        predicted = get_integer("Enter predicted value: ")

        predicted_values.append(predicted)

        index += 1

    # Calculate total absolute error.

    index = 0

    total_error = 0

    while index < count:

        error = abs(
            actual_values[index] - predicted_values[index]
        )

        total_error += error

        print("\nActual:", actual_values[index])

        print("Predicted:", predicted_values[index])

        print("Absolute error:", error)

        index += 1

    # Calculate MAE.

    mae = total_error / count

    print("\nMean Absolute Error:", round(mae, 2))


# =====================================================================
# SECTION 13: APPLICATION MENU
# =====================================================================

# This is the main menu of our application.
#
# A while loop keeps the application running.
#
# The application stops only when the user
# selects option 10.
#
# This is called a menu-driven application.


def display_menu():

    print("\n" + "=" * 75)

    print("       MATHEMATICAL AND DATA ANALYSIS MENU")

    print("=" * 75)

    print("1. Addition Calculator")

    print("2. Multiplication Calculator")

    print("3. Factorial Calculator")

    print("4. Prime Number Detector")

    print("5. Fibonacci Generator")

    print("6. Number Reversal")

    print("7. Sum of Digits")

    print("8. Palindrome Detector")

    print("9. Dataset and MAE Analysis")

    print("10. Exit Application")

    print("=" * 75)


# =====================================================================
# SECTION 14: MAIN APPLICATION LOOP
# =====================================================================

# This is the most important section.
#
# while True creates a loop that continues
# until we explicitly terminate it.
#
# The user chooses an option.
#
# Conditional statements determine which
# function should execute.
#
# break exits the application when option 10
# is selected.


print("\nAPPLICATION STARTED!")

while True:

    display_menu()

    choice = get_integer("Select an option (1-10): ")

    if choice == 1:

        addition_calculator()

    elif choice == 2:

        multiplication_calculator()

    elif choice == 3:

        factorial_calculator()

    elif choice == 4:

        prime_number_checker()

    elif choice == 5:

        fibonacci_generator()

    elif choice == 6:

        number_reversal()

    elif choice == 7:

        sum_of_digits()

    elif choice == 8:

        palindrome_detector()

    elif choice == 9:

        print("\n1. Dataset Analysis")

        print("2. Mean Absolute Error")

        analysis_choice = get_integer("Choose analysis type: ")

        if analysis_choice == 1:

            dataset_analysis()

        elif analysis_choice == 2:

            mean_absolute_error()

        else:

            print("Invalid analysis option.")

    elif choice == 10:

        print("\nThank you for using our application!")

        print("Application terminated successfully.")

        break

    else:

        print("Invalid menu selection.")

        print("Please choose a number between 1 and 10.")


# =====================================================================
# END OF DAY 013 - CHALLENGE.PY
# =====================================================================
