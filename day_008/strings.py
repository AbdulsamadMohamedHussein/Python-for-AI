
# ================================================================
# DAY 008 - PYTHON STRINGS
#
# Bachelor's in Artificial Intelligence
# 90-Day Python Programming Journey
#
# LESSON: STRINGS IN PYTHON
#
# Topics Covered:
# 1. Introduction to Strings
# 2. Single, Double and Triple Quotes
# 3. String Variables
# 4. String Length
# 5. String Indexing
# 6. Negative Indexing
# 7. String Slicing
# 8. String Concatenation
# 9. String Repetition
# 10. Uppercase and Lowercase
# 11. Removing Spaces
# 12. Replacing Characters
# 13. Finding Characters
# 14. Counting Characters
# 15. Splitting Strings
# 16. Joining Strings
# 17. Checking String Contents
# 18. Membership Operators
# 19. Escape Characters
# 20. F-Strings
#
# ================================================================


# ================================================================
# SECTION 1: INTRODUCTION TO STRINGS
# ================================================================

# A string is a sequence of characters.
#
# Characters can include:
# Letters, numbers, spaces and special symbols.
#
# Strings are written inside quotation marks.

print("=" * 65)

print("DAY 008 - INTRODUCTION TO PYTHON STRINGS")

print("=" * 65)

# Creating string variables.

student_name = "Abdulsamad Mohamed"

student_country = "Pakistan"

student_university = "Guilin University"

student_course = "Artificial Intelligence"

# Display string variables.

print("\nSTUDENT INFORMATION")

print("Name:", student_name)

print("Country:", student_country)

print("University:", student_university)

print("Course:", student_course)


# ================================================================
# SECTION 2: DIFFERENT TYPES OF QUOTATION MARKS
# ================================================================

# Python allows single and double quotation marks.
#
# Both create strings.
# Their behaviour is generally the same.

print("\nSINGLE AND DOUBLE QUOTATION MARKS")

# Single quotation marks.

first_string = 'Learning Python'

# Double quotation marks.

second_string = "Learning Artificial Intelligence"

print(first_string)

print(second_string)

# Triple quotation marks allow multiline strings.

university_description = """
Guilin University
Bachelor's in Artificial Intelligence
Python Programming
"""

print(university_description)

# Triple quotes are also used for documentation strings.


# ================================================================
# SECTION 3: CHECKING STRING DATA TYPES
# ================================================================

# Python provides type() to identify data types.
#
# The str data type represents strings.

print("\nCHECKING STRING DATA TYPES")

name = "Abdulsamad"

course = "AI"

country = "Pakistan"

print(type(name))

print(type(course))

print(type(country))

# All three variables have the str data type.


# ================================================================
# SECTION 4: STRING LENGTH USING len()
# ================================================================

# len() counts the total number of characters.
#
# IMPORTANT:
# Spaces are also counted as characters.

print("\nSTRING LENGTH")

full_name = "Abdulsamad Mohamed"

name_length = len(full_name)

print("Name:", full_name)

print("Total Characters:", name_length)

# Another example.

message = "Python is amazing"

print("Message Length:", len(message))


# ================================================================
# SECTION 5: POSITIVE STRING INDEXING
# ================================================================

# Every character in a string has an index number.
#
# Python indexing starts from ZERO.
#
# Example:
#
# P  Y  T  H  O  N
# 0  1  2  3  4  5

print("\nPOSITIVE STRING INDEXING")

language = "PYTHON"

print("Complete String:", language)

print("Index 0:", language[0])

print("Index 1:", language[1])

print("Index 2:", language[2])

print("Index 3:", language[3])

print("Index 4:", language[4])

print("Index 5:", language[5])

# language[0] returns P.
# language[1] returns Y.
# language[5] returns N.


# ================================================================
# SECTION 6: NEGATIVE STRING INDEXING
# ================================================================

# Negative indexing starts from the END of a string.
#
# Example:
#
# P   Y   T   H   O   N
# -6 -5  -4  -3  -2  -1

