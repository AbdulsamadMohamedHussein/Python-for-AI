# DAY 013 — PYTHON WHILE LOOPS

## Bachelor's in Artificial Intelligence
### 90-Day Python Programming Journey

**Subject:** Python Programming  
**Topic:** While Loops and Iteration  
**Level:** Beginner to Intermediate  
**Main File:** `while_loops.py`

---

# 1. Introduction to While Loops

A while loop is a control-flow structure in Python that repeatedly executes a block of code as long as a specified condition evaluates to True.

Loops are important because computers often need to perform repetitive operations.

For example:
- Counting numbers.
- Calculating mathematical expressions.
- Processing datasets.
- Validating user input.
- Running interactive applications.
- Performing repetitive calculations in Machine Learning.

### Basic syntax

```python
while condition:

    statement
```

The loop continues while the condition is True.

When the condition becomes False, Python terminates the loop.

### Example

```python
number = 1

while number <= 5:

    print(number)

    number += 1
```

Output:

```text
1
2
3
4
5
```

**Explanation:**

1. Initialize number at 1.
2. Check whether number is less than or equal to 5.
3. Print the current number.
4. Increase number by one.
5. Repeat until the condition becomes False.

---

# 2. Understanding the Three Main Components

Every basic counter-controlled while loop contains three important components.

| Component | Meaning | Example |
|---|---|---|
| Initialization | Starting value | `number = 1` |
| Condition | Determines whether the loop continues | `number <= 10` |
| Update | Changes the variable | `number += 1` |

### Example

```python
number = 1

while number <= 10:

    print(number)

    number += 1
```

**Important:** Forgetting to update the counter can create an infinite loop.

---

# 3. Understanding Boolean Conditions

A Boolean expression produces either True or False.

While loops depend on Boolean conditions.

Examples:

```python
number = 10

print(number > 5)    # True

print(number < 5)    # False

print(number == 10)  # True

print(number != 10)  # False
```

Common comparison operators:

| Operator | Meaning |
|---|---|
| `==` | Equal to |
| `!=` | Not equal to |
| `>` | Greater than |
| `<` | Less than |
| `>=` | Greater than or equal to |
| `<=` | Less than or equal to |

Logical operators can combine conditions.

| Operator | Meaning |
|---|---|
| `and` | Both conditions must be True |
| `or` | At least one condition must be True |
| `not` | Reverses the Boolean result |

Example:

```python
age = 25

while age >= 18 and age <= 30:

    print("Age is within the range.")

    age += 1
```

---

# 4. Understanding Infinite Loops

An infinite loop is a loop that never terminates naturally.

Example:

```python
number = 1

while number <= 5:

    print(number)
```

Why does this happen?

Because number never changes.

It remains equal to 1, so the condition remains True.

### Correct version

```python
number = 1

while number <= 5:

    print(number)

    number += 1
```

Infinite loops are not always mistakes. They are deliberately used in interactive applications and servers when an explicit exit condition exists.

Example:

```python
while True:

    command = input("Enter exit to stop: ")

    if command == "exit":

        break
```

---

# 5. Counting Forwards and Backwards

A while loop can count in either direction.

### Counting forwards

```python
number = 1

while number <= 10:

    print(number)

    number += 1
```

### Counting backwards

```python
number = 10

while number >= 1:

    print(number)

    number -= 1
```

The `+=` operator increases a variable.

The `-=` operator decreases a variable.

---

# 6. Even and Odd Numbers

The modulo operator `%` calculates the remainder after division.

A number is even if it is divisible by 2 without a remainder.

Mathematical condition:

\[
n \bmod 2 = 0
\]

A number is odd if:

\[
n \bmod 2 \neq 0
\]

### Python example

```python
number = 1

while number <= 20:

    if number % 2 == 0:

        print("Even:", number)

    else:

        print("Odd:", number)

    number += 1
```

This introduces the combination of loops and conditional statements.

---

# 7. Accumulators

An accumulator is a variable that stores a running result during repeated calculations.

It is commonly used for:
- Summation.
- Multiplication.
- Statistical calculations.
- Financial calculations.
- Dataset processing.

### Example: Summation

```python
number = 1

total = 0

while number <= 5:

    total += number

    number += 1

print(total)
```

Output:

```text
15
```

