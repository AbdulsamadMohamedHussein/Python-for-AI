
# =================================================================
# DAY 009 - PYTHON STRING METHODS
#
# Bachelor's in Artificial Intelligence
# 90-Day Python Programming Journey
#
# LESSON: STRING METHODS IN PYTHON
#
# OBJECTIVE:
# Learn how to manipulate, clean, search, validate,
# format and process textual information using Python.
#
# TOPICS:
# 1. upper()
# 2. lower()
# 3. capitalize()
# 4. title()
# 5. swapcase()
# 6. strip()
# 7. lstrip()
# 8. rstrip()
# 9. replace()
# 10. find()
# 11. index()
# 12. count()
# 13. startswith()
# 14. endswith()
# 15. split()
# 16. rsplit()
# 17. join()
# 18. partition()
# 19. isalpha()
# 20. isdigit()
# 21. isalnum()
# 22. isspace()
# 23. center()
# 24. zfill()
# 25. islower()
# 26. isupper()
# 27. istitle()
# 28. isdecimal()
# 29. isnumeric()
# 30. removeprefix()
# 31. removesuffix()
#
# =================================================================


# =================================================================
# SECTION 1: INTRODUCTION TO STRING METHODS
# =================================================================

# A string method is a built-in operation that allows
# us to perform an action on a string.
#
# A method is called using dot notation.
#
# Syntax:
#
# string.method()
#
# Example:
#
# name.upper()
#
# IMPORTANT:
# Most string methods return a NEW string.
# They do not modify the original string because
# Python strings are immutable.

print("=" * 70)

print("DAY 009 - PYTHON STRING METHODS")

print("=" * 70)

print("Welcome to Day 009 of our Python learning journey!")


# =================================================================
# SECTION 2: upper()
# =================================================================

# upper() converts all alphabetic characters into uppercase.
#
# It does not modify numbers or punctuation.
#
# Example:
# python becomes PYTHON.

print("\nSECTION 2: UPPER()")

text = "python programming"

uppercase_text = text.upper()

print("Original:", text)

print("Uppercase:", uppercase_text)


# =================================================================
# SECTION 3: lower()
# =================================================================

# lower() converts alphabetic characters into lowercase.
#
# It is useful when comparing text without considering
# uppercase and lowercase differences.

print("\nSECTION 3: LOWER()")

text = "ARTIFICIAL INTELLIGENCE"

lowercase_text = text.lower()

print("Original:", text)

print("Lowercase:", lowercase_text)


# =================================================================
# SECTION 4: capitalize()
# =================================================================

# capitalize() converts the first character to uppercase.
# The remaining cased characters become lowercase.

print("\nSECTION 4: CAPITALIZE()")

text = "pYTHON PROGRAMMING"

result = text.capitalize()

print("Original:", text)

print("Capitalized:", result)


# =================================================================
# SECTION 5: title()
# =================================================================

# title() converts the beginning of each word into uppercase.
#
# Example:
# python programming becomes Python Programming.

print("\nSECTION 5: TITLE()")

text = "learning python for artificial intelligence"

result = text.title()

print("Original:", text)

print("Title Case:", result)


# =================================================================
# SECTION 6: swapcase()
# =================================================================

# swapcase() reverses the case of alphabetic characters.
#
# Uppercase becomes lowercase.
# Lowercase becomes uppercase.

print("\nSECTION 6: SWAPCASE()")

text = "Python PROGRAMMING"

result = text.swapcase()

print("Original:", text)

print("Swapped Case:", result)


# =================================================================
# SECTION 7: strip()
# =================================================================

# strip() removes whitespace from BOTH ends of a string.
#
# It does not remove spaces between words.

print("\nSECTION 7: STRIP()")

student_name = "   Abdulsamad Mohamed   "

print("Original:", repr(student_name))

result = student_name.strip()

print("After Strip:", repr(result))

# repr() helps us see spaces clearly.


# =================================================================
# SECTION 8: lstrip()
# =================================================================

# lstrip() removes whitespace from the LEFT side.

print("\nSECTION 8: LSTRIP()")

text = "     Python Programming"

result = text.lstrip()

print("Original:", repr(text))

print("Left Strip:", repr(result))


# =================================================================
# SECTION 9: rstrip()
# =================================================================

# rstrip() removes whitespace from the RIGHT side.

print("\nSECTION 9: RSTRIP()")

text = "Python Programming     "

result = text.rstrip()

print("Original:", repr(text))

print("Right Strip:", repr(result))


# =================================================================
# SECTION 10: replace()
# =================================================================

