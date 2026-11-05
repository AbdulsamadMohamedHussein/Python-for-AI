
# =====================================================================
# DAY 014 - NUMBER GUESSING GAME
# 30 FULLY SOLVED PYTHON EXERCISES
#
# Bachelor's in Artificial Intelligence
# 90-Day Python Programming Journey
#
# TOPICS:
# 1. Random number generation
# 2. Random integers
# 3. Conditional statements
# 4. While loops
# 5. User input
# 6. Input validation
# 7. Attempt tracking
# 8. Score calculation
# 9. Game difficulty
# 10. Functions
# 11. Game development
#
# =====================================================================

import random


# =====================================================================
# EXERCISE 1: GENERATE A RANDOM NUMBER
# =====================================================================

# QUESTION:
# Generate a random integer between 1 and 10.
#
# EXPLANATION:
# random.randint(a, b) generates an integer
# between a and b, including both boundaries.

print("\n" + "=" * 70)
print("EXERCISE 1: RANDOM NUMBER")
print("=" * 70)

number = random.randint(1, 10)

print("Random number:", number)


# =====================================================================
# EXERCISE 2: GENERATE FIVE RANDOM NUMBERS
# =====================================================================

# QUESTION:
# Generate five random numbers between 1 and 100.
#
# EXPLANATION:
# We use a for loop to repeat random generation
# five times.
#
# Each iteration produces a new random integer.

print("\n" + "=" * 70)
print("EXERCISE 2: FIVE RANDOM NUMBERS")
print("=" * 70)

counter = 1

while counter <= 5:

    number = random.randint(1, 100)

    print("Random number", counter, ":", number)

    counter += 1


# =====================================================================
# EXERCISE 3: GENERATE A RANDOM EVEN NUMBER
# =====================================================================

# QUESTION:
# Generate a random even number between 1 and 50.
#
# EXPLANATION:
# We repeatedly generate numbers until we
# find one divisible by 2.
#
# An even number has remainder zero after
# division by 2.

print("\n" + "=" * 70)
print("EXERCISE 3: RANDOM EVEN NUMBER")
print("=" * 70)

number = random.randint(1, 50)

while number % 2 != 0:

    number = random.randint(1, 50)

print("Random even number:", number)


# =====================================================================
# EXERCISE 4: GENERATE A RANDOM PASSWORD DIGIT
# =====================================================================

# QUESTION:
# Generate a random four-digit numerical code.
#
# EXPLANATION:
# randint(1000, 9999) produces an integer
# containing four decimal digits.
#
# This is only a demonstration, not secure
# password or authentication generation.

print("\n" + "=" * 70)
print("EXERCISE 4: RANDOM FOUR-DIGIT CODE")
print("=" * 70)

code = random.randint(1000, 9999)

print("Generated code:", code)


# =====================================================================
# EXERCISE 5: SIMULATE A DICE ROLL
# =====================================================================

# QUESTION:
# Simulate rolling a six-sided dice.
#
# EXPLANATION:
# A normal six-sided dice contains
# numbers from 1 to 6.
#
# We randomly select one of those values.

print("\n" + "=" * 70)
print("EXERCISE 5: DICE ROLL")
print("=" * 70)

dice = random.randint(1, 6)

print("Dice result:", dice)


# =====================================================================
# EXERCISE 6: COMPARE TWO NUMBERS
# =====================================================================

# QUESTION:
# Compare a user's guess with a secret number.
#
# EXPLANATION:
# There are three possible situations:
#
# Guess > Secret = Too high.
# Guess < Secret = Too low.
# Guess == Secret = Correct.

print("\n" + "=" * 70)
print("EXERCISE 6: COMPARE NUMBERS")
print("=" * 70)

secret_number = 50

guess = 70

if guess > secret_number:

    print("Too high!")

elif guess < secret_number:

    print("Too low!")

else:

    print("Correct!")


# =====================================================================
# EXERCISE 7: CHECK WHETHER A GUESS IS CORRECT
# =====================================================================