Mathematical representation:

\[
S=1+2+3+4+5
\]

\[
S=15
\]

General summation notation:

\[
S=\sum_{i=1}^{n}x_i
\]

---

# 8. Factorial Calculations

Factorial is the product of all positive integers from 1 up to a given integer.

Mathematical notation:

\[
n!=n(n-1)(n-2)\cdots 1
\]

Example:

\[
5!=5\times4\times3\times2\times1
\]

\[
5!=120
\]

Special rule:

\[
0!=1
\]

### Python implementation

```python
number = 5

factorial = 1

counter = 1

while counter <= number:

    factorial *= counter

    counter += 1

print(factorial)
```

Factorials are important in:
- Combinatorics.
- Probability.
- Permutations.
- Statistical mathematics.
- Mathematical modelling.

---

# 9. Understanding Integer Division and Modulo

Two particularly important operators are:

| Operator | Purpose |
|---|---|
| `%` | Returns the remainder |
| `//` | Returns the floor of the division |

Example:

```python
print(17 % 10)   # 7

print(17 // 10)  # 1
```

These operators are particularly useful for digit-based mathematical problems.

### Extracting digits

```python
number = 1234

while number > 0:

    digit = number % 10

    print(digit)

    number //= 10
```

Output:

```text
4
3
2
1
```

Notice that the digits are extracted from right to left.

---

# 10. Counting the Digits of a Number

We can count the digits of an integer using repeated integer division.

Example:

```python
number = 12345

count = 0

while number > 0:

    number //= 10

    count += 1

print(count)
```

Output:

```text
5
```

Mathematical idea:

\[
12345\rightarrow1234\rightarrow123\rightarrow12\rightarrow1\rightarrow0
\]

Each division removes one decimal digit.

Special cases such as zero and negative integers should be handled separately in a complete application.

---

# 11. Reversing a Number

A while loop can reverse an integer mathematically.

Example:

\[
12345\rightarrow54321
\]

### Python implementation

```python
number = 12345

reversed_number = 0

while number > 0:

    digit = number % 10

    reversed_number = reversed_number * 10 + digit

    number //= 10

print(reversed_number)
```

### How the calculation works

| Original number | Extracted digit | Reversed number |
|---|---:|---:|
| 12345 | 5 | 5 |
| 1234 | 4 | 54 |
| 123 | 3 | 543 |
| 12 | 2 | 5432 |
| 1 | 1 | 54321 |

This is an excellent exercise for understanding integer operations.

---

# 12. Palindrome Numbers

A palindrome is a number that reads the same forwards and backwards.

Examples:

- 121
- 1331
- 1221
- 555

Mathematical condition:

\[
\text{Original Number}=\text{Reversed Number}
\]

### Python implementation

```python
number = 121

original = number

reversed_number = 0

while number > 0:

    digit = number % 10

    reversed_number = reversed_number * 10 + digit

    number //= 10

if original == reversed_number:

    print("Palindrome")

else:

    print("Not a palindrome")
```

---

# 13. Fibonacci Sequence

The Fibonacci sequence is a mathematical sequence in which each new term is the sum of the previous two terms.

Sequence:

\[
0,1,1,2,3,5,8,13,21,34,\ldots
\]

Mathematical definition:

\[
F_n=F_{n-1}+F_{n-2}
\]

Initial conditions:

\[
F_0=0,\quad F_1=1
\]

### Python implementation

```python
first = 0

second = 1

count = 0

while count < 10:

    print(first)

    next_number = first + second

    first = second

    second = next_number

    count += 1
```

Applications:
- Mathematical modelling.
- Algorithm design.
- Recursion and iteration studies.
- Sequence analysis.

---

# 14. Prime Number Detection

A prime number is an integer greater than 1 that has exactly two positive divisors: 1 and itself.

Examples:

2, 3, 5, 7, 11, 13, 17.

### Python implementation

```python
number = 29

divisor = 2

is_prime = number > 1

while is_prime and divisor * divisor <= number:

    if number % divisor == 0:

        is_prime = False

        break

    divisor += 1

if is_prime:

    print("Prime number")

else:

    print("Not prime")
```

### Why stop at the square root?

If a number has a factor greater than its square root, it must have a corresponding factor smaller than its square root.

Therefore, checking possible divisors only up to:

\[
d\leq\sqrt{n}
\]

is sufficient.

This improves algorithm efficiency.

---

# 15. break Statement

The break statement immediately terminates the nearest enclosing loop.

Example:

```python
number = 1

while number <= 10:

    if number == 5:

        break

    print(number)

    number += 1
```

Output:

```text
1
2
3
4
```

When the counter reaches 5, the loop terminates.

Applications:
- Stopping a search.
- Exiting interactive menus.
- Ending password attempts.
- Terminating a search when a result is found.

---

# 16. continue Statement

The continue statement skips the remaining statements in the current iteration and moves to the next iteration.

Example:

```python
number = 0

while number < 10:

    number += 1

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

Important: In while loops, update the counter before continuing when necessary. Otherwise, the same condition may remain True indefinitely.

### Difference between break and continue

| break | continue |
|---|---|
| Terminates the nearest loop | Skips the current iteration |
| Exits the loop | Continues with the next iteration |
| Stops further loop execution | Allows future iterations |

---

# 17. else with While Loops

Python allows an else block after a while loop.

The else block executes when the loop terminates normally because its condition becomes False.

Example:

```python
number = 1

while number <= 5:

    print(number)

    number += 1

else:

    print("Loop completed.")
```

If break terminates the loop, the else block is skipped.

This feature can be useful when searching for an item or checking whether a condition was satisfied.

---

# 18. Nested While Loops

A nested while loop is a while loop placed inside another while loop.

Example:

```python
row = 1

while row <= 3:

    column = 1

    while column <= 3:

        print(row, column)

        column += 1

    row += 1
```

Explanation:

- The outer loop controls the rows.
- The inner loop controls the columns.
- The inner loop completes all its iterations before the outer loop advances.

If both loops execute three times:

\[
3\times3=9
\]

Total inner-loop executions equal nine.

Applications:
- Matrix processing.
- Tabular data.
- Image processing.
- Multi-dimensional datasets.

---

# 19. Star Patterns Using Nested Loops

Example:

```python
row = 1

while row <= 5:

    column = 1

    while column <= row:

        print("*", end=" ")

        column += 1

    print()

    row += 1
```

Output:

```text
*
* *
* * *
* * * *
* * * * *
```

This exercise teaches how nested loops control repeated structures.

---

# 20. Iterating Through Lists Using While Loops

Lists contain multiple elements.

We can process list elements using their index positions.

Example:

```python
numbers = [10, 20, 30, 40, 50]

index = 0

while index < len(numbers):

    print(numbers[index])

    index += 1
```

Important concepts:

- Python list indexing starts at zero.
- `len()` returns the number of elements.
- The index identifies the current position.

This method is useful when we need to control the index manually.

---

# 21. Finding Maximum and Minimum Values

A while loop can identify the largest and smallest values in a numerical dataset.

### Maximum

```python
numbers = [45, 89, 12, 100, 67]

largest = numbers[0]

index = 1

while index < len(numbers):

    if numbers[index] > largest:

        largest = numbers[index]

    index += 1

print(largest)
```

### Minimum

```python
numbers = [45, 89, 12, 100, 67]

smallest = numbers[0]

index = 1

while index < len(numbers):

    if numbers[index] < smallest:

        smallest = numbers[index]

    index += 1

print(smallest)
```

These are fundamental descriptive statistics operations.

For a production-quality function, handle an empty dataset before accessing its first element.

---

# 22. Arithmetic Mean

The arithmetic mean is the sum of all observations divided by the number of observations.

Formula:

\[
\bar{x}=\frac{1}{n}\sum_{i=1}^{n}x_i
\]

Where:

- \(\bar{x}\) = Mean.
- \(n\) = Number of observations.
- \(x_i\) = Individual observation.

Example:

```python
numbers = [10, 20, 30, 40, 50]

total = 0

index = 0

while index < len(numbers):

    total += numbers[index]

    index += 1

average = total / len(numbers)

print(average)
```

Result:

\[
\bar{x}=\frac{150}{5}=30
\]

This mathematical concept is fundamental to statistics and Machine Learning.

---

# 23. Input Validation

Input validation ensures that the user provides acceptable information.

Example:

```python
while True:

    try:

        age = int(input("Enter your age: "))

        if age >= 0:

            break

        else:

            print("Age cannot be negative.")

    except ValueError:

        print("Enter a valid whole number.")

