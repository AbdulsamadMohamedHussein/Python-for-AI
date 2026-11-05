# DAY 012 — PYTHON FOR LOOPS

## Bachelor's in Artificial Intelligence
### 90-Day Python Programming Journey

**Main Topic:** For Loops and Iteration  
**Programming Language:** Python  
**Level:** Beginner to Intermediate

---

# 1. Introduction to Loops

A loop is a programming structure that executes a block of code repeatedly.

Loops help programmers avoid writing the same instructions multiple times.

For example, imagine printing numbers from 1 to 100.

Without loops, we would need 100 print statements.

With a for loop, we can accomplish this using just two lines:

```python
for number in range(1, 101):

    print(number)
```

**Why are loops important?**

- Reduce repetitive code.
- Process large amounts of information.
- Perform mathematical calculations.
- Analyze datasets.
- Train Machine Learning models.
- Process images and numerical arrays.

---

# 2. What Is Iteration?

Iteration means repeating a particular operation.

Every complete execution of a loop is called an iteration.

Example:

```python
for number in range(1, 4):

    print(number)
```

Output:

```text
1
2
3
```

The loop executes three iterations.

| Iteration | Value of number |
|---|---:|
| 1 | 1 |
| 2 | 2 |
| 3 | 3 |

During every iteration, the variable receives a new value.

---

# 3. Understanding For Loop Syntax

Basic syntax:

```python
for variable in sequence:

    statement
```

Explanation:

| Component | Purpose |
|---|---|
| for | Starts the loop |
| variable | Stores the current item |
| in | Iterates through a sequence |
| sequence | Collection of items |
| colon | Begins the loop block |
| indentation | Defines the repeated statements |

Example:

```python
subjects = ["Python", "Mathematics", "Statistics"]

for subject in subjects:

    print(subject)
```

The loop processes every subject individually.

---

# 4. Understanding the range() Function

The range() function generates a sequence of integers.

Syntax:

```python
range(start, stop, step)
```

| Parameter | Explanation |
|---|---|
| start | Starting value |
| stop | Stopping boundary, excluded |
| step | Increment or decrement |

## A. range(stop)

```python
for number in range(5):

    print(number)
```

Output:

```text
0
1
2
3
4
```

The sequence begins at zero by default.

## B. range(start, stop)

```python
for number in range(1, 6):

    print(number)
```

Output:

```text
1
2
3
4
5
```

The stopping value is excluded.

## C. range(start, stop, step)

```python
for number in range(2, 11, 2):

    print(number)
```

Output:

```text
2
4
6
8
10
```

The step value determines how much the number increases.

## D. Counting Backwards

```python
for number in range(10, 0, -1):

    print(number)
```

Output:

```text
10
9
8
7
6
5
4
3
2
1
```

A negative step allows us to count backwards.

---

# 5. Iterating Through Strings

A string is a sequence of characters.

A for loop can process each character individually.

Example:

```python
word = "PYTHON"

for character in word:

    print(character)
```

Output:

```text
P
Y
T
H
O
N
```

Practical applications:

- Counting characters.
- Searching for specific letters.
- Text analysis.
- Natural Language Processing.
- Processing textual datasets.

---

# 6. Counting Vowels Using a Loop

We can use a loop to count vowels in a sentence.

Example:

```python
sentence = "Artificial Intelligence"

vowel_count = 0

for character in sentence.lower():

    if character in "aeiou":

        vowel_count += 1

print("Vowels:", vowel_count)
```

Explanation:

- vowel_count starts at zero.
- The loop processes every character.
- The condition checks whether a character is a vowel.
- If it is a vowel, the counter increases by one.

The `+=` operator is a shorter way of adding a value to an existing variable.

---

# 7. For Loops with Lists

Lists store multiple values.

Example:

```python
numbers = [10, 20, 30, 40, 50]

for number in numbers:

    print(number)
```

The loop processes every element.

## Calculating the Sum of a List

