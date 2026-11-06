# DAY 015 — PYTHON LISTS
## Bachelor's in Artificial Intelligence
### 90-Day Python Programming Journey

**Subject:** Python Programming  
**Topic:** Lists and Data Processing  
**Level:** Beginner to Intermediate  
**Main File:** `lists.py`

---

# 1. Introduction to Python Lists

A list is a built-in Python data structure that stores multiple elements inside a single variable.

Lists are useful when we need to store, organize, access and process collections of data.

Example:

```python
fruits = ["Apple", "Banana", "Mango", "Orange"]

print(fruits)
```

Output:

```text
['Apple', 'Banana', 'Mango', 'Orange']
```

### Characteristics of Python Lists

1. Ordered: Elements maintain their positions.
2. Mutable: Elements can be modified.
3. Allow duplicates: The same value can appear multiple times.
4. Flexible: Different data types can exist in one list.
5. Dynamic: Elements can be added or removed.

Example:

```python
data = [10, "Python", 3.14, True, 10]

print(data)
```

---

# 2. Creating Lists

Lists are created using square brackets `[]`.

### List of integers

```python
numbers = [10, 20, 30, 40, 50]

print(numbers)
```

### List of strings

```python
names = ["Ali", "Ahmed", "John"]

print(names)
```

### List of floating-point numbers

```python
measurements = [1.5, 2.7, 3.9, 4.2]

print(measurements)
```

### Empty list

```python
empty_list = []

print(empty_list)
```

### Using the list() constructor

```python
numbers = list((10, 20, 30))

print(numbers)
```

The `list()` constructor can convert an iterable into a list.

---

# 3. List Indexing

Indexing means accessing an element using its position.

Python uses zero-based indexing.

Example:

```python
numbers = [10, 20, 30, 40, 50]
```

| Index | Element |
|---:|---:|
| 0 | 10 |
| 1 | 20 |
| 2 | 30 |
| 3 | 40 |
| 4 | 50 |

### Accessing elements

```python
print(numbers[0])
print(numbers[1])
print(numbers[2])
```

Output:

```text
10
20
30
```

### Negative indexing

Negative indexing starts from the end.

| Index | Element |
|---:|---:|
| -1 | 50 |
| -2 | 40 |
| -3 | 30 |
| -4 | 20 |
| -5 | 10 |

Example:

```python
print(numbers[-1])
print(numbers[-2])
```

Output:

```text
50
40
```

**Important:** Accessing an index outside the valid range raises an `IndexError`.

---

# 4. Finding List Length

The `len()` function returns the number of elements in a list.

Example:

```python
students = ["Ali", "Ahmed", "John", "David"]

print(len(students))
```

Output:

```text
4
```

Mathematical relationship:

If a list contains n elements, its valid positive indexes are:

\[
0,1,2,\ldots,n-1
\]

The last valid index is:

\[
n-1
\]

---

# 5. List Slicing

Slicing extracts a portion of a list.

### Syntax

```python
list_name[start:stop:step]
```

- Start: Starting index.
- Stop: Ending boundary, excluded.
- Step: Distance between selected elements.

Example:

```python
numbers = [10, 20, 30, 40, 50, 60]

print(numbers[1:4])
```

Output:

```text
[20, 30, 40]
```

### Common slicing operations

```python
numbers = [10, 20, 30, 40, 50, 60]

print(numbers[:3])

print(numbers[2:])

print(numbers[:])

print(numbers[::2])

print(numbers[::-1])
```

Output:

```text
[10, 20, 30]
[30, 40, 50, 60]
[10, 20, 30, 40, 50, 60]
[10, 30, 50]
[60, 50, 40, 30, 20, 10]
```

Slicing creates a new outer list rather than modifying the original list.

---

# 6. Modifying List Elements

Python lists are mutable.

This means we can change elements after creating a list.

Example:

```python
colors = ["Red", "Blue", "Green"]

colors[1] = "Purple"

print(colors)
```

Output:

```text
['Red', 'Purple', 'Green']
```

### Modifying multiple elements

```python
numbers = [10, 20, 30, 40, 50]

numbers[1:3] = [200, 300]

print(numbers)
```

Output:

```text
[10, 200, 300, 40, 50]
```

---

# 7. Adding Elements to Lists

Python provides three important methods for adding elements.

## 7.1 append()

Adds one element to the end of a list.

```python
fruits = ["Apple", "Banana"]

fruits.append("Mango")

print(fruits)
```

Output:

```text
['Apple', 'Banana', 'Mango']
```

## 7.2 insert()

Adds an element at a specified index.

```python
fruits = ["Apple", "Banana", "Mango"]

fruits.insert(1, "Orange")

print(fruits)
```

Output:

```text
['Apple', 'Orange', 'Banana', 'Mango']
```

## 7.3 extend()

Adds multiple elements from another iterable.

```python
first = [1, 2, 3]

second = [4, 5, 6]

first.extend(second)

print(first)
```

Output:

```text
[1, 2, 3, 4, 5, 6]
```

### Difference between append() and extend()

```python
a = [1, 2]

a.append([3, 4])

print(a)
```

Output:

```text
[1, 2, [3, 4]]
```

Using extend():

```python
a = [1, 2]

a.extend([3, 4])

print(a)
```

Output:

```text
[1, 2, 3, 4]
```

---

# 8. Removing Elements from Lists

## 8.1 remove()

Removes the first occurrence of a specified value.

```python
fruits = ["Apple", "Banana", "Mango"]

fruits.remove("Banana")

print(fruits)
```

## 8.2 pop()

Removes and returns an element.

```python
numbers = [10, 20, 30, 40]

removed = numbers.pop()

print(removed)

print(numbers)
```

Without an index, pop() removes the last element.

With an index:

```python
numbers.pop(1)
```

## 8.3 del

Deletes an element or slice by index.

```python
numbers = [10, 20, 30, 40]

del numbers[1]

print(numbers)
```

## 8.4 clear()

Removes all elements.

```python
numbers = [10, 20, 30]

numbers.clear()

print(numbers)
```

Output:

```text
[]
```

### Comparison

| Method | Purpose |
|---|---|
| remove() | Removes first matching value |
| pop() | Removes and returns an element |
| del | Deletes by index or slice |
| clear() | Removes all elements |

---

# 9. Searching and Counting

## 9.1 index()

Returns the index of the first matching element.

```python
fruits = ["Apple", "Banana", "Mango"]

print(fruits.index("Mango"))
```

Output:

```text
2
```

## 9.2 count()

Counts how many times a value occurs.

```python
numbers = [10, 20, 10, 30, 10]

print(numbers.count(10))
```

Output:

```text
3
```

## 9.3 Membership operators

The `in` operator checks whether an element exists.

```python
fruits = ["Apple", "Banana", "Mango"]

print("Apple" in fruits)

print("Orange" in fruits)
```

Output:

```text
True
False
```

The `not in` operator checks whether an element is absent.

---

# 10. Sorting Lists

Sorting arranges elements in a particular order.

## 10.1 sort()

Modifies the original list.

Ascending order:

```python
numbers = [50, 10, 40, 20, 30]

numbers.sort()

print(numbers)
```

Output:

```text
[10, 20, 30, 40, 50]
```

Descending order:

```python
numbers.sort(reverse=True)

print(numbers)
```

## 10.2 sorted()

Returns a new sorted list without modifying the original.

```python
numbers = [50, 10, 40, 20, 30]

new_list = sorted(numbers)

print(new_list)

print(numbers)
```

### Difference

| sort() | sorted() |
|---|---|
| List method | Built-in function |
| Changes original list | Creates a new list |
| Returns None | Returns sorted list |

---

# 11. Reversing Lists

