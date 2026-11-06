# DAY 017 — PYTHON SETS
## Bachelor's in Artificial Intelligence
### 90-Day Python Programming Journey

**Subject:** Python Programming  
**Topic:** Python Sets  
**Level:** Beginner to Intermediate  
**Main File:** `sets.py`

---

# 1. Introduction to Python Sets

A set is a built-in Python data structure used to store unique elements.

Sets are unordered collections that do not allow duplicate values.

Example:

```python
numbers = {10, 20, 30, 40, 50}

print(numbers)
```

Output:

```text
{10, 20, 30, 40, 50}
```

The displayed order is not guaranteed.

## Characteristics of Sets

1. Unordered: Sets do not guarantee element positions.
2. Mutable: We can add and remove elements.
3. Unique elements: Duplicate values are automatically eliminated.
4. No indexing: We cannot access elements using positions.
5. Hashable elements: Set elements must be hashable.
6. Mathematical operations: Sets support union, intersection and difference.
7. Iterable: We can process sets using loops.

---

# 2. Creating Sets

Sets are commonly created using curly brackets `{}`.

### Integer set

```python
numbers = {10, 20, 30, 40, 50}

print(numbers)
```

### String set

```python
names = {"Ali", "Ahmed", "John"}

print(names)
```

### Floating-point set

```python
measurements = {1.5, 2.5, 3.5}

print(measurements)
```

### Mixed set

```python
data = {"Python", 25, 3.14, True}

print(data)
```

Python allows different hashable data types in a set.

---

# 3. Creating an Empty Set

An important distinction exists between empty dictionaries and empty sets.

Incorrect:

```python
empty = {}
```

This creates a dictionary.

Correct:

```python
empty = set()

print(type(empty))
```

Output:

```text
<class 'set'>
```

---

# 4. Duplicate Elements

Sets automatically eliminate duplicate values.

Example:

```python
numbers = {10, 20, 10, 30, 20, 40}

print(numbers)
```

Output:

```text
{10, 20, 30, 40}
```

Only unique elements remain.

This makes sets useful for data cleaning and duplicate removal.

## Important equality behavior

Python considers equal values as duplicates in sets.

For example:

```python
values = {1, 1.0, True}

print(values)
```

These values compare equal in Python, so the set retains only one representative.

---

# 5. Converting Lists into Sets

The `set()` constructor converts an iterable into a set.

Example:

```python
numbers = [10, 20, 10, 30, 20, 40]

unique_numbers = set(numbers)

print(unique_numbers)
```

Output:

```text
{10, 20, 30, 40}
```

This is useful when removing duplicate values from datasets.

However, converting a list into a set does not preserve its original order.

---

# 6. Adding Elements

## 6.1 add()

The `add()` method inserts one element.

```python
fruits = {"Apple", "Banana", "Mango"}

fruits.add("Orange")

print(fruits)
```

If the element already exists, nothing changes.

## 6.2 update()

The `update()` method inserts multiple elements from an iterable.

```python
numbers = {10, 20, 30}

numbers.update([40, 50, 60])

print(numbers)
```

It can accept lists, tuples, sets and other iterables.

---

# 7. Removing Elements

Python provides several methods for removing set elements.

## 7.1 remove()

Removes a specified element.

```python
numbers = {10, 20, 30, 40}

numbers.remove(20)

print(numbers)
```

If the element does not exist, Python raises `KeyError`.

## 7.2 discard()

Removes an element if it exists.

```python
numbers = {10, 20, 30}

numbers.discard(20)

numbers.discard(100)

print(numbers)
```

Unlike `remove()`, `discard()` does not raise an error when an element is missing.

## 7.3 pop()

Removes and returns an arbitrary element.

```python
numbers = {10, 20, 30}

removed = numbers.pop()

print("Removed:", removed)

print("Remaining:", numbers)
```

Do not assume which element will be removed.

## 7.4 clear()

Removes every element.

```python
numbers = {10, 20, 30}

numbers.clear()

print(numbers)
```

Output:

```text
set()
```

---

# 8. Membership Operators

