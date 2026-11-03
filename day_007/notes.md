
# DAY 007 - Python Fundamentals Revision

## Overview

Today we revised the Python fundamentals learned during
Days 001-006.

We combined individual Python concepts to build practical
applications.

Today's main projects were:

1. AI Student Performance Analyzer
2. Solved Python Exercises
3. AI Student Management and Performance System

The purpose was to understand how different Python concepts
work together in a real programming application.

---

## 1. Variables

A variable is a named location used to store information.

Example:

```python
student_name = "Abdulsamad"
student_age = 23
student_score = 95.5
```

Explanation:

- student_name stores text.
- student_age stores a whole number.
- student_score stores a decimal number.

Variables allow us to store and reuse information.

In AI programming, variables are used to store datasets,
model parameters, accuracy scores and other information.

---

## 2. Python Data Types

Python has several built-in data types.

### String (str)

Used to store text.

```python
name = "Abdulsamad"
```

### Integer (int)

Used to store whole numbers.

```python
age = 23
```

### Float (float)

Used to store decimal numbers.

```python
accuracy = 95.5
```

### Boolean (bool)

Stores either True or False.

```python
is_student = True
```

### NoneType

Represents the absence of a value.

```python
result = None
```

We can identify a variable's data type using type().

```python
print(type(name))
print(type(age))
print(type(accuracy))
print(type(is_student))
```

---

## 3. Type Conversion

Type conversion means changing one data type into another.

Important conversion functions:

- int() converts a value into an integer.
- float() converts a value into a float.
- str() converts a value into a string.
- bool() converts a value into a Boolean.

Example:

```python
number = "100"

integer_number = int(number)

decimal_number = float(number)

text_number = str(integer_number)

print(integer_number)
print(decimal_number)
print(text_number)
```

Important:

The input() function always returns a string.

Therefore, numerical input should be converted when
we need to perform mathematical calculations.

Example:

```python
age = int(input("Enter your age: "))

height = float(input("Enter your height: "))
```

---

## 4. User Input and Output

The input() function collects information from users.

The print() function displays information.

Example:

```python
name = input("Enter your name: ")

print("Welcome", name)
```

We can also use strip() to remove unnecessary
spaces from the beginning and end of text.

```python
name = input("Enter your name: ").strip()
```

---

## 5. Arithmetic Operators

Arithmetic operators perform mathematical calculations.

| Operator | Meaning | Example |
|---|---|---|
| + | Addition | 10 + 5 |
| - | Subtraction | 10 - 5 |
| * | Multiplication | 10 * 5 |
| / | Division | 10 / 5 |
| // | Floor division | 10 // 3 |
| % | Modulus | 10 % 3 |
| ** | Exponentiation | 2 ** 3 |

Example:

```python
a = 20
b = 6

print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a // b)
print(a % b)
print(a ** b)
```

Important:

- Division returns a floating-point result.
- Floor division returns the quotient rounded down.
- Modulus returns the remainder.
- Exponentiation calculates powers.

---

## 6. Comparison Operators

Comparison operators compare two values.

| Operator | Meaning |
|---|---|
| == | Equal to |
| != | Not equal to |
| > | Greater than |
| < | Less than |
| >= | Greater than or equal to |
| <= | Less than or equal to |

Example:

```python
math_marks = 90
physics_marks = 85

print(math_marks > physics_marks)
print(math_marks == physics_marks)
print(math_marks != physics_marks)
```

Comparison operators return Boolean values:

True or False.

---

## 7. Logical Operators

Logical operators combine multiple conditions.

### AND

Both conditions must be True.

```python
age = 23
score = 90

result = age > 18 and score >= 50

print(result)
```

### OR

At least one condition must be True.

```python
maths = 85
python = 95

result = maths >= 90 or python >= 90

print(result)
```

### NOT

Reverses a Boolean result.

```python
is_student = True

print(not is_student)
```

Logical operators are important when developing
decision-making systems.

---

## 8. Conditional Statements

Conditional statements allow programs to make decisions.

Python uses:

- if
- elif
- else

Example:

```python
marks = 85

if marks >= 90:

    print("Grade A")

elif marks >= 80:

    print("Grade B")

elif marks >= 70:

    print("Grade C")

else:

    print("Needs Improvement")
```

Python checks the conditions from top to bottom.

The first condition that evaluates to True is executed.

---

## 9. Augmented Assignment Operators

Augmented assignment operators update existing variables.

| Operator | Meaning |
|---|---|
| += | Add and assign |
| -= | Subtract and assign |
| *= | Multiply and assign |
| /= | Divide and assign |

Example:

```python
score = 50

score += 10

score -= 5

score *= 2

score /= 2

print(score)
```

These operators make code shorter and easier to read.

---

## 10. String Formatting

F-strings allow variables to be inserted directly
inside strings.

Example:

```python
name = "Abdulsamad"
age = 23

print(f"My name is {name} and I am {age} years old.")
```

### Decimal formatting

```python
accuracy = 95.6789

print(f"Accuracy: {accuracy:.2f}%")
```

Output:

Accuracy: 95.68%

The .2f specifies two decimal places.

### sep parameter

Changes the separator between printed values.

```python
print("Python", "NumPy", "Pandas", sep=" | ")
```

