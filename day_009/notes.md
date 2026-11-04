
# DAY 009 - PYTHON STRING METHODS

## Bachelor's in Artificial Intelligence
### 90-Day Python Programming Journey

---

# 1. Introduction to String Methods

String methods are built-in Python operations that
allow us to manipulate, clean, search and validate text.

A method is called using dot notation.

Syntax:

```python
string.method()
```

Example:

```python
name = "abdulsamad"

print(name.upper())
```

Output:

```text
ABDULSAMAD
```

Important:

- String methods are called using dot notation.
- Most string methods return a new string or another value.
- Python strings are immutable.
- Methods do not modify the original string directly.

---

# 2. Changing Letter Cases

Python provides several methods for changing
uppercase and lowercase characters.

## upper()

Converts all alphabetic characters into uppercase.

```python
text = "python programming"

print(text.upper())
```

Output:

```text
PYTHON PROGRAMMING
```

## lower()

Converts alphabetic characters into lowercase.

```python
text = "PYTHON PROGRAMMING"

print(text.lower())
```

Output:

```text
python programming
```

## capitalize()

Converts the first character to uppercase
and the remaining cased characters to lowercase.

```python
text = "pYTHON PROGRAMMING"

print(text.capitalize())
```

Output:

```text
Python programming
```

## title()

Capitalizes the beginning of each word
according to Python's title-case rules.

```python
text = "learning python programming"

print(text.title())
```

Output:

```text
Learning Python Programming
```

## swapcase()

Changes uppercase characters into lowercase
and lowercase characters into uppercase.

```python
text = "Python PROGRAMMING"

print(text.swapcase())
```

Output:

```text
pYTHON programming
```

### Comparison Table

| Method | Purpose |
|---|---|
| upper() | Converts to uppercase |
| lower() | Converts to lowercase |
| capitalize() | Capitalizes first character |
| title() | Applies title case |
| swapcase() | Reverses letter cases |

---

# 3. Removing Unnecessary Spaces

Python provides three important methods
for removing surrounding whitespace.

## strip()

Removes whitespace from both ends.

```python
name = "   Abdulsamad   "

print(name.strip())
```

Output:

```text
Abdulsamad
```

## lstrip()

Removes whitespace from the left side.

```python
name = "   Python"

print(name.lstrip())
```

## rstrip()

Removes whitespace from the right side.

```python
name = "Python   "

print(name.rstrip())
```

Important:

These methods do not remove spaces
between words.

### Comparison Table

| Method | Purpose |
|---|---|
| strip() | Removes whitespace from both ends |
| lstrip() | Removes left whitespace |
| rstrip() | Removes right whitespace |

---

# 4. replace()

The replace() method replaces a character
or substring with another value.

Syntax:

```python
string.replace(old, new, count)
```

Parameters:

- old: Text we want to replace.
- new: Replacement text.
- count: Maximum number of replacements (optional).

Example:

```python
text = "I am learning Java"

result = text.replace("Java", "Python")

print(result)
```

Output:

```text
I am learning Python
```

### Limited Replacement

```python
text = "AI is useful. AI is powerful."

result = text.replace("AI", "Python", 1)

print(result)
```

Output:

```text
Python is useful. AI is powerful.
```

---

# 5. find()

find() searches for a substring.

It returns the starting index of the first occurrence.

If the substring does not exist, it returns -1.

Example:

```python
text = "Python is important for AI"

print(text.find("Python"))

print(text.find("Java"))
```

Output:

```text
0
-1
```

Important:

find() does not raise an error when text is missing.

---

# 6. index()

index() searches for a substring and returns
the position of its first occurrence.

Example:

```python
text = "Python Programming"

print(text.index("Programming"))
```

Output:

```text
7
```

If the substring does not exist, index()
raises a ValueError.

### Difference Between find() and index()

| find() | index() |
|---|---|
| Searches for text | Searches for text |
| Returns position | Returns position |
| Missing text returns -1 | Missing text raises ValueError |
| Does not raise ValueError for missing text | Raises ValueError |

Example:

```python
text = "Python Programming"

print(text.find("Java"))

# This raises ValueError:
# print(text.index("Java"))
```

---

# 7. count()