The `in` operator checks whether an element exists.

```python
languages = {"Python", "Java", "C++"}

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

Set membership is typically O(1) on average.

---

# 9. Set Length

The `len()` function returns the number of unique elements.

```python
numbers = {10, 20, 30, 40, 50}

print(len(numbers))
```

Output:

```text
5
```

---

# 10. Iterating Through Sets

We can use a `for` loop to process set elements.

```python
fruits = {"Apple", "Banana", "Mango"}

for fruit in fruits:

    print(fruit)
```

Remember that iteration order is not guaranteed.

If a consistent sorted display is required:

```python
for fruit in sorted(fruits):

    print(fruit)
```

`sorted()` returns a list.

---

# 11. Mathematical Set Theory

Set theory is a branch of mathematics that studies collections of distinct objects.

It is particularly important for understanding data relationships and mathematical reasoning in AI.

Consider:

A = {1, 2, 3, 4}

B = {3, 4, 5, 6}

We can perform several mathematical operations on these sets.

---

# 12. Set Union

Union combines all unique elements from two sets.

Mathematical symbol:

A ∪ B

Python operator:

```python
A | B
```

Python method:

```python
A.union(B)
```

Example:

```python
A = {1, 2, 3, 4}

B = {3, 4, 5, 6}

result = A | B

print(result)
```

Output:

```text
{1, 2, 3, 4, 5, 6}
```

Mathematical definition:

A ∪ B = {x : x ∈ A or x ∈ B}

Union includes every element belonging to either set.

---

# 13. Set Intersection

Intersection returns elements common to both sets.

Mathematical symbol:

A ∩ B

Python operator:

```python
A & B
```

Python method:

```python
A.intersection(B)
```

Example:

```python
A = {1, 2, 3, 4}

B = {3, 4, 5, 6}

result = A & B

print(result)
```

Output:

```text
{3, 4}
```

Mathematical definition:

A ∩ B = {x : x ∈ A and x ∈ B}

---

# 14. Set Difference

Difference returns elements present in the first set but absent from the second set.

Mathematical notation:

A − B

Python operator:

```python
A - B
```

Example:

```python
A = {1, 2, 3, 4, 5}

B = {3, 4, 5, 6, 7}

print(A - B)

print(B - A)
```

Output:

```text
{1, 2}
{6, 7}
```

IMPORTANT:

Set difference is not commutative.

In general:

A − B ≠ B − A

---

# 15. Symmetric Difference

Symmetric difference returns elements belonging to either set, but not both.

Mathematical symbol:

A △ B

Python operator:

```python
A ^ B
```

Python method:

```python
A.symmetric_difference(B)
```

Example:

```python
A = {1, 2, 3, 4}

B = {3, 4, 5, 6}

result = A ^ B

print(result)
```

Output:

```text
{1, 2, 5, 6}
```

Mathematical formula:

A △ B = (A − B) ∪ (B − A)

Another equivalent formula:

A △ B = (A ∪ B) − (A ∩ B)

---

# 16. Venn Diagram Interpretation

Venn diagrams visually represent mathematical relationships between sets.

Consider two overlapping sets, A and B.

- The entire area of A and B represents union.
- The overlapping region represents intersection.
- The portion of A outside B represents A − B.
- The portion of B outside A represents B − A.
- The two non-overlapping portions together represent symmetric difference.

### Visual representation

```text
              SET A             SET B

          ___________       ___________
        /           \     /           \
       /   A ONLY    \___/   B ONLY    \
      |               |                 |
      |               |                 |
       \             / \               /
        \___________/   \_____________/

                 OVERLAP
              A INTERSECTION B
```

The overlapping region contains elements shared by both sets.

---

# 17. Subsets

A set A is a subset of B if every element of A also belongs to B.

Mathematical symbol:

A ⊆ B

Python operator:

```python
A <= B
```

Python method:

```python
A.issubset(B)
```

Example:

```python
A = {1, 2}

B = {1, 2, 3, 4}

