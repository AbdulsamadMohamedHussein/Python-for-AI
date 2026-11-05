
# =====================================================================
# DAY 014 - NUMBER GUESSING GAME
#
# Bachelor's in Artificial Intelligence
# 90-Day Python Programming Journey
#
# MAIN TOPIC:
# RANDOM NUMBER GENERATION AND GAME DEVELOPMENT
#
# LEARNING OBJECTIVES:
# 1. Understand the random module.
# 2. Generate random numbers.
# 3. Use while loops in practical applications.
# 4. Accept and validate user input.
# 5. Apply conditional statements.
# 6. Track user attempts.
# 7. Create difficulty levels.
# 8. Calculate scores.
# 9. Use functions.
# 10. Build an interactive Python game.
#
# =====================================================================


# =====================================================================
# SECTION 1: IMPORTING THE RANDOM MODULE
# =====================================================================

# Python provides a built-in module called random.
#
# The random module allows us to generate
# pseudo-random numbers.
#
# We use it to select a secret number
# that the player must guess.

import random


print("\n" + "=" * 65)

print("WELCOME TO THE NUMBER GUESSING GAME!")

print("=" * 65)


# =====================================================================
# SECTION 2: GENERATING A RANDOM NUMBER
# =====================================================================

# random.randint(start, stop)
#
# This function generates a random integer
# between the starting and stopping values.
#
# IMPORTANT:
# Both boundaries are included.
#
# Therefore:
#
# random.randint(1, 100)
#
# Can generate 1, 2, 3, ..., 100.

secret_number = random.randint(1, 100)

print("A secret number has been generated.")

print("The number is between 1 and 100.")


# =====================================================================
# SECTION 3: INITIALIZING THE GAME VARIABLES
# =====================================================================

# attempts tracks how many guesses
# the player has made.
#
# maximum_attempts controls how many guesses
# the player is allowed.
#
# game_over determines whether the game
# should continue or terminate.

attempts = 0

maximum_attempts = 10

game_over = False


# =====================================================================
# SECTION 4: DISPLAYING GAME INSTRUCTIONS
# =====================================================================

print("\nGAME INSTRUCTIONS")

print("-" * 40)

print("1. Guess a number between 1 and 100.")

print("2. You have 10 attempts.")

print("3. The computer gives you hints.")

print("4. Guess correctly to win!")

print("-" * 40)


# =====================================================================
# SECTION 5: MAIN GAME LOOP
# =====================================================================

# while not game_over:
#
# This means the loop continues as long as
# game_over is False.
#
# The game will stop when:
#
# 1. The player guesses correctly.
# 2. The maximum number of attempts is reached.

while not game_over:

    # Calculate how many attempts remain.

    remaining_attempts = maximum_attempts - attempts

    print("\nAttempts remaining:", remaining_attempts)

    # ---------------------------------------------------------------
    # SECTION 5A: ACCEPTING USER INPUT
    # ---------------------------------------------------------------

    # input() accepts information from the player.
    #
    # We use try and except to handle invalid input.
    #
    # int() converts the entered text into an integer.
    #
    # If the player enters letters, ValueError occurs.

    try:

        guess = int(input("Enter your guess: "))

    except ValueError:

        print("Invalid input!")

        print("Please enter a whole number.")

        # continue skips this iteration.
        # The invalid input does not count as an attempt.

        continue

    # ---------------------------------------------------------------
    # SECTION 5B: CHECKING THE VALID RANGE
    # ---------------------------------------------------------------

    # The player must enter a number
    # between 1 and 100.

    if guess < 1 or guess > 100:

        print("Your guess must be between 1 and 100.")

        continue

    # ---------------------------------------------------------------
    # SECTION 5C: COUNTING ATTEMPTS
    # ---------------------------------------------------------------

    # Only valid guesses count as attempts.

    attempts += 1

    # ---------------------------------------------------------------
    # SECTION 5D: COMPARING THE GUESS
    # ---------------------------------------------------------------

    # There are three possible situations:
    #
    # 1. Guess is greater than the secret number.
    # 2. Guess is smaller than the secret number.
    # 3. Guess equals the secret number.

    if guess > secret_number:

        print("Too high! Try a smaller number.")

    elif guess < secret_number:

        print("Too low! Try a bigger number.")

    else:

        print("\nCONGRATULATIONS!")

        print("You guessed the correct number!")

        print("Secret number:", secret_number)

        print("Attempts used:", attempts)

        # End the game after a correct guess.

        game_over = True

    # ---------------------------------------------------------------
    # SECTION 5E: CHECKING THE ATTEMPT LIMIT
    # ---------------------------------------------------------------

    # If the player has used all attempts
    # without guessing correctly, the game ends.

    if not game_over and attempts >= maximum_attempts:

        print("\nGAME OVER!")

        print("You have used all your attempts.")

        print("The secret number was:", secret_number)

        game_over = True


