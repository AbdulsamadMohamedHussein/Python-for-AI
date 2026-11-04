
# =================================================================
# DAY 009 - PYTHON STRING METHODS
# SOLVED EXERCISES
#
# Bachelor's in Artificial Intelligence
# 90-Day Python Programming Journey
#
# TOTAL: 25 SOLVED EXERCISES
#
# Topics:
# Uppercase, Lowercase, Capitalization, String Cleaning,
# Replacement, Searching, Counting, Splitting, Joining,
# Validation, Formatting and AI Text Preprocessing.
#
# =================================================================


# =================================================================
# EXERCISE 1: CONVERT TEXT INTO UPPERCASE
# =================================================================

# QUESTION:
# Create a variable containing a lowercase sentence.
# Convert the complete sentence into uppercase.
#
# CONCEPT:
# upper() converts all alphabetic characters into uppercase.

print("\n" + "=" * 70)
print("EXERCISE 1: UPPERCASE")
print("=" * 70)

sentence = "learning python for artificial intelligence"

# Apply upper() to convert the sentence.

uppercase_sentence = sentence.upper()

print("Original Sentence:", sentence)

print("Uppercase Sentence:", uppercase_sentence)


# =================================================================
# EXERCISE 2: CONVERT TEXT INTO LOWERCASE
# =================================================================

# QUESTION:
# Convert an uppercase sentence into lowercase.
#
# CONCEPT:
# lower() converts alphabetic characters into lowercase.
# This is useful when comparing text without considering
# differences between uppercase and lowercase.

print("\n" + "=" * 70)
print("EXERCISE 2: LOWERCASE")
print("=" * 70)

sentence = "ARTIFICIAL INTELLIGENCE IS THE FUTURE"

lowercase_sentence = sentence.lower()

print("Original:", sentence)

print("Lowercase:", lowercase_sentence)


# =================================================================
# EXERCISE 3: CAPITALIZE A SENTENCE
# =================================================================

# QUESTION:
# Capitalize the first character of a sentence.
#
# CONCEPT:
# capitalize() converts the first character to uppercase
# and the remaining cased characters to lowercase.

print("\n" + "=" * 70)
print("EXERCISE 3: CAPITALIZE")
print("=" * 70)

sentence = "pYTHON PROGRAMMING IS INTERESTING"

result = sentence.capitalize()

print("Original:", sentence)

print("Capitalized:", result)


# =================================================================
# EXERCISE 4: CONVERT TEXT INTO TITLE CASE
# =================================================================

# QUESTION:
# Convert a sentence so that each word starts
# with an uppercase letter.
#
# CONCEPT:
# title() applies title-case formatting to words.

print("\n" + "=" * 70)
print("EXERCISE 4: TITLE CASE")
print("=" * 70)

sentence = "learning python for machine learning"

result = sentence.title()

print("Original:", sentence)

print("Title Case:", result)


# =================================================================
# EXERCISE 5: SWAP UPPERCASE AND LOWERCASE
# =================================================================

# QUESTION:
# Change uppercase letters into lowercase
# and lowercase letters into uppercase.
#
# CONCEPT:
# swapcase() reverses the case of alphabetic characters.

print("\n" + "=" * 70)
print("EXERCISE 5: SWAPCASE")
print("=" * 70)

text = "Python PROGRAMMING For AI"

result = text.swapcase()

print("Original:", text)

print("Swapped Case:", result)


# =================================================================
# EXERCISE 6: REMOVE SPACES USING strip()
# =================================================================

# QUESTION:
# Remove unnecessary spaces from the beginning
# and end of a student's name.
#
# CONCEPT:
# strip() removes surrounding whitespace.
# It does not remove spaces between words.

print("\n" + "=" * 70)
print("EXERCISE 6: STRIP")
print("=" * 70)

student_name = "     Abdulsamad Mohamed     "

# repr() makes the surrounding spaces visible.

print("Original:", repr(student_name))

clean_name = student_name.strip()

print("Clean Name:", repr(clean_name))


# =================================================================
# EXERCISE 7: REMOVE LEFT AND RIGHT SPACES
# =================================================================

# QUESTION:
# Demonstrate lstrip() and rstrip().
#
# CONCEPT:
# lstrip() removes whitespace from the left.
# rstrip() removes whitespace from the right.

print("\n" + "=" * 70)
print("EXERCISE 7: LSTRIP AND RSTRIP")
print("=" * 70)

