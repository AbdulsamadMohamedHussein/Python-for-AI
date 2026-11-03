
# DAY 008 - PYTHON STRINGS

## Bachelor's in Artificial Intelligence
### 90-Day Python Programming Journey

---

## 1. Introduction to Strings

A string is a sequence of characters enclosed within quotation marks.

Strings can contain:

- Letters
- Numbers
- Spaces
- Special characters
- Symbols

Example:

```python
name = "Abdulsamad"
country = 'Pakistan'
course = "Artificial Intelligence"
```

Python supports three quotation styles:

1. Single quotes: ' '
2. Double quotes: " "
3. Triple quotes: ''' ''' or """ """

Strings are represented by the `str` data type.

---

## 2. String Length

The `len()` function calculates the total number
of characters in a string.

Example:

```python
name = "Abdulsamad"

print(len(name))
```

Output:

```text
10
```

Important:

Spaces and punctuation are also counted as characters.

---

## 3. String Indexing

Indexing allows us to access individual characters
inside a string.

Python indexing starts from ZERO.

Example:

```python
language = "PYTHON"

print(language[0])
print(language[1])
print(language[2])
```

Output:

```text
P
Y
T
```

### Negative Indexing

Negative indexing starts from the end.

| Character | Positive Index | Negative Index |
|---|---:|---:|
| P | 0 | -6 |
| Y | 1 | -5 |
| T | 2 | -4 |
| H | 3 | -3 |
| O | 4 | -2 |
| N | 5 | -1 |

Example:

```python
language = "PYTHON"

print(language[-1])
print(language[-2])
```

Output:

```text
N
O
```

---

## 4. String Slicing

Slicing extracts a portion of a string.

Syntax:

```python
string[start:end]
```

The starting index is included.
The ending index is excluded.

Example:

```python
language = "PYTHON"

print(language[0:3])
print(language[2:5])
print(language[:3])
print(language[3:])
```

Output:

```text
PYT
THO
PYT
HON
```

### Slicing with Step

Syntax:

```python
string[start:end:step]
```

Example:

```python
language = "PYTHON"

print(language[::2])
print(language[::-1])
```

Output:

```text
PTO
NOHTYP
```

A negative step allows us to move backwards.

---

## 5. String Concatenation

Concatenation means joining two or more strings.

The `+` operator joins strings.

Example:

```python
first_name = "Abdulsamad"
last_name = "Mohamed"

full_name = first_name + " " + last_name

print(full_name)
```

Output:

```text
Abdulsamad Mohamed
```

---

## 6. String Repetition

The multiplication operator `*` repeats strings.

Example:

```python
word = "Python "

print(word * 3)
```

Output:

```text
Python Python Python
```

---

## 7. Uppercase and Lowercase Methods

Python provides several methods for changing
the appearance of text.

| Method | Purpose |
|---|---|
| upper() | Converts text to uppercase |
| lower() | Converts text to lowercase |
| title() | Capitalizes each word |
| capitalize() | Capitalizes the first character |

Example:

```python
text = "python programming"

print(text.upper())
print(text.lower())
print(text.title())
print(text.capitalize())
```

---

## 8. Removing Unnecessary Spaces

Python provides three important methods.

| Method | Purpose |
|---|---|
| strip() | Removes spaces from both ends |
| lstrip() | Removes spaces from the left |
| rstrip() | Removes spaces from the right |

Example:

```python
name = "   Abdulsamad   "

print(name.strip())
print(name.lstrip())
print(name.rstrip())
```

These methods do not remove spaces between words.

---

## 9. Replacing Text

The `replace()` method replaces a character
or substring with another value.

Syntax:

```python
string.replace(old, new)
```

Example:

```python
text = "I am learning Java"

updated_text = text.replace("Java", "Python")

print(updated_text)
```

Output:

```text
I am learning Python
```

We can also limit the number of replacements.

```python
text.replace("AI", "Python", 1)
```

Important:

Strings are immutable, so `replace()` creates
a new string rather than modifying the original.

---

## 10. Finding Words and Characters

The `find()` method searches for a substring.

It returns the index of the first occurrence.

If the substring does not exist, it returns `-1`.

Example:

```python
text = "Python is important for AI"

print(text.find("Python"))
print(text.find("important"))
print(text.find("Java"))
```

Output:

```text
0
10
-1
```

---

## 11. Counting Characters

The `count()` method counts occurrences
of a character or substring.

Example:

```python
text = "Python is amazing"

print(text.count("a"))
print(text.count("i"))
print(text.count("Python"))
```

Important:

String searching and counting are case-sensitive.

---

## 12. Splitting Strings

The `split()` method divides a string into
a list of smaller strings.

Example:

```python
student = "Abdulsamad,23,Pakistan"

information = student.split(",")

print(information)
```

Output:

```text
['Abdulsamad', '23', 'Pakistan']
```

We can also access individual elements:

```python
print(information[0])
print(information[1])
print(information[2])
```

By default, `split()` separates text using whitespace.

---

## 13. Joining Strings

The `join()` method combines elements
of an iterable into a single string.

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

Different separators can be used.

```python
print("-".join(words))
print(", ".join(words))
```

---

## 14. Checking String Contents

Python provides methods for validating
the contents of strings.

| Method | Purpose |
|---|---|
| isalpha() | Checks whether all characters are letters |
| isdigit() | Checks whether all characters are digits |
| isalnum() | Checks whether all characters are letters or digits |
| isspace() | Checks whether all characters are whitespace |
| islower() | Checks whether cased letters are lowercase |
| isupper() | Checks whether cased letters are uppercase |

