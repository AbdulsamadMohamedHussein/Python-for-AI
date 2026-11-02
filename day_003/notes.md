# DAY 003 — PYTHON DATA TYPES
## Bachelor's in Artificial Intelligence

**Learning Journey:** Python for AI  
**Day:** 003  
**Topic:** Understanding Python Data Types  
**Status:** Completed

---

# 1. Introduction to Python Data Types

A data type defines the kind of value stored in a Python object.

Python uses data types to understand how information should be stored, processed and manipulated.

For example:

```python
student_name = "Abdulsamad"
student_age = 23
student_height = 1.75
is_student = True
```

Python recognizes these values as different data types.

### Why are data types important?

Data types are important because:

1. They determine the kind of information a variable represents.
2. They help Python perform appropriate operations.
3. They help organize and manage information.
4. They are essential when processing datasets.
5. They are fundamental to Artificial Intelligence and Machine Learning.

---

# 2. Main Python Data Types

Python provides several built-in data types.

| Data Type | Description | Example |
|---|---|---|
| int | Whole numbers | `25` |
| float | Decimal numbers | `25.5` |
| str | Text | `"Python"` |
| bool | True or False | `True` |
| NoneType | Absence of a value | `None` |
| complex | Complex numbers | `3 + 4j` |
| list | Ordered, mutable collection | `[1, 2, 3]` |
| tuple | Ordered, immutable collection | `(1, 2, 3)` |
| set | Collection of unique elements | `{1, 2, 3}` |
| dict | Key-value collection | `{"age": 23}` |
| range | Sequence of integers | `range(5)` |
| bytes | Immutable binary data | `b"Python"` |

---

# 3. Integer (int)

An integer represents a whole number without a decimal point.

Examples:

```python
age = 23
marks = 85
students = 100
temperature = -5

print(age)
print(type(age))
```

Output:

```text
23
<class 'int'>
```

Integers can be positive, negative or zero.

### Applications in AI

- Image dimensions.
- Number of training epochs.
- Number of observations.
- Number of classes in a classification task.

---

# 4. Float (float)

A float represents a numerical value containing a decimal point.

Examples:

```python
height = 1.75
learning_rate = 0.001
accuracy = 96.5
temperature = 36.8

print(height)
print(type(height))
```

Output:

```text
1.75
<class 'float'>
```

### Applications in AI

Float values are particularly important in Machine Learning and Deep Learning.

Examples include:

- Learning rates.
- Model weights.
- Prediction probabilities.
- Loss values.
- Accuracy measurements.

Example:

```python
learning_rate = 0.001
prediction_probability = 0.985

print(learning_rate)
print(prediction_probability)
```

---

# 5. String (str)

A string represents text or a sequence of characters.

Strings can be created using single quotes or double quotes.

Examples:

```python
student_name = "Abdulsamad"
country = 'Kenya'
course = "Artificial Intelligence"

print(student_name)
print(type(student_name))
```

### Important string operations

```python
name = "Abdulsamad Mohamed"

print(name.upper())
print(name.lower())
print(len(name))
print(name.title())
```

| Method | Function |
|---|---|
| `upper()` | Converts text to uppercase |
| `lower()` | Converts text to lowercase |
| `title()` | Capitalizes each word |
| `len()` | Counts characters |

### String concatenation

Combining strings is called concatenation.

```python
first_name = "Abdulsamad"
last_name = "Mohamed"

full_name = first_name + " " + last_name

print(full_name)
```

### F-strings

F-strings allow variables to be inserted directly into strings.

```python
name = "Abdulsamad"
age = 23

print(f"My name is {name} and I am {age} years old.")
```

### Applications in AI

- Dataset labels.
- Text classification.
- Natural Language Processing (NLP).
- Chatbots.
- Sentiment analysis.
- Image classification labels.

---

# 6. Boolean (bool)

A Boolean represents one of two logical values:

- `True`
- `False`

Examples:

```python
is_student = True
is_graduated = False

print(is_student)
print(is_graduated)

print(type(is_student))
```

### Boolean operators

| Operator | Meaning |
|---|---|
| `and` | Both conditions must be True |
| `or` | At least one condition must be True |
| `not` | Reverses a Boolean value |

Example:

```python
age = 23
is_registered = True

eligible = age >= 18 and is_registered

print(eligible)
```

### Applications in AI

- Checking whether a model is trained.
- Validating predictions.
- Checking whether a condition is satisfied.
- Controlling program execution.

---

# 7. NoneType

`None` represents the absence of a value.

It is different from zero, False and an empty string.

Example:

```python
model_result = None

print(model_result)
print(type(model_result))
```

Output:

```text
None
<class 'NoneType'>
```

### Applications in AI

- Representing unavailable predictions.
- Initializing variables before calculations.
- Handling missing information.
- Representing an uninitialized model result.

---

# 8. Complex Numbers

Complex numbers contain a real component and an imaginary component.

Python uses `j` to represent the imaginary component.

Example:

```python
number = 3 + 4j

print(number)
print(number.real)
print(number.imag)
print(type(number))
```