# QUESTION:
# Check whether the player has guessed
# the correct number.
#
# EXPLANATION:
# The equality operator (==) compares values.
#
# It returns True when both values are equal.

print("\n" + "=" * 70)
print("EXERCISE 7: CORRECT GUESS")
print("=" * 70)

secret_number = 35

guess = 35

if guess == secret_number:

    print("Congratulations! Correct guess.")

else:

    print("Incorrect guess.")


# =====================================================================
# EXERCISE 8: CHECK THE GUESSING RANGE
# =====================================================================

# QUESTION:
# Check whether a guess is between 1 and 100.
#
# EXPLANATION:
# A valid guess must satisfy both boundaries.
#
# If the guess is less than 1 or greater than 100,
# it is invalid.

print("\n" + "=" * 70)
print("EXERCISE 8: VALID GUESS")
print("=" * 70)

guess = 75

if guess >= 1 and guess <= 100:

    print("Valid guess.")

else:

    print("Invalid guess.")


# =====================================================================
# EXERCISE 9: GIVE A HIGH OR LOW HINT
# =====================================================================

# QUESTION:
# Provide a hint depending on the user's guess.
#
# EXPLANATION:
# We compare the guess with the secret number
# and display an appropriate message.

print("\n" + "=" * 70)
print("EXERCISE 9: HIGH OR LOW HINT")
print("=" * 70)

secret_number = 65

guess = 40

if guess > secret_number:

    print("Your guess is too high.")

elif guess < secret_number:

    print("Your guess is too low.")

else:

    print("You guessed correctly.")


# =====================================================================
# EXERCISE 10: CHECK THE DISTANCE FROM THE ANSWER
# =====================================================================

# QUESTION:
# Tell the player whether their guess
# is close to the secret number.
#
# EXPLANATION:
# abs() calculates the absolute difference.
#
# If the difference is 5 or less,
# the guess is considered close.

print("\n" + "=" * 70)
print("EXERCISE 10: CLOSE GUESS")
print("=" * 70)

secret_number = 50

guess = 47

difference = abs(secret_number - guess)

if difference <= 5:

    print("Very close!")

else:

    print("You are far from the answer.")


# =====================================================================
# EXERCISE 11: CREATE A BASIC GUESSING LOOP
# =====================================================================

# QUESTION:
# Allow the user to guess until the answer is correct.
#
# EXPLANATION:
# while True keeps the game running.
#
# break terminates the loop when the guess
# matches the secret number.

print("\n" + "=" * 70)
print("EXERCISE 11: BASIC GUESSING LOOP")
print("=" * 70)

secret_number = 25

while True:

    guess = int(input("Guess the number (1-50): "))

    if guess == secret_number:

        print("Correct! You win!")

        break

    elif guess > secret_number:

        print("Too high.")

    else:

        print("Too low.")


# =====================================================================
# EXERCISE 12: LIMIT THE NUMBER OF ATTEMPTS
# =====================================================================

# QUESTION:
# Give the player only five attempts.
#
# EXPLANATION:
# attempts counts valid guesses.
#
# The loop stops when the player wins
# or uses all five attempts.

print("\n" + "=" * 70)
print("EXERCISE 12: LIMITED ATTEMPTS")
print("=" * 70)

secret_number = 30

attempts = 0

maximum_attempts = 5

while attempts < maximum_attempts:

    guess = int(input("Enter your guess: "))

    attempts += 1

    if guess == secret_number:

        print("Congratulations!")

        break

    elif guess > secret_number:

        print("Too high.")

    else:

        print("Too low.")

if guess != secret_number:

    print("Game over! Secret number:", secret_number)

print("Attempts used:", attempts)


# =====================================================================
# EXERCISE 13: COUNT REMAINING ATTEMPTS
# =====================================================================

# QUESTION:
# Display how many guesses remain.
#
# EXPLANATION:
#
# Remaining attempts =
# Maximum attempts - Attempts used.
#
# This helps the player understand
# how many opportunities remain.