print(A <= B)
```

Output:

```text
True
```

A set is also a subset of itself.

Therefore:

A ⊆ A

---

# 18. Proper Subsets

A is a proper subset of B when:

1. Every element of A belongs to B.
2. A is not equal to B.

Mathematical symbol:

A ⊂ B

Python operator:

```python
A < B
```

Example:

```python
A = {1, 2}

B = {1, 2, 3}

print(A < B)
```

Output:

```text
True
```

However:

```python
A = {1, 2}

B = {1, 2}

print(A < B)
```

Output:

```text
False
```

The two sets are equal, so neither is a proper subset of the other.

---

# 19. Supersets

A is a superset of B if A contains every element of B.

Mathematical symbol:

A ⊇ B

Python operator:

```python
A >= B
```

Python method:

```python
A.issuperset(B)
```

Example:

```python
A = {1, 2, 3, 4, 5}

B = {1, 2, 3}

print(A >= B)
```

Output:

```text
True
```

---

# 20. Disjoint Sets

Two sets are disjoint if they have no common elements.

Mathematical condition:

A ∩ B = ∅

Python method:

```python
A.isdisjoint(B)
```

Example:

```python
A = {1, 2, 3}

B = {4, 5, 6}

print(A.isdisjoint(B))
```

Output:

```text
True
```

If they share even one element, they are not disjoint.

---

# 21. Cardinality of Sets

Cardinality means the number of distinct elements in a set.

Notation:

|A|

Example:

A = {10, 20, 30, 40}

Therefore:

|A| = 4

Python:

```python
A = {10, 20, 30, 40}

print(len(A))
```

## Important cardinality formula

For two finite sets:

|A ∪ B| = |A| + |B| − |A ∩ B|

This formula prevents counting common elements twice.

Example:

|A| = 5

|B| = 4

|A ∩ B| = 2

Then:

|A ∪ B| = 5 + 4 − 2

|A ∪ B| = 7

This is called the inclusion-exclusion principle for two sets.

---

# 22. Frozen Sets

A frozenset is an immutable version of a set.

Example:

```python
numbers = frozenset([10, 20, 30, 40])

print(numbers)
```

Unlike ordinary sets, frozen sets cannot be modified.

They do not support:

- add()
- remove()
- discard()
- clear()

However, they support mathematical set operations.

## Frozen sets as dictionary keys

Because frozensets are immutable and hashable when their elements are hashable, they can be used as dictionary keys.

```python
locations = {

    frozenset([10, 20]): "Point A",

    frozenset([30, 40]): "Point B"

}

print(locations[frozenset([20, 10])])
```

Output:

```text
Point A
```

---

# 23. Set Comprehensions

Set comprehensions provide a concise way to create sets.

Syntax:

```python
{expression for item in iterable}
```

Example:

```python
squares = {

    number ** 2

    for number in range(1, 6)

}

print(squares)
```

Output:

```text
{1, 4, 9, 16, 25}
```

## Conditional set comprehension

```python
even_numbers = {

    number

    for number in range(1, 21)

    if number % 2 == 0

}

print(even_numbers)
```

Output:

```text
{2, 4, 6, 8, 10, 12, 14, 16, 18, 20}
```

---

# 24. Removing Duplicates While Preserving Order

A normal set does not preserve the original sequence order.

If we need unique elements while maintaining the original order, we can use a dictionary.

Example:

```python
numbers = [10, 20, 10, 30, 20, 40]

unique_numbers = list(dict.fromkeys(numbers))

print(unique_numbers)
```

Output:

```text
[10, 20, 30, 40]
```

This is useful in data preprocessing when sequence order matters.

---

# 25. Mathematical Statistics Using Sets

Sets can be used for numerical analysis when the goal is to analyze distinct observations.

Consider:

X = {10, 20, 30, 40, 50}

## 25.1 Mean

The arithmetic mean is:

x̄ = Σxᵢ / n

Where:

- x̄ = Mean.
- xᵢ = Individual observation.
- n = Number of observations.

Example:

Mean = (10 + 20 + 30 + 40 + 50) / 5

Mean = 30

Python:

```python
data = {10, 20, 30, 40, 50}

