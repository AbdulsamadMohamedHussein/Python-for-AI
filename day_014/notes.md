# DAY 014 — RANDOM NUMBERS AND GAME DEVELOPMENT

## Bachelor's in Artificial Intelligence
### 90-Day Python Programming Journey

**Subject:** Python Programming  
**Topic:** Random Number Generation and Interactive Game Development  
**Level:** Beginner to Intermediate  
**Main File:** `number_guessing_game.py`

---

# 1. Introduction to Random Number Generation

Random number generation is the process of producing numbers that appear unpredictable.

In Python, we use the built-in `random` module to generate pseudo-random numbers.

Random numbers are useful in:

- Games.
- Computer simulations.
- Statistical experiments.
- Probability modelling.
- Data science.
- Machine Learning.
- Artificial Intelligence.

For example, in a number guessing game, the computer generates a secret number that the player must discover.

### Importing the random module

```python
import random
```

The import statement makes the functions inside the random module available to our program.

---

# 2. Understanding random.randint()

The `randint()` function generates a random integer between two specified boundaries.

### Syntax

```python
random.randint(start, stop)
```

Both boundaries are included.

Example:

```python
import random

number = random.randint(1, 100)

print(number)
```

Possible outputs include:

```text
5
27
48
73
100
```

Every execution can produce a different result.

### Important distinction

`randint(1, 100)` can generate both 1 and 100.

---

# 3. Other Important Random Functions

Python provides several useful functions in the random module.

| Function | Purpose |
|---|---|
| `random.randint(a, b)` | Random integer between a and b |
| `random.random()` | Random floating-point number from 0.0 up to, but not including, 1.0 |
| `random.uniform(a, b)` | Random floating-point number between two boundaries |
| `random.choice(sequence)` | Selects one random element |
| `random.shuffle(list)` | Randomly rearranges a list |
| `random.randrange(start, stop)` | Selects a value from a range |

### Example: random.random()

```python
import random

number = random.random()

print(number)
```

Possible output:

```text
0.735214
```

### Example: random.choice()

```python
import random

colors = ["red", "blue", "green", "yellow"]

selected_color = random.choice(colors)

print(selected_color)
```

The computer randomly selects one color.

### Example: random.shuffle()

```python
import random

numbers = [1, 2, 3, 4, 5]

random.shuffle(numbers)

print(numbers)
```

The list is rearranged in random order.

---

# 4. Understanding Pseudo-Random Numbers

Python's standard random module uses a pseudo-random number generator.

A pseudo-random number generator produces numbers using a deterministic mathematical algorithm.

The numbers appear random, but the sequence is determined by an internal state and starting seed.

### Understanding random.seed()

```python
import random

random.seed(10)

print(random.randint(1, 100))
```

A fixed seed allows reproducible random sequences.

If the same seed and same sequence of random operations are used, the results can be reproduced.

### Why is this important?

Reproducibility is important in:

- Machine Learning experiments.
- Model training.
- Scientific simulations.
- Testing algorithms.
- Debugging programs.

**Important:** Python's standard random module is not suitable for security-sensitive operations such as generating passwords or authentication tokens. The `secrets` module is designed for those purposes.

---

# 5. Probability Fundamentals

Probability measures how likely an event is to occur.

Its value ranges from 0 to 1.

\[
0\leq P(A)\leq1
\]

Where:

- 0 means an impossible event.
- 1 means a certain event.
- Values between 0 and 1 represent different likelihoods.

### Basic probability formula

\[
P(A)=\frac{\text{Favourable Outcomes}}{\text{Total Equally Likely Outcomes}}
\]

Example: Rolling a six-sided dice.

Possible outcomes:

\[
S=\{1,2,3,4,5,6\}
\]

Probability of rolling a 3:

\[
P(3)=\frac{1}{6}
\]

Probability of rolling an even number:

\[
P(E)=\frac{3}{6}
\]

\[
P(E)=0.5=50\%
\]

This introduces the mathematical foundation of random simulations.

---