print("Your age is:", age)
```

Important concepts:

| Concept | Purpose |
|---|---|
| try | Attempts to execute code |
| except | Handles an exception |
| ValueError | Occurs when conversion receives an invalid value |
| break | Stops the input loop |
| while True | Keeps asking until the input is accepted |

Input validation is important in interactive software applications.

---

# 24. Menu-Driven Applications

A menu-driven application presents different operations to the user.

A while loop keeps the application running until the user chooses to exit.

Example:

```python
while True:

    print("1. Addition")

    print("2. Multiplication")

    print("3. Exit")

    choice = input("Select an option: ")

    if choice == "1":

        print("Addition selected.")

    elif choice == "2":

        print("Multiplication selected.")

    elif choice == "3":

        print("Goodbye!")

        break

    else:

        print("Invalid selection.")
```

Applications:
- Banking systems.
- Student management software.
- Inventory management.
- Calculator applications.
- Interactive data analysis programs.

Our Day 013 challenge applies this concept in a complete mathematical and data analysis application.

---

# 25. Statistical Data Processing

Loops allow us to process individual observations in a dataset.

Suppose:

\[
X=[10,20,30,40,50]
\]

We can calculate:

- Total.
- Average.
- Maximum.
- Minimum.
- Number of even values.
- Number of odd values.

Example:

```python
dataset = [10, 20, 30, 40, 50]

index = 0

total = 0

while index < len(dataset):

    total += dataset[index]

    index += 1

average = total / len(dataset)

print("Total:", total)

print("Average:", average)
```

In real-world data science, NumPy and Pandas provide more efficient operations for numerical and tabular data.

Understanding loops first helps us understand how these operations work conceptually.

---

# 26. Machine Learning Connection: Mean Absolute Error

Mean Absolute Error (MAE) measures the average absolute difference between actual and predicted values.

Formula:

\[
MAE=\frac{1}{n}\sum_{i=1}^{n}|y_i-\hat{y}_i|
\]

Where:

- \(n\) = Number of observations.
- \(y_i\) = Actual value.
- \(\hat{y}_i\) = Predicted value.

Example:

Actual:

\[
[100,200,300,400]
\]

Predicted:

\[
[90,210,280,390]
\]

Absolute errors:

\[
[10,10,20,10]
\]

Therefore:

\[
MAE=\frac{10+10+20+10}{4}
\]

\[
\boxed{MAE=12.5}
\]

Python implementation:

```python
actual = [100, 200, 300, 400]

predicted = [90, 210, 280, 390]

index = 0

total_error = 0

while index < len(actual):

    error = abs(actual[index] - predicted[index])

    total_error += error

    index += 1

mae = total_error / len(actual)

print("MAE:", mae)
```

A lower MAE generally means smaller average absolute prediction errors when comparing models on the same dataset and target scale.

---

# 27. Time Complexity of While Loops

Time complexity describes how an algorithm's running time grows as input size increases.

It is commonly expressed using Big-O notation.

### Constant time: O(1)

An operation that performs a fixed amount of work.

```python
number = 10

print(number)
```

### Linear time: O(n)

A loop that processes n elements.

```python
counter = 0

while counter < n:

    counter += 1
```

### Quadratic time: O(n²)

Two nested loops, each executing approximately n times.

```python
row = 0

while row < n:

    column = 0

    while column < n:

        column += 1

    row += 1