# =====================================================================
# SECTION 6: FINAL GAME REPORT
# =====================================================================

print("\n" + "=" * 65)

print("GAME SUMMARY")

print("=" * 65)

if attempts > 0:

    print("Total valid guesses:", attempts)

print("Secret number:", secret_number)

print("Thank you for playing!")

print("=" * 65)


# =====================================================================
# SECTION 7: INTRODUCTION TO DIFFICULTY LEVELS
# =====================================================================

# Different games can have different difficulty levels.
#
# Here is an example of how we select
# a maximum number based on difficulty.

print("\nDIFFICULTY LEVEL EXAMPLE")

difficulty = "medium"

if difficulty == "easy":

    upper_limit = 20

    allowed_attempts = 10

elif difficulty == "medium":

    upper_limit = 50

    allowed_attempts = 7

elif difficulty == "hard":

    upper_limit = 100

    allowed_attempts = 5

else:

    upper_limit = 100

    allowed_attempts = 10


print("Selected difficulty:", difficulty)

print("Maximum number:", upper_limit)

print("Allowed attempts:", allowed_attempts)


# =====================================================================
# SECTION 8: UNDERSTANDING SCORE CALCULATION
# =====================================================================

# A simple scoring system can reward players
# who guess correctly using fewer attempts.
#
# This is an introductory scoring formula.
#
# Score = Maximum possible score - Attempts penalty.
#
# We use a lower bound of zero to prevent
# negative scores.

maximum_score = 100

attempt_penalty = 10

score = max(0, maximum_score - attempts * attempt_penalty)


print("\nSCORE CALCULATION")

print("Maximum score:", maximum_score)

print("Attempts used:", attempts)

print("Final score:", score)


# =====================================================================
# SECTION 9: USING FUNCTIONS
# =====================================================================

# Functions organize code into reusable blocks.
#
# This example creates a function
# that generates a new secret number.


def generate_secret_number():

    return random.randint(1, 100)


new_secret = generate_secret_number()

print("\nA new secret number has been generated.")

# We deliberately do not print the actual number
# because the player should not see it!


# =====================================================================
# SECTION 10: SIMPLE GAME RESTART LOGIC
# =====================================================================

# A game can allow the player to restart.
#
# This example demonstrates the logic
# without starting another full game.


play_again = "yes"

if play_again.lower() == "yes":

    print("\nThe game can be restarted!")

else:

    print("\nThank you for playing!")


# =====================================================================
# FINAL LESSON SUMMARY
# =====================================================================

print("\n" + "=" * 65)

print("DAY 014 - NUMBER GUESSING GAME")

print("=" * 65)


topics = [

    "Importing the Random Module",

    "Generating Random Integers",

    "Understanding randint()",

    "Initializing Variables",

    "While Loops",

    "Accepting User Input",

    "Input Validation",

    "Conditional Statements",

    "Comparing Numbers",

    "Tracking Attempts",

    "Using break and continue",

    "Maximum Attempt Limits",

    "Game Termination",

    "Difficulty Levels",

    "Score Calculation",

    "Functions",

    "Game Restart Logic"

]


index = 0

while index < len(topics):

    print(index + 1, topics[index], "- Covered")

    index += 1


print("\nDAY 014 LESSON COMPLETED!")

print("=" * 65)


# =====================================================================
# END OF DAY 014 - NUMBER_GUESSING_GAME.PY
# =====================================================================