print("\nNEGATIVE STRING INDEXING")

language = "PYTHON"

print("Last Character:", language[-1])

print("Second Last:", language[-2])

print("Third Last:", language[-3])

print("First Character:", language[-6])


# ================================================================
# SECTION 7: STRING SLICING
# ================================================================

# Slicing extracts a portion of a string.
#
# Syntax:
#
# string[start:end]
#
# The starting index is INCLUDED.
# The ending index is EXCLUDED.

print("\nSTRING SLICING")

language = "PYTHON"

# Extract characters from index 0 to 2.

print("First Three:", language[0:3])

# Extract characters from index 2 to 5.

print("Middle Section:", language[2:5])

# Extract from the beginning to index 3.

print("Beginning:", language[:3])

# Extract from index 3 to the end.

print("Ending:", language[3:])

# Copy the complete string using slicing.

print("Complete String:", language[:])


# ================================================================
# SECTION 8: SLICING WITH STEP
# ================================================================

# Slicing also supports a step value.
#
# Syntax:
#
# string[start:end:step]
#
# Step determines how many positions Python moves.

print("\nSTRING SLICING WITH STEP")

language = "PYTHON"

# Select every second character.

print("Every Second Character:", language[::2])

# Reverse the string using a negative step.

print("Reversed String:", language[::-1])

# Select characters from index 1 to 5 with step 2.

print("Selected Characters:", language[1:5:2])


# ================================================================
# SECTION 9: STRING CONCATENATION
# ================================================================

# Concatenation means joining strings together.
#
# The + operator joins two or more strings.

print("\nSTRING CONCATENATION")

first_name = "Abdulsamad"

last_name = "Mohamed"

# Join strings with a space.

full_name = first_name + " " + last_name

print("Full Name:", full_name)

# Join additional information.

introduction = "My name is " + full_name

print(introduction)


# ================================================================
# SECTION 10: STRING REPETITION
# ================================================================

# The * operator repeats a string.
#
# For example:
# "Hello" * 3 produces HelloHelloHello.

print("\nSTRING REPETITION")

word = "Python "

print(word * 3)

# Create decorative separators.

print("*" * 40)

print("=" * 40)


# ================================================================
# SECTION 11: UPPERCASE AND LOWERCASE
# ================================================================

# upper() converts letters into uppercase.
#
# lower() converts letters into lowercase.
#
# title() capitalizes the beginning of each word.
#
# capitalize() capitalizes only the first character
# and lowercases the remaining characters.

print("\nUPPERCASE AND LOWERCASE")

text = "python programming for artificial intelligence"

print("Original:", text)

print("Uppercase:", text.upper())

print("Lowercase:", text.lower())

print("Title Case:", text.title())

print("Capitalize:", text.capitalize())


# ================================================================
# SECTION 12: REMOVING SPACES
# ================================================================

# strip() removes spaces from both ends.
#
# lstrip() removes spaces from the left.
#
# rstrip() removes spaces from the right.
#
# These methods do not remove spaces between words.

print("\nREMOVING UNNECESSARY SPACES")

student_name = "   Abdulsamad Mohamed   "

print("Original:", repr(student_name))

print("Strip:", repr(student_name.strip()))

print("Left Strip:", repr(student_name.lstrip()))

print("Right Strip:", repr(student_name.rstrip()))

# repr() makes surrounding spaces easier to see.


# ================================================================
# SECTION 13: REPLACING CHARACTERS
# ================================================================

# replace() replaces one part of a string with another.
#
# Syntax:
#
# string.replace(old, new)
#
# We can optionally specify how many replacements to make.

print("\nSTRING REPLACEMENT")

message = "I am learning Java programming"

# Replace Java with Python.

updated_message = message.replace("Java", "Python")

print("Original:", message)

print("Updated:", updated_message)

# Replace only the first matching occurrence.

sentence = "AI is useful. AI is powerful."