count() counts how many times a character
or substring appears.

Example:

```python
text = "Python is amazing. Python is powerful."

print(text.count("Python"))

print(text.count("a"))
```

Output:

```text
2
3
```

Important:

String counting is case-sensitive.

---

# 8. startswith()

Checks whether a string begins with
a specified character or substring.

Example:

```python
email = "student@gmail.com"

print(email.startswith("student"))

print(email.startswith("admin"))
```

Output:

```text
True
False
```

---

# 9. endswith()

Checks whether a string ends with
a specified character or substring.

Example:

```python
filename = "machine_learning.py"

print(filename.endswith(".py"))

print(filename.endswith(".txt"))
```

Output:

```text
True
False
```

### Comparison

| Method | Purpose |
|---|---|
| startswith() | Checks beginning |
| endswith() | Checks ending |

Both return Boolean values: True or False.

---

# 10. split()

split() divides a string into smaller strings
and returns a list.

Syntax:

```python
string.split(separator, maxsplit)
```

Example:

```python
sentence = "Python is important for AI"

words = sentence.split()

print(words)
```

Output:

```text
['Python', 'is', 'important', 'for', 'AI']
```

### Custom Separator

```python
student = "Abdulsamad,23,Pakistan"

information = student.split(",")

print(information)
```

Output:

```text
['Abdulsamad', '23', 'Pakistan']
```

### maxsplit

maxsplit controls the maximum number of splits.

```python
text = "Python is very useful"

print(text.split(" ", 2))
```

Output:

```text
['Python', 'is', 'very useful']
```

---

# 11. rsplit()

rsplit() works like split(), but performs
splitting from the right when maxsplit is limited.

Example:

```python
text = "Python is very useful"

print(text.rsplit(" ", 2))
```

Output:

```text
['Python is', 'very', 'useful']
```

### Difference Between split() and rsplit()

| split() | rsplit() |
|---|---|
| Splits from the left | Splits from the right |
| maxsplit limits splits from the left | maxsplit limits splits from the right |
| Returns a list | Returns a list |

---

# 12. join()

join() combines elements of an iterable
into one string.

Syntax:

```python
separator.join(iterable)
```

Example:

```python
words = ["Python", "is", "important"]

sentence = " ".join(words)

print(sentence)
```

Output:

```text
Python is important
```

Different separators:

```python
print("-".join(words))

print(", ".join(words))
```

Output:

```text
Python-is-important
Python, is, important
```

Important:

All elements being joined must be strings.

---

# 13. partition()

partition() divides a string into three parts.

It returns a tuple containing:

1. Text before the separator.
2. The separator itself.
3. Text after the separator.

Example:

```python
email = "student@gmail.com"

result = email.partition("@")

print(result)
```

Output:

```text
('student', '@', 'gmail.com')
```

We can access individual elements:

```python
print(result[0])
print(result[1])
print(result[2])
```

Output:

```text
student
@
gmail.com
```

If the separator is missing, partition()
returns the original string followed by two empty strings.

---

# 14. Checking String Contents

Python provides methods that check
whether strings contain particular characters.

These methods return Boolean values.

## isalpha()

Checks whether all characters are alphabetic.

```python
print("Python".isalpha())
```

Output:

```text
True
```

Spaces and digits make it return False.

## isdigit()

Checks whether all characters are digits.

```python
print("12345".isdigit())
```

Output:

```text
True
```

## isalnum()

Checks whether all characters are letters or numbers.

```python
print("Python123".isalnum())
```

Output:

```text
True
```

Spaces and punctuation return False.

## isspace()

Checks whether all characters are whitespace.

```python
print("     ".isspace())
```

Output:

```text
True
```

## islower()

Checks whether all cased characters are lowercase.

```python
print("python".islower())
```

Output:

```text
True
```

## isupper()

Checks whether all cased characters are uppercase.

```python
print("PYTHON".isupper())
```

Output:

```text
True
```

## istitle()

Checks whether the string follows title-case rules.

```python
print("Python Programming".istitle())
```

Output:

```text
True
```

### Validation Comparison Table

