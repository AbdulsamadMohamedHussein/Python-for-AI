# DAY 004 — PYTHON TYPE CONVERSION

**Course:** Bachelor's in Artificial Intelligence  
**Program:** 90-Day Python Programming Journey  
**Topic:** Type Conversion in Python  
**Student:** Abdulsamad Mohamed

---

# 1. Introduction to Type Conversion

Type conversion is the process of changing a value from one data type into another data type.

Python provides several built-in functions that allow us to convert data types.

For example:

```python
age = "23"

age = int(age)

print(age)
print(type(age))
```

Output:

```text
23
<class 'int'>
```

Initially, the value was a string. After conversion, it became an integer.

**Why is type conversion important?**

- It allows mathematical calculations.
- It helps process user input.
- It helps clean datasets.
- It prepares numerical data for Machine Learning.
- It allows us to work with image pixels in Computer Vision.

# 2. Types of Type Conversion

There are two major categories of type conversion.

## 2.1 Implicit Type Conversion

Implicit conversion happens automatically when Python converts one compatible numerical type into another.

Example:

```python
integer_number = 10
float_number = 5.5

result = integer_number + float_number

print(result)
print(type(result))
```

Output:

```text
15.5
<class 'float'>
```

Python automatically converts the integer into a floating-point representation during the calculation.

## 2.2 Explicit Type Conversion

Explicit conversion happens when the programmer manually converts a value using a conversion function.

Example:

```python
age = "23"

converted_age = int(age)

print(converted_age)
print(type(converted_age))
```

Output:

```text
23
<class 'int'>
```

Here, we explicitly used `int()` to convert a string into an integer.

# 3. Important Python Type Conversion Functions

| Function | Purpose | Example |
|---|---|---|
| `int()` | Converts into integer | `int("25")` |
| `float()` | Converts into float | `float("25.5")` |
| `str()` | Converts into string | `str(100)` |
| `bool()` | Converts into Boolean | `bool(1)` |
| `list()` | Converts into list | `list((1, 2))` |
| `tuple()` | Converts into tuple | `tuple([1, 2])` |
| `set()` | Converts into set | `set([1, 2, 2])` |
| `dict()` | Creates a dictionary | `dict([("a", 1)])` |

# 4. Integer Conversion — int()

The `int()` function converts compatible values into integers.

Example:

```python
number = "100"

converted_number = int(number)

print(converted_number)
print(type(converted_number))
```

Output:

```text
100
<class 'int'>
```

**Important:** When converting a float into an integer, Python removes the decimal portion rather than rounding it.

```python
number = 95.85

print(int(number))
```

Output:

```text
95
```

# 5. Float Conversion — float()

The `float()` function converts compatible values into floating-point numbers.

Example:

```python
marks = "95.5"

converted_marks = float(marks)

print(converted_marks)
print(type(converted_marks))
```

Output:

```text
95.5
<class 'float'>
```

Floats are especially important in AI because numerical calculations frequently involve decimal values.

Examples:

- Model accuracy
- Learning rates
- Loss values
- Prediction probabilities
- Numerical measurements

# 6. String Conversion — str()

The `str()` function converts compatible values into strings.

Example:

```python
age = 23

age_text = str(age)

print(age_text)
print(type(age_text))
```

Output:

```text
23
<class 'str'>
```

String conversion is useful when displaying numerical information in messages or combining information into text.

# 7. Boolean Conversion — bool()

The `bool()` function converts values into Boolean values.

Boolean values are:

- True
- False

Examples:

```python
print(bool(1))
print(bool(0))

print(bool("Python"))
print(bool(""))

print(bool(100))
print(bool([]))
```

Output:

```text
True
False
True
False
True
False
```

**Important concept:**

Most non-zero numbers and non-empty collections are truthy.

Zero, empty strings and empty collections are falsy.

Boolean values are important in programming decisions, conditions and classification logic.

# 8. Collection Conversion

Python allows us to convert between different collection types.

## 8.1 List Conversion

```python
numbers = (10, 20, 30)

converted_list = list(numbers)

print(converted_list)
```

Output:

```text
[10, 20, 30]
```

## 8.2 Tuple Conversion

```python
numbers = [10, 20, 30]

converted_tuple = tuple(numbers)

print(converted_tuple)
```

Output:

```text
(10, 20, 30)
```

## 8.3 Set Conversion

```python
numbers = [10, 20, 20, 30, 30]

converted_set = set(numbers)

print(converted_set)
```

Output:

```text
{10, 20, 30}
```

A set automatically removes duplicate elements.

Remember:

- List: Ordered and mutable.
- Tuple: Ordered and immutable.
- Set: Stores unique elements and is unordered.

# 9. Dictionary Conversion

A dictionary stores information in key-value pairs.

Example:

```python
student_data = [
    ("name", "Abdulsamad"),
    ("age", 23),
    ("course", "Artificial Intelligence")
]

student_dictionary = dict(student_data)

print(student_dictionary)
```

Output:

```text
{
    'name': 'Abdulsamad',
    'age': 23,
    'course': 'Artificial Intelligence'
}
```

We can access individual values using their keys.

```python
print(student_dictionary["name"])
print(student_dictionary["age"])
```

Dictionaries are useful for storing structured information, including AI model configurations.

# 10. User Input and Type Conversion

One of the most important things we learned today is that Python's `input()` function always returns a string.

Example:

```python
age = input("Enter your age: ")

print(type(age))
```

Even if the user enters 23, the result is:

```text
<class 'str'>
```

To perform mathematical calculations, we must convert the input.

```python
age = int(input("Enter your age: "))

future_age = age + 5

print("Your age after five years:", future_age)
```

For decimal values:

```python
marks = float(input("Enter your marks: "))

print("Your marks:", marks)
```