mean = sum(data) / len(data)

print(mean)
```

IMPORTANT:

Using a set removes duplicate observations. Do not use this approach when repeated observations and their frequencies are statistically important.

## 25.2 Population Variance

Population variance measures the spread of observations around their population mean.

Formula:

σ² = Σ(xᵢ − μ)² / N

Where:

- σ² = Population variance.
- xᵢ = Individual observation.
- μ = Population mean.
- N = Number of observations.

For:

X = {10, 20, 30, 40, 50}

Mean = 30

Variance:

σ² = [(10−30)² + (20−30)² + (30−30)² + (40−30)² + (50−30)²] / 5

σ² = 1000 / 5

σ² = 200

## 25.3 Standard Deviation

Standard deviation is the square root of variance.

σ = √σ²

For this dataset:

σ = √200

σ ≈ 14.14

---

# 26. Sets in Data Science

Sets are useful for processing datasets containing repeated values.

### Example: Unique student records

```python
students = [

    "Ali",

    "Ahmed",

    "Ali",

    "John",

    "Ahmed"

]

unique_students = set(students)

print(unique_students)

print(len(unique_students))
```

Applications include:

- Duplicate detection.
- Unique category identification.
- Data cleaning.
- Comparing datasets.
- Finding shared records.
- Identifying missing categories.

---

# 27. Sets in Artificial Intelligence

Sets are useful in several AI-related programming tasks.

## 27.1 Machine Learning: Unique Class Labels

```python
labels = [

    "Cat",

    "Dog",

    "Cat",

    "Bird",

    "Dog"

]

unique_labels = set(labels)

print(unique_labels)
```

This helps identify the distinct classes in a classification dataset.

## 27.2 Feature Comparison

```python
dataset_A = {

    "age",

    "height",

    "weight",

    "income"

}

dataset_B = {

    "age",

    "weight",

    "education",

    "experience"

}

common = dataset_A & dataset_B

print(common)
```

This identifies common feature names between two datasets.

## 27.3 Computer Vision: Unique Object Classes

```python
detected_objects = [

    "Car",

    "Person",

    "Car",

    "Bicycle",

    "Person"

]

unique_objects = set(detected_objects)

print(unique_objects)
```

This example identifies unique object categories in detection results.

## 27.4 Natural Language Processing

```python
sentence = "python is powerful and python is useful"

words = sentence.lower().split()

unique_words = set(words)

print(unique_words)
```

This demonstrates vocabulary deduplication.

In real NLP systems, additional preprocessing and tokenization are often required.

---

# 28. Time Complexity of Sets

Time complexity describes how an algorithm's computational requirements grow with input size.

Python sets are generally implemented using hash tables.

Let n represent the number of elements.

| Operation | Average time complexity |
|---|---|
| Add | O(1) |
| Remove | O(1) |
| Discard | O(1) |
| Membership | O(1) |
| Length | O(1) |
| Iteration | O(n) |
| Union | O(n + m) |
| Intersection | O(min(n, m)) typical |
| Difference | O(n) typical |
| Symmetric difference | O(n + m) |

These are typical or simplified costs. Actual performance depends on implementation details and hash collisions.

## Understanding O(1)

Constant time means an operation takes approximately constant time on average.

Example:

```python
numbers = {10, 20, 30, 40}

print(20 in numbers)
```

## Understanding O(n)

Linear time means computational work grows with the number of elements.

Example:

```python
for number in numbers:

    print(number)
