
# DAY 005 - PYTHON OPERATORS

## Python for Artificial Intelligence
### 90-Day Python Programming Journey

---

# 1. What Are Python Operators?

Operators are special symbols or keywords used to
perform operations on variables and values.

The values on which operators perform operations
are called operands.

Example:

```python
a = 10
b = 5

result = a + b

print(result)
```

Output:
15

In this example:

- a and b are operands.
- + is the operator.
- 15 is the result.

Operators are important in AI because machine learning
requires mathematical calculations, comparisons,
logical decisions and parameter updates.

---

# 2. Types of Python Operators

Python has seven major categories of operators.

1. Arithmetic Operators
2. Assignment Operators
3. Comparison Operators
4. Logical Operators
5. Bitwise Operators
6. Membership Operators
7. Identity Operators

---

# 3. Arithmetic Operators

Arithmetic operators perform mathematical calculations.

| Operator | Meaning |
|----------|---------|
| + | Addition |
| - | Subtraction |
| * | Multiplication |
| / | Division |
| // | Floor Division |
| % | Modulus |
| ** | Exponentiation |

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
print(a ** 2)
```

Output:

```text
26
14
120
3.3333333333333335
3
2
400
```

Important concepts:

- Division (/) returns a floating-point result.
- Floor division (//) rounds down to the nearest
  integer.
- Modulus (%) returns the remainder.
- Exponentiation (**) raises a number to a power.

AI Applications:

Arithmetic operators are used for:

- Calculating averages.
- Calculating prediction errors.
- Computing model accuracy.
- Performing mathematical calculations.
- Updating model parameters.

---

# 4. Assignment Operators

Assignment operators assign or update variable values.

| Operator | Example | Equivalent |
|----------|---------|------------|
| = | x = 10 | Assign 10 |
| += | x += 5 | x = x + 5 |
| -= | x -= 5 | x = x - 5 |
| *= | x *= 5 | x = x * 5 |
| /= | x /= 5 | x = x / 5 |
| //= | x //= 5 | x = x // 5 |
| %= | x %= 5 | x = x % 5 |
| **= | x **= 2 | x = x ** 2 |

Example:

```python
score = 100

score += 20
print(score)

score -= 10
print(score)

score *= 2
print(score)
```

Output:

```text
120
110
220
```

Important:

The operator += adds a value to the existing variable
and stores the updated result.

AI Applications:

- Updating learning rates.
- Updating model parameters.
- Managing training counters.
- Updating numerical values.

---

# 5. Comparison Operators

Comparison operators compare two values.

They return Boolean values: True or False.

| Operator | Meaning |
|----------|---------|
| == | Equal to |
| != | Not equal to |
| > | Greater than |
| < | Less than |
| >= | Greater than or equal to |
| <= | Less than or equal to |

Example:

```python
marks = 85

print(marks == 85)
print(marks != 90)
print(marks > 50)
print(marks < 50)
print(marks >= 85)
print(marks <= 100)
```

Output:

```text
True
True
True
False
True
True
```

Important difference:

= assigns a value.

== compares two values.

AI Applications:

- Checking model accuracy.
- Comparing predictions.
- Evaluating performance thresholds.
- Checking numerical conditions.

---

# 6. Logical Operators

Logical operators combine multiple conditions.

Python has three main logical operators.

| Operator | Meaning |
|----------|---------|
| and | Both conditions must be True |
| or | At least one condition must be True |
| not | Reverses the Boolean result |

Example:

```python
age = 23
marks = 85

print(age >= 18 and marks >= 50)

print(age >= 18 or marks >= 90)

print(not True)
```

Output:

```text
True
True
False
```

Explanation:

AND:
Both conditions must be satisfied.

OR:
At least one condition must be satisfied.

NOT:
Reverses True into False and False into True.

AI Applications:

- Data filtering.
- Decision-making systems.
- Conditional processing.
- Checking multiple model requirements.

---

# 7. Bitwise Operators

Bitwise operators work directly with the binary
representation of integers.

Binary uses two digits:

0 and 1.

Example:

5 = 0101
3 = 0011

| Operator | Name |
|----------|------|
| & | Bitwise AND |
| \| | Bitwise OR |
| ^ | Bitwise XOR |
| ~ | Bitwise NOT |
| << | Left Shift |
| >> | Right Shift |

Example:

```python
a = 5
b = 3

print(a & b)
print(a | b)
print(a ^ b)
print(~a)
print(a << 1)
print(a >> 1)
```

Output:

```text
1
7
6
-6
10
2
```

Explanation:

AND:
Both corresponding bits must be 1.

OR:
At least one corresponding bit must be 1.

XOR:
Corresponding bits must be different.

NOT:
Inverts the bits.

Left Shift:
Moves bits to the left.

Right Shift:
Moves bits to the right.

AI Applications:

- Binary data processing.
- Image masks.
- Computer vision operations.
- Low-level numerical processing.

---

# 8. Membership Operators

Membership operators check whether an element
exists inside a collection.

Two membership operators:

- in
- not in

Example:

```python
ai_topics = [
    "Python",
    "Machine Learning",
    "Deep Learning"
]