# 11. Exception Handling During Conversion

Sometimes Python cannot convert a value because the input is invalid.

Example:

```python
age = int("twenty")
```

This produces a `ValueError`.

We can handle this using `try` and `except`.

```python
try:

    age = int(input("Enter your age: "))

    print("Your age is:", age)

except ValueError:

    print("Please enter a valid number.")
```

Important commands:

- `try`: Executes code that might generate an error.
- `except`: Handles the error.
- `ValueError`: Indicates that a value is inappropriate for the requested conversion.

Exception handling makes Python programs more reliable.

# 12. List Comprehension

Today we also used list comprehension to convert multiple values efficiently.

Example:

```python
ages = ["20", "21", "22", "23"]

converted_ages = [
    int(age) for age in ages
]

print(converted_ages)
```

Output:

```text
[20, 21, 22, 23]
```

The same operation can be performed using a normal for loop.

```python
ages = ["20", "21", "22", "23"]

converted_ages = []

for age in ages:

    converted_ages.append(int(age))

print(converted_ages)
```

List comprehension provides a shorter way to create a new list from an existing iterable.

# 13. Important Python Functions

## type()

Identifies the data type of a value.

```python
number = 100

print(type(number))
```

## isinstance()

Checks whether a value belongs to a particular data type.

```python
number = 100

print(isinstance(number, int))
```

Output:

```text
True
```

## round()

Rounds a numerical value.

```python
accuracy = 95.6789

print(round(accuracy, 2))
```

Output:

```text
95.68
```

## sum()

Calculates the sum of numerical values.

```python
marks = [80, 90, 95]

print(sum(marks))
```

Output:

```text
265
```

## len()

Returns the number of elements.

```python
students = ["John", "Mary", "David"]

print(len(students))
```

Output:

```text
3
```

# 14. Application of Type Conversion in Artificial Intelligence

Type conversion is important in preparing data for AI applications.

## 14.1 Machine Learning

Machine Learning algorithms require appropriately represented numerical inputs.

For example:

```python
accuracy = "95.5"

accuracy = float(accuracy)

print(accuracy)
```

This allows us to perform numerical calculations with the accuracy value.

## 14.2 Dataset Preprocessing

Real-world datasets may contain numerical information stored as text.

Example:

```python
student_marks = ["80.5", "90.0", "95.5"]

cleaned_marks = [
    float(mark) for mark in student_marks
]

average = sum(cleaned_marks) / len(cleaned_marks)

print(average)
```

This demonstrates how we can convert data before calculating statistical measurements.

## 14.3 Computer Vision

Images contain numerical pixel values.

For standard 8-bit image channels, pixel values range from 0 to 255.

We can normalize them using:

\[
x_{\text{normalized}}=\frac{x}{255}
\]

Example:

```python
pixels = [0, 128, 255]

normalized_pixels = [
    pixel / 255.0 for pixel in pixels
]

print(normalized_pixels)
```

Output:

```text
[0.0, 0.5019607843137255, 1.0]
```

This transforms the pixel values into a range between 0 and 1.

This is a common preprocessing operation in Computer Vision.

## 14.4 Deep Learning

Deep learning frameworks such as PyTorch use tensors to represent numerical data.

Tensor data types include:

- `torch.float32`
- `torch.float64`
- `torch.int64`
- `torch.int32`

The correct numerical type matters when performing tensor operations and training neural networks.

We will study these concepts when we reach PyTorch.

# 15. Day 004 Coding Challenge Summary

**Project:** AI Dataset Preprocessing and Image Data Management System.

In our challenge.py, we developed a simplified preprocessing program that:

1. Created a raw dataset.
2. Inspected original data types.
3. Converted strings into integers and floats.
4. Handled invalid numerical conversions.
5. Created a cleaned dataset.
6. Calculated student averages.
7. Used Boolean values for eligibility.
8. Converted image pixels into floats.
9. Normalized image pixel values.
10. Created an AI model configuration.
11. Validated data types using `isinstance()`.
12. Generated a final preprocessing report.

This project connected basic Python programming with practical AI data preparation.

# 16. Important Concepts to Remember

| Concept | What it means |
|---|---|
| Type Conversion | Changing one data type into another |
| Implicit Conversion | Automatic conversion |
| Explicit Conversion | Programmer-controlled conversion |
| Integer | Whole numerical value |
| Float | Decimal numerical value |
| String | Text representation |
| Boolean | True or False |
| List Comprehension | Short method of creating lists |
| Exception Handling | Managing programming errors |
| Data Preprocessing | Preparing raw data for analysis or AI |
| Normalization | Scaling numerical values into a chosen range |

# 17. Day 004 Learning Outcomes

After completing Day 004, I should be able to:

- Explain implicit and explicit type conversion.
- Convert strings into integers and floats.
- Convert numbers into strings.
- Understand Boolean conversion.
- Convert between lists, tuples and sets.
- Create dictionaries from key-value pairs.
- Convert user input into appropriate numerical types.
- Handle conversion errors using try and except.
- Use list comprehension.
- Understand how type conversion supports dataset preprocessing.
- Understand basic image pixel normalization.
- Explain why numerical data types matter in Machine Learning and Deep Learning.

# 18. Conclusion

Today I learned that Python data types are not just programming concepts. They are fundamental to preparing and processing information for Artificial Intelligence.

Before a Machine Learning model can learn from data, the data must be represented in appropriate formats.

Type conversion helps us transform raw information into useful numerical representations.

I also learned how Python can be applied to simple dataset preprocessing and Computer Vision operations.

**My learning principle:**

One day at a time. One concept at a time. Building strong foundations for Artificial Intelligence.

---

**END OF DAY 004 — PYTHON TYPE CONVERSION**

**Next Lesson: DAY 005 — PYTHON OPERATORS**