```python
numbers = [10, 20, 30, 40, 50]

total = 0

for number in numbers:

    total += number

print("Total:", total)
```

Mathematical representation:

\[
S=\sum_{i=1}^{n}x_i
\]

The summation symbol means adding all the values together.

---

# 8. Calculating an Average

The arithmetic mean is calculated by dividing the sum of all values by the number of observations.

Formula:

\[
\bar{x}=\frac{\sum_{i=1}^{n}x_i}{n}
\]

Example:

```python
marks = [80, 90, 75, 85, 95]

total = 0

for mark in marks:

    total += mark

average = total / len(marks)

print("Average:", average)
```

Explanation:

1. Calculate the total.
2. Count the observations using len().
3. Divide total by the number of observations.

This concept is essential in statistics and Machine Learning.

---

# 9. Iterating Through Tuples

A tuple stores multiple values.

Unlike lists, tuples cannot be modified after creation.

Example:

```python
coordinates = (10, 20, 30, 40)

for coordinate in coordinates:

    print(coordinate)
```

Tuples can be processed using the same for loop structure as lists.

---

# 10. Iterating Through Sets

A set stores unique elements.

Example:

```python
numbers = {10, 20, 30, 40, 50}

for number in numbers:

    print(number)
```

Important characteristics:

- Sets contain unique elements.
- Sets do not guarantee a particular iteration order.
- Duplicate values are removed.

---

# 11. Iterating Through Dictionaries

Dictionaries store information as key-value pairs.

Example:

```python
student = {

    "name": "Ali",

    "age": 22,

    "marks": 90

}
```

## A. Iterate Through Keys

```python
for key in student:

    print(key)
```

## B. Iterate Through Values

```python
for value in student.values():

    print(value)
```

## C. Iterate Through Keys and Values

```python
for key, value in student.items():

    print(key, value)
```

Dictionaries are important when processing structured datasets.

---

# 12. Understanding enumerate()

The enumerate() function provides both the index and the corresponding value.

Example:

```python
subjects = ["Python", "Mathematics", "Statistics"]

for index, subject in enumerate(subjects):

    print(index, subject)
```

Output:

```text
0 Python
1 Mathematics
2 Statistics
```

We can change the starting index:

```python
for index, subject in enumerate(subjects, start=1):

    print(index, subject)
```

Output:

```text
1 Python
2 Mathematics
3 Statistics
```

Applications:

- Numbering records.
- Processing datasets.
- Tracking element positions.
- Generating reports.

---

# 13. Understanding break

The break statement immediately terminates the nearest loop.

Example:

```python
for number in range(1, 11):

    if number == 5:

        break

    print(number)
```

Output:

```text
1
2
3
4
```

When the number reaches five, Python terminates the loop.

---

# 14. Understanding continue

The continue statement skips the current iteration and moves to the next iteration.

Example:

```python
for number in range(1, 11):

    if number == 5:

        continue

    print(number)
```

Output:

```text
1
2
3
4
6
7
8
9
10
```

Difference:

| break | continue |
|---|---|
| Terminates the loop | Skips current iteration |
| No further iterations | Remaining iterations continue |
| Exits the nearest loop | Moves to the next iteration |

---

# 15. Using else with For Loops

Python allows an else block after a for loop.

The else block executes when the loop finishes normally.

Example:

```python
for number in range(1, 6):

    print(number)

else:

    print("Loop completed.")
```

Important:

If the loop terminates through break, its else block does not execute.

Example:

```python
for number in range(1, 6):

    if number == 3:

        break

else:

    print("Loop completed normally.")
```

The else block is skipped because break terminates the loop.

---

# 16. Nested For Loops

A nested loop is a loop inside another loop.

Example:

```python
for outer in range(1, 4):

    for inner in range(1, 4):

        print(outer, inner)
```

Explanation:

- The outer loop executes three times.
- During each outer iteration, the inner loop executes three times.
- Total inner executions: 3 × 3 = 9.

