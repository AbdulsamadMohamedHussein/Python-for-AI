# DAY 016 — PYTHON TUPLES
## Bachelor's in Artificial Intelligence
### 90-Day Python Programming Journey

**Subject:** Python Programming  
**Topic:** Python Tuples  
**Level:** Beginner to Intermediate  
**Main File:** `tuples.py`

---

# 1. Introduction to Python Tuples

A tuple is a built-in Python data structure used to store multiple elements in a single variable.

Tuples are ordered and immutable.

Immutable means that we cannot directly change, add or remove individual elements after creating a tuple.

Example:

```python
student = ("Ali", 20, 3.8, "Artificial Intelligence")

print(student)
```

Output:

```text
('Ali', 20, 3.8, 'Artificial Intelligence')
```

## Characteristics of Tuples

1. Ordered: Elements maintain their positions.
2. Immutable: Elements cannot be reassigned.
3. Duplicates allowed: Repeated values are permitted.
4. Different data types: Tuples can contain integers, strings, floats and booleans.
5. Indexed: Elements can be accessed using indexes.
6. Iterable: Tuples can be processed using loops.
7. Hashable when all their elements are hashable: Such tuples can be used as dictionary keys.

---

# 2. Creating Tuples

Tuples are commonly created using parentheses `()`.

### Integer tuple

```python
numbers = (10, 20, 30, 40, 50)

print(numbers)
```

### String tuple

```python
names = ("Ali", "Ahmed", "John")

print(names)
```

### Floating-point tuple

```python
measurements = (1.5, 2.5, 3.5, 4.5)

print(measurements)
```

### Mixed tuple

```python
data = ("Python", 25, 3.14, True)

print(data)
```

### Empty tuple

```python
empty = ()

print(empty)
```

### Using the tuple() constructor

```python
numbers = tuple([10, 20, 30])

print(numbers)
```

The `tuple()` constructor converts an iterable into a tuple.

---

# 3. Single-Element Tuples

A single-element tuple requires a comma.

Correct:

```python
number = (10,)

print(type(number))
```

Output:

```text
<class 'tuple'>
```

Incorrect:

```python
number = (10)

print(type(number))
```

Output:

```text
<class 'int'>
```

The parentheses alone do not create a tuple. The comma is what makes it a tuple.

---

# 4. Tuple Indexing

Indexing allows us to access individual elements using their positions.

Python uses zero-based indexing.

Example:

```python
numbers = (10, 20, 30, 40, 50)
```

| Index | Element |
|---:|---:|
| 0 | 10 |
| 1 | 20 |
| 2 | 30 |
| 3 | 40 |
| 4 | 50 |

Example:

```python
print(numbers[0])
print(numbers[2])
print(numbers[4])
```

Output:

```text
10
30
50
```

The first element has index 0.

The last element has index:

\[
n-1
\]

Where n is the number of elements.

---

# 5. Negative Indexing

Negative indexing starts from the end of the tuple.

Example:

```python
numbers = (10, 20, 30, 40, 50)
```

| Negative index | Element |
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
print(numbers[-3])
```

Output:

```text
50
40
30
```

Negative indexing is useful when we want to access elements from the end.

---

# 6. Tuple Slicing

Slicing extracts a portion of a tuple.

### Syntax

```python
tuple_name[start:stop:step]
```

- Start: Starting index.
- Stop: Ending boundary, excluded.
- Step: Distance between selected elements.

Example:

```python
numbers = (10, 20, 30, 40, 50, 60)

print(numbers[1:4])
```

Output:

```text
(20, 30, 40)
```

### Different slicing operations

```python
numbers = (10, 20, 30, 40, 50, 60)

print(numbers[:3])

print(numbers[2:])

print(numbers[:])

print(numbers[::2])