# replace() replaces a particular character or substring.
#
# Syntax:
#
# string.replace(old, new, count)
#
# old = text we want to replace.
# new = replacement text.
# count = maximum number of replacements (optional).

print("\nSECTION 10: REPLACE()")

text = "I am learning Java programming."

result = text.replace("Java", "Python")

print("Original:", text)

print("Updated:", result)

# Replace only the first occurrence.

sentence = "AI is useful. AI is powerful. AI is important."

result = sentence.replace("AI", "Python", 1)

print("Limited Replacement:", result)


# =================================================================
# SECTION 11: find()
# =================================================================

# find() searches for a substring.
#
# It returns the index of the first occurrence.
#
# If the substring does not exist, it returns -1.
#
# Unlike index(), find() does not raise an error
# when the substring is missing.

print("\nSECTION 11: FIND()")

text = "Python is important for Artificial Intelligence"

position = text.find("Artificial")

missing_position = text.find("Java")

print("Artificial Position:", position)

print("Java Position:", missing_position)


# =================================================================
# SECTION 12: index()
# =================================================================

# index() searches for a substring.
#
# It returns the position of the first occurrence.
#
# If the substring does not exist, it raises ValueError.

print("\nSECTION 12: INDEX()")

text = "Python Programming"

position = text.index("Programming")

print("Programming Position:", position)

# We use try and except to handle missing text safely.

try:

    missing_position = text.index("Java")

    print(missing_position)

except ValueError:

    print("Java was not found in the string.")


# =================================================================
# SECTION 13: count()
# =================================================================

# count() calculates how many times a substring appears.
#
# Counting is case-sensitive.

print("\nSECTION 13: COUNT()")

text = "Python is amazing. Python is powerful."

print("Python Count:", text.count("Python"))

print("Letter a Count:", text.count("a"))

print("Letter p Count:", text.count("p"))


# =================================================================
# SECTION 14: startswith()
# =================================================================

# startswith() checks whether a string begins
# with a particular character or substring.
#
# It returns True or False.

print("\nSECTION 14: STARTSWITH()")

email = "student@gmail.com"

print("Starts with student:", email.startswith("student"))

print("Starts with admin:", email.startswith("admin"))


# =================================================================
# SECTION 15: endswith()
# =================================================================

# endswith() checks whether a string ends
# with a particular character or substring.

print("\nSECTION 15: ENDSWITH()")

email = "student@gmail.com"

print("Ends with .com:", email.endswith(".com"))

print("Ends with .org:", email.endswith(".org"))


# =================================================================
# SECTION 16: split()
# =================================================================

# split() divides a string into a list.
#
# By default, whitespace is used as the separator.
#
# We can also provide a custom separator.

print("\nSECTION 16: SPLIT()")

sentence = "Python is important for AI"

words = sentence.split()

print("Original:", sentence)

print("Words:", words)

# Split using commas.

student_data = "Abdulsamad,23,Pakistan,AI"

information = student_data.split(",")

print("Student Information:", information)

# maxsplit limits the number of splits.

text = "Python is very useful"

result = text.split(" ", 2)

print("Limited Split:", result)


# =================================================================
# SECTION 17: rsplit()
# =================================================================

# rsplit() works like split().
#
# The difference is that rsplit() splits from the RIGHT.
#
# maxsplit controls how many splits are performed.

print("\nSECTION 17: RSPLIT()")

text = "Python is very useful for AI"

result = text.rsplit(" ", 2)

print("Original:", text)

print("Right Split:", result)


# =================================================================
# SECTION 18: join()
# =================================================================

# join() combines elements of an iterable into a string.
#
# The string before .join() becomes the separator.
#
# Syntax:
#
# separator.join(iterable)

print("\nSECTION 18: JOIN()")

words = ["Python", "is", "important", "for", "AI"]

sentence = " ".join(words)

print("Joined Sentence:", sentence)

# Join using hyphens.

hyphen_text = "-".join(words)

print("Hyphenated Text:", hyphen_text)

# Join using commas.

comma_text = ", ".join(words)

print("Comma Separated:", comma_text)


# =================================================================
# SECTION 19: partition()
# =================================================================

# partition() divides a string into THREE parts.
#
# It returns a tuple containing:
#
# 1. Text before the separator.
# 2. The separator itself.
# 3. Text after the separator.
#
# If the separator is missing, the result is:
# (original_string, '', '')

print("\nSECTION 19: PARTITION()")

email = "student@gmail.com"

result = email.partition("@")

print("Original Email:", email)

print("Partition Result:", result)

print("Username:", result[0])