The `reverse()` method reverses the current order of elements.

```python
numbers = [10, 20, 30, 40]

numbers.reverse()

print(numbers)
```

Output:

```text
[40, 30, 20, 10]
```

Remember:

- reverse() reverses the existing order.
- sort(reverse=True) sorts in descending order.
- [::-1] creates a reversed copy using slicing.

These operations are not identical.

---

# 12. Copying Lists

There is an important difference between copying and referencing.

### Reference assignment

```python
original = [10, 20, 30]

reference = original

reference.append(40)

print(original)
```

Output:

```text
[10, 20, 30, 40]
```

Both variables refer to the same list object.

### Creating a shallow copy

Using copy():

```python
original = [10, 20, 30]

copied = original.copy()

copied.append(40)

print(original)

print(copied)
```

Output:

```text
[10, 20, 30]
[10, 20, 30, 40]
```

Other shallow-copy approaches include:

```python
copied = original[:]
```

and:

```python
copied = list(original)
```

**Important:** Shallow copies do not recursively copy nested mutable objects.

---

# 13. Iterating Through Lists

Iteration means processing elements one by one.

### Using a for loop

```python
numbers = [10, 20, 30, 40]

for number in numbers:

    print(number)
```

### Using a while loop

```python
numbers = [10, 20, 30, 40]

index = 0

while index < len(numbers):

    print(numbers[index])

    index += 1
```

### Using enumerate()

enumerate() provides both the index and the value.

```python
students = ["Ali", "Ahmed", "John"]

for index, student in enumerate(students):

    print(index, student)
```

This is useful when we need to process elements together with their positions.

---

# 14. Basic Numerical Operations

Python provides several built-in functions for numerical lists.

| Function | Purpose |
|---|---|
| sum() | Calculates total |
| len() | Counts elements |
| min() | Finds minimum |
| max() | Finds maximum |
| sorted() | Returns sorted elements |
| round() | Rounds numerical results |

Example:

```python
numbers = [10, 20, 30, 40, 50]

print(sum(numbers))

print(len(numbers))

print(min(numbers))

print(max(numbers))
```

Output:

```text
150
5
10
50
```

---

# 15. Nested Lists

A nested list is a list containing other lists.

Example:

```python
matrix = [

    [1, 2, 3],

    [4, 5, 6],

    [7, 8, 9]

]
```

This structure represents a 3 × 3 matrix.

### Accessing nested elements

```python
print(matrix[0])

print(matrix[0][1])

print(matrix[2][2])
```

Output:

```text
[1, 2, 3]
2
9
```

The first index identifies the row, and the second identifies the column.

### Matrix representation

\[
A=
\begin{bmatrix}
1&2&3\\
4&5&6\\
7&8&9
\end{bmatrix}
\]

Nested lists are useful for learning how multidimensional data is organized.

---

# 16. Iterating Through Nested Lists

We use nested loops to process every element.

```python
matrix = [

    [1, 2, 3],

    [4, 5, 6],

    [7, 8, 9]

]

for row in matrix:

    for value in row:

        print(value)
```

The outer loop processes each row.

The inner loop processes each element in that row.

---

# 17. List Comprehensions

List comprehensions provide a concise way to create lists.

### Basic syntax

```python
[expression for item in iterable]
```

Example:

```python
squares = [number ** 2 for number in range(1, 6)]

print(squares)
```

Output:

```text
[1, 4, 9, 16, 25]
```

### List comprehension with conditions

```python
even_numbers = [

    number

    for number in range(1, 21)

    if number % 2 == 0

]

print(even_numbers)
```

### Equivalent traditional loop

```python
squares = []

for number in range(1, 6):

    squares.append(number ** 2)
```

List comprehensions are concise, but readability should always come first.

---

# 18. List Unpacking

Unpacking assigns individual list elements to variables.

Example:

```python
coordinates = [10, 20, 30]

x, y, z = coordinates

print(x)

print(y)

print(z)
```