print("\n" + "=" * 70)
print("EXERCISE 13: REMAINING ATTEMPTS")
print("=" * 70)

maximum_attempts = 10

attempts = 0

while attempts < maximum_attempts:

    print("Attempts remaining:", maximum_attempts - attempts)

    guess = int(input("Enter a guess: "))

    attempts += 1

    if guess == 45:

        print("Correct!")

        break

    else:

        print("Incorrect.")

print("Attempts used:", attempts)


# =====================================================================
# EXERCISE 14: TRACK THE BEST ATTEMPT
# =====================================================================

# QUESTION:
# Track how many guesses the player uses.
#
# EXPLANATION:
# We store the number of attempts required
# to find the correct answer.
#
# A smaller attempt count means the player
# found the answer more quickly.

print("\n" + "=" * 70)
print("EXERCISE 14: ATTEMPT TRACKER")
print("=" * 70)

secret_number = 20

attempts = 0

while True:

    guess = int(input("Guess the number: "))

    attempts += 1

    if guess == secret_number:

        print("You won!")

        print("You needed", attempts, "attempts.")

        break

    else:

        print("Try again.")


# =====================================================================
# EXERCISE 15: ADD A MAXIMUM SCORE
# =====================================================================

# QUESTION:
# Calculate a score based on attempts.
#
# EXPLANATION:
# Every attempt reduces the possible score
# by ten points.
#
# The score cannot become negative.

print("\n" + "=" * 70)
print("EXERCISE 15: SCORE CALCULATION")
print("=" * 70)

maximum_score = 100

attempts = 4

score = max(0, maximum_score - attempts * 10)

print("Attempts:", attempts)

print("Final score:", score)


# =====================================================================
# EXERCISE 16: HANDLE INVALID INPUT
# =====================================================================

# QUESTION:
# Prevent the program from crashing
# when a player enters letters instead of numbers.
#
# EXPLANATION:
# int() cannot convert arbitrary text
# into an integer.
#
# ValueError handles this situation.
#
# The loop continues until valid input is received.

print("\n" + "=" * 70)
print("EXERCISE 16: INPUT VALIDATION")
print("=" * 70)

while True:

    try:

        guess = int(input("Enter a whole number: "))

        print("Valid input:", guess)

        break

    except ValueError:

        print("Please enter a valid integer.")


# =====================================================================
# EXERCISE 17: CHECK THE GUESSING RANGE
# =====================================================================

# QUESTION:
# Only accept numbers between 1 and 100.
#
# EXPLANATION:
# We combine input conversion with range validation.
#
# Invalid entries do not terminate the application.

print("\n" + "=" * 70)
print("EXERCISE 17: RANGE VALIDATION")
print("=" * 70)

while True:

    try:

        guess = int(input("Enter a number from 1 to 100: "))

        if 1 <= guess <= 100:

            print("Accepted:", guess)

            break

        else:

            print("Number must be between 1 and 100.")

    except ValueError:

        print("Enter a whole number.")


# =====================================================================
# EXERCISE 18: PREVENT NEGATIVE GUESSES
# =====================================================================

# QUESTION:
# Reject negative numbers.
#
# EXPLANATION:
# A guessing game using positive integers
# should not accept negative guesses.

print("\n" + "=" * 70)
print("EXERCISE 18: NEGATIVE INPUT VALIDATION")
print("=" * 70)

while True:

    try:

        guess = int(input("Enter a positive number: "))

        if guess > 0:

            print("Valid positive number.")

            break

        else:

            print("Negative numbers and zero are not allowed.")

    except ValueError:

        print("Invalid input.")


# =====================================================================
# EXERCISE 19: USE CONTINUE FOR INVALID GUESSES
# =====================================================================

# QUESTION:
# Skip guesses outside the permitted range.
#
# EXPLANATION:
# continue skips the current iteration.
#
# Invalid values do not count as attempts.