Output:

```text
(3+4j)
3.0
4.0
<class 'complex'>
```

### Applications

Complex numbers are useful in advanced mathematics and specialized scientific computing, including signal processing and Fourier analysis.

---

# 9. List (list)

A list stores multiple elements in a single variable.

Lists are:

- Ordered.
- Mutable.
- Able to contain duplicate values.
- Able to contain different data types.

Example:

```python
student_marks = [85, 90, 95, 88]

print(student_marks)
print(student_marks[0])
print(student_marks[-1])
```

### List indexing

Python indexing starts from zero.

| Index | Value |
|---|---|
| 0 | 85 |
| 1 | 90 |
| 2 | 95 |
| 3 | 88 |

### Modifying a list

```python
marks = [80, 85, 90]

marks[0] = 100

print(marks)
```

### Important list methods

```python
marks = [80, 85, 90]

marks.append(95)
marks.insert(1, 88)
marks.remove(90)
marks.pop()

print(marks)
```

| Method | Purpose |
|---|---|
| `append()` | Adds an element at the end |
| `insert()` | Adds an element at a specific position |
| `remove()` | Removes a specified value |
| `pop()` | Removes and returns an element |
| `sort()` | Sorts a list |
| `reverse()` | Reverses a list |

### Applications in AI

- Storing dataset records.
- Storing class labels.
- Collecting predictions.
- Managing training information.
- Storing experimental results.

---

# 10. Tuple (tuple)

A tuple stores multiple elements in an ordered collection.

Unlike lists, tuples are immutable.

This means their elements cannot be reassigned after creation.

Example:

```python
coordinates = (10, 20)

print(coordinates)
print(coordinates[0])
print(type(coordinates))
```

Attempting to change an element directly produces an error.

```python
coordinates = (10, 20)

# coordinates[0] = 50  # TypeError
```

### Applications in AI

Tuples are useful for representing fixed information such as:

- Image dimensions.
- RGB colour values.
- Fixed coordinates.
- Input shapes.

Example:

```python
image_shape = (224, 224, 3)

print(image_shape)
```

This represents an image with a height of 224 pixels, width of 224 pixels and three colour channels.

---

# 11. Set (set)

A set stores unique elements.

Sets automatically remove duplicate values.

They are mutable and do not guarantee a fixed display order.

Example:

```python
student_ids = {101, 102, 103, 101, 102}

print(student_ids)
```

The duplicate values are removed.

### Set operations

```python
numbers = {1, 2, 3, 4}

numbers.add(5)
numbers.remove(2)

print(numbers)
```

### Important set operations

```python
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

print(A.union(B))
print(A.intersection(B))
print(A.difference(B))
```

| Operation | Meaning |
|---|---|
| `union()` | Combines elements |
| `intersection()` | Finds common elements |
| `difference()` | Finds elements in the first set but not the second |

### Applications in AI

- Identifying unique dataset labels.
- Removing duplicate categories.
- Comparing sets of features.
- Managing unique identifiers.

---

# 12. Dictionary (dict)

A dictionary stores information in key-value pairs.

Each key identifies its corresponding value.

Example:

```python
student = {
    "name": "Abdulsamad",
    "age": 23,
    "country": "Kenya",
    "course": "Artificial Intelligence"
}

print(student)
print(student["name"])
print(student["age"])
```

### Adding and updating dictionary values

```python
student = {
    "name": "Abdulsamad",
    "age": 23
}

student["university"] = "Guilin University"
student["age"] = 24

print(student)
```

### Important dictionary methods

| Method | Purpose |
|---|---|
| `keys()` | Returns dictionary keys |
| `values()` | Returns dictionary values |
| `items()` | Returns key-value pairs |
| `get()` | Retrieves a value safely |
| `update()` | Updates dictionary information |
| `pop()` | Removes a key-value pair |

### Applications in AI

Dictionaries are useful for storing:

- Model configurations.
- Dataset metadata.
- Training parameters.
- Prediction results.
- Information about machine learning experiments.

Example:

```python
ai_model = {
    "model_name": "Image Classifier",
    "learning_rate": 0.001,
    "epochs": 50,
    "accuracy": 96.5
}

print(ai_model["model_name"])
print(ai_model["learning_rate"])
```

---

# 13. Range (range)

The range data type represents a sequence of integers.

It is commonly used in loops.

Example:

```python
numbers = range(1, 6)

print(list(numbers))
```

Output:

```text
[1, 2, 3, 4, 5]
```

Important:

The ending number is excluded.

### Applications

- Repeating operations.
- Iterating through dataset records.
- Running training epochs.
- Performing repeated calculations.

---

# 14. Bytes (bytes)

Bytes represent an immutable sequence of bytes.

They are useful for binary information.

Example:

```python
binary_data = b"Python"

print(binary_data)
print(type(binary_data))
```

### Applications

- Reading binary files.
- Processing image files.
- Handling audio files.
- Working with network data.

---

# 15. Checking Data Types Using type()

The `type()` function identifies the data type of an object.