new_sentence = sentence.replace("AI", "Python", 1)

print(new_sentence)


# ================================================================
# SECTION 14: FINDING CHARACTERS AND WORDS
# ================================================================

# find() searches for a word or character.
#
# It returns the index of the first occurrence.
#
# If the text is not found, it returns -1.

print("\nFINDING CHARACTERS AND WORDS")

sentence = "Python is important for Artificial Intelligence"

position = sentence.find("important")

print("Position of important:", position)

position_python = sentence.find("Python")

print("Position of Python:", position_python)

missing_word = sentence.find("Java")

print("Position of Java:", missing_word)


# ================================================================
# SECTION 15: COUNTING CHARACTERS
# ================================================================

# count() counts how many times a character
# or substring appears in a string.

print("\nCOUNTING CHARACTERS")

text = "Artificial Intelligence"

print("Number of i:", text.count("i"))

print("Number of a:", text.count("a"))

print("Number of Intelligence:", text.count("Intelligence"))

# Counting is case-sensitive.
# Uppercase I and lowercase i are different.


# ================================================================
# SECTION 16: SPLITTING STRINGS
# ================================================================

# split() separates a string into a list.
#
# By default, it separates text using whitespace.
#
# We can also provide a separator.

print("\nSPLITTING STRINGS")

student_information = "Abdulsamad,Pakistan,23,AI"

# Split using commas.

student_data = student_information.split(",")

print("Original String:", student_information)

print("Separated Data:", student_data)

# Split a sentence into individual words.

sentence = "Python is important for AI"

words = sentence.split()

print("Words:", words)


# ================================================================
# SECTION 17: JOINING STRINGS
# ================================================================

# join() combines elements of an iterable into one string.
#
# The string before .join() becomes the separator.

print("\nJOINING STRINGS")

words = ["Python", "is", "important", "for", "AI"]

# Join words using spaces.

sentence = " ".join(words)

print("Sentence:", sentence)

# Join words using hyphens.

joined_text = "-".join(words)

print("Hyphenated Text:", joined_text)

# Join words using commas.

comma_text = ", ".join(words)

print("Comma Separated:", comma_text)


# ================================================================
# SECTION 18: CHECKING STRING CONTENTS
# ================================================================

# Python provides methods to check string contents.
#
# isalpha() checks whether all characters are letters.
#
# isdigit() checks whether all characters are digits.
#
# isalnum() checks whether all characters are
# letters or numbers.
#
# isspace() checks whether all characters are whitespace.
#
# islower() checks whether all cased letters are lowercase.
#
# isupper() checks whether all cased letters are uppercase.

print("\nCHECKING STRING CONTENTS")

text = "Python"

number = "12345"

mixed = "Python123"

spaces = "     "

print("Is Alphabetic:", text.isalpha())

print("Is Numeric:", number.isdigit())

print("Is Alphanumeric:", mixed.isalnum())

print("Is Whitespace:", spaces.isspace())

print("Is Lowercase:", text.islower())

print("Is Uppercase:", text.isupper())


# ================================================================
# SECTION 19: MEMBERSHIP OPERATORS
# ================================================================

# The in operator checks whether a character
# or word exists inside a string.
#
# The not in operator checks whether it does not exist.

print("\nSTRING MEMBERSHIP OPERATORS")

sentence = "Artificial Intelligence is the future"

print("Artificial" in sentence)

print("Python" in sentence)

print("Python" not in sentence)

print("future" in sentence)


# ================================================================
# SECTION 20: ESCAPE CHARACTERS
# ================================================================

# Escape characters perform special functions in strings.
#
# \n creates a new line.
#
# \t creates a horizontal tab.
#
# \\ displays a backslash.
#
# \' displays a single quotation mark.
#
# \" displays a double quotation mark.

print("\nESCAPE CHARACTERS")

print("Hello\nWorld")

print("Python\tProgramming")

print("C:\\Users\\Student\\Python")

print('I\'m learning Python')

print("Python says: \"Keep Learning\"")