print("\n" + "=" * 70)
print("EXERCISE 19: CONTINUE STATEMENT")
print("=" * 70)

secret_number = 15

attempts = 0

while attempts < 5:

    guess = int(input("Enter a number from 1 to 20: "))

    if not 1 <= guess <= 20:

        print("Invalid range.")

        continue

    attempts += 1

    if guess == secret_number:

        print("Correct!")

        break

    else:

        print("Incorrect.")

print("Valid attempts:", attempts)


# =====================================================================
# EXERCISE 20: CREATE A REPLAY QUESTION
# =====================================================================

# QUESTION:
# Ask the player whether they want
# to play another round.
#
# EXPLANATION:
# lower() converts the answer into lowercase.
#
# This makes YES, Yes and yes equivalent.

print("\n" + "=" * 70)
print("EXERCISE 20: REPLAY QUESTION")
print("=" * 70)

answer = input("Would you like to play again? (yes/no): ")

if answer.lower() == "yes":

    print("Starting another round!")

else:

    print("Thank you for playing!")


# =====================================================================
# EXERCISE 21: CREATE EASY DIFFICULTY
# =====================================================================

# QUESTION:
# Configure an easy guessing game.
#
# EXPLANATION:
# Easy mode uses a smaller number range
# and allows more attempts.

print("\n" + "=" * 70)
print("EXERCISE 21: EASY DIFFICULTY")
print("=" * 70)

minimum = 1

maximum = 20

maximum_attempts = 10

secret_number = random.randint(minimum, maximum)

print("Easy mode selected.")

print("Guess between", minimum, "and", maximum)

print("Attempts allowed:", maximum_attempts)


# =====================================================================
# EXERCISE 22: CREATE MEDIUM DIFFICULTY
# =====================================================================

# QUESTION:
# Configure medium difficulty.
#
# EXPLANATION:
# Medium mode increases the number range
# and decreases the number of attempts.

print("\n" + "=" * 70)
print("EXERCISE 22: MEDIUM DIFFICULTY")
print("=" * 70)

minimum = 1

maximum = 50

maximum_attempts = 7

secret_number = random.randint(minimum, maximum)

print("Medium mode selected.")

print("Guess between", minimum, "and", maximum)

print("Attempts allowed:", maximum_attempts)


# =====================================================================
# EXERCISE 23: CREATE HARD DIFFICULTY
# =====================================================================

# QUESTION:
# Configure hard difficulty.
#
# EXPLANATION:
# Hard mode provides a larger range
# and fewer attempts.

print("\n" + "=" * 70)
print("EXERCISE 23: HARD DIFFICULTY")
print("=" * 70)

minimum = 1

maximum = 100

maximum_attempts = 5

secret_number = random.randint(minimum, maximum)

print("Hard mode selected.")

print("Guess between", minimum, "and", maximum)

print("Attempts allowed:", maximum_attempts)


# =====================================================================
# EXERCISE 24: CREATE A DIFFICULTY MENU
# =====================================================================

# QUESTION:
# Allow the user to select a difficulty level.
#
# EXPLANATION:
# Conditions determine which settings
# are assigned to the game.

print("\n" + "=" * 70)
print("EXERCISE 24: DIFFICULTY MENU")
print("=" * 70)

difficulty = input("Choose easy, medium or hard: ").lower()

if difficulty == "easy":

    maximum = 20

    maximum_attempts = 10

elif difficulty == "medium":

    maximum = 50

    maximum_attempts = 7

elif difficulty == "hard":

    maximum = 100

    maximum_attempts = 5

else:

    maximum = 100

    maximum_attempts = 10

    difficulty = "normal"

print("Difficulty:", difficulty)

print("Number range:", maximum)

print("Maximum attempts:", maximum_attempts)


# =====================================================================
# EXERCISE 25: CREATE A HINT SYSTEM
# =====================================================================

# QUESTION:
# Give an additional hint when the guess is close.
#
# EXPLANATION:
# abs() calculates the absolute distance.
#
# A difference of five or less means
# the player is close to the answer.