Example:

```python
age = 23
height = 1.75
name = "Abdulsamad"
is_student = True

print(type(age))
print(type(height))
print(type(name))
print(type(is_student))
```

This is useful when debugging programs and understanding the values being processed.

---

# 16. Checking Data Types Using isinstance()

The `isinstance()` function checks whether an object belongs to a specified type.

It returns True or False.

Example:

```python
age = 23
name = "Abdulsamad"

print(isinstance(age, int))
print(isinstance(name, str))
print(isinstance(age, str))
```

Output:

```text
True
True
False
```

### Difference between type() and isinstance()

| Function | Purpose |
|---|---|
| `type()` | Identifies an object's type |
| `isinstance()` | Checks whether an object belongs to a specified type |

---

# 17. Mutable and Immutable Data Types

This is one of the most important concepts in Python.

### Mutable

Mutable objects can be changed after creation.

Examples:

- Lists.
- Dictionaries.
- Sets.

Example:

```python
marks = [80, 85, 90]

marks[0] = 100

print(marks)
```

### Immutable

Immutable objects cannot have their contents changed after creation.

Examples:

- Integers.
- Floats.
- Strings.
- Tuples.
- Booleans.
- Bytes.

Example:

```python
language = "Python"

language = language + " Programming"

print(language)
```

The original string was not modified. A new string was created and assigned to the variable.

### Comparison

| Mutable | Immutable |
|---|---|
| List | Integer |
| Dictionary | Float |
| Set | String |
| | Tuple |
| | Boolean |
| | Bytes |

Understanding mutability is important when working with large datasets and managing objects in Python programs.

---

# 18. Mixed Data Types

Python collections can store different data types together.

Example:

```python
student_record = [
    "Abdulsamad",
    23,
    95.5,
    True,
    None
]

print(student_record)
```

This is called a heterogeneous collection.

It is useful when storing records containing different types of information.

---

# 19. Importance of Data Types in Artificial Intelligence

Data types form the foundation of AI programming.

An AI system processes different forms of information.

Consider an image classification model:

```python
image_width = 224
image_height = 224
image_channels = 3

image_label = "Cat"

prediction_confidence = 0.985

is_prediction_correct = True

image_shape = (224, 224, 3)

model_information = {
    "name": "Image Classifier",
    "accuracy": 96.5,
    "trained": True
}
```

### How data types are applied in AI

| AI Information | Python Data Type |
|---|---|
| Image width | Integer |
| Image height | Integer |
| Learning rate | Float |
| Prediction confidence | Float |
| Image label | String |
| Prediction status | Boolean |
| Image dimensions | Tuple |
| Dataset records | List |
| Unique labels | Set |
| Model configuration | Dictionary |

### Connection to future AI libraries

**NumPy:** Uses numerical arrays to perform mathematical operations efficiently.

**Pandas:** Uses structured tables to organize, manipulate and analyse datasets.

**Matplotlib:** Uses numerical and categorical data to create visualizations.

**PyTorch:** Uses tensors to represent numerical data for machine learning and deep learning.

These libraries build upon the Python foundations we are learning now.

---

# 20. Practical Applications of Day 003

Today we developed three practical Python programs:

1. `data_types.py`
   - Studied Python's built-in data types.
   - Explored their characteristics and applications.

2. `exercises.py`
   - Completed 10 solved practical exercises.
   - Practised data types and collection operations.

3. `challenge.py`
   - Built an AI Student and Image Classification Management System.
   - Combined multiple data types into one practical program.

---

# 21. Important Commands Learned

| Command | Function |
|---|---|
| `type()` | Identifies data type |
| `isinstance()` | Checks object type |
| `len()` | Counts elements |
| `max()` | Finds maximum value |
| `min()` | Finds minimum value |
| `sum()` | Calculates total |
| `append()` | Adds an item to a list |
| `add()` | Adds an item to a set |
| `items()` | Retrieves dictionary key-value pairs |
| `range()` | Generates an integer sequence |
| `is` | Tests object identity |
| `in` | Checks membership |

---

# 22. Day 003 Summary

Today I learned:

- What Python data types are.
- Integer and floating-point values.
- Strings and Boolean values.
- NoneType and complex numbers.
- Lists and tuples.
- Sets and dictionaries.
- Range and bytes.
- Data type identification using `type()`.
- Type checking using `isinstance()`.
- Mutable and immutable objects.
- Mixed data types.
- Applications of Python data types in AI.

**Main lesson:** Understanding data types is essential because AI systems process different kinds of information, including numerical values, text, labels, datasets and tensors.

---

# 23. Day 003 Completion Record

| File | Status |
|---|---|
| `data_types.py` | Completed |
| `exercises.py` | Completed |
| `challenge.py` | Completed |
| `notes.md` | Completed |

**Day 003: Python Data Types — Completed**

---

## Learning Philosophy

One day at a time. One concept at a time. One project at a time.

**Goal: Becoming a competent Python programmer and eventually an Artificial Intelligence and Machine Learning Engineer.**