Nested loops are useful for:

- Matrix processing.
- Tables.
- Image pixel processing.
- Multi-dimensional datasets.
- Generating patterns.

---

# 17. Multiplication Tables

Nested loops can generate multiplication tables.

Example:

```python
for number in range(1, 6):

    for multiplier in range(1, 11):

        result = number * multiplier

        print(number, "x", multiplier, "=", result)
```

The outer loop selects the number.

The inner loop calculates its multiples.

---

# 18. Mathematical Applications of For Loops

Loops are extremely useful for mathematical calculations.

## A. Summation

\[
S=1+2+3+\cdots+n
\]

Python:

```python
total = 0

for number in range(1, 101):

    total += number

print(total)
```

## B. Factorial

Factorial is the product of all positive integers up to a given number.

\[
n!=n(n-1)(n-2)\cdots1
\]

Example:

\[
5!=5\times4\times3\times2\times1=120
\]

Python:

```python
number = 5

factorial = 1

for value in range(1, number + 1):

    factorial *= value

print(factorial)
```

Remember that:

\[
0!=1
\]

## C. Sum of Squares

\[
S=\sum_{i=1}^{n}i^2
\]

Example:

```python
total = 0

for number in range(1, 6):

    total += number ** 2

print(total)
```

Result:

\[
1+4+9+16+25=55
\]

---

# 19. Prime Number Checking

A prime number is an integer greater than one that has exactly two positive divisors: one and itself.

Examples:

2, 3, 5, 7, 11, 13.

Python:

```python
number = 29

if number > 1:

    for divisor in range(2, int(number ** 0.5) + 1):

        if number % divisor == 0:

            print("Not prime.")

            break

    else:

        print("Prime.")

else:

    print("Not prime.")
```

Why check only up to the square root?

If a number has a divisor larger than its square root, it must also have a corresponding divisor smaller than its square root.

Therefore, checking beyond the square root is unnecessary.

---

# 20. Fibonacci Sequence

The Fibonacci sequence is a mathematical sequence where each new number is the sum of the previous two numbers.

Sequence:

\[
0,1,1,2,3,5,8,13,21,\ldots
\]

Formula:

\[
F_n=F_{n-1}+F_{n-2}
\]

Python:

```python
first = 0

second = 1

for number in range(10):

    print(first)

    next_number = first + second

    first = second

    second = next_number
```

This exercise introduces iterative mathematical sequence generation.

---

# 21. Finding the Largest and Smallest Values

A loop can identify the maximum and minimum values in a dataset.

## Largest Value

```python
numbers = [45, 89, 12, 100, 67]

largest = numbers[0]

for number in numbers:

    if number > largest:

        largest = number

print(largest)
```

## Smallest Value

```python
numbers = [45, 89, 12, 100, 67]

smallest = numbers[0]

for number in numbers:

    if number < smallest:

        smallest = number

print(smallest)
```

These operations are important in descriptive statistics and data preprocessing.

---

# 22. Understanding zip()

The zip() function combines corresponding elements from multiple sequences.

Example:

```python
names = ["Ali", "Ahmed", "Sara"]

marks = [85, 90, 95]

for name, mark in zip(names, marks):

    print(name, mark)
```

Output:

```text
Ali 85
Ahmed 90
Sara 95
```

By default, zip() stops when the shortest iterable is exhausted.

Applications:

- Pairing actual and predicted values.
- Combining names and marks.
- Processing multiple datasets.
- Comparing corresponding observations.

---

# 23. List Comprehension

List comprehension is a concise way to create a new list.

Normal loop:

```python
squares = []

for number in range(1, 6):

    squares.append(number ** 2)

print(squares)
```

List comprehension:

```python
squares = [number ** 2 for number in range(1, 6)]

print(squares)
```

Both produce:

```text
[1, 4, 9, 16, 25]
```

List comprehension is useful when creating lists through simple transformations and filtering.

---

