
# DAY 002 — VARIABLES IN PYTHON

## 1. What Are Variables?

A variable is a name that refers to a value or object in Python.

Variables allow us to store information and use it
whenever we need it in a program.

Example:

```python
student_name = "Abdulsamad"
student_age = 23
country = "Kenya"

print(student_name)
print(student_age)
print(country)
```

Output:

```text
Abdulsamad
23
Kenya
```

Explanation:

- student_name stores a student's name.
- student_age stores the student's age.
- country stores the country.
- print() displays the values.

## 2. Variable Assignment

Variable assignment means giving a value to a variable.

The equal sign (=) is called the assignment operator.

Example:

```python
age = 23
name = "Abdulsamad"
```

Explanation:

- age is the variable name.
- 23 is the assigned value.
- = assigns the value to the variable.

Important:

The = symbol is used for assignment, not comparison.

## 3. Printing Variables

The print() function displays information
in the Python terminal.

Example:

```python
name = "Ali"
age = 25

print(name)
print(age)

print("My name is", name)
print("My age is", age)
```

Output:

```text
Ali
25
My name is Ali
My age is 25
```

## 4. Variables Can Store Different Values

A variable can refer to different types of values.

Examples:

```python
name = "Abdulsamad"
age = 23
height = 1.75
is_student = True
```

These values represent:

- name: Text
- age: Integer number
- height: Decimal number
- is_student: Boolean value

We will study these data types in detail in Day 003.

## 5. Changing Variable Values (Reassignment)

A variable can be assigned a new value.

Example:

```python
course = "Python"

print(course)

course = "Machine Learning"

print(course)
```

Output:

```text
Python
Machine Learning
```

Explanation:

The first assignment gives course the value Python.

The second assignment replaces its previous value
with Machine Learning.

## 6. Multiple Variable Assignment

Python allows us to assign values to multiple
variables in one statement.

Example:

```python
name, age, country = "Ali", 23, "Kenya"

print(name)
print(age)
print(country)
```

Output:

```text
Ali
23
Kenya
```

Each variable receives its corresponding value.

## 7. Assigning the Same Value to Multiple Variables

Python allows multiple variables to receive
the same value in one statement.

Example:

```python
x = y = z = 100

print(x)
print(y)
print(z)
```

Output:

```text
100
100
100
```

## 8. Swapping Variables

Swapping means exchanging the values of two variables.

Example:

```python
a = 10
b = 20

a, b = b, a

print(a)
print(b)
```

Output:

```text
20
10
```

Explanation:

Python allows us to exchange the values
without creating a temporary variable.

## 9. Rules for Naming Variables

Python has specific rules for naming variables.

RULE 1:
A variable name must start with a letter
or an underscore (_).

RULE 2:
A variable name cannot start with a number.

RULE 3:
Variable names cannot contain spaces.

RULE 4:
Variable names cannot contain hyphens.

RULE 5:
Python keywords cannot be used as variable names.

RULE 6:
Python is case-sensitive.

Examples:

Valid variable names:

```python
student_name = "Ali"
student_age = 23
_age = 25
marks2 = 90
studentAge = 21
```

Invalid variable names:

```python
# 2student = "Ali"
# student-name = "Ali"
# student name = "Ali"
# class = "AI"
```

## 10. Python Is Case-Sensitive

Python treats uppercase and lowercase letters
as different characters.

Example:

```python
name = "Ali"
Name = "Ahmed"
NAME = "John"

print(name)
print(Name)
print(NAME)
```

Output:

```text
Ali
Ahmed
John
```

These are three different variables.

## 11. Checking Variable Types Using type()

The type() function tells us the type of an object.

Example:

```python
name = "Ali"
age = 23
height = 1.75
is_student = True

print(type(name))
print(type(age))
print(type(height))
print(type(is_student))
```

Output:

```text
<class 'str'>
<class 'int'>
<class 'float'>
<class 'bool'>
```

Explanation:

- str = String (text)
- int = Integer (whole number)
- float = Floating-point number (decimal)
- bool = Boolean (True or False)

## 12. F-Strings in Python

An f-string allows us to insert variables
directly inside a text message.