# 6. Simulating a Dice Roll

A six-sided dice produces values between 1 and 6.

### Python implementation

```python
import random

dice = random.randint(1, 6)

print("Dice result:", dice)
```

We can simulate 1,000 dice rolls.

```python
import random

counter = 0

while counter < 1000:

    dice = random.randint(1, 6)

    print(dice)

    counter += 1
```

This demonstrates repeated random experiments.

In probability, repeated experiments help us understand how observed frequencies compare with theoretical probabilities.

---

# 7. Understanding Conditional Statements

Conditional statements allow programs to make decisions.

Python provides:

- `if`
- `elif`
- `else`

### Basic syntax

```python
if condition:

    statement

elif another_condition:

    statement

else:

    statement
```

### Example

```python
secret_number = 50

guess = 70

if guess > secret_number:

    print("Too high!")

elif guess < secret_number:

    print("Too low!")

else:

    print("Correct!")
```

The computer compares the guess with the secret number and chooses the appropriate response.

This is the central decision-making mechanism of our guessing game.

---

# 8. Comparison Operators

Comparison operators compare two values and produce a Boolean result.

| Operator | Meaning |
|---|---|
| `==` | Equal to |
| `!=` | Not equal to |
| `>` | Greater than |
| `<` | Less than |
| `>=` | Greater than or equal to |
| `<=` | Less than or equal to |

Example:

```python
number = 20

print(number == 20)
print(number > 10)
print(number < 5)
```

Output:

```text
True
True
False
```

Boolean values are fundamental to Python decision-making.

---

# 9. While Loops in Game Development

A while loop repeatedly executes a block of code while its condition remains True.

In our guessing game, the player must be allowed to guess repeatedly.

### Syntax

```python
while condition:

    statement
```

### Example

```python
secret_number = 25

while True:

    guess = int(input("Guess the number: "))

    if guess == secret_number:

        print("You won!")

        break
```

The loop continues until the correct answer is entered.

The `break` statement terminates the loop.

---

# 10. break and continue

These two statements control loop execution.

### break

Immediately terminates the nearest enclosing loop.

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

### continue

Skips the remaining statements in the current iteration.

```python
number = 0

while number < 5:

    number += 1

    if number == 3:

        continue

    print(number)
```

Output:

```text
1
2
4
5
```

### Comparison

| break | continue |
|---|---|
| Terminates the loop | Skips the current iteration |
| Exits the loop | Continues to the next iteration |
| Used to stop execution | Used to skip unwanted operations |

---

# 11. User Input and Type Conversion

The `input()` function accepts information from users.

However, input() always returns a string.

Example:

```python
guess = input("Enter a number: ")
```

If we want to perform numerical comparisons, we must convert the string into an integer.

```python
guess = int(input("Enter a number: "))
```

### Example

```python
age = int(input("Enter your age: "))

print(age + 5)
```

If the user enters 20, the result is 25.

---

# 12. Input Validation

Input validation ensures that users provide acceptable information.

For example, a guessing game should not accept letters instead of numbers.

### Understanding ValueError

```python
number = int("hello")
```

This produces a ValueError because Python cannot convert the text into an integer.

We can handle this using try and except.

### Python implementation

```python
while True:

    try:

        guess = int(input("Enter a number: "))

        break

    except ValueError:

        print("Invalid input. Try again.")
```

The program continues asking until a valid integer is provided.

### Range validation

```python
guess = int(input("Enter a number: "))

if 1 <= guess <= 100:

    print("Valid guess.")

else:

    print("Invalid range.")
```

Input validation improves the reliability of software applications.

---

# 13. Tracking Attempts

In our guessing game, we need to track how many guesses the player makes.

We use a counter variable.

### Python implementation

```python
attempts = 0

guess = 25

attempts += 1

print("Attempts:", attempts)
```

The increment operator:

```python
attempts += 1
```

is equivalent to:

```python
attempts = attempts + 1
```

### Remaining attempts formula

\[
R=M-A
\]

Where:

- R = Remaining attempts.
- M = Maximum allowed attempts.
- A = Attempts already used.

Example:

\[
R=10-4=6
\]

The player has six attempts remaining.

---

# 14. Understanding Game Difficulty Levels

Games often contain different difficulty settings.

Our project includes three levels.

| Difficulty | Number range | Attempts |
|---|---:|---:|
| Easy | 1–20 | 10 |
| Medium | 1–50 | 7 |
| Hard | 1–100 | 5 |

### Python implementation

```python
difficulty = input("Choose difficulty: ").lower()

if difficulty == "easy":

    maximum = 20

    attempts = 10

elif difficulty == "medium":

    maximum = 50

    attempts = 7

elif difficulty == "hard":

    maximum = 100

    attempts = 5

else:

    print("Invalid difficulty.")
```

Difficulty selection allows the program to adapt its behaviour according to user choices.

---

# 15. Understanding Absolute Difference

Absolute difference measures the distance between two numerical values without considering their signs.

Mathematical formula:

\[
D=|x-y|
\]

Example:

\[
D=|50-45|
\]

\[
D=5
\]

Python provides the built-in `abs()` function.

```python
secret_number = 50

guess = 45

difference = abs(secret_number - guess)

print(difference)
```

Output:

```text
5
```

We use this calculation to provide proximity hints.

For example:

| Difference | Hint |
|---|---|
| 0 | Correct |
| 1–3 | Very close |
| 4–7 | Close |
| 8–15 | Getting warmer |
| Above 15 | Far away |

These thresholds are game-design choices, not mathematical laws.

---

# 16. Functions in Game Development

Functions organize code into reusable blocks.

They improve:

- Readability.
- Reusability.
- Organization.
- Testing.
- Maintenance.

### Basic function

```python
def welcome():

    print("Welcome to the game!")

welcome()
```

### Function with parameters

```python
def calculate_score(attempts):

    score = 100 - (attempts - 1) * 10

    return max(0, score)


result = calculate_score(3)

print(result)
```

Output:

```text
80
```

### Understanding return

The `return` statement sends a result back to the calling code.

This allows functions to calculate information that other parts of the application can use.

---

# 17. Score Calculation

Our game rewards players who use fewer attempts.

A simple scoring formula is:

\[
S=\max(0,M-P(A-1))
\]

Where:

- S = Final score.
- M = Maximum score.
- P = Penalty per additional attempt.
- A = Attempts used.

Example:

Maximum score:

\[
M=100
\]

Penalty:

\[
P=10
\]

Attempts:

\[
A=3
\]

Therefore:

\[
S=100-10(3-1)
\]

\[
\boxed{S=80}
\]

The maximum score depends on the selected difficulty in our project.

---

# 18. Multiple Rounds

A multiple-round game allows the player to repeat the guessing process.

We use an outer loop to control rounds and an inner loop to control guesses.

### Python implementation

```python
round_number = 1

while round_number <= 3:

    secret_number = random.randint(1, 10)

    attempts = 0

    while True:

        guess = int(input("Guess: "))

        attempts += 1

        if guess == secret_number:

            print("You won!")

            break

        else:

            print("Try again.")

    round_number += 1
```

### Explanation

- The outer loop controls the number of rounds.
- The inner loop controls guesses within each round.
- A new secret number is generated for every round.

Nested loops are useful for understanding complex application logic.

---

# 19. Tracking Best Performance

We can track the player's best performance.

A player who wins using fewer attempts has a better attempt record.

### Python implementation

```python
best_attempts = None

current_attempts = 3

if best_attempts is None or current_attempts < best_attempts:

    best_attempts = current_attempts

print("Best performance:", best_attempts)
```

The `None` value indicates that no performance has been recorded yet.

We use this technique in our challenge project.

---

# 20. Statistical Analysis of Game Performance

Our guessing game collects numerical information.

We can use this information to calculate basic statistics.

### Total rounds

\[
T=W+L
\]

Where:

- T = Total rounds.
- W = Successful rounds.
- L = Failed rounds.

### Win percentage

\[
Win\ Rate=\frac{W}{T}\times100
\]

Example:

A player wins four rounds out of five.

\[
Win\ Rate=\frac{4}{5}\times100
\]

\[
\boxed{80\%}
\]

### Average attempts per successful round

\[
\bar{A}=\frac{\text{Total Attempts}}{\text{Successful Rounds}}
\]

These statistics allow us to evaluate player performance.

Important: If failed rounds are included in total attempts, this average is not strictly the average attempts per successful round. For that statistic, we should maintain a separate successful-attempt total.

---

# 21. Understanding Global Variables

A global variable is defined outside a function.

It can be accessed by functions within the same module.

Example:

```python
total_rounds = 0

def play_game():

    global total_rounds

    total_rounds += 1

play_game()

print(total_rounds)
```

Output:

```text
1
```

The `global` keyword allows the function to modify the module-level variable.

Global variables can be useful for small applications, but larger programs often use classes or structured data objects to manage state more cleanly.

---

# 22. Main Function and Program Execution

A main function organizes the application's starting point.

Example:

```python
def main():

    print("Game started!")

    print("Welcome!")


if __name__ == "__main__":

    main()
```

### What does this mean?

`__name__` is a special Python variable.

When a file is executed directly, its value is `"__main__"`.

This structure allows us to execute the application directly while also making its functions available for importing into other files.

It is widely used in professional Python projects.

---

# 23. Algorithm Design

An algorithm is a finite sequence of well-defined instructions for solving a problem.

Our guessing game follows this algorithm:

1. Start the application.
2. Display the main menu.
3. Ask the player to select a difficulty.
4. Generate a random secret number.
5. Ask the player for a guess.
6. Validate the input.
7. Compare the guess with the secret number.
8. Display a high or low hint.
9. Update the attempt counter.
10. Repeat until the player wins or attempts run out.
11. Calculate the score.
12. Update game statistics.
13. Ask whether the player wants another round.
14. Exit when the player chooses to stop.

### Algorithmic thinking

When developing software, we should:

- Understand the problem.
- Identify inputs.
- Identify outputs.
- Design the processing steps.
- Consider exceptional situations.
- Test the solution.

This approach is important throughout computer science.

---

# 24. Time Complexity

Time complexity describes how an algorithm's running time grows as input size increases.

We use Big-O notation.

### O(1) — Constant time

```python
number = 10

print(number)
```

The operation takes a constant amount of work.

### O(n) — Linear time

```python
counter = 0

while counter < n:

    counter += 1
```

The number of iterations increases with n.

### O(n²) — Quadratic time

```python
row = 0

while row < n:

    column = 0

    while column < n:

        column += 1

    row += 1
```

The nested loops perform approximately n² iterations.

### Important distinction

A basic guessing game with a fixed maximum of five, seven or ten attempts has a bounded number of guessing iterations.

If the allowed attempts are represented by a variable n, the worst-case guessing loop is O(n).

---

# 25. Randomness and Reproducibility in Machine Learning

Random number generation is important in Machine Learning.

Randomness is used in:

- Initializing model parameters.
- Shuffling training datasets.
- Selecting training samples.
- Data augmentation.
- Randomized algorithms.
- Experimental simulations.

### Example: Reproducible random generation

```python
import random

random.seed(42)

numbers = []

for i in range(5):

    numbers.append(random.randint(1, 100))

print(numbers)
```

The fixed seed makes the generated sequence reproducible.

In future lessons, we will use NumPy's random number generator for numerical experiments and Machine Learning workflows.

---

# 26. Randomness in Artificial Intelligence

Randomness plays an important role in many AI systems.

| AI Application | Use of randomness |
|---|---|
| Neural Networks | Parameter initialization |
| Machine Learning | Dataset shuffling |
| Computer Vision | Random image augmentation |
| Reinforcement Learning | Exploration |
| Simulations | Generating experimental scenarios |
| Optimization | Randomized search methods |