| Method | Purpose |
|---|---|
| isalpha() | Checks letters |
| isdigit() | Checks digit characters |
| isalnum() | Checks letters and digits |
| isspace() | Checks whitespace |
| islower() | Checks lowercase |
| isupper() | Checks uppercase |
| istitle() | Checks title case |

Important:

These methods generally require a non-empty string
to return True.

---

# 15. isdecimal()

isdecimal() checks whether every character
is a decimal character.

Example:

```python
print("12345".isdecimal())
```

Output:

```text
True
```

It is more restrictive than isdigit().

---

# 16. isnumeric()

isnumeric() checks whether every character
is numeric.

It recognizes a wider range of Unicode
numeric characters than isdecimal().

Example:

```python
print("12345".isnumeric())
```

Output:

```text
True
```

### Difference Between isdecimal(), isdigit() and isnumeric()

| Method | Recognition |
|---|---|
| isdecimal() | Decimal characters |
| isdigit() | Decimal digits and additional digit characters |
| isnumeric() | A broader range of numeric characters |

Example:

```python
print("123".isdecimal())  # True
print("123".isdigit())    # True
print("123".isnumeric())  # True

print("²".isdecimal())    # False
print("²".isdigit())      # True
print("²".isnumeric())    # True
```

---

# 17. center()

center() places text in the middle
of a specified width.

Syntax:

```python
string.center(width, fillchar)
```

Example:

```python
text = "PYTHON"

print(text.center(20))
```

We can also specify a fill character:

```python
print(text.center(20, "*"))
```

The total output width is 20 characters.

---

# 18. zfill()

zfill() adds zeros to the beginning
of a string until it reaches the requested width.

Example:

```python
student_id = "125"

print(student_id.zfill(6))
```

Output:

```text
000125
```

This method is useful for formatting identifiers.

---

# 19. removeprefix()

removeprefix() removes a specified prefix
if the string begins with it.

Example:

```python
url = "https://www.python.org"

result = url.removeprefix("https://")

print(result)
```

Output:

```text
www.python.org
```

If the prefix does not exist,
the original string is returned.

---

# 20. removesuffix()

removesuffix() removes a specified suffix
if the string ends with it.

Example:

```python
filename = "machine_learning.py"

result = filename.removesuffix(".py")

print(result)
```

Output:

```text
machine_learning
```

If the suffix does not exist,
the original string is returned.

---

# 21. Important String Methods Summary

| Method | Main Purpose |
|---|---|
| upper() | Uppercase |
| lower() | Lowercase |
| capitalize() | Capitalize first character |
| title() | Title case |
| swapcase() | Reverse letter cases |
| strip() | Remove surrounding whitespace |
| lstrip() | Remove left whitespace |
| rstrip() | Remove right whitespace |
| replace() | Replace text |
| find() | Search for text |
| index() | Search or raise ValueError |
| count() | Count occurrences |
| startswith() | Check beginning |
| endswith() | Check ending |
| split() | Split from left |
| rsplit() | Split from right |
| join() | Combine strings |
| partition() | Divide into three parts |
| isalpha() | Check alphabetic characters |
| isdigit() | Check digit characters |
| isalnum() | Check letters and digits |
| isspace() | Check whitespace |
| islower() | Check lowercase |
| isupper() | Check uppercase |
| istitle() | Check title case |
| isdecimal() | Check decimal characters |
| isnumeric() | Check numeric characters |
| center() | Center text |
| zfill() | Add leading zeros |
| removeprefix() | Remove prefix |
| removesuffix() | Remove suffix |

---

# 22. Method Chaining

Method chaining means applying multiple
string methods in a single expression.

Example:

```python
email = "   STUDENT@GMAIL.COM   "

clean_email = email.strip().lower()

print(clean_email)
```

Output:

```text
student@gmail.com
```

Explanation:

1. strip() removes surrounding spaces.
2. lower() converts the remaining text to lowercase.

Method chaining makes code shorter and readable.

---

# 23. Practical Applications of String Methods

String methods are used in many real-world applications.

### A. Email Cleaning

```python
email = " STUDENT@GMAIL.COM "

clean_email = email.strip().lower()

print(clean_email)
```

### B. Student Name Formatting

```python
name = "   abdulsamad mohamed   "

formatted_name = name.strip().title()

print(formatted_name)
```