# 24. Two-Dimensional Lists and Matrix Processing

A two-dimensional list contains lists inside another list.

Example:

```python
matrix = [

    [1, 2, 3],

    [4, 5, 6],

    [7, 8, 9]

]
```

We can process every element using nested loops.

```python
for row in matrix:

    for value in row:

        print(value, end=" ")

    print()
```

A matrix is a rectangular arrangement of numbers.

Mathematical representation:

\[
A=
\begin{bmatrix}
1&2&3\\
4&5&6\\
7&8&9
\end{bmatrix}
\]

Matrices are fundamental in:

- Linear algebra.
- Machine Learning.
- Deep Learning.
- Computer Vision.
- Neural networks.

---

# 25. For Loops in Data Analysis

Loops allow us to process multiple observations.

Example:

```python
marks = [78, 85, 92, 67, 88]

total = 0

for mark in marks:

    total += mark

average = total / len(marks)

print("Average:", average)
```

In real data analysis, datasets may contain thousands or millions of observations.

Python libraries such as NumPy and Pandas provide more efficient tools for processing large numerical datasets.

---

# 26. For Loops in Artificial Intelligence

Loops are essential in AI programming.

Examples include:

1. Processing training datasets.
2. Calculating prediction errors.
3. Updating model parameters.
4. Processing image pixels.
5. Evaluating predictions.
6. Iterating through batches.
7. Training neural networks.

## Example: Prediction Error

Actual values:

\[
y=[100,200,300,400]
\]

Predicted values:

\[
\hat y=[90,210,280,390]
\]

Absolute error:

\[
|y_i-\hat y_i|
\]

Python:

```python
actual_values = [100, 200, 300, 400]

predicted_values = [90, 210, 280, 390]

for actual, predicted in zip(actual_values, predicted_values):

    error = abs(actual - predicted)

    print(error)
```

---

# 27. Mean Absolute Error (MAE)

Mean Absolute Error is a regression evaluation metric.

It measures the average absolute difference between actual and predicted values.

Formula:

\[
MAE=\frac{1}{n}\sum_{i=1}^{n}|y_i-\hat y_i|
\]

Where:

- \(n\) = Number of observations.
- \(y_i\) = Actual value.
- \(\hat y_i\) = Predicted value.

Python:

```python
actual = [100, 200, 300, 400]

predicted = [90, 210, 280, 390]

total_error = 0

for real, prediction in zip(actual, predicted):

    total_error += abs(real - prediction)

mae = total_error / len(actual)

print("MAE:", mae)
```

Result:

\[
MAE=\frac{10+10+20+10}{4}=12.5
\]

A lower MAE generally indicates smaller average absolute prediction errors.

---

# 28. Common Mistakes in For Loops

| Mistake | Explanation |
|---|---|
| Missing colon | Loop syntax becomes invalid |
| Incorrect indentation | Python cannot identify the loop block |
| Wrong range boundary | The stop value is excluded |
| Infinite assumptions | A for loop follows its iterable |
| Modifying a list while iterating | Can cause skipped or unexpected elements |
| Incorrect accumulator initialization | Can produce incorrect calculations |
| Empty collection | Accessing its first element causes an error |
| Incorrect nested loop indentation | Changes the execution structure |

### Important Example: Empty Lists

Incorrect:

```python
numbers = []

largest = numbers[0]
```

This causes an IndexError.

Safer:

```python
numbers = []

if numbers:

    largest = numbers[0]

else:

    print("List is empty.")
```

---

# 29. Time Complexity Introduction

Time complexity describes how an algorithm's running time grows as input size increases.

A single loop processing \(n\) elements generally has:

\[
O(n)
\]

Example:

```python
for number in range(n):

    print(number)
```

A nested loop where both loops process \(n\) elements generally has:

\[
O(n^2)
\]

Example:

```python
for first in range(n):

    for second in range(n):

        print(first, second)
```