print(numbers[::-1])
```

Output:

```text
(10, 20, 30)
(30, 40, 50, 60)
(10, 20, 30, 40, 50, 60)
(10, 30, 50)
(60, 50, 40, 30, 20, 10)
```

Slicing creates a new tuple.

---

# 7. Tuple Immutability

One of the most important characteristics of tuples is immutability.

After creating a tuple, we cannot directly modify its elements.

Example:

```python
numbers = (10, 20, 30)

numbers[0] = 100
```

This produces:

```text
TypeError
```

Why?

Because tuple elements cannot be reassigned.

## How to change tuple data

We can convert the tuple into a list, modify the list and convert it back.

```python
numbers = (10, 20, 30)

temporary = list(numbers)

temporary[0] = 100

numbers = tuple(temporary)

print(numbers)
```

Output:

```text
(100, 20, 30)
```

Important: We created a new tuple. We did not modify the original tuple.

## Important exception: Mutable objects inside tuples

A tuple can contain a mutable object such as a list.

```python
data = (10, 20, [30, 40])

data[2].append(50)

print(data)
```

Output:

```text
(10, 20, [30, 40, 50])
```

The tuple's structure remains unchanged, but its contained list can be modified.

This distinction is important in advanced Python programming.

---

# 8. Tuple Length

The `len()` function returns the total number of elements.

```python
students = ("Ali", "Ahmed", "John", "David")

print(len(students))
```

Output:

```text
4
```

---

# 9. Tuple Methods

Tuples have two primary built-in methods.

## 9.1 count()

Counts how many times a value appears.

```python
numbers = (10, 20, 10, 30, 10, 40)

print(numbers.count(10))
```

Output:

```text
3
```

## 9.2 index()

Returns the index of the first occurrence of a value.

```python
fruits = ("Apple", "Banana", "Mango", "Orange")

print(fruits.index("Mango"))
```

Output:

```text
2
```

If the value does not exist, `index()` raises a ValueError.

---

# 10. Membership Operators

The `in` operator checks whether an element exists.

```python
languages = ("Python", "Java", "C++")

print("Python" in languages)

print("PHP" in languages)
```

Output:

```text
True
False
```

The `not in` operator checks whether an element is absent.

```python
print("PHP" not in languages)
```

Output:

```text
True
```

---

# 11. Tuple Concatenation

Concatenation joins two tuples using the `+` operator.

Example:

```python
first = (10, 20, 30)

second = (40, 50, 60)

combined = first + second

print(combined)
```

Output:

```text
(10, 20, 30, 40, 50, 60)
```

Concatenation creates a new tuple.

It does not modify the original tuples.

---

# 12. Tuple Repetition

The multiplication operator repeats tuple elements.

Example:

```python
numbers = (1, 2, 3)

result = numbers * 3

print(result)
```

Output:

```text
(1, 2, 3, 1, 2, 3, 1, 2, 3)
```

---

# 13. Tuple Packing

Tuple packing means placing multiple values into a single tuple.

Example:

```python
student = "Ali", 20, 90, "Python"

print(student)

print(type(student))
```

Python automatically packs these values into a tuple.

---

# 14. Tuple Unpacking

Tuple unpacking assigns individual tuple elements to separate variables.

Example:

```python
student = ("Ali", 20, 90)

name, age, marks = student

print(name)

print(age)

print(marks)
```

Output:

```text
Ali
20
90
```

The number of variables must match the number of elements unless starred unpacking is used.

## Starred unpacking

```python
numbers = (10, 20, 30, 40, 50)

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

The starred variable receives a list.

---

# 15. Swapping Variables Using Tuples

Python supports simultaneous assignment.

Example:

```python
a = 100

b = 200

a, b = b, a

print(a)

print(b)
```

Output:

```text
200
100
```

This operation uses tuple packing and unpacking.

It is a useful feature of Python.

---

# 16. Nested Tuples

A nested tuple contains other tuples.

Example:

```python
students = (

    ("Ali", 20, 90),

    ("Ahmed", 22, 85),

    ("John", 21, 95)

)

print(students)
```

### Accessing nested elements

```python
print(students[0])

print(students[0][0])

print(students[1][1])

print(students[2][2])
```

Nested tuples can represent structured records and multidimensional data.

---

# 17. Iterating Through Tuples

Iteration means processing elements one by one.

### Using a for loop

```python
fruits = ("Apple", "Banana", "Mango")

for fruit in fruits:

    print(fruit)
```

### Using a while loop

```python
numbers = (10, 20, 30, 40)

index = 0

while index < len(numbers):

    print(numbers[index])

    index += 1
```

### Using enumerate()

```python
subjects = ("Mathematics", "Statistics", "Python")

for index, subject in enumerate(subjects, start=1):

    print(index, subject)
```

`enumerate()` returns an iterator containing index-value pairs.

---

# 18. Sorting Tuples

Tuples cannot be sorted in place because they are immutable.

However, Python's `sorted()` function can sort their elements.

Example:

```python
numbers = (50, 10, 40, 20, 30)

result = sorted(numbers)

print(result)
```

Output:

```text
[10, 20, 30, 40, 50]
```

Notice that `sorted()` returns a list.

To obtain a tuple:

```python
sorted_tuple = tuple(sorted(numbers))

print(sorted_tuple)
```

Output:

```text
(10, 20, 30, 40, 50)
```

---

# 19. Minimum, Maximum and Sum

Python provides built-in functions for numerical tuples.

| Function | Purpose |
|---|---|
| min() | Finds smallest value |
| max() | Finds largest value |
| sum() | Calculates total |
| len() | Counts elements |
| sorted() | Returns sorted list |

Example:

```python
numbers = (10, 20, 30, 40, 50)

print(min(numbers))

print(max(numbers))

print(sum(numbers))

print(len(numbers))
```

---

# 20. Mathematical Applications of Tuples

Tuples can store numerical observations for mathematical calculations.

Consider:

\[
X=(10,20,30,40,50)
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
numbers = (10, 20, 30, 40, 50)

mean = sum(numbers) / len(numbers)

print(mean)
```

## 20.2 Median

The median is the middle observation after sorting.

For an odd number of observations:

\[
Median=x_{\frac{n+1}{2}}
\]

For an even number of observations:

\[
Median=\frac{x_{\frac n2}+x_{\frac n2+1}}{2}
\]

Example:

\[
X=(10,20,30,40,50)
\]

\[
Median=30
\]

## 20.3 Range

The range is the difference between the maximum and minimum values.

\[
Range=X_{\max}-X_{\min}
\]

Example:

\[
Range=50-10=40
\]

## 20.4 Population Variance

Variance measures how far observations spread from their population mean.

\[
\sigma^2=\frac{\sum_{i=1}^{n}(x_i-\mu)^2}{n}
\]

Where:

- \(\sigma^2\) = Population variance.
- \(x_i\) = Individual observation.
- \(\mu\) = Population mean.
- \(n\) = Number of observations.

## 20.5 Population Standard Deviation

Standard deviation is the square root of population variance.

\[
\sigma=\sqrt{\sigma^2}
\]

It measures the spread of data around the mean.

---

# 21. Mathematical Coordinates Using Tuples

Tuples are useful for representing fixed coordinates.

Example:

```python
point = (5, 10)

x, y = point

print("X:", x)

print("Y:", y)
```

## Euclidean Distance

The Euclidean distance from the origin is:

\[
d=\sqrt{x^2+y^2}
\]

For a point (5, 10):

\[
d=\sqrt{5^2+10^2}
\]

\[
d=\sqrt{125}
\]

\[
d\approx11.18
\]

Python:

```python
point = (5, 10)

x, y = point

distance = (x**2 + y**2)**0.5

print(round(distance, 2))
```

This is useful for understanding coordinate systems in computer vision and machine learning.

---

# 22. Tuple Comparison

Python compares tuples lexicographically.

This means it compares corresponding elements from left to right.

Example:

```python
first = (10, 20, 30)

second = (10, 20, 40)

print(first == second)

print(first < second)
```

Output:

```text
False
True
```

The first two elements are equal.

The third elements determine the comparison.

---

# 23. Converting Lists and Tuples

## List to tuple

```python
numbers_list = [10, 20, 30]

numbers_tuple = tuple(numbers_list)

print(numbers_tuple)
```

## Tuple to list

```python
numbers_tuple = (10, 20, 30)

numbers_list = list(numbers_tuple)

print(numbers_list)
```

Conversion is useful when we need to move between mutable and immutable sequences.

---

# 24. Tuples as Dictionary Keys

Tuples can be used as dictionary keys if all their elements are hashable.

Example:

```python
locations = {

    (10, 20): "Point A",

    (30, 40): "Point B",

    (50, 60): "Point C"

}

print(locations[(10, 20)])
```

Output:

```text
Point A
```

This is useful when representing coordinate-based information.

A tuple containing a list cannot be used as a dictionary key because lists are unhashable.

---

# 25. Time Complexity of Tuple Operations

Time complexity describes how computational work grows as the input size increases.

Let n represent the number of elements.

| Operation | Typical time complexity |
|---|---|
| Indexing | O(1) |
| Length | O(1) |
| Count | O(n) |
| Index search | O(n) |
| Membership search | O(n) |
| Iteration | O(n) |
| Concatenation | O(n + m) |
| Slicing | O(k) |
| Sorting with sorted() | O(n log n) |

Where:

- n = Number of elements.
- m = Size of the second tuple.
- k = Number of selected elements.

### Understanding O(1)

Constant time means the operation does not grow with the number of elements.

Example:

```python
numbers = (10, 20, 30, 40)

print(numbers[0])
```

### Understanding O(n)

Linear time means the operation may examine every element.

Example:

```python
numbers = (10, 20, 30, 40)

for number in numbers:

    print(number)
```

---

# 26. Tuples Versus Lists

Both are ordered sequence data structures.

However, they have important differences.

| Feature | List | Tuple |
|---|---|---|
| Syntax | [] | () |
| Ordered | Yes | Yes |
| Mutable | Yes | No |
| Duplicates | Yes | Yes |
| Indexing | Yes | Yes |
| Slicing | Yes | Yes |
| append() | Yes | No |
| remove() | Yes | No |
| count() | Yes | Yes |
| index() | Yes | Yes |
| Hashable | No | Sometimes |

### When should we use lists?

Use lists when:

- Elements need to be added or deleted.
- Data changes frequently.
- We need a mutable collection.

### When should we use tuples?

Use tuples when:

- Data should remain structurally unchanged.
- We represent fixed records.
- We represent coordinates.
- We need an immutable sequence.
- We need a hashable composite key.

---

# 27. Tuples in Artificial Intelligence

Tuples provide useful ways to organize structured information in programming.

They can represent:

| AI Area | Tuple Application |
|---|---|
| Machine Learning | Fixed feature records |
| Computer Vision | Image coordinates |
| Statistics | Numerical observations |
| Neural Networks | Fixed dimensions |
| Natural Language Processing | Structured token records |
| Data Science | Immutable data records |

### Example 1: Machine Learning Dataset

```python
dataset = (

    (1.5, 2.3, 1),

    (2.1, 3.4, 0),

    (3.2, 4.5, 1)

)

for observation in dataset:

    print(observation)
```

Each record contains two features and one class label.

### Example 2: Computer Vision Coordinates

```python
bounding_box = (100, 150, 300, 400)

x_min, y_min, x_max, y_max = bounding_box

print("Left:", x_min)

print("Top:", y_min)

print("Right:", x_max)

print("Bottom:", y_max)
```

This represents the coordinates of a rectangular bounding box.

### Example 3: Model Configuration

```python
model_configuration = (

    0.001,

    100,

    32

)

learning_rate, epochs, batch_size = model_configuration

print("Learning rate:", learning_rate)

print("Epochs:", epochs)

print("Batch size:", batch_size)
```

These are examples of fixed configuration records, not complete machine learning models.

---

# 28. Common Tuple Errors

| Error | Cause | Solution |
|---|---|---|
| IndexError | Invalid index | Check tuple length |
| ValueError | Missing element in index() | Check membership |
| TypeError | Attempting direct modification | Create a new tuple |
| TypeError | Unhashable nested object used as key | Use hashable elements |
| ValueError | Incorrect unpacking count | Match variables and elements |

Example of safe indexing:

```python
numbers = (10, 20, 30)

if len(numbers) > 3:

    print(numbers[3])

else:

    print("Index does not exist.")
```

---

# 29. Day 016 Project Architecture

Our project folder:

```text
day_016/
│
├── tuples.py
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
| tuples.py | Complete Python tuple lesson |
| exercises.py | 30 solved tuple exercises |
| challenge.py | Student Records and Academic Performance System |
| notes.md | Complete theoretical revision |

---

# 30. Day 016 Learning Checklist

- [ ] Understand Python tuples.
- [ ] Create different types of tuples.
- [ ] Create empty tuples.
- [ ] Create single-element tuples.
- [ ] Understand positive indexing.
- [ ] Understand negative indexing.
- [ ] Apply tuple slicing.
- [ ] Understand immutability.
- [ ] Understand mutable objects inside tuples.
- [ ] Use len().
- [ ] Use count().
- [ ] Use index().
- [ ] Apply membership operators.
- [ ] Understand concatenation.
- [ ] Understand repetition.
- [ ] Practise tuple packing.
- [ ] Practise tuple unpacking.
- [ ] Use starred unpacking.
- [ ] Swap variables.
- [ ] Create nested tuples.
- [ ] Iterate through tuples.
- [ ] Use enumerate().
- [ ] Sort tuples.
- [ ] Calculate mean and median.
- [ ] Calculate variance and standard deviation.
- [ ] Understand tuple time complexity.
- [ ] Compare lists and tuples.
- [ ] Understand tuples in AI applications.

---

# 31. Connection to Our Six-Month AI Learning Journey

Day 016 prepares us for several upcoming subjects.

| Future Subject | Connection |
|---|---|
| Mathematics for AI | Coordinates and numerical sequences |
| Statistics | Numerical observations |
| Data Structures | Immutable collections |
| NumPy | Multidimensional numerical arrays |
| Pandas | Structured data processing |
| Machine Learning | Feature records and labels |
| Deep Learning | Model configuration and dimensions |
| Computer Vision | Coordinates and bounding boxes |

---

# 32. Final Reflection

Today I learned how Python tuples store ordered and immutable collections of elements.

I practised tuple creation, indexing, negative indexing, slicing, packing, unpacking, concatenation and iteration.

I understood the difference between mutable lists and immutable tuples.

I also learned how tuples can represent coordinates, structured records, statistical observations and introductory machine learning datasets.

Most importantly, I developed a better understanding of Python data structures and their role in artificial intelligence programming.

## DAY 016 — COMPLETED

**Main Topic:** Python Tuples

**Main Lesson:** tuples.py

**Exercises:** 30 solved exercises

**Challenge:** Student Records and Academic Performance System

**Notes:** Complete theoretical revision

### OUR NEXT OBJECTIVE

- Strengthen Python programming.
- Improve mathematical reasoning.
- Learn advanced data structures.
- Begin NumPy and Pandas.
- Progress toward Machine Learning and Deep Learning.

ONE CONCEPT AT A TIME. ONE DAY AT A TIME.

WE ARE BUILDING REAL AI FOUNDATIONS! 🚀