### C. File Extension Checking

```python
filename = "machine_learning.py"

if filename.endswith(".py"):
    print("Python file detected.")
```

### D. Extracting Email Information

```python
email = "student@gmail.com"

username, separator, domain = email.partition("@")

print("Username:", username)
print("Domain:", domain)
```

### E. Basic Text Cleaning

```python
message = "  HELLO PYTHON!  "

cleaned = message.strip().lower().replace("!", ".")

print(cleaned)
```

Output:

```text
hello python.
```

---

# 24. String Methods in Artificial Intelligence

String methods are important in Natural Language
Processing (NLP).

NLP is a field of Artificial Intelligence
that enables computers to process and analyze
human language.

Applications include:

1. Chatbots.
2. Sentiment analysis.
3. Language translation.
4. Text classification.
5. Search engines.
6. Document processing.
7. Information extraction.

### Basic NLP Text Preprocessing

Example:

```python
message = "   PYTHON IS AMAZING!   "

# Remove surrounding spaces.

cleaned = message.strip()

# Convert to lowercase.

cleaned = cleaned.lower()

# Replace punctuation.

cleaned = cleaned.replace("!", ".")

# Separate individual words.

words = cleaned.split()

print(cleaned)

print(words)
```

Output:

```text
python is amazing.
['python', 'is', 'amazing.']
```

This is basic rule-based text preprocessing,
not a complete NLP pipeline.

---

# 25. Day 009 Practical Project

## Project: Student Information & Text Processing System

File: challenge.py

We developed a practical application that:

- Collects student information.
- Cleans student names.
- Formats names using title().
- Validates basic email structure.
- Converts emails into lowercase.
- Generates student IDs using zfill().
- Stores information in dictionaries.
- Searches student information.
- Extracts email usernames and domains.
- Analyzes student names.
- Generates a formatted student report.

Important:

The email checks are basic format checks.
They do not verify whether an email account exists.

---

# 26. Day 009 Solved Exercises

File: exercises.py

We completed 25 solved exercises.

Topics included:

1. Uppercase.
2. Lowercase.
3. Capitalize.
4. Title case.
5. Swapcase.
6. Strip.
7. Lstrip and rstrip.
8. Replace.
9. Limited replacement.
10. Find.
11. Find versus index.
12. Count.
13. Startswith.
14. Endswith.
15. Split.
16. Custom split.
17. Rsplit.
18. Join.
19. Partition.
20. String validation.
21. Case validation.
22. Zfill.
23. Center.
24. Prefix and suffix.
25. AI text preprocessing.

---

# 27. Important Programming Lessons

Today I learned:

- How Python string methods work.
- How to manipulate uppercase and lowercase text.
- How to remove unnecessary whitespace.
- How to replace and search for text.
- How to count substring occurrences.
- How to split and join strings.
- How to validate string contents.
- How to format identifiers.
- How to extract information from email addresses.
- How to combine multiple string methods.
- How to use functions for reusable operations.
- How to validate user input.
- How to handle ValueError.
- How to store structured information using dictionaries.
- How to perform basic text preprocessing.

---

# 28. Day 009 Folder Structure

```text
day_009/
│
├── string_methods.py
├── exercises.py
├── challenge.py
└── notes.md
```

---

# 29. Learning Progress

| Day | Topic | Status |
|---|---|---|
| Day 001 | Introduction to Python | Completed |
| Day 002 | Variables | Completed |
| Day 003 | Data Types | Completed |
| Day 004 | Type Conversion | Completed |
| Day 005 | Operators | Completed |
| Day 006 | Input and Output | Completed |
| Day 007 | Fundamentals Revision | Completed |
| Day 008 | Python Strings | Completed |
| Day 009 | Python String Methods | Completed |

---

# FINAL REFLECTION

Day 009 helped me understand how to manipulate,
clean, search, validate and format textual data
using Python string methods.

I also developed a practical Student Information
and Text Processing System.

This lesson strengthened my understanding
of Python programming and prepared me for
future work in data processing and NLP.

## My Learning Goal

To become a skilled Artificial Intelligence
and Machine Learning Engineer.

One day at a time.
One concept at a time.
One project at a time.

KEEP LEARNING!