print("\n" + "=" * 70)
print("EXERCISE 25: HINT SYSTEM")
print("=" * 70)

secret_number = 60

guess = 56

difference = abs(secret_number - guess)

if guess > secret_number:

    print("Too high.")

elif guess < secret_number:

    print("Too low.")

if difference <= 5 and guess != secret_number:

    print("Hint: You are very close!")


# =====================================================================
# EXERCISE 26: BUILD A COMPLETE GUESSING FUNCTION
# =====================================================================

# QUESTION:
# Build a reusable number guessing game.
#
# EXPLANATION:
# A function groups the game logic.
#
# return sends the final result
# back to the part of the program that called it.

print("\n" + "=" * 70)
print("EXERCISE 26: GUESSING FUNCTION")
print("=" * 70)


def guessing_game():

    secret_number = random.randint(1, 20)

    attempts = 0

    while True:

        try:

            guess = int(input("Guess between 1 and 20: "))

        except ValueError:

            print("Enter a valid integer.")

            continue

        if not 1 <= guess <= 20:

            print("Guess must be between 1 and 20.")

            continue

        attempts += 1

        if guess == secret_number:

            print("Correct!")

            print("Attempts:", attempts)

            return attempts

        elif guess > secret_number:

            print("Too high.")

        else:

            print("Too low.")


# Call the function to play.

game_attempts = guessing_game()


# =====================================================================
# EXERCISE 27: BUILD A SCORE FUNCTION
# =====================================================================

# QUESTION:
# Calculate the final game score.
#
# EXPLANATION:
# Fewer attempts produce a higher score.
#
# max() prevents negative scores.

print("\n" + "=" * 70)
print("EXERCISE 27: SCORE FUNCTION")
print("=" * 70)


def calculate_score(attempts):

    maximum_score = 100

    penalty = 10

    final_score = max(0, maximum_score - attempts * penalty)

    return final_score


score = calculate_score(3)

print("Final score:", score)


# =====================================================================
# EXERCISE 28: CREATE A MULTIPLE-ROUND GAME
# =====================================================================

# QUESTION:
# Allow the player to play three rounds.
#
# EXPLANATION:
# The outer while loop controls the rounds.
#
# Each round generates a new secret number.
#
# The inner while loop controls guessing.

print("\n" + "=" * 70)
print("EXERCISE 28: MULTIPLE ROUNDS")
print("=" * 70)

round_number = 1

while round_number <= 3:

    secret_number = random.randint(1, 10)

    attempts = 0

    print("\nROUND", round_number)

    while True:

        try:

            guess = int(input("Guess between 1 and 10: "))

        except ValueError:

            print("Enter a valid number.")

            continue

        if not 1 <= guess <= 10:

            print("Enter a number between 1 and 10.")

            continue

        attempts += 1

        if guess == secret_number:

            print("You won this round!")

            break

        elif guess > secret_number:

            print("Too high.")

        else:

            print("Too low.")

    print("Attempts:", attempts)

    round_number += 1


# =====================================================================
# EXERCISE 29: TRACK BEST PERFORMANCE
# =====================================================================

# QUESTION:
# Track the player's best performance
# across multiple rounds.
#
# EXPLANATION:
# A lower attempt count is better.
#
# We update best_attempts whenever
# the player performs better.
#
# This example runs three rounds.

print("\n" + "=" * 70)
print("EXERCISE 29: BEST PERFORMANCE")
print("=" * 70)

round_number = 1

best_attempts = None

while round_number <= 3:

    secret_number = random.randint(1, 10)

    attempts = 0

    print("\nROUND", round_number)

    while True:

        try:

            guess = int(input("Guess between 1 and 10: "))

        except ValueError:

            print("Invalid input.")

            continue

        if not 1 <= guess <= 10:

            print("Invalid range.")

            continue

        attempts += 1

        if guess == secret_number:

            print("Correct!")

            break

        elif guess > secret_number:

            print("Too high.")

        else:

            print("Too low.")

    print("Attempts this round:", attempts)

    if best_attempts is None or attempts < best_attempts:

        best_attempts = attempts

    print("Best performance so far:", best_attempts)

    round_number += 1