```

---

# 29. Lists Versus Sets Versus Tuples

These three data structures are essential Python fundamentals.

| Feature | List | Tuple | Set |
|---|---|---|---|
| Syntax | [] | () | {} |
| Ordered sequence | Yes | Yes | No |
| Mutable | Yes | No | Yes |
| Duplicates | Yes | Yes | No |
| Indexing | Yes | Yes | No |
| Slicing | Yes | Yes | No |
| Membership | O(n) | O(n) | O(1) average |
| Main purpose | General collections | Fixed sequences | Unique elements |

### When to use lists

Use lists when:

- Data changes frequently.
- Duplicate values matter.
- Order matters.
- Indexing is required.

### When to use tuples

Use tuples when:

- Data should remain structurally unchanged.
- You need fixed records.
- You represent coordinates.
- You need an immutable sequence.

### When to use sets

Use sets when:

- You need unique elements.
- You need fast membership checks.
- You need mathematical set operations.
- You need duplicate removal.

---

# 30. Common Set Errors

| Error | Cause | Solution |
|---|---|---|
| TypeError | Attempting indexing | Iterate or convert to another structure |
| KeyError | Missing value with remove() | Use discard() or check membership |
| TypeError | Adding a list to a set | Use a tuple if its elements are hashable |
| TypeError | Using a set as a dictionary key | Use frozenset |
| TypeError | Directly modifying a frozen set | Create a new frozenset |

Example of invalid indexing:

```python
numbers = {10, 20, 30}

# numbers[0] is invalid.
```

Correct approach:

```python
for number in numbers:

    print(number)
```

---

# 31. Day 017 Project Architecture

Our folder structure:

```text
day_017/
│
├── sets.py
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
| sets.py | Complete Python sets lesson |
| exercises.py | 30 solved programming exercises |
| challenge.py | Student Enrollment and Course Analysis System |
| notes.md | Complete theoretical reference |

---

# 32. Day 017 Learning Checklist

- [ ] Understand Python sets.
- [ ] Create different sets.
- [ ] Create an empty set.
- [ ] Understand duplicate removal.
- [ ] Convert lists into sets.
- [ ] Use add().
- [ ] Use update().
- [ ] Use remove().
- [ ] Use discard().
- [ ] Use pop().
- [ ] Use clear().
- [ ] Apply membership operators.
- [ ] Iterate through sets.
- [ ] Understand union.
- [ ] Understand intersection.
- [ ] Understand difference.
- [ ] Understand symmetric difference.
- [ ] Check subsets.
- [ ] Check proper subsets.
- [ ] Check supersets.
- [ ] Check disjoint sets.
- [ ] Understand cardinality.
- [ ] Understand frozen sets.
- [ ] Apply set comprehensions.
- [ ] Remove duplicates.
- [ ] Understand inclusion-exclusion.
- [ ] Calculate mean and variance.
- [ ] Understand time complexity.
- [ ] Apply sets to data science.
- [ ] Understand AI applications.

---

# 33. Connection to Our Six-Month AI Learning Journey

Day 017 prepares us for upcoming subjects.

| Future Subject | Connection |
|---|---|
| Mathematics for AI | Set theory and mathematical relationships |
| Statistics | Unique observations and data analysis |
| Data Structures | Hash tables and membership |
| NumPy | Numerical data processing |
| Pandas | Data cleaning and duplicate detection |
| Machine Learning | Classification labels and features |
| Deep Learning | Data preprocessing |
| Computer Vision | Object categories and detection labels |
| NLP | Vocabulary and unique tokens |

---

# 34. Final Reflection

Today I learned that Python sets are mutable, unordered collections that store unique elements.

I practised creating, modifying and removing elements from sets.

I learned mathematical set operations, including union, intersection, difference and symmetric difference.

I also studied subsets, supersets, disjoint sets, cardinality and frozen sets.

I applied set theory to statistics, data processing, machine learning labels, feature comparison and introductory AI examples.

Most importantly, I developed a stronger understanding of mathematical set theory and its connection to programming and artificial intelligence.

---

# DAY 017 — COMPLETED

**Main Topic:** Python Sets

**Main Lesson:** sets.py

**Exercises:** 30 solved exercises

**Challenge:** Student Enrollment and Course Analysis System

**Notes:** Complete theoretical reference

### OUR NEXT OBJECTIVE

- Continue mastering Python.
- Develop stronger mathematical reasoning.
- Study advanced data structures.
- Prepare for NumPy and Pandas.
- Progress toward Machine Learning and Deep Learning.

ONE CONCEPT AT A TIME.

ONE DAY AT A TIME.

WE ARE BUILDING REAL AI FOUNDATIONS! 🚀