### Starred unpacking

```python
numbers = [10, 20, 30, 40, 50]

first, *middle, last = numbers

print(first)

print(middle)

print(last)
```

Output:

```text
10
[20, 30, 40]
50
```

---

# 19. List Concatenation and Repetition

### Concatenation

The + operator joins lists.

```python
first = [1, 2, 3]

second = [4, 5, 6]

combined = first + second

print(combined)
```

### Repetition

The * operator repeats a list.

```python
zeros = [0] * 5

print(zeros)
```

Output:

```text
[0, 0, 0, 0, 0]
```

Be careful with nested mutable lists when using repetition because inner objects may be shared.

---

# 20. Mathematical Applications of Lists

Lists are useful for storing numerical observations.

Consider:

\[
X=[10,20,30,40,50]
\]

## 20.1 Arithmetic Mean

The mean is the sum of observations divided by their number.

\[
\bar{x}=\frac{\sum_{i=1}^{n}x_i}{n}
\]

Example:

\[
\bar{x}=\frac{10+20+30+40+50}{5}
\]

\[
\boxed{\bar{x}=30}
\]

Python:

```python
numbers = [10, 20, 30, 40, 50]

mean = sum(numbers) / len(numbers)

print(mean)
```

## 20.2 Median

The median is the middle value after sorting.

For an odd number of observations:

\[
Median=x_{\frac{n+1}{2}}
\]

For an even number of observations:

\[
Median=\frac{x_{\frac{n}{2}}+x_{\frac{n}{2}+1}}{2}
\]

Example:

\[
X=[10,20,30,40,50]
\]

\[
Median=30
\]

## 20.3 Range

The range is the difference between maximum and minimum values.

\[
Range=X_{\max}-X_{\min}
\]

Example:

\[
Range=50-10=40
\]

Python:

```python
numbers = [10, 20, 30, 40, 50]

data_range = max(numbers) - min(numbers)

print(data_range)
```

## 20.4 Population Variance

Variance measures the average squared deviation from the population mean.

\[
\sigma^2=\frac{\sum_{i=1}^{n}(x_i-\mu)^2}{n}
\]

Where:

- \(\sigma^2\) = Population variance.
- \(x_i\) = Individual observation.
- \(\mu\) = Population mean.
- \(n\) = Number of observations.

## 20.5 Population Standard Deviation

Standard deviation is the square root of variance.

\[
\sigma=\sqrt{\sigma^2}
\]

It measures how spread out observations are around the mean.

---

# 21. Lists in Statistics and Data Analysis

Consider a dataset:

```python
student_scores = [70, 80, 90, 85, 75]
```

We can calculate:

```python
total = sum(student_scores)

count = len(student_scores)

mean = total / count

highest = max(student_scores)

lowest = min(student_scores)

print("Total:", total)

print("Count:", count)

print("Mean:", mean)

print("Highest:", highest)

print("Lowest:", lowest)
```

These are basic descriptive statistical operations.

Later, we will use dedicated scientific libraries to perform much larger and more complex analyses.

---

# 22. Lists in Artificial Intelligence

Lists provide an introduction to representing data in programming.

AI applications frequently process collections of observations.

Examples:

| AI Application | Example of data |
|---|---|
| Machine Learning | Features and labels |
| Computer Vision | Pixel values |
| Natural Language Processing | Token IDs |
| Statistics | Numerical observations |
| Neural Networks | Weights and outputs |
| Reinforcement Learning | Actions and rewards |

### Example: Machine Learning predictions

```python
predictions = [0.85, 0.72, 0.91, 0.66]

print(predictions)
```

These values could represent predicted probabilities from a classification model.

### Example: Actual labels

```python
actual_labels = [1, 0, 1, 1]

print(actual_labels)
```

These represent binary class labels.

The lists are introductory representations, not a complete machine learning implementation.