text = "     Python Programming     "

left_cleaned = text.lstrip()

right_cleaned = text.rstrip()

print("Original:", repr(text))

print("Left Cleaned:", repr(left_cleaned))

print("Right Cleaned:", repr(right_cleaned))


# =================================================================
# EXERCISE 8: REPLACE A WORD
# =================================================================

# QUESTION:
# Replace Java with Python in a sentence.
#
# CONCEPT:
# replace(old, new) creates a new string with
# the specified replacement.

print("\n" + "=" * 70)
print("EXERCISE 8: REPLACE")
print("=" * 70)

sentence = "I am learning Java programming."

updated_sentence = sentence.replace("Java", "Python")

print("Original:", sentence)

print("Updated:", updated_sentence)


# =================================================================
# EXERCISE 9: REPLACE ONLY THE FIRST OCCURRENCE
# =================================================================

# QUESTION:
# Replace only the first occurrence of AI with Python.
#
# CONCEPT:
# replace(old, new, count) allows us to limit
# the number of replacements.

print("\n" + "=" * 70)
print("EXERCISE 9: LIMITED REPLACEMENT")
print("=" * 70)

sentence = "AI is powerful. AI is useful. AI is important."

# The third argument 1 means replace only once.

result = sentence.replace("AI", "Python", 1)

print("Original:", sentence)

print("Updated:", result)


# =================================================================
# EXERCISE 10: FIND THE POSITION OF A WORD
# =================================================================

# QUESTION:
# Find the position of Python in a sentence.
#
# CONCEPT:
# find() returns the starting index of the first match.
# It returns -1 if the substring is not found.

print("\n" + "=" * 70)
print("EXERCISE 10: FIND")
print("=" * 70)

sentence = "Python is important for Artificial Intelligence."

position = sentence.find("Python")

print("Sentence:", sentence)

print("Python Position:", position)


# =================================================================
# EXERCISE 11: COMPARE find() AND index()
# =================================================================

# QUESTION:
# Search for a word that does not exist.
# Demonstrate the difference between find() and index().
#
# CONCEPT:
# find() returns -1 when the text is missing.
# index() raises ValueError when the text is missing.
#
# try and except allow us to handle that error.

print("\n" + "=" * 70)
print("EXERCISE 11: FIND AND INDEX")
print("=" * 70)

sentence = "Python is useful for AI."

# find() does not raise an error.

print("find() Result:", sentence.find("Java"))

# index() raises ValueError if Java is missing.

try:

    position = sentence.index("Java")

    print("index() Result:", position)

except ValueError:

    print("index() Result: Java was not found.")


# =================================================================
# EXERCISE 12: COUNT WORD OCCURRENCES
# =================================================================

# QUESTION:
# Count how many times Python appears in a sentence.
#
# CONCEPT:
# count() counts occurrences of a character or substring.
# String counting is case-sensitive.

print("\n" + "=" * 70)
print("EXERCISE 12: COUNT")
print("=" * 70)

sentence = "Python is useful. Python is powerful. Python is popular."

python_count = sentence.count("Python")

print("Sentence:", sentence)

print("Python Occurrences:", python_count)


# =================================================================
# EXERCISE 13: CHECK STARTING TEXT
# =================================================================

# QUESTION:
# Check whether an email address starts with student.
#
# CONCEPT:
# startswith() returns True if the string begins
# with the specified substring.

print("\n" + "=" * 70)
print("EXERCISE 13: STARTSWITH")
print("=" * 70)

email = "student@gmail.com"

result = email.startswith("student")

print("Email:", email)

print("Starts with student:", result)


# =================================================================
# EXERCISE 14: CHECK ENDING TEXT
# =================================================================

# QUESTION:
# Check whether a filename ends with .py.
#
# CONCEPT:
# endswith() checks the ending of a string.
# It returns True or False.

print("\n" + "=" * 70)
print("EXERCISE 14: ENDSWITH")
print("=" * 70)

filename = "machine_learning.py"

result = filename.endswith(".py")

print("Filename:", filename)

print("Is Python File:", result)


# =================================================================
# EXERCISE 15: SPLIT A SENTENCE
# =================================================================

# QUESTION:
# Separate a sentence into individual words.
#
# CONCEPT:
# split() divides a string into a list.
# By default, whitespace is used as the separator.

print("\n" + "=" * 70)
print("EXERCISE 15: SPLIT")
print("=" * 70)