print("Separator:", result[1])

print("Domain:", result[2])


# =================================================================
# SECTION 20: isalpha()
# =================================================================

# isalpha() returns True if all characters are letters.
#
# Spaces, digits and punctuation make it return False.
#
# The string must contain at least one character.

print("\nSECTION 20: ISALPHA()")

name = "Abdulsamad"

text = "Python123"

print("Name is Alphabetic:", name.isalpha())

print("Text is Alphabetic:", text.isalpha())


# =================================================================
# SECTION 21: isdigit()
# =================================================================

# isdigit() checks whether all characters are digits.
#
# It recognizes certain Unicode digit characters too.
#
# Spaces and punctuation return False.

print("\nSECTION 21: ISDIGIT()")

number = "12345"

mixed = "123ABC"

print("Number is Digit:", number.isdigit())

print("Mixed is Digit:", mixed.isdigit())


# =================================================================
# SECTION 22: isalnum()
# =================================================================

# isalnum() checks whether every character
# is a letter or a number.
#
# Spaces and punctuation return False.

print("\nSECTION 22: ISALNUM()")

text_one = "Python123"

text_two = "Python 123"

print("Python123:", text_one.isalnum())

print("Python 123:", text_two.isalnum())


# =================================================================
# SECTION 23: isspace()
# =================================================================

# isspace() checks whether a string contains
# only whitespace characters.
#
# Whitespace includes spaces, tabs and newlines.

print("\nSECTION 23: ISSPACE()")

text_one = "     "

text_two = "Python"

print("Only Spaces:", text_one.isspace())

print("Python:", text_two.isspace())


# =================================================================
# SECTION 24: islower()
# =================================================================

# islower() checks whether all cased characters
# in the string are lowercase.
#
# The string must contain at least one cased character.

print("\nSECTION 24: ISLOWER()")

text_one = "python programming"

text_two = "Python Programming"

print("Lowercase:", text_one.islower())

print("Mixed Case:", text_two.islower())


# =================================================================
# SECTION 25: isupper()
# =================================================================

# isupper() checks whether all cased characters
# in the string are uppercase.

print("\nSECTION 25: ISUPPER()")

text_one = "PYTHON"

text_two = "Python"

print("Uppercase:", text_one.isupper())

print("Mixed Case:", text_two.isupper())


# =================================================================
# SECTION 26: istitle()
# =================================================================

# istitle() checks whether each word follows
# title-case capitalization rules.
#
# It returns a Boolean value.

print("\nSECTION 26: ISTITLE()")

text_one = "Python Programming"

text_two = "python programming"

print("Title Case:", text_one.istitle())

print("Not Title Case:", text_two.istitle())


# =================================================================
# SECTION 27: isdecimal()
# =================================================================

# isdecimal() checks whether all characters
# are decimal characters.
#
# It is more restrictive than isdigit().

print("\nSECTION 27: ISDECIMAL()")

number = "12345"

print("Is Decimal:", number.isdecimal())

print("Contains Letters:", "123ABC".isdecimal())


# =================================================================
# SECTION 28: isnumeric()
# =================================================================

# isnumeric() checks whether all characters
# are numeric characters.
#
# It recognizes a wider range of Unicode numeric
# characters than isdecimal().

print("\nSECTION 28: ISNUMERIC()")

number = "12345"

print("Is Numeric:", number.isnumeric())


# =================================================================
# SECTION 29: center()
# =================================================================

# center() places a string in the middle
# of a specified width.
#
# Syntax:
#
# string.center(width, fillchar)
#
# fillchar is optional and must be one character.

print("\nSECTION 29: CENTER()")

text = "PYTHON"

result = text.center(30)

print(result)

# Use * to fill the empty positions.

result = text.center(30, "*")

print(result)


# =================================================================
# SECTION 30: zfill()
# =================================================================

# zfill() adds zeros to the LEFT of a string.
#
# The width determines the total length.
#
# It is useful for formatting numerical identifiers.

print("\nSECTION 30: ZFILL()")

student_id = "25"

formatted_id = student_id.zfill(6)

print("Original ID:", student_id)

print("Formatted ID:", formatted_id)


# =================================================================
# SECTION 31: removeprefix()
# =================================================================

# removeprefix() removes a specified prefix
# if the string starts with that prefix.
#
# If the prefix is missing, the original string is returned.

print("\nSECTION 31: REMOVEPREFIX()")

url = "https://www.python.org"

clean_url = url.removeprefix("https://")

print("Original URL:", url)

print("Updated URL:", clean_url)