# ================================================================
# SECTION 21: F-STRINGS
# ================================================================

# F-strings allow us to insert variables
# directly inside strings.
#
# They are useful for creating readable output.
#
# Put the letter f before the quotation mark.

print("\nF-STRINGS")

student = "Abdulsamad"

age = 23

course = "Artificial Intelligence"

print(f"My name is {student}.")

print(f"I am {age} years old.")

print(f"I am studying {course}.")

# F-strings also support calculations.

print(f"Next year I will be {age + 1} years old.")


# ================================================================
# SECTION 22: STRING IMMUTABILITY
# ================================================================

# Strings in Python are IMMUTABLE.
#
# Immutable means that an existing string cannot
# be changed directly character by character.
#
# Instead, we create a new string.

print("\nSTRING IMMUTABILITY")

language = "Python"

# This creates a new string.

updated_language = "J" + language[1:]

print("Original String:", language)

print("New String:", updated_language)

# The original string remains unchanged.


# ================================================================
# SECTION 23: PRACTICAL STRING APPLICATION
# ================================================================

# Now we combine several string methods.
#
# This example processes a student's information.

print("\nPRACTICAL STUDENT INFORMATION PROCESSING")

raw_name = "   abdulsamad mohamed   "

raw_email = "  ABDULSAMAD@GMAIL.COM  "

# Remove unnecessary spaces.

clean_name = raw_name.strip()

clean_email = raw_email.strip()

# Format the name.

formatted_name = clean_name.title()

# Convert email into lowercase.

formatted_email = clean_email.lower()

print("Original Name:", repr(raw_name))

print("Clean Name:", formatted_name)

print("Original Email:", repr(raw_email))

print("Clean Email:", formatted_email)

print("Name Length:", len(formatted_name))

print("Email Contains @:", "@" in formatted_email)


# ================================================================
# SECTION 24: STRINGS IN ARTIFICIAL INTELLIGENCE
# ================================================================

# AI applications frequently process textual data.
#
# For example:
# - Chatbots process user messages.
# - NLP systems analyze sentences.
# - Search engines process search queries.
# - AI systems clean text before analysis.
#
# Below is a simple text-cleaning demonstration.
#
# This is not a trained AI model.
# It demonstrates basic text preprocessing.

print("\nSTRINGS IN ARTIFICIAL INTELLIGENCE")

user_message = "   HELLO! I AM LEARNING PYTHON FOR AI.   "

# Remove surrounding spaces.

clean_message = user_message.strip()

# Convert text to lowercase.

clean_message = clean_message.lower()

# Replace an exclamation mark with a period.

clean_message = clean_message.replace("!", ".")

# Split the message into words.

message_words = clean_message.split()

# Count the words.

word_count = len(message_words)

print("Original Message:", repr(user_message))

print("Cleaned Message:", clean_message)

print("Individual Words:", message_words)

print("Total Words:", word_count)


# ================================================================
# SECTION 25: FINAL LEARNING SUMMARY
# ================================================================

print("\n" + "=" * 65)

print("DAY 008 - PYTHON STRINGS COMPLETED")

print("=" * 65)

print("Introduction to Strings: Completed")

print("String Length: Completed")

print("Positive Indexing: Completed")

print("Negative Indexing: Completed")

print("String Slicing: Completed")

print("String Concatenation: Completed")

print("String Repetition: Completed")

print("Uppercase and Lowercase: Completed")

print("Removing Spaces: Completed")

print("String Replacement: Completed")

print("Finding and Counting: Completed")

print("Splitting and Joining: Completed")

print("Checking String Contents: Completed")

print("Membership Operators: Completed")

print("Escape Characters: Completed")

print("F-Strings: Completed")

print("String Immutability: Completed")

print("AI Text Preprocessing Introduction: Completed")

print("\nKEEP LEARNING PYTHON!")

print("=" * 65)


# ================================================================
# END OF DAY 008 - STRINGS.PY
# ================================================================
