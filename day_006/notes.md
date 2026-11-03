
# DAY 006 - PYTHON INPUT AND OUTPUT

## Python for Artificial Intelligence
### 90-Day Python Programming Journey

---

# 1. Introduction to Input and Output

Input and Output are fundamental concepts in Python programming.

Input means receiving information from the user.

Output means displaying information to the user.

Python uses two important built-in functions:

| Function | Purpose |
|----------|---------|
| input() | Receives information from the user |
| print() | Displays information on the screen |

Example:

```python
name = input("Enter your name: ")

print("Welcome", name)
```

If the user enters:

Abdulsamad

Output:

Welcome Abdulsamad

Input and Output are important in AI because applications
must collect information, process it and produce results.

---

# 2. The print() Function

The print() function displays information in the terminal.

Example:

```python
print("Hello World")

print(100)

print(25.5)

print(True)
```

Output:

```text
Hello World
100
25.5
True
```

We can display:

- Strings
- Integers
- Floating-point numbers
- Boolean values
- Variables
- Mathematical calculations

Example using variables:

```python
student_name = "Abdulsamad"

student_age = 23

print("Name:", student_name)

print("Age:", student_age)
```

The print() function is useful for displaying
program results, reports and debugging information.

---

# 3. The input() Function

The input() function allows users to enter information.

Example:

```python
name = input("Enter your name: ")

print("Your name is:", name)
```

Python waits for the user to enter information
and press Enter.

IMPORTANT:

The input() function always returns a string.

Example:

```python
age = input("Enter your age: ")

print(type(age))
```

Even if the user enters 23, Python initially
stores the value as a string.

---

# 4. Type Conversion with input()

Sometimes we need numerical values for mathematical
calculations.

We use type conversion to change the input
into the appropriate data type.

## Integer Conversion

int() converts a valid numerical string into an integer.

Example:

```python
age = int(input("Enter your age: "))

print(age)

print(type(age))
```

## Float Conversion

float() converts a valid numerical string
into a floating-point number.

Example:

```python
height = float(input("Enter your height: "))

print(height)

print(type(height))
```

Important functions:

| Function | Purpose |
|----------|---------|
| int() | Converts to integer |
| float() | Converts to floating-point number |
| str() | Converts to string |

These conversions are essential when collecting
numerical information from users.

---

# 5. Performing Calculations with User Input

We can collect numerical values and perform
mathematical operations.

Example:

```python
number_1 = float(input("Enter first number: "))

number_2 = float(input("Enter second number: "))

addition = number_1 + number_2

subtraction = number_1 - number_2

multiplication = number_1 * number_2

division = number_1 / number_2

print("Addition:", addition)

print("Subtraction:", subtraction)

print("Multiplication:", multiplication)

print("Division:", division)
```

We must check that the denominator is not zero
before performing division.

Example:

```python
if number_2 != 0:

    division = number_1 / number_2

else:

    print("Cannot divide by zero.")
```

This combines input, mathematical operators
and conditional statements.

---

# 6. The sep Parameter

The sep parameter controls the separator
between multiple values in print().

By default, Python uses a space.

Example:

```python
print("Python", "AI", "Machine Learning")
```

Output:

```text
Python AI Machine Learning
```

Using sep:

```python
print("Python", "AI", "Machine Learning", sep=" | ")
```

Output:

```text
Python | AI | Machine Learning
```

Another example:

```python
print("2026", "11", "03", sep="-")
```

Output:

```text
2026-11-03
```

The sep parameter is useful for formatting
information and reports.

---

# 7. The end Parameter

By default, print() moves to a new line
after displaying information.

The end parameter changes this behaviour.

Example:

```python
print("Hello")

print("World")
```

Output:

```text
Hello
World
```

Using end:

```python
print("Hello", end=" ")

print("World")
```

Output:

```text
Hello World
```

Another example:

```python
print("Python", end=" -> ")

print("Artificial Intelligence")
```

Output:

```text
Python -> Artificial Intelligence
```