print("\nBest overall attempt count:", best_attempts)


# =====================================================================
# EXERCISE 30: COMPLETE GUESSING GAME ANALYSIS
# =====================================================================

# QUESTION:
# Create a complete guessing game that tracks:
#
# 1. Total rounds.
# 2. Successful rounds.
# 3. Failed rounds.
# 4. Total attempts.
# 5. Average attempts per successful round.
#
# EXPLANATION:
# This combines game development and
# basic statistical analysis.
#
# The game runs for five rounds.
#
# Each round has five attempts.
#
# At the end, we calculate a performance report.

print("\n" + "=" * 70)
print("EXERCISE 30: COMPLETE GAME ANALYSIS")
print("=" * 70)

total_rounds = 5

round_number = 1

successful_rounds = 0

failed_rounds = 0

total_attempts = 0

while round_number <= total_rounds:

    secret_number = random.randint(1, 20)

    attempts = 0

    maximum_attempts = 5

    won = False

    print("\nROUND", round_number)

    while attempts < maximum_attempts:

        try:

            guess = int(input("Guess between 1 and 20: "))

        except ValueError:

            print("Enter a valid integer.")

            continue

        if not 1 <= guess <= 20:

            print("Guess must be between 1 and 20.")

            continue

        attempts += 1

        total_attempts += 1

        if guess == secret_number:

            print("Congratulations! You won.")

            won = True

            break

        elif guess > secret_number:

            print("Too high.")

        else:

            print("Too low.")

    if won:

        successful_rounds += 1

    else:

        failed_rounds += 1

        print("Round lost.")

        print("Secret number:", secret_number)

    print("Attempts used:", attempts)

    round_number += 1


# Calculate game statistics.

if successful_rounds > 0:

    average_attempts = (
        total_attempts / successful_rounds
    )

else:

    average_attempts = 0


win_percentage = (
    successful_rounds / total_rounds
) * 100


# Display the final report.

print("\n" + "=" * 70)

print("FINAL GAME PERFORMANCE REPORT")

print("=" * 70)

print("Total rounds:", total_rounds)

print("Successful rounds:", successful_rounds)

print("Failed rounds:", failed_rounds)

print("Total valid attempts:", total_attempts)

print("Average attempts per successful round:",
      round(average_attempts, 2))

print("Win percentage:", round(win_percentage, 2), "%")

print("=" * 70)


# =====================================================================
# FINAL EXERCISE SUMMARY
# =====================================================================

exercise_names = [

    "Generate Random Number",

    "Generate Five Random Numbers",

    "Random Even Number",

    "Random Four-Digit Code",

    "Dice Simulation",

    "Compare Two Numbers",

    "Check Correct Guess",

    "Validate Guessing Range",

    "High or Low Hint",

    "Close Guess Detection",

    "Basic Guessing Loop",

    "Limited Attempts",

    "Remaining Attempts",

    "Attempt Tracker",

    "Score Calculation",

    "Input Validation",

    "Range Validation",

    "Negative Input Validation",

    "Continue Statement",

    "Replay Question",

    "Easy Difficulty",

    "Medium Difficulty",

    "Hard Difficulty",

    "Difficulty Menu",

    "Hint System",

    "Guessing Function",

    "Score Function",

    "Multiple Rounds",

    "Best Performance",

    "Complete Game Analysis"

]

print("\n" + "=" * 70)

print("DAY 014 - EXERCISES COMPLETED")

print("=" * 70)

index = 0

while index < len(exercise_names):

    print(index + 1, exercise_names[index], "- Completed")

    index += 1

print("\nALL 30 EXERCISES FINISHED!")

print("=" * 70)


# =====================================================================
# END OF DAY 014 - EXERCISES.PY
# =====================================================================