print("Python" in ai_topics)

print("Robotics" in ai_topics)

print("Robotics" not in ai_topics)
```

Output:

```text
True
False
True
```

AI Applications:

- Checking dataset categories.
- Checking available labels.
- Searching for specific values.
- Validating data.

---

# 9. Identity Operators

Identity operators check whether two variables
refer to the same object in memory.

Two identity operators:

- is
- is not

Example:

```python
list_1 = [10, 20, 30]

list_2 = list_1

list_3 = [10, 20, 30]

print(list_1 is list_2)

print(list_1 is list_3)

print(list_1 == list_3)
```

Output:

```text
True
False
True
```

Important difference:

is checks object identity.

== checks whether values are equal.

AI Applications:

- Checking whether an object is None.
- Debugging Python objects.
- Understanding references to data objects.

---

# 10. Operator Precedence

Operator precedence determines the order in which
Python performs operations.

Common precedence order:

1. Parentheses ()
2. Exponentiation **
3. Multiplication, division, floor division, modulus
4. Addition and subtraction
5. Comparison operators
6. not
7. and
8. or

Example:

```python
result = 10 + 5 * 2

print(result)
```

Output:

20

Why?

Multiplication happens before addition.

Using parentheses:

```python
result = (10 + 5) * 2

print(result)
```

Output:

30

Parentheses allow us to control the order of
mathematical calculations.

---

# 11. Boolean Values

Boolean values represent logical truth.

Python has only two Boolean values:

True
False

Example:

```python
is_student = True

is_graduated = False

print(is_student)
print(is_graduated)
```

Boolean values are important when working with
conditions and decision-making systems.

---

# 12. Operators in Artificial Intelligence

Operators are essential in AI and machine learning.

They help us perform mathematical calculations,
evaluate predictions and update model parameters.

## Example 1: Model Accuracy

Accuracy measures the percentage of correct predictions.

Formula:

Accuracy = (Correct Predictions / Total Predictions) * 100

Example:

```python
correct_predictions = 940
total_predictions = 1000

accuracy = (
    correct_predictions / total_predictions
) * 100

print(accuracy)
```

Output:

94.0

The model correctly classified 94% of the images.

## Example 2: Prediction Error

```python
actual_value = 100
predicted_value = 92

error = actual_value - predicted_value

print(error)
```

Output:

8

Prediction error measures the difference between
the actual and predicted values.

## Example 3: Learning Rate Update

```python
learning_rate = 0.01

learning_rate *= 0.90

print(learning_rate)
```

Output:

0.009000000000000001

The learning rate was reduced by 10%.

These are simplified examples of operations used
during machine learning development.

---

# 13. Important Python Functions Used Today

We also used some built-in Python functions.

| Function | Purpose |
|----------|---------|
| print() | Displays information |
| abs() | Returns the absolute value |
| type() | Checks an object's data type |

Important:

abs() and print() are functions, not operators.

---

# 14. Common Mistakes to Avoid

1. Confusing = with ==.
2. Confusing / with //.
3. Forgetting that % returns the remainder.
4. Using is instead of == for value comparisons.
5. Forgetting operator precedence.
6. Using AND when OR is required.
7. Forgetting that comparisons return Boolean values.
8. Dividing by zero.

---

# 15. What I Learned in Day 005

Today I learned:

- What Python operators are.
- What operands are.
- Arithmetic operators.
- Assignment operators.
- Comparison operators.
- Logical operators.
- Bitwise operators.
- Membership operators.
- Identity operators.
- Operator precedence.
- Boolean values.
- How operators are applied in AI calculations.
- How to calculate model accuracy.
- How to calculate prediction errors.
- How to update a learning rate.

I also developed an AI Model Performance Analyzer
using Python operators.

---

# 16. Day 005 Files Completed

day_005/

1. operators.py
   Main lesson covering all operator categories.

2. exercises.py
   Twelve solved practical exercises.

3. challenge.py
   AI Model Performance Analyzer.

4. notes.md
   Complete learning notes and revision material.

---

# 17. Connection to Future AI Topics

The knowledge gained today will help me understand:

- NumPy mathematical operations.
- Pandas data filtering.
- Statistical calculations.
- Machine Learning formulas.
- Neural network computations.
- PyTorch tensor operations.

Operators are among the fundamental building blocks
of numerical programming in Artificial Intelligence.

---

# DAY 005 COMPLETED

One day at a time.
One concept at a time.
One step closer to becoming an AI Engineer.

My goal is to understand Python deeply and apply
it practically in Artificial Intelligence.

END OF DAY 005.