Example:

```python
text = "Python"
number = "12345"
mixed = "Python123"

print(text.isalpha())
print(number.isdigit())
print(mixed.isalnum())
```

These methods return Boolean values:

True or False.

---

## 15. Membership Operators

The `in` and `not in` operators check whether
a substring exists inside another string.

Example:

```python
sentence = "Artificial Intelligence is powerful"

print("Artificial" in sentence)

print("Python" in sentence)

print("Python" not in sentence)
```

These operators return True or False.

---

## 16. Escape Characters

Escape characters perform special operations
inside strings.

| Escape Character | Purpose |
|---|---|
| \n | New line |
| \t | Tab space |
| \\ | Backslash |
| \' | Single quotation mark |
| \" | Double quotation mark |

Example:

```python
print("Hello\nWorld")

print("Python\tProgramming")

print("I\'m learning Python")
```

---

## 17. F-Strings

F-strings allow variables and expressions
to be inserted directly inside strings.

Example:

```python
name = "Abdulsamad"
age = 23

print(f"My name is {name}.")
print(f"I am {age} years old.")
```

### Decimal Formatting

We can control the number of decimal places.

```python
accuracy = 95.6789

print(f"Accuracy: {accuracy:.2f}%")
```

Output:

```text
Accuracy: 95.68%
```

F-strings make output more readable.

---

## 18. String Immutability

Strings in Python are immutable.

Immutable means an existing string cannot
be modified character by character.

Example:

```python
language = "Python"

# This would produce a TypeError:
# language[0] = "J"

# Instead, create a new string.

new_language = "J" + language[1:]

print(new_language)
```

Output:

```text
Jython
```

The original string remains unchanged.

---

## 19. Important Built-in String Operations

| Function or Method | Purpose |
|---|---|
| len() | Counts characters |
| upper() | Converts to uppercase |
| lower() | Converts to lowercase |
| title() | Capitalizes words |
| capitalize() | Capitalizes first character |
| strip() | Removes surrounding whitespace |
| replace() | Replaces text |
| find() | Finds a substring |
| count() | Counts occurrences |
| split() | Separates text into a list |
| join() | Combines iterable elements |
| isalpha() | Checks letters |
| isdigit() | Checks digits |
| isalnum() | Checks letters and digits |
| startswith() | Checks the beginning |
| endswith() | Checks the ending |

---

## 20. Introduction to Text Preprocessing in AI

Artificial Intelligence frequently processes
large amounts of textual information.

Natural Language Processing (NLP) is a field
of AI that allows computers to process
and analyze human language.

Examples of NLP applications:

1. Chatbots
2. Language translation
3. Sentiment analysis
4. Text classification
5. Search engines
6. Document analysis

### Basic Text Cleaning

Example:

```python
message = "   HELLO PYTHON FOR AI!   "

cleaned_message = message.strip()

cleaned_message = cleaned_message.lower()

cleaned_message = cleaned_message.replace("!", ".")

print(cleaned_message)
```

Output:

```text
hello python for ai.
```

### Word Tokenization

Tokenization means dividing text into smaller units,
such as individual words.

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

We will study more advanced tokenization
and NLP techniques in future lessons.

---

## 21. Day 008 Practical Project

### Project Name: AI Text Analyzer

File: challenge.py

We developed a text analyzer that:

- Accepts user input.
- Cleans text.
- Converts text to lowercase.
- Counts characters.
- Counts words.
- Counts sentences approximately.
- Identifies longest and shortest words.
- Counts vowels and consonants.
- Counts digits and special characters.
- Searches for a word.
- Reverses text.
- Generates an analysis report.

This project combines multiple Python concepts
into one practical application.

Important:

This is a rule-based text analyzer.
It is not a trained Machine Learning model.

---

## 22. Solved Exercises

File: exercises.py

We completed 20 solved exercises.

The exercises covered:

1. Creating and displaying strings.
2. Finding string length.
3. Positive indexing.
4. Negative indexing.
5. String slicing.
6. Reversing strings.
7. String concatenation.
8. String repetition.
9. Uppercase and lowercase.
10. Removing spaces.
11. Replacing words.
12. Finding words.
13. Counting characters.
14. Splitting strings.
15. Joining strings.
16. Checking string contents.
17. Membership operators.
18. Escape characters.
19. F-strings.
20. Basic AI text preprocessing.

---

## 23. Important Lessons Learned

Today I learned:

- Strings are sequences of characters.
- Python indexing starts from zero.
- Negative indexing starts from the end.
- Slicing extracts parts of strings.
- Strings are immutable.
- Concatenation joins strings.
- String methods help clean and manipulate text.
- split() converts text into a list.
- join() combines iterable elements.
- F-strings improve output formatting.
- Text preprocessing is important in NLP.
- Functions organize reusable code.
- Dictionaries store structured information.
- Loops allow us to process individual characters.
- Conditional statements help programs make decisions.

---

## 24. Day 008 File Structure

```text
day_008/
│
├── strings.py
├── exercises.py
├── challenge.py
└── notes.md
```

---

## 25. Learning Progress

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

---

## Final Reflection

Day 008 helped me understand how Python handles
textual information.

I learned how to access, manipulate, search,
clean and analyze strings.

I also developed a practical AI Text Analyzer
using Python functions, loops, lists, dictionaries
and string methods.

These concepts will provide a foundation
for studying Natural Language Processing
and Machine Learning.

### My Learning Goal

To become a skilled Artificial Intelligence
and Machine Learning Engineer.

One day at a time.
One concept at a time.
One project at a time.

KEEP LEARNING!