sentence = "Python is important for Artificial Intelligence"

words = sentence.split()

print("Original Sentence:", sentence)

print("Separated Words:", words)

print("First Word:", words[0])

print("Last Word:", words[-1])


# =================================================================
# EXERCISE 16: SPLIT USING A CUSTOM SEPARATOR
# =================================================================

# QUESTION:
# Separate student information using commas.
#
# CONCEPT:
# split(",") separates the string wherever a comma appears.

print("\n" + "=" * 70)
print("EXERCISE 16: CUSTOM SPLIT")
print("=" * 70)

student_record = "Abdulsamad,23,Pakistan,Artificial Intelligence"

student_information = student_record.split(",")

print("Original Record:", student_record)

print("Student Information:", student_information)

# Access individual values from the resulting list.

print("Name:", student_information[0])

print("Age:", student_information[1])

print("Country:", student_information[2])

print("Course:", student_information[3])


# =================================================================
# EXERCISE 17: SPLIT FROM THE RIGHT
# =================================================================

# QUESTION:
# Split a sentence into two parts from the right.
#
# CONCEPT:
# rsplit() works like split(), but processes separators
# from the right when a maximum split count is specified.

print("\n" + "=" * 70)
print("EXERCISE 17: RSPLIT")
print("=" * 70)

sentence = "Python is very useful for AI"

result = sentence.rsplit(" ", 2)

print("Original:", sentence)

print("Right Split:", result)


# =================================================================
# EXERCISE 18: JOIN WORDS
# =================================================================

# QUESTION:
# Join individual words into one complete sentence.
#
# CONCEPT:
# join() combines iterable elements into a string.
# The string before .join() becomes the separator.

print("\n" + "=" * 70)
print("EXERCISE 18: JOIN")
print("=" * 70)

words = ["Python", "is", "important", "for", "AI"]

# Join using spaces.

sentence = " ".join(words)

print("Sentence:", sentence)

# Join using hyphens.

hyphen_sentence = "-".join(words)

print("Hyphenated:", hyphen_sentence)

# Join using commas.

comma_sentence = ", ".join(words)

print("Comma Separated:", comma_sentence)


# =================================================================
# EXERCISE 19: PARTITION AN EMAIL ADDRESS
# =================================================================

# QUESTION:
# Divide an email address into username,
# separator and domain.
#
# CONCEPT:
# partition() returns a tuple of three elements:
# text before separator, separator, text after separator.

print("\n" + "=" * 70)
print("EXERCISE 19: PARTITION")
print("=" * 70)

email = "student@gmail.com"

result = email.partition("@")

print("Original Email:", email)

print("Partition Result:", result)

print("Username:", result[0])

print("Separator:", result[1])

print("Domain:", result[2])


# =================================================================
# EXERCISE 20: VALIDATE STRING CONTENTS
# =================================================================

# QUESTION:
# Check whether strings contain letters, digits,
# or a combination of letters and digits.
#
# CONCEPT:
# isalpha() checks letters only.
# isdigit() checks digit characters.
# isalnum() checks letters or digits without spaces.

print("\n" + "=" * 70)
print("EXERCISE 20: STRING VALIDATION")
print("=" * 70)

name = "Abdulsamad"

number = "12345"

student_id = "AI12345"

invalid_text = "AI 12345"

print("Name is Alphabetic:", name.isalpha())

print("Number is Numeric:", number.isdigit())

print("Student ID is Alphanumeric:", student_id.isalnum())

print("Text with Space is Alphanumeric:", invalid_text.isalnum())


# =================================================================
# EXERCISE 21: CHECK STRING CASE
# =================================================================

# QUESTION:
# Check whether a string is lowercase, uppercase
# or follows title-case formatting.
#
# CONCEPT:
# islower(), isupper() and istitle() return Boolean values.

print("\n" + "=" * 70)
print("EXERCISE 21: CASE VALIDATION")
print("=" * 70)

lower_text = "python programming"

upper_text = "PYTHON PROGRAMMING"

title_text = "Python Programming"

print("Lowercase:", lower_text.islower())

print("Uppercase:", upper_text.isupper())

print("Title Case:", title_text.istitle())


# =================================================================
# EXERCISE 22: FORMAT A STUDENT ID USING zfill()
# =================================================================