The end parameter is useful for controlling
the arrangement of output.

---

# 8. Escape Characters

Escape characters control the formatting
of strings.

Important escape characters:

| Character | Purpose |
|-----------|---------|
| \n | New line |
| \t | Horizontal tab |
| \\ | Displays a backslash |
| \" | Displays double quotation marks |
| \' | Displays single quotation marks |

## New Line

```python
print("Hello\nWorld")
```

Output:

```text
Hello
World
```

## Tab

```python
print("Name:\tAbdulsamad")
```

Output:

```text
Name:   Abdulsamad
```

## Backslash

```python
print("Python\\AI")
```

Output:

```text
Python\AI
```

Escape characters help us format
text and organize program output.

---

# 9. Formatted Strings (F-Strings)

F-strings allow us to insert variables
and expressions directly into strings.

We place the letter f before the quotation marks.

Variables are placed inside curly brackets {}.

Example:

```python
name = "Abdulsamad"

age = 23

print(f"My name is {name}.")

print(f"I am {age} years old.")
```

Output:

```text
My name is Abdulsamad.
I am 23 years old.
```

We can also perform calculations inside f-strings.

Example:

```python
age = 23

print(f"Next year I will be {age + 1}.")
```

Output:

```text
Next year I will be 24.
```

F-strings make Python programs easier to read
and produce professional output.

---

# 10. Decimal Formatting

F-strings allow us to control the number
of decimal places displayed.

Example:

```python
accuracy = 95.678945

print(f"{accuracy:.2f}")

print(f"{accuracy:.3f}")

print(f"{accuracy:.1f}")
```

Output:

```text
95.68
95.679
95.7
```

Explanation:

| Format | Meaning |
|--------|---------|
| :.1f | One decimal place |
| :.2f | Two decimal places |
| :.3f | Three decimal places |
| :.4f | Four decimal places |

This is particularly useful when displaying
accuracy, percentages and statistical results.

IMPORTANT:

Decimal formatting changes how a number is displayed.
It does not change the original stored value.

---

# 11. Multiple Inputs Using split()

The split() method separates a string into
multiple parts.

Example:

```python
numbers = input("Enter two numbers: ").split()
```

If the user enters:

```text
10 20
```

Python produces:

```python
["10", "20"]
```

We can assign the separated values to variables.

Example:

```python
number_1, number_2 = input(
    "Enter two numbers: "
).split()

number_1 = int(number_1)

number_2 = int(number_2)

total = number_1 + number_2

print("Total:", total)
```

IMPORTANT:

The split() method produces strings.

We must convert them into numerical values
before performing mathematical calculations.

---

# 12. Input Validation Using try and except

Users sometimes enter incorrect information.

For example:

```python
age = int("Hello")
```

This produces a ValueError because Hello
cannot be converted into an integer.

We use try and except to handle such errors.

Example:

```python
user_age = input("Enter your age: ")

try:

    age = int(user_age)

    print("Your age is:", age)

except ValueError:

    print("Invalid input!")

    print("Please enter a whole number.")
```

Explanation:

- try contains code that might produce an error.
- except handles a specified error.
- ValueError occurs when a value has an inappropriate format.

Input validation helps make programs more reliable.

---

# 13. Truthy and Falsy Values in Input

Python can evaluate values as True or False
inside conditional statements.

Examples:

| Value | Boolean Behaviour |
|-------|-------------------|
| "" | False |
| "Python" | True |
| 0 | False |
| 1 | True |
| [] | False |
| [10, 20] | True |
| None | False |

Example:

```python
username = input("Enter username: ")

if username:

    print("Username entered successfully.")

else:

    print("Username cannot be empty.")
```

An empty string is falsy.

A non-empty string is truthy.

The strip() method can remove unnecessary
leading and trailing whitespace.

Example:

```python
username = input("Enter username: ").strip()
```

---

# 14. Input and Output in Artificial Intelligence

Input and Output are important in AI applications.

An AI application commonly follows this process:

1. Collect information.
2. Prepare the information.
3. Process the information.
4. Generate a prediction.
5. Display the result.

## Example 1: Student Data Collection

```python
student_name = input("Enter student name: ")

mathematics = float(input("Enter Mathematics marks: "))

physics = float(input("Enter Physics marks: "))

python_marks = float(input("Enter Python marks: "))

average = (
    mathematics + physics + python_marks
) / 3

print(f"Student: {student_name}")

print(f"Average Marks: {average:.2f}")
```

## Example 2: AI Model Information

```python
model_name = input("Enter model name: ")

accuracy = float(input("Enter model accuracy: "))

epochs = int(input("Enter training epochs: "))

learning_rate = float(input("Enter learning rate: "))

print(f"Model: {model_name}")

print(f"Accuracy: {accuracy:.2f}%")

print(f"Epochs: {epochs}")

print(f"Learning Rate: {learning_rate:.5f}")
```

This demonstrates collecting and displaying
machine learning model information.

---

# 15. Connection to Computer Vision

Input and Output can also be used to collect
and display image-related numerical information.

An 8-bit image channel has values from 0 to 255.

We can normalize these values into a range
between 0 and 1.

Formula:

Normalized Value = Pixel Value / 255

Example:

```python
pixel = 128

normalized_pixel = pixel / 255

print(f"Normalized Pixel: {normalized_pixel:.4f}")
```

Output:

```text
Normalized Pixel: 0.5020
```

This is a simple example of numerical
preprocessing used in Computer Vision.

Later, we will learn how NumPy and PyTorch
process complete image arrays and tensors.

---

# 16. Important Python Functions and Methods

| Function / Method | Purpose |
|-------------------|---------|
| print() | Displays information |
| input() | Receives user information |
| int() | Converts to integer |
| float() | Converts to float |
| str() | Converts to string |
| type() | Checks data type |
| split() | Separates a string |
| strip() | Removes surrounding whitespace |
| abs() | Returns absolute value |

These functions and methods make it easier
to collect, convert and process information.

---

# 17. Common Mistakes to Avoid

1. Forgetting that input() returns a string.
2. Performing mathematical calculations on strings.
3. Forgetting int() or float() when necessary.
4. Dividing by zero.
5. Using incorrect f-string syntax.
6. Forgetting the colon in :.2f.
7. Forgetting that split() returns strings.
8. Forgetting indentation inside try and except.
9. Entering invalid numerical information.
10. Confusing sep and end.

---

# 18. What I Learned in Day 006

Today I learned:

- The meaning of Input and Output.
- The print() function.
- The input() function.
- Collecting information from users.
- Displaying variables.
- Integer and float conversion.
- Performing calculations using user input.
- The sep parameter.
- The end parameter.
- Escape characters.
- Formatted strings (f-strings).
- Decimal formatting.
- The split() method.
- Input validation using try and except.
- Truthy and falsy values.
- Collecting AI model information.
- Basic image pixel normalization.

I also developed an interactive AI Student
Data Analyzer using Python.

---

# 19. Day 006 Files Completed

day_006/

1. input_output.py
   Main lesson covering Python Input and Output.

2. exercises.py
   Twelve solved practical exercises.

3. challenge.py
   Interactive AI Student Data Analyzer.

4. notes.md
   Complete revision notes and explanations.

---

# 20. Connection to Future AI Topics

The knowledge gained today will help me understand:

- Collecting datasets.
- Reading CSV files using Pandas.
- Processing numerical information using NumPy.
- Collecting image information.
- Building interactive AI applications.
- Preparing data for Machine Learning.
- Displaying model predictions.
- Building interfaces for Deep Learning applications.

Input and Output are fundamental parts of
interactive programming and AI application development.

---

# DAY 006 COMPLETED

One day at a time.
One concept at a time.
One step closer to becoming an AI Engineer.

My objective is not simply to memorize Python syntax.
I want to understand how Python works and how
I can apply it in Artificial Intelligence.

END OF DAY 006.