---

# 23. Mean Absolute Error

Mean Absolute Error (MAE) measures the average absolute difference between actual and predicted values.

Formula:

\[
MAE=\frac{1}{n}\sum_{i=1}^{n}|y_i-\hat{y}_i|
\]

Where:

- \(y_i\) = Actual value.
- \(\hat{y}_i\) = Predicted value.
- \(n\) = Number of observations.

Example:

```python
actual = [100, 200, 300]

predicted = [90, 210, 280]

errors = []

for i in range(len(actual)):

    errors.append(abs(actual[i] - predicted[i]))

mae = sum(errors) / len(errors)

print("MAE:", mae)
```

Output:

```text
MAE: 13.333333333333334
```

MAE is an important regression evaluation metric.

---

# 24. Time Complexity of List Operations

Time complexity describes how the computational work grows as the input size increases.

Let n represent the number of elements in a list.

| Operation | Typical time complexity |
|---|---|
| Indexing | O(1) |
| Updating by index | O(1) |
| Append | O(1) amortized |
| Pop from end | O(1) |
| Insert at beginning | O(n) |
| Remove by value | O(n) |
| Searching with in | O(n) |
| Count | O(n) |
| Reverse | O(n) |
| Copy | O(n) |
| Sorting | O(n log n) |

### Understanding O(1)

Constant time means the operation does not grow with list size.

Example:

```python
numbers = [10, 20, 30, 40]

print(numbers[0])
```

### Understanding O(n)

Linear time means the amount of work grows proportionally with the number of elements.

Example:

```python
numbers = [10, 20, 30, 40]

for number in numbers:

    print(number)
```

### Understanding O(n log n)

Efficient comparison-based sorting algorithms generally have O(n log n) time complexity.

Python's sorting implementation uses Timsort.

---

# 25. Important Python List Methods Summary

| Method | Description |
|---|---|
| append() | Adds one element |
| insert() | Adds at a specific index |
| extend() | Adds elements from an iterable |
| remove() | Removes first matching value |
| pop() | Removes and returns an element |
| clear() | Removes all elements |
| index() | Finds first matching index |
| count() | Counts occurrences |
| sort() | Sorts original list |
| reverse() | Reverses original list |
| copy() | Creates a shallow copy |

Remember that most of these methods modify the original list and return `None`. Exceptions include methods such as pop() and index(), which return useful results.

---

# 26. Common List Errors

| Error | Cause | Solution |
|---|---|---|
| IndexError | Invalid index | Check list length |
| ValueError | Missing value in remove/index | Check membership first |
| TypeError | Incompatible operations | Check data types |
| NameError | Undefined variable | Define the variable |
| Incorrect output | Wrong index or slice | Verify positions |
| Unexpected modification | Shared reference | Use copy() |
| ZeroDivisionError | Empty dataset average | Check length before division |

Example of safe average calculation:

```python
numbers = []

if len(numbers) > 0:

    average = sum(numbers) / len(numbers)

    print(average)

else:

    print("Dataset is empty.")
```

---

# 27. Lists Versus Tuples

Lists and tuples are both sequence data structures.

| Feature | List | Tuple |
|---|---|---|
| Syntax | [] | () |
| Ordered | Yes | Yes |
| Mutable | Yes | No |
| Duplicates | Yes | Yes |
| Indexing | Yes | Yes |
| Slicing | Yes | Yes |

Example:

```python
my_list = [10, 20, 30]

my_tuple = (10, 20, 30)
```

Lists are suitable when data needs to change.

Tuples are suitable when a sequence should remain immutable.

---

# 28. Lists Versus NumPy Arrays

This distinction is particularly important for our AI journey.

Python lists are general-purpose collections.

NumPy arrays are designed for efficient numerical computation.