# QUESTION:
# Convert the student ID 125 into a six-character ID
# by adding zeros to the beginning.
#
# CONCEPT:
# zfill(width) adds leading zeros until the string
# reaches the specified width.

print("\n" + "=" * 70)
print("EXERCISE 22: ZFILL")
print("=" * 70)

student_id = "125"

formatted_id = student_id.zfill(6)

print("Original ID:", student_id)

print("Formatted ID:", formatted_id)


# =================================================================
# EXERCISE 23: CENTER TEXT
# =================================================================

# QUESTION:
# Display PYTHON in the center of a field
# with a total width of 30 characters.
#
# CONCEPT:
# center() places a string in the middle of a field.
# The optional second argument specifies the fill character.

print("\n" + "=" * 70)
print("EXERCISE 23: CENTER")
print("=" * 70)

text = "PYTHON"

result = text.center(30, "*")

print(result)


# =================================================================
# EXERCISE 24: REMOVE PREFIX AND SUFFIX
# =================================================================

# QUESTION:
# Remove https:// from a URL.
# Remove .py from a filename.
#
# CONCEPT:
# removeprefix() removes matching text from the beginning.
# removesuffix() removes matching text from the end.

print("\n" + "=" * 70)
print("EXERCISE 24: PREFIX AND SUFFIX")
print("=" * 70)

url = "https://www.python.org"

filename = "machine_learning.py"

clean_url = url.removeprefix("https://")

clean_filename = filename.removesuffix(".py")

print("Original URL:", url)

print("Clean URL:", clean_url)

print("Original Filename:", filename)

print("Clean Filename:", clean_filename)


# =================================================================
# EXERCISE 25: AI TEXT PREPROCESSING
# =================================================================

# QUESTION:
# A user provides a message containing:
# - Unnecessary spaces.
# - Uppercase letters.
# - Repeated words.
# - Unnecessary punctuation.
#
# Clean the message using multiple string methods.
#
# CONCEPT:
# Text preprocessing is an important part of
# Natural Language Processing (NLP).
#
# Our task is a basic rule-based text-cleaning example.
# It is not a trained AI model.

print("\n" + "=" * 70)
print("EXERCISE 25: AI TEXT PREPROCESSING")
print("=" * 70)

# Original message.

raw_message = "   PYTHON is AMAZING! Python is useful!   "

print("Original Message:", repr(raw_message))

# STEP 1:
# Remove unnecessary spaces from both ends.

clean_message = raw_message.strip()

# STEP 2:
# Convert the message to lowercase.

clean_message = clean_message.lower()

# STEP 3:
# Replace exclamation marks with periods.

clean_message = clean_message.replace("!", ".")

# STEP 4:
# Split the sentence into individual words.

words = clean_message.split()

# STEP 5:
# Count the total number of words.

total_words = len(words)

# STEP 6:
# Count how many times python appears.

python_count = words.count("python")

# STEP 7:
# Join the words back into one sentence.

final_message = " ".join(words)

# Display the final results.

print("Cleaned Message:", clean_message)

print("Individual Words:", words)

print("Total Words:", total_words)

print("Python Occurrences:", python_count)

print("Final Message:", final_message)


# =================================================================
# FINAL EXERCISE SUMMARY
# =================================================================

print("\n" + "=" * 70)

print("DAY 009 - SOLVED EXERCISES SUMMARY")

print("=" * 70)

print("1. Uppercase - Completed")

print("2. Lowercase - Completed")

print("3. Capitalize - Completed")

print("4. Title Case - Completed")

print("5. Swapcase - Completed")

print("6. Strip - Completed")

print("7. Lstrip and Rstrip - Completed")

print("8. Replace - Completed")

print("9. Limited Replacement - Completed")

print("10. Find - Completed")

print("11. Find and Index - Completed")

print("12. Count - Completed")

print("13. Startswith - Completed")

print("14. Endswith - Completed")

print("15. Split - Completed")

print("16. Custom Split - Completed")

print("17. Rsplit - Completed")

print("18. Join - Completed")

print("19. Partition - Completed")

print("20. String Validation - Completed")

print("21. Case Validation - Completed")

print("22. Zfill - Completed")

print("23. Center - Completed")

print("24. Prefix and Suffix - Completed")

print("25. AI Text Preprocessing - Completed")

print("\nALL 25 EXERCISES COMPLETED SUCCESSFULLY!")

print("=" * 70)


# =================================================================
# END OF DAY 009 - EXERCISES.PY
# =================================================================