### end parameter

Changes what print() displays at the end.

```python
print("Hello", end=" ")

print("World")
```

---

## 11. Useful Built-in Functions

We practised several useful Python functions.

### max()

Finds the highest value.

```python
scores = [85, 90, 95, 88]

print(max(scores))
```

### min()

Finds the lowest value.

```python
print(min(scores))
```

### all()

Returns True when every item in an iterable
is True.

```python
scores_valid = all(
    0 <= score <= 100
    for score in [85, 90, 95]
)

print(scores_valid)
```

### type()

Identifies the data type.

```python
number = 100

print(type(number))
```

---

## 12. Input Validation

Input validation checks whether information entered
by a user meets the required conditions.

Example:

```python
marks = float(input("Enter marks: "))

if 0 <= marks <= 100:

    print("Valid marks")

else:

    print("Invalid marks")
```

We also revised try and except for handling errors.

```python
try:

    age = int(input("Enter your age: "))

    print(age)

except ValueError:

    print("Please enter a valid whole number.")
```

ValueError occurs when a value cannot be converted
into the requested data type.

---

## 13. Mathematical Calculations

We developed an academic performance calculator.

Total marks:

```python
total = mathematics + physics + python + chemistry
```

Average:

```python
average = total / 4
```

Percentage:

```python
percentage = (total / 400) * 100
```

Example:

Mathematics = 90

Physics = 85

Python = 95

Chemistry = 88

Total = 358

Average = 89.5

Percentage = 89.5%

---

## 14. AI Data Normalization

Normalization is a data preprocessing technique.

It transforms numerical values into a different
numerical scale.

In our project, we used simple division by 100.

Formula:

Normalized Value = Original Value / 100

Example:

```python
original_score = 85

normalized_score = original_score / 100

print(normalized_score)
```

Output:

0.85

This is a simple scaling demonstration.

In Machine Learning, other normalization methods
include Min-Max Scaling and Standardization.

We will study these properly when we reach
NumPy and Machine Learning.

---

## 15. Basic AI Model Information

We created variables to represent an imaginary
AI model.

Example:

```python
model_name = "Image Classifier"

accuracy = 95.5

epochs = 50

learning_rate = 0.001
```

Explanation:

- Model name identifies the model.
- Accuracy represents its performance metric.
- Epochs represent complete passes through training data.
- Learning rate controls the size of optimization steps.

These variables introduced us to information
commonly used in Machine Learning.

Our program only stored and analyzed these values.
It did not train an actual AI model.

---

## 16. Important Lessons from Day 007

Today we learned how to:

1. Store information using variables.
2. Identify Python data types.
3. Convert between data types.
4. Collect information using input().
5. Display information using print().
6. Perform mathematical calculations.
7. Compare numerical values.
8. Combine conditions using logical operators.
9. Make decisions using if, elif and else.
10. Format output using f-strings.
11. Validate user input.
12. Handle ValueError using try and except.
13. Find maximum and minimum values.
14. Calculate academic performance.
15. Perform basic numerical normalization.
16. Generate structured reports.

---

## 17. Projects Completed on Day 007

### Project 1: AI Student Performance Analyzer

File: revision_project.py

We developed an application that:

- Collects student information.
- Accepts examination marks.
- Calculates total and average marks.
- Calculates percentages.
- Assigns academic grades.
- Performs basic data normalization.
- Generates a student report.

### Project 2: Solved Exercises

File: exercises.py

We completed 15 exercises covering:

- Variables and data types.
- Type conversion.
- Basic calculator.
- Arithmetic operators.
- Comparison operators.
- Logical operators.
- User input.
- Academic calculations.
- Grade classification.
- String formatting.
- Input validation.
- Data normalization.

### Project 3: AI Student Management System

File: challenge.py

We developed a larger application that combines
student registration, academic analysis and
basic AI model information.

---

## 18. Important Python Commands Revision

| Command | Purpose |
|---|---|
| print() | Display information |
| input() | Collect user input |
| type() | Identify data type |
| int() | Convert to integer |
| float() | Convert to float |
| str() | Convert to string |
| bool() | Convert to Boolean |
| max() | Find maximum |
| min() | Find minimum |
| all() | Check whether all values are True |
| strip() | Remove surrounding whitespace |
| split() | Separate a string into parts |

---

## 19. Day 007 Learning Summary

Day 007 was a revision and integration day.

We combined the Python fundamentals learned
during the first six days into practical applications.

We also developed a basic understanding of how
Python handles academic data and numerical
information used in Artificial Intelligence.

The most important lesson was learning how
individual Python concepts work together
to create complete programs.

---

## 20. Progress

| Day | Topic | Status |
|---|---|---|
| Day 001 | Introduction to Python | Completed |
| Day 002 | Variables | Completed |
| Day 003 | Data Types | Completed |
| Day 004 | Type Conversion | Completed |
| Day 005 | Operators | Completed |
| Day 006 | Input and Output | Completed |
| Day 007 | Fundamentals Revision Project | Completed |

---

## Final Note

Seven days completed!

One day at a time.
One concept at a time.
One project at a time.

My long-term goal is to become an AI and
Machine Learning Engineer.

The next stage of my journey will continue
building my Python programming foundation.

Let's keep learning!