# =================================================================
# SECTION 32: removesuffix()
# =================================================================

# removesuffix() removes a specified suffix
# if the string ends with that suffix.

print("\nSECTION 32: REMOVESUFFIX()")

filename = "machine_learning.py"

clean_filename = filename.removesuffix(".py")

print("Original Filename:", filename)

print("Updated Filename:", clean_filename)


# =================================================================
# SECTION 33: PRACTICAL EXAMPLE - EMAIL CLEANING
# =================================================================

# In real-world applications, users may enter information
# with unnecessary spaces or inconsistent capitalization.
#
# We can use string methods to clean this information.
#
# This is basic data cleaning, not complete email validation.

print("\nSECTION 33: PRACTICAL EMAIL CLEANING")

raw_email = "   STUDENT@GMAIL.COM   "

# Remove surrounding spaces.

clean_email = raw_email.strip()

# Convert email into lowercase.

clean_email = clean_email.lower()

print("Original Email:", repr(raw_email))

print("Clean Email:", clean_email)

# Check whether it contains @.

if "@" in clean_email and clean_email.count("@") == 1:

    print("Basic Email Format Check: Passed")

else:

    print("Basic Email Format Check: Failed")

# Check the ending.

if clean_email.endswith(".com"):

    print("Email Domain Ending: .com")

else:

    print("Email Domain Ending: Other")


# =================================================================
# SECTION 34: PRACTICAL EXAMPLE - STUDENT DATA CLEANING
# =================================================================

# Imagine a student record arrives from a dataset.
#
# The information contains unnecessary spaces
# and inconsistent capitalization.
#
# We will clean the information.

print("\nSECTION 34: STUDENT DATA CLEANING")

raw_student_name = "   ABDULSAMAD MOHAMED   "

raw_country = "   pAkIsTaN   "

raw_course = "   artificial intelligence   "

# Clean student name.

student_name = raw_student_name.strip().title()

# Clean country.

country = raw_country.strip().title()

# Clean course.

course = raw_course.strip().title()

print("Student Name:", student_name)

print("Country:", country)

print("Course:", course)


# =================================================================
# SECTION 35: PRACTICAL EXAMPLE - TEXT ANALYSIS
# =================================================================

# We will combine several string methods.
#
# The program will:
# 1. Clean the sentence.
# 2. Convert it to lowercase.
# 3. Split it into words.
# 4. Count the words.
# 5. Search for Python.
# 6. Join the words again.

print("\nSECTION 35: PRACTICAL TEXT ANALYSIS")

sentence = "   PYTHON is useful for Artificial Intelligence.   "

# Clean unnecessary spaces.

clean_sentence = sentence.strip()

# Convert to lowercase.

clean_sentence = clean_sentence.lower()

# Split into individual words.

words = clean_sentence.split()

# Count words.

total_words = len(words)

# Search for Python.

python_exists = "python" in words

# Join the words.

final_sentence = " ".join(words)

print("Original:", repr(sentence))

print("Cleaned:", clean_sentence)

print("Words:", words)

print("Total Words:", total_words)

print("Python Exists:", python_exists)

print("Final Sentence:", final_sentence)


# =================================================================
# SECTION 36: FINAL LEARNING SUMMARY
# =================================================================

print("\n" + "=" * 70)

print("DAY 009 - PYTHON STRING METHODS COMPLETED")

print("=" * 70)

print("upper(): Completed")

print("lower(): Completed")

print("capitalize(): Completed")

print("title(): Completed")

print("swapcase(): Completed")

print("strip(): Completed")

print("lstrip(): Completed")

print("rstrip(): Completed")

print("replace(): Completed")

print("find(): Completed")

print("index(): Completed")

print("count(): Completed")

print("startswith(): Completed")

print("endswith(): Completed")

print("split(): Completed")

print("rsplit(): Completed")

print("join(): Completed")

print("partition(): Completed")

print("isalpha(): Completed")

print("isdigit(): Completed")

print("isalnum(): Completed")

print("isspace(): Completed")

print("islower(): Completed")

print("isupper(): Completed")

print("istitle(): Completed")

print("isdecimal(): Completed")

print("isnumeric(): Completed")

print("center(): Completed")

print("zfill(): Completed")

print("removeprefix(): Completed")

print("removesuffix(): Completed")

print("Practical Text Cleaning: Completed")

print("Practical Student Data Cleaning: Completed")

print("Practical Text Analysis: Completed")

print("\nKEEP LEARNING PYTHON!")

print("=" * 70)


# =================================================================
# END OF DAY 009 - STRING_METHODS.PY
# =================================================================