### Reinforcement Learning connection

In reinforcement learning, an agent interacts with an environment.

The agent may choose actions based on its current knowledge or explore alternative actions.

This introduces the exploration-exploitation trade-off.

Our guessing game is not a reinforcement learning system, but it introduces basic concepts of interaction, actions, feedback and outcomes.

---

# 27. Common Programming Errors

| Error | Cause | Solution |
|---|---|---|
| ValueError | Invalid integer conversion | Use try/except |
| TypeError | Incorrect data types | Check types |
| NameError | Undefined variable | Define variables |
| IndentationError | Incorrect indentation | Fix indentation |
| Infinite loop | Incorrect termination logic | Check loop conditions |
| ZeroDivisionError | Division by zero | Validate denominator |
| Logic error | Incorrect game conditions | Test each branch |
| Incorrect score | Wrong scoring formula | Verify calculations |

---

# 28. Day 014 Project Architecture

Our complete folder structure:

```text
day_014/
│
├── number_guessing_game.py
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
| number_guessing_game.py | Main lesson and code demonstrations |
| exercises.py | 30 solved programming exercises |
| challenge.py | Advanced interactive guessing game |
| notes.md | Complete theoretical revision notes |

---

# 29. Day 014 Learning Checklist

- [ ] Understand the random module.
- [ ] Use random.randint().
- [ ] Understand random.random().
- [ ] Use random.choice().
- [ ] Understand pseudo-random numbers.
- [ ] Understand random seeds.
- [ ] Learn probability fundamentals.
- [ ] Use conditional statements.
- [ ] Apply while loops.
- [ ] Understand break and continue.
- [ ] Accept user input.
- [ ] Convert strings into integers.
- [ ] Validate user input.
- [ ] Track attempts.
- [ ] Implement difficulty levels.
- [ ] Calculate scores.
- [ ] Use functions and parameters.
- [ ] Build multiple-round applications.
- [ ] Track player performance.
- [ ] Calculate win percentages.
- [ ] Understand basic algorithm complexity.
- [ ] Understand randomness in AI.
- [ ] Complete all 30 exercises.
- [ ] Complete the advanced challenge.

---

# 30. Connection to Our Six-Month AI Degree

Day 014 contributes to our long-term AI learning objectives.

| Future Subject | Knowledge gained |
|---|---|
| Mathematics for AI | Probability and numerical reasoning |
| Statistics | Frequencies and performance analysis |
| Python Programming | Functions, loops and conditions |
| NumPy | Random numerical generation |
| Machine Learning | Reproducible experiments |
| Deep Learning | Understanding random initialization |
| Computer Vision | Understanding random image transformations |
| Reinforcement Learning | Interaction and exploration concepts |

The purpose of these foundations is to prepare us for increasingly complex AI applications.

---

# 31. Final Reflection

Today I learned how to generate pseudo-random numbers using Python's random module.

I understood the fundamentals of probability, conditional statements, loops and user input validation.

I learned how to develop an interactive guessing game using functions, difficulty levels, attempt tracking, hints and score calculations.

I also practised basic statistical analysis by calculating win percentages and average performance.

Most importantly, I discovered how random number generation connects to reproducibility, Machine Learning, simulations and Artificial Intelligence.

**My next objectives:**

- Strengthen Python programming.
- Develop algorithmic thinking.
- Improve mathematical reasoning.
- Learn NumPy and Pandas.
- Study Mathematics and Statistics for AI.
- Progress toward Machine Learning and Deep Learning.

---

## DAY 014 — COMPLETED

**Topic:** Random Number Generation and Game Development

**Main Project:** Advanced Number Guessing Game

**Exercises:** 30 solved exercises

**Challenge:** Interactive multi-level guessing game

**Notes:** Complete theoretical revision

ONE DAY AT A TIME. ONE CONCEPT AT A TIME. ONE PROJECT AT A TIME.

KEEP BUILDING. KEEP LEARNING. KEEP IMPROVING! 🚀