We use the letter f before quotation marks.

Variables are placed inside curly brackets {}.

Example:

```python
name = "Ali"
age = 23

print(f"My name is {name}")
print(f"I am {age} years old.")
```

Output:

```text
My name is Ali
I am 23 years old.
```

F-strings make displaying variable information easier.

## 13. Constants in Python

A constant is a value that should normally
remain unchanged throughout a program.

Python does not strictly enforce constants.

By convention, programmers use uppercase names.

Example:

```python
PI = 3.14159
MAX_STUDENTS = 100
UNIVERSITY_NAME = "AI University"

print(PI)
print(MAX_STUDENTS)
print(UNIVERSITY_NAME)
```

Important:

Uppercase naming is a convention.
Python still allows these variables to be reassigned.

## 14. Comments in Python

Comments are explanations written inside code.

Python ignores comments when executing a program.

We use the # symbol to create a comment.

Example:

```python
# This is a comment

student_name = "Ali"

# Display the student name
print(student_name)
```

Comments help programmers understand their code.

## 15. Important Python Commands

| Command | Purpose |
|---------|---------|
| print() | Displays information |
| type() | Checks the type of an object |
| = | Assigns a value |
| f-string | Inserts variables into text |
| # | Creates a comment |
| \n | Creates a new line |
| a, b = b, a | Swaps two values |

## 16. Where Are Variables Used in AI?

Variables are extremely important in Artificial Intelligence.

They store information required by AI programs.

Example:

```python
model_name = "Image Classifier"

learning_rate = 0.001

epochs = 100

batch_size = 32

accuracy = 95.5

print(model_name)
print(learning_rate)
print(epochs)
print(batch_size)
print(accuracy)
```

Explanation:

1. model_name:
   Stores the name of an AI model.

2. learning_rate:
   Controls the size of parameter updates
   during model training.

3. epochs:
   Number of complete passes through the training dataset.

4. batch_size:
   Number of training examples processed
   in one batch.

5. accuracy:
   Measures the proportion of correct predictions
   in a classification task.

These variables will become very important
when we study Machine Learning and PyTorch.

## 17. Important Differences to Remember

| Concept | Meaning |
|---------|---------|
| Variable | A name referring to a value or object |
| Assignment | Giving a value to a variable |
| Reassignment | Giving a variable a new value |
| Multiple assignment | Assigning multiple variables together |
| Swapping | Exchanging variable values |
| Constant | A value intended to remain unchanged |
| Case-sensitive | Uppercase and lowercase are different |

## 18. Common Beginner Mistakes

Mistake 1: Using an invalid variable name.

Incorrect:

```python
2name = "Ali"
```

Correct:

```python
name2 = "Ali"
```

Mistake 2: Forgetting quotation marks around text.

Incorrect:

```python
name = Ali
```

Correct:

```python
name = "Ali"
```

Mistake 3: Confusing uppercase and lowercase.

Example:

```python
age = 23
Age = 25

print(age)
print(Age)
```

These are different variables.

Mistake 4: Confusing assignment with comparison.

```python
age = 23
```

The single equals sign assigns a value.

## 19. Day 002 Summary

Today we learned:

1. What variables are.
2. How to create variables.
3. How to assign values.
4. How to print variables.
5. How to change variable values.
6. Multiple variable assignment.
7. Assigning the same value to multiple variables.
8. Swapping variables.
9. Variable naming rules.
10. Python case sensitivity.
11. Checking types using type().
12. Using f-strings.
13. Understanding constants.
14. Writing comments.
15. Applying variables in AI programming.

## 20. Revision Questions

1. What is a variable in Python?
2. What is variable assignment?
3. What does the print() function do?
4. Can we change a variable's value?
5. What is multiple assignment?
6. What does swapping mean?
7. What are the rules for naming variables?
8. Is Python case-sensitive?
9. What does type() do?
10. What is an f-string?
11. What is a constant?
12. Why are variables important in AI?

## Final Learning Reminder

Do not just memorize Python commands.

Understand what they do, why they are used
and how to apply them in real programs.

One day at a time.
One concept at a time.

END OF DAY 002.