```

| Complexity | Meaning |
|---|---|
| O(1) | Constant |
| O(n) | Linear |
| O(n²) | Quadratic |
| O(log n) | Logarithmic |

Understanding algorithmic complexity becomes important when working with large AI datasets.

---

# 28. Common While Loop Errors

| Error | Explanation | Solution |
|---|---|---|
| Infinite loop | Condition never becomes False | Update the counter |
| Missing colon | Invalid syntax | Add `:` |
| Incorrect indentation | Incorrect loop structure | Use consistent indentation |
| Wrong condition | Loop stops too early or too late | Check comparison operators |
| Incorrect initialization | Wrong starting value | Initialize correctly |
| IndexError | Accessing an invalid list index | Check list length |
| ZeroDivisionError | Dividing by zero | Validate denominator |
| ValueError | Invalid data conversion | Use try and except |

---

# 29. For Loop vs While Loop

| Feature | For Loop | While Loop |
|---|---|---|
| Main purpose | Iterate over an iterable | Repeat while a condition is True |
| Common usage | Processing lists and ranges | Input validation and condition-based repetition |
| Counter | Often managed automatically | Often managed manually |
| Termination | Iterable is exhausted | Condition becomes False |
| Infinite loop risk | Possible | Common if update or exit logic is missing |

Both loops are important in professional Python programming.

---

# 30. Day 013 Practical Project

## Interactive Mathematical and Data Analysis System

File: `challenge.py`

Our project combines multiple Python concepts into one interactive application.

### Project features

1. Addition calculator.
2. Multiplication calculator.
3. Factorial calculator.
4. Prime number detector.
5. Fibonacci generator.
6. Number reversal.
7. Sum of digits.
8. Palindrome detector.
9. Dataset analysis.
10. Mean Absolute Error calculator.
11. Input validation.
12. Interactive menu.
13. Continuous execution.
14. Exit functionality.

### Programming concepts used

| Concept | Application |
|---|---|
| While loops | Repeated execution |
| Functions | Organizing reusable code |
| Conditions | Making decisions |
| Lists | Storing numerical observations |
| Accumulators | Calculating totals |
| break | Exiting loops |
| continue | Skipping iterations |
| try/except | Handling invalid input |
| Mathematical operations | Performing calculations |
| Statistical formulas | Analysing datasets |

---

# 31. Day 013 Files and Folder Structure

```text
day_013/
│
├── while_loops.py
├── exercises.py
├── challenge.py
└── notes.md
```

### Purpose of each file

| File | Purpose |
|---|---|
| while_loops.py | Main lesson and demonstrations |
| exercises.py | 30 solved exercises |
| challenge.py | Practical application |
| notes.md | Complete revision notes |

---

# 32. Day 013 Learning Checklist

- [ ] Understand while loop syntax.
- [ ] Understand initialization, condition and update.
- [ ] Write counting loops.
- [ ] Identify infinite loops.
- [ ] Use break and continue.
- [ ] Understand nested while loops.
- [ ] Calculate factorials.
- [ ] Generate Fibonacci sequences.
- [ ] Detect prime numbers.
- [ ] Reverse numbers.
- [ ] Process lists using indexes.
- [ ] Calculate statistical averages.
- [ ] Understand Mean Absolute Error.
- [ ] Understand basic time complexity.
- [ ] Complete all 30 exercises.
- [ ] Complete the practical challenge.

---

# 33. Connection to Our Six-Month AI Learning Journey

While loops provide important foundations for future AI programming.

| Future AI Subject | Connection |
|---|---|
| Mathematics for AI | Repeated mathematical calculations |
| Statistics | Processing numerical observations |
| NumPy | Understanding numerical operations |
| Pandas | Understanding dataset processing |
| Machine Learning | Understanding iterative algorithms |
| Deep Learning | Understanding training iterations |
| Computer Vision | Understanding repeated image processing |

An important distinction: modern AI libraries often use optimized numerical operations rather than manually writing Python loops for every calculation.

Nevertheless, understanding iteration is essential for understanding how algorithms operate.

---

# 34. Final Reflection

Day 013 introduced me to condition-controlled repetition using Python while loops.

I learned how to initialize variables, construct loop conditions, update counters and prevent infinite loops.

I practised mathematical operations including factorial calculations, summation, Fibonacci sequences, prime number detection and digit manipulation.

I also learned how to process lists, calculate averages, validate user input and create menu-driven applications.

Most importantly, I connected Python programming with statistical analysis and Machine Learning through Mean Absolute Error.

**My next learning objectives:**

- Strengthen Python programming fundamentals.
- Develop mathematical problem-solving skills.
- Learn NumPy and Pandas.
- Study Statistics for AI.
- Progress toward Machine Learning.
- Build practical Deep Learning and Computer Vision projects.

**ONE DAY AT A TIME. ONE CONCEPT AT A TIME. ONE PROJECT AT A TIME.**

KEEP LEARNING! 🚀

---

**DAY 013 — PYTHON WHILE LOOPS: COMPLETED NOTES**