| Structure | Typical complexity |
|---|---|
| Single loop | O(n) |
| Two nested loops | O(n²) |
| Three nested loops | O(n³) |

These are useful introductory rules; actual complexity depends on the operations and loop bounds.

Algorithmic complexity becomes increasingly important as we work with large AI datasets.

---

# 30. Day 012 Practical Project

## Student Performance and Data Analysis System

File: challenge.py

We developed a complete academic data analysis project.

### Project Features

- Student dataset creation.
- Individual student totals.
- Individual student averages.
- Academic grade classification.
- Pass and fail analysis.
- Highest performing student.
- Lowest performing student.
- Class average.
- Subject average analysis.
- Best and weakest subject identification.
- Even and odd mark counting.
- Pass percentage calculation.
- Individual performance reports.
- AI prediction error analysis.

### Main Concepts Used

| Concept | Application |
|---|---|
| For loops | Processing students |
| Nested loops | Processing marks and subjects |
| Dictionaries | Storing student records |
| Lists | Storing examination marks |
| zip() | Pairing subjects and marks |
| enumerate() | Accessing subject positions |
| Functions | Reusable calculations |
| Conditions | Academic classification |

---

# 31. Day 012 Solved Exercises

File: exercises.py

We completed 30 exercises covering:

1. Printing numbers.
2. Even numbers.
3. Odd numbers.
4. Counting backwards.
5. Multiplication tables.
6. Summation.
7. Factorial.
8. String iteration.
9. Vowel counting.
10. List summation.
11. Average calculation.
12. Largest value.
13. Smallest value.
14. Even and odd counting.
15. enumerate().
16. Dictionary iteration.
17. break.
18. continue.
19. Prime number checking.
20. Fibonacci sequence.
21. Multiplication tables.
22. Star patterns.
23. Sum of squares.
24. Product of list elements.
25. zip().
26. List comprehension.
27. Matrix iteration.
28. Student performance.
29. Mean Absolute Error.
30. Dataset processing.

---

# 32. Important Concepts Summary

| Concept | Meaning |
|---|---|
| Loop | Repeats instructions |
| Iteration | One execution of a loop |
| range() | Generates integer sequences |
| break | Terminates the nearest loop |
| continue | Skips the current iteration |
| else | Executes after normal loop completion |
| Nested loop | Loop inside another loop |
| enumerate() | Provides index and value |
| zip() | Combines corresponding elements |
| List comprehension | Concise list creation |
| Accumulator | Variable that collects values |
| Matrix | Two-dimensional numerical structure |
| Time complexity | Describes algorithm growth |

---

# 33. Day 012 Folder Structure

```text
day_012/
│
├── for_loop.py
├── exercises.py
├── challenge.py
└── notes.md
```

---

# 34. Learning Progress

| Day | Topic | Status |
|---|---|---|
| 001 | Introduction to Python | Completed |
| 002 | Variables | Completed |
| 003 | Data Types | Completed |
| 004 | Type Conversion | Completed |
| 005 | Operators | Completed |
| 006 | Input and Output | Completed |
| 007 | Python Fundamentals Revision | Completed |
| 008 | Python Strings | Completed |
| 009 | String Methods | Completed |
| 010 | Conditional Statements | Completed |
| 011 | Nested Conditions | Completed |
| 012 | Python For Loops | Completed |

---

# 35. Final Reflection

Day 012 helped me understand iteration and how Python processes sequences of information.

I learned how to use for loops with strings, lists, tuples, sets and dictionaries.

I also practised mathematical calculations, nested loops, dataset processing, matrix iteration and basic statistical analysis.

Most importantly, I developed a Student Performance and Data Analysis System.

These skills will support my future studies in:

- Mathematics for AI.
- Data Science.
- Machine Learning.
- Deep Learning.
- Computer Vision.

**MY LONG-TERM GOAL**

Become a skilled Artificial Intelligence and Machine Learning Engineer.

One day at a time. One concept at a time. One project at a time.

KEEP LEARNING! 🚀