| Feature | Python List | NumPy Array |
|---|---|---|
| General-purpose storage | Yes | Numerical focus |
| Different data types | Yes | Usually homogeneous |
| Element-wise mathematics | Requires suitable operations or loops | Built-in vectorization |
| Multidimensional data | Nested lists | Native multidimensional arrays |
| Numerical performance | Less optimized for numerical operations | Highly optimized |
| Machine Learning workflows | Useful | Very important |

Example using Python lists:

```python
a = [1, 2, 3]

b = [4, 5, 6]

result = [a[i] + b[i] for i in range(len(a))]

print(result)
```

Output:

```text
[5, 7, 9]
```

Later with NumPy:

```python
import numpy as np

a = np.array([1, 2, 3])

b = np.array([4, 5, 6])

result = a + b

print(result)
```

Output:

```text
[5 7 9]
```

NumPy makes numerical operations more convenient and efficient.

---

# 29. Day 015 Project Architecture

Our project folder:

```text
day_015/
│
├── lists.py
│
├── exercises.py
│
├── challenge.py
│
└── notes.md
```

### File descriptions

| File | Purpose |
|---|---|
| lists.py | Main Python lists lesson |
| exercises.py | 30 solved exercises |
| challenge.py | Student Performance and Dataset Analysis System |
| notes.md | Complete theoretical notes |

---

# 30. Day 015 Learning Checklist

- [ ] Understand Python lists.
- [ ] Create different types of lists.
- [ ] Understand positive indexing.
- [ ] Understand negative indexing.
- [ ] Use len().
- [ ] Apply list slicing.
- [ ] Modify list elements.
- [ ] Use append().
- [ ] Use insert().
- [ ] Use extend().
- [ ] Use remove().
- [ ] Use pop().
- [ ] Understand del.
- [ ] Use clear().
- [ ] Use count().
- [ ] Use index().
- [ ] Sort lists.
- [ ] Reverse lists.
- [ ] Copy lists correctly.
- [ ] Iterate using for loops.
- [ ] Iterate using while loops.
- [ ] Understand nested lists.
- [ ] Use list comprehensions.
- [ ] Perform list unpacking.
- [ ] Calculate mean and median.
- [ ] Understand variance and standard deviation.
- [ ] Understand MAE.
- [ ] Understand list time complexity.
- [ ] Understand lists in AI.
- [ ] Understand the difference between lists and NumPy arrays.

---

# 31. Connection to Our Six-Month AI Learning Journey

Day 015 builds important foundations for upcoming subjects.

| Future subject | Connection |
|---|---|
| Mathematics for AI | Numerical data and mathematical operations |
| Statistics | Mean, median and variance |
| Python Programming | Data structures and algorithms |
| NumPy | Multidimensional numerical arrays |
| Pandas | Dataset manipulation |
| Machine Learning | Features, labels and predictions |
| Deep Learning | Numerical tensors and model parameters |
| Computer Vision | Image pixel data and matrices |

---

# 32. Final Reflection

Today I learned how Python lists store and organize collections of data.

I practised indexing, slicing, modification, insertion, deletion, sorting, searching and iteration.

I learned how to create nested lists and matrices, use list comprehensions, and process numerical datasets.

I also studied descriptive statistics, including mean, median, variance and standard deviation.

Most importantly, I understood how Python lists introduce the data representation concepts that we will later use in NumPy, Pandas and Machine Learning.

## DAY 015 — COMPLETED

**Main Topic:** Python Lists

**Main Lesson:** lists.py

**Exercises:** 30 solved exercises

**Challenge:** Student Performance and Dataset Analysis System

**Notes:** Complete theoretical revision

### OUR NEXT OBJECTIVE

- Strengthen Python programming.
- Improve mathematical reasoning.
- Develop problem-solving ability.
- Learn NumPy and Pandas.
- Progress toward Machine Learning and Deep Learning.

ONE DAY AT A TIME. ONE CONCEPT AT A TIME.

WE ARE BUILDING REAL AI FOUNDATIONS! 🚀