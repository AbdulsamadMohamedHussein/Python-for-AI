
# DAY 010 - PYTHON CONDITIONAL STATEMENTS

## Bachelor's in Artificial Intelligence
### 90-Day Python Programming Journey

---

# 1. Introduction to Conditional Statements

Conditional statements allow Python programs to make
decisions based on specific conditions.

A condition is an expression that evaluates to:

- True
- False

Python executes different instructions depending
on whether a condition is True or False.

### Real-Life Example

Imagine a student examination:

- If marks are 90 or above, Grade A+.
- If marks are 80 or above, Grade A.
- If marks are 70 or above, Grade B.
- Otherwise, another grade is assigned.

Python uses conditional statements to implement
this type of decision-making logic.

---

# 2. Boolean Data Type

Boolean is a built-in Python data type.

It has only two possible values:

```python
True
False
```

Example:

```python
is_student = True

is_employed = False

print(is_student)
print(is_employed)

print(type(is_student))
```

Output:

```text
True
False
<class 'bool'>
```

Boolean values are extremely important
because conditional statements depend on them.

---

# 3. The if Statement

The if statement executes a block of code
only when its condition is True.

### Syntax

```python
if condition:
    statement
```

### Example

```python
age = 23

if age >= 18:

    print("You are an adult.")
```

Output:

```text
You are an adult.
```

### Explanation

- if: Starts a conditional statement.
- age >= 18: Checks the condition.
- Colon (:): Begins the code block.
- Indentation: Identifies the instructions belonging
  to the condition.

If the condition is False, the block is skipped.

---

# 4. The if-else Statement

if-else provides two possible execution paths.

If the condition is True, the if block executes.

If the condition is False, the else block executes.

### Syntax

```python
if condition:

    statement_if_true

else:

    statement_if_false
```

### Example

```python
age = 16

if age >= 18:

    print("You are an adult.")

else:

    print("You are a minor.")
```

Output:

```text
You are a minor.
```

---

# 5. The if-elif-else Statement

elif means "else if".

It allows Python to check multiple conditions.

### Syntax

```python
if condition_1:

    statement_1

elif condition_2:

    statement_2

elif condition_3:

    statement_3

else:

    default_statement
```

### Example: Grade Calculator

```python
marks = 85

if marks >= 90:

    print("Grade A+")

elif marks >= 80:

    print("Grade A")

elif marks >= 70:

    print("Grade B")

elif marks >= 60:

    print("Grade C")

elif marks >= 50:

    print("Grade D")

else:

    print("Grade F")
```

Output:

```text
Grade A
```

### Important Rule

Python checks conditions from top to bottom.

The first True condition executes.

The remaining branches are skipped.

The order of conditions is important.

---

# 6. Comparison Operators

Comparison operators compare two values.

They return Boolean results: True or False.

| Operator | Meaning | Example |
|---|---|---|
| == | Equal to | 5 == 5 |
| != | Not equal to | 5 != 3 |
| > | Greater than | 8 > 5 |
| < | Less than | 3 < 8 |
| >= | Greater than or equal | 8 >= 8 |
| <= | Less than or equal | 5 <= 8 |

### Example

```python
x = 10

y = 20

print(x == y)
print(x != y)
print(x > y)
print(x < y)
print(x >= y)
print(x <= y)
```

Output:

```text
False
True
False
True
False
True
```

### Important Difference

```python
x = 10
```

Single equal sign assigns a value.

```python
x == 10
```

Double equal sign compares values.

Never confuse assignment (=) with comparison (==).

---

# 7. Logical Operators

Logical operators combine multiple conditions.

Python has three main logical operators:

1. and
2. or
3. not

## A. AND Operator

AND returns True only when BOTH conditions are True.

Example:

```python
age = 23

has_id = True

if age >= 18 and has_id:

    print("Access granted.")

else:

    print("Access denied.")
```

Both requirements must be satisfied.

### AND Truth Table

| A | B | A and B |
|---|---|---|
| True | True | True |
| True | False | False |
| False | True | False |
| False | False | False |

## B. OR Operator

OR returns True if at least ONE condition is True.

Example:

```python
has_email = False

has_phone = True

if has_email or has_phone:

    print("Contact information available.")

else:

    print("No contact information.")
```

### OR Truth Table

| A | B | A or B |
|---|---|---|
| True | True | True |
| True | False | True |
| False | True | True |
| False | False | False |

## C. NOT Operator

NOT reverses a Boolean value.

Example:

```python
is_raining = False

if not is_raining:

    print("You can go outside.")

else:

    print("It is raining.")
```

### NOT Truth Table

| A | not A |
|---|---|
| True | False |
| False | True |

---

# 8. Nested if Statements

Nested conditions mean placing one if statement
inside another if statement.

Example:

```python
age = 23

has_id = True

if age >= 18:

    print("Age requirement satisfied.")

    if has_id:

        print("Identity verified.")

    else:

        print("Please provide identification.")

else:

    print("Age requirement not satisfied.")
```

### Explanation

First, Python checks the age.

If age >= 18 is True, Python enters the outer block.

Then it checks whether the person has an ID.

The inner condition executes only when Python
reaches that part of the outer block.

Nested conditions are useful when decisions
depend on multiple stages.

---

# 9. Modulo Operator (%)

The modulo operator returns the remainder
after division.

Example:

```python
print(10 % 2)
print(15 % 2)
print(20 % 3)
```

Output:

```text
0
1
2
```

### Checking Even and Odd Numbers

A number is even if its remainder after division
by 2 is zero.

```python
number = 12

if number % 2 == 0:

    print("Even number.")

else:

    print("Odd number.")
```

Mathematical representation:

Even number:

n mod 2 = 0

Odd number:

n mod 2 = 1

This concept is useful in many programming problems.

---

# 10. Conditions with User Input

input() collects information from the user.

We can combine input() with conditional statements.

Example:

```python
name = input("Enter your name: ").strip()

if name:

    print("Welcome", name.title())

else:

    print("Name cannot be empty.")
```

Explanation:

- input() collects the name.
- strip() removes surrounding whitespace.
- if checks whether the resulting string is non-empty.

An empty string evaluates to False.

A non-empty string evaluates to True.

---

# 11. Membership Operators

Membership operators check whether an element
exists inside a sequence.

There are two main membership operators:

- in
- not in

## A. in

Returns True if an element exists.

```python
courses = [
    "Python",
    "Machine Learning",
    "Deep Learning"
]

if "Python" in courses:

    print("Course available.")
```

## B. not in

Returns True if an element does not exist.

```python
courses = [
    "Python",
    "Machine Learning",
    "Deep Learning"
]

if "Java" not in courses:

    print("Java is not available.")
```

These operators are useful for checking
membership in lists, tuples, sets and strings.

---

# 12. Ternary Conditional Expressions

A ternary expression allows us to write
a simple conditional expression in one line.

### Syntax

```python
value_if_true if condition else value_if_false
```

### Example

```python
age = 23

status = "Adult" if age >= 18 else "Minor"

print(status)
```

Output:

```text
Adult
```

Ternary expressions are useful for simple decisions.

For complicated conditions, normal if-else statements
are generally easier to understand.

---

# 13. Multiple Conditions

We can combine multiple conditions
using logical operators.

Example:

```python
marks = 85

attendance = 90

if marks >= 50 and attendance >= 75:

    print("Student passed.")

else:

    print("Student did not meet the requirements.")
```

Both conditions must be True.

We can also use OR:

```python
temperature = 35

if temperature < 10 or temperature > 30:

    print("Temperature is outside the preferred range.")
```

---

# 14. Checking Positive, Negative or Zero

A number can be:

- Positive
- Negative
- Zero

Example:

```python
number = -15

if number > 0:

    print("Positive number.")

elif number < 0:

    print("Negative number.")

else:

    print("Zero.")
```

This demonstrates how elif handles
multiple possible outcomes.

---

# 15. Leap Year Calculation

A leap year contains 366 days.

A year is a leap year if:

1. It is divisible by 400.

OR

2. It is divisible by 4 but not divisible by 100.

### Python Code

```python
year = 2024

if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):

    print("Leap year.")

else:

    print("Not a leap year.")
```

Examples:

| Year | Result |
|---|---|
| 2024 | Leap year |
| 2023 | Not a leap year |
| 2000 | Leap year |
| 1900 | Not a leap year |

This exercise demonstrates combining
AND, OR and NOT-related comparison logic.

---

# 16. Nested Conditions vs elif

These two concepts are different.

### Nested if

One conditional statement exists inside another.

```python
if age >= 18:

    if has_id:

        print("Access granted.")
```

### elif

Checks another condition when a previous
condition was False.

```python
if marks >= 90:

    print("A+")

elif marks >= 80:

    print("A")
```

| Nested if | elif |
|---|---|
| Condition inside another condition | Additional condition in the same chain |
| Useful for dependent decisions | Useful for multiple alternatives |
| Can have multiple indentation levels | Usually uses the same indentation |

---

# 17. Exception Handling with Conditions

Sometimes users enter incorrect information.

For example, int() cannot convert ordinary
alphabetic text into an integer.

We can handle this using try and except.

Example:

```python
try:

    age = int(input("Enter your age: "))

    if age >= 18:

        print("Adult.")

    else:

        print("Minor.")

except ValueError:

    print("Please enter a valid whole number.")
```

Explanation:

- try contains code that might raise an error.
- except handles the specified error.
- ValueError occurs when conversion receives
  an unsuitable value.

Exception handling makes programs more robust.

---

# 18. Functions with Conditional Statements

Functions allow us to reuse decision-making logic.

Example:

```python
def calculate_grade(marks):

    if marks >= 90:

        return "A+"

    elif marks >= 80:

        return "A"

    elif marks >= 70:

        return "B"

    elif marks >= 60:

        return "C"

    elif marks >= 50:

        return "D"

    else:

        return "F"


grade = calculate_grade(85)

print(grade)
```

Output:

```text
A
```

The function receives marks and returns a grade.

This makes code easier to organize and reuse.

---

# 19. Practical Applications of Conditional Statements

Conditional statements are used in many applications.

### A. Login Systems

```python
username = "student"

password = "python123"

if username == "student" and password == "python123":

    print("Login successful.")

else:

    print("Incorrect credentials.")
```

This is only a learning example.
Real applications require secure password handling.

### B. Student Grading

```python
marks = 85

if marks >= 50:

    print("Passed.")

else:

    print("Failed.")
```

### C. Temperature Classification

```python
temperature = 35

if temperature < 10:

    print("Cold.")

elif temperature < 25:

    print("Moderate.")

elif temperature < 35:

    print("Warm.")

else:

    print("Hot.")
```

### D. Scholarship Eligibility

```python
marks = 90

attendance = 85

if marks >= 85 and attendance >= 80:

    print("Eligible.")

else:

    print("Not eligible.")
```

---

# 20. Conditional Statements in Artificial Intelligence

Conditional statements are important
for building rule-based systems.

A rule-based system makes decisions
using predefined rules.

Example:

```python
marks = 88

attendance = 90

if marks >= 80 and attendance >= 75:

    result = "Excellent"

elif marks >= 50 and attendance >= 60:

    result = "Satisfactory"

else:

    result = "Needs Improvement"

print(result)
```

This is an example of rule-based decision-making.

### Applications

1. Expert systems.
2. Rule-based chatbots.
3. Fraud detection rules.
4. Data validation.
5. Decision-support systems.
6. Academic evaluation systems.
7. Automated workflows.

Important:

A rule-based Python program is not automatically
a Machine Learning model.

Machine Learning models learn patterns
from data rather than relying only on manually
written decision rules.

---

# 21. Conditional Logic and Mathematics

Conditional statements are closely related
to mathematical inequalities and Boolean logic.

Examples:

| Mathematical expression | Python expression |
|---|---|
| x = 10 | x == 10 |
| x is not 10 | x != 10 |
| x > 10 | x > 10 |
| x is at least 10 | x >= 10 |
| x is less than 10 | x < 10 |
| x is at most 10 | x <= 10 |

### Example: Multiple Conditions

Mathematical condition:

5 < x < 20

Python:

```python
x = 12

if 5 < x < 20:

    print("Within range.")
```

Python supports chained comparisons.

---

# 22. Important Operators Summary

| Operator | Purpose |
|---|---|
| == | Equal |
| != | Not equal |
| > | Greater than |
| < | Less than |
| >= | Greater than or equal |
| <= | Less than or equal |
| and | Both conditions true |
| or | At least one condition true |
| not | Reverse Boolean |
| in | Check membership |
| not in | Check absence |
| % | Calculate remainder |

---

# 23. Day 010 Solved Exercises

File: exercises.py

We completed 30 solved exercises.

Topics:

1. Adult check.
2. Positive number.
3. Positive or negative.
4. Even or odd.
5. Equality check.
6. Greater number.
7. Largest of three numbers.
8. Pass or fail.
9. Grade calculator.
10. Voting eligibility.
11. Logical AND.
12. Logical OR.
13. Logical NOT.
14. Nested conditions.
15. Divisibility.
16. Leap year.
17. Login system.
18. Membership operator.
19. NOT IN operator.
20. Ternary expression.
21. Temperature classification.
22. Password length.
23. Empty name validation.
24. Smallest of three numbers.
25. Triangle classification.
26. Simple calculator.
27. Scholarship eligibility.
28. Weekday or weekend.
29. Shipping cost.
30. Rule-based student decision system.

---

# 24. Day 010 Practical Challenge

## Project: Student Grading and Academic Performance
## Management System

File: challenge.py

We developed a practical application using
conditional statements and other Python concepts.

### Project Features

- Collects student information.
- Validates student names.
- Collects student age.
- Collects marks for five subjects.
- Calculates total marks.
- Calculates average marks.
- Assigns examination grades.
- Determines pass or fail.
- Evaluates attendance.
- Checks scholarship eligibility.
- Classifies academic performance.
- Generates a final student report.

### Mathematical Formulas

Total marks:

Total = Sum of all subject marks

Average:

Average = Total Marks / Number of Subjects

Example:

| Subject | Marks |
|---|---:|
| Mathematics | 90 |
| Python | 85 |
| Statistics | 80 |
| Computer Science | 95 |
| Artificial Intelligence | 90 |
| Total | 440 |

Average:

440 / 5 = 88

The student's grade is A.

### Example Scholarship Rules

Average marks >= 85

AND

Attendance >= 80%

AND

All subjects passed.

These are example rules created for our project.

---

# 25. Important Programming Lessons

Today I learned:

1. How conditional statements work.
2. How Python evaluates Boolean expressions.
3. How to use if statements.
4. How to use if-else statements.
5. How to use if-elif-else.
6. How to compare values.
7. How to combine conditions.
8. How logical AND works.
9. How logical OR works.
10. How logical NOT works.
11. How nested conditions work.
12. How to use membership operators.
13. How to write ternary expressions.
14. How to validate user input.
15. How to handle ValueError.
16. How to create decision-making functions.
17. How to implement rule-based systems.
18. How to combine programming logic with mathematics.

---

# 26. Day 010 Folder Structure

```text
day_010/
│
├── conditionals.py
├── exercises.py
├── challenge.py
└── notes.md
```

---

# 27. Learning Progress

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
| Day 010 | Conditional Statements | Completed |

---

# FINAL REFLECTION

Day 010 helped me understand how Python
makes decisions using conditional statements.

I learned how to compare values, combine conditions,
validate information and create decision-making programs.

I also developed a Student Academic Performance
Management System using Python.

These skills will support my future studies
in Data Science, Machine Learning and Artificial Intelligence.

## MY LEARNING GOAL

To become a skilled Artificial Intelligence
and Machine Learning Engineer.

One day at a time.
One concept at a time.
One project at a time.

KEEP LEARNING!
