
# =====================================================================
# DAY 012 - PYTHON FOR LOOPS
#
# PRACTICAL PROJECT:
# STUDENT PERFORMANCE AND DATA ANALYSIS SYSTEM
#
# Bachelor's in Artificial Intelligence
# 90-Day Python Programming Journey
#
# CONCEPTS USED:
# 1. For loops
# 2. Nested for loops
# 3. Lists
# 4. Dictionaries
# 5. Functions
# 6. Conditional statements
# 7. enumerate()
# 8. zip()
# 9. Mathematical calculations
# 10. Data processing
# 11. Statistical analysis
#
# =====================================================================


# =====================================================================
# SECTION 1: PROJECT INTRODUCTION
# =====================================================================

print("\n" + "=" * 75)

print("       STUDENT PERFORMANCE AND DATA ANALYSIS SYSTEM")

print("=" * 75)

print("Welcome to the Student Data Analysis System.")

print("This program analyzes academic performance.")

print("=" * 75)


# =====================================================================
# SECTION 2: STUDENT DATASET
# =====================================================================

# A dictionary stores student names as keys
# and their examination marks as values.
#
# Each student has five examination subjects.
#
# This is our sample dataset.

students = {

    "Ali": [85, 90, 78, 92, 88],

    "Ahmed": [70, 75, 80, 65, 72],

    "Sara": [95, 98, 92, 96, 94],

    "John": [45, 50, 48, 55, 40],

    "Mary": [88, 85, 90, 87, 91],

    "David": [60, 65, 58, 70, 62],

    "Fatima": [92, 89, 95, 94, 97],

    "James": [35, 42, 38, 45, 40]

}


subjects = [

    "Mathematics",

    "Python",

    "Statistics",

    "Machine Learning",

    "Computer Science"

]


# =====================================================================
# SECTION 3: DISPLAY STUDENT RECORDS
# =====================================================================

# The outer loop processes each student.
#
# The inner loop processes each student's marks.
#
# This demonstrates nested for loops.

print("\n" + "=" * 75)

print("SECTION 3: STUDENT RECORDS")

print("=" * 75)


for student_name, marks in students.items():

    print("\nStudent:", student_name)

    # zip() pairs each subject with its corresponding mark.

    for subject, mark in zip(subjects, marks):

        print(subject, ":", mark)


# =====================================================================
# SECTION 4: CALCULATE INDIVIDUAL STUDENT TOTALS
# =====================================================================

# We calculate the total marks for every student.
#
# total starts at zero.
#
# Every examination mark is added to total.

print("\n" + "=" * 75)

print("SECTION 4: INDIVIDUAL STUDENT TOTALS")

print("=" * 75)


student_totals = {}

for student_name, marks in students.items():

    total = 0

    for mark in marks:

        total += mark

    # Store each student's total in a dictionary.

    student_totals[student_name] = total

    print(student_name, "Total Marks:", total)


# =====================================================================
# SECTION 5: CALCULATE INDIVIDUAL AVERAGES
# =====================================================================

# Formula:
#
# Average = Total Marks / Number of Subjects
#
# len(marks) calculates the number of subjects.
#
# We store the average of every student.

print("\n" + "=" * 75)

print("SECTION 5: STUDENT AVERAGES")

print("=" * 75)


student_averages = {}

for student_name, marks in students.items():

    total = 0

    for mark in marks:

        total += mark

    average = total / len(marks)

    student_averages[student_name] = average

    print(student_name, "Average:", round(average, 2))


# =====================================================================
# SECTION 6: ASSIGN ACADEMIC GRADES
# =====================================================================

# We use conditional statements to assign grades.
#
# Example grading scale:
#
# 90 - 100 = A+
# 80 - 89  = A
# 70 - 79  = B
# 60 - 69  = C
# 50 - 59  = D
# Below 50 = F

print("\n" + "=" * 75)

print("SECTION 6: ACADEMIC GRADES")

print("=" * 75)


student_grades = {}


for student_name, average in student_averages.items():

    if average >= 90:

        grade = "A+"

    elif average >= 80:

        grade = "A"

    elif average >= 70:

        grade = "B"

    elif average >= 60:

        grade = "C"

    elif average >= 50:

        grade = "D"

    else:

        grade = "F"

    student_grades[student_name] = grade

    print(student_name, "Grade:", grade)


# =====================================================================
# SECTION 7: IDENTIFY PASS AND FAIL STUDENTS
# =====================================================================

# A student passes if their average is at least 50.
#
# We create two lists:
#
# passed_students
# failed_students
#
# Each student is classified using a condition.

print("\n" + "=" * 75)

print("SECTION 7: PASS AND FAIL ANALYSIS")

print("=" * 75)


passed_students = []

failed_students = []


for student_name, average in student_averages.items():

    if average >= 50:

        passed_students.append(student_name)

    else:

        failed_students.append(student_name)


print("Passed Students:", passed_students)

print("Failed Students:", failed_students)

print("Total Passed:", len(passed_students))

print("Total Failed:", len(failed_students))


# =====================================================================
# SECTION 8: FIND THE HIGHEST PERFORMING STUDENT
# =====================================================================

# We initially assume the first student
# has the highest average.
#
# We compare every other student against
# the highest average found so far.

print("\n" + "=" * 75)

print("SECTION 8: HIGHEST PERFORMER")

print("=" * 75)


highest_student = None

highest_average = float("-inf")


for student_name, average in student_averages.items():

    if average > highest_average:

        highest_average = average

        highest_student = student_name


print("Highest Performer:", highest_student)

print("Highest Average:", round(highest_average, 2))


# =====================================================================
# SECTION 9: FIND THE LOWEST PERFORMING STUDENT
# =====================================================================

# We use the same logic as the highest performer.
#
# This time, we look for the smallest average.

print("\n" + "=" * 75)

print("SECTION 9: LOWEST PERFORMER")

print("=" * 75)


lowest_student = None

lowest_average = float("inf")


for student_name, average in student_averages.items():

    if average < lowest_average:

        lowest_average = average

        lowest_student = student_name


print("Lowest Performer:", lowest_student)

print("Lowest Average:", round(lowest_average, 2))


# =====================================================================
# SECTION 10: CALCULATE CLASS AVERAGE
# =====================================================================

# Formula:
#
# Class Average =
# Sum of all student averages / Number of students
#
# We use a loop to calculate the total average.

print("\n" + "=" * 75)

print("SECTION 10: CLASS AVERAGE")

print("=" * 75)


class_total = 0


for average in student_averages.values():

    class_total += average


class_average = class_total / len(student_averages)


print("Class Average:", round(class_average, 2))


# =====================================================================
# SECTION 11: SUBJECT PERFORMANCE ANALYSIS
# =====================================================================

# We calculate the average mark for each subject.
#
# For each subject position, we collect
# that subject's marks from every student.
#
# The outer loop processes subjects.
# The inner loop processes students.

print("\n" + "=" * 75)

print("SECTION 11: SUBJECT PERFORMANCE")

print("=" * 75)


subject_averages = {}


for index, subject in enumerate(subjects):

    total = 0

    for student_name, marks in students.items():

        total += marks[index]

    average = total / len(students)

    subject_averages[subject] = average

    print(subject, "Average:", round(average, 2))


# =====================================================================
# SECTION 12: FIND THE BEST PERFORMING SUBJECT
# =====================================================================

# We compare the averages of all subjects.
#
# The subject with the highest average
# is considered the strongest subject.

print("\n" + "=" * 75)

print("SECTION 12: BEST PERFORMING SUBJECT")

print("=" * 75)


best_subject = None

best_subject_average = float("-inf")


for subject, average in subject_averages.items():

    if average > best_subject_average:

        best_subject_average = average

        best_subject = subject


print("Best Subject:", best_subject)

print("Subject Average:", round(best_subject_average, 2))


# =====================================================================
# SECTION 13: FIND THE WEAKEST PERFORMING SUBJECT
# =====================================================================

# We identify the subject with the lowest average.

print("\n" + "=" * 75)

print("SECTION 13: WEAKEST PERFORMING SUBJECT")

print("=" * 75)


weakest_subject = None

weakest_subject_average = float("inf")


for subject, average in subject_averages.items():

    if average < weakest_subject_average:

        weakest_subject_average = average

        weakest_subject = subject


print("Weakest Subject:", weakest_subject)

print("Subject Average:", round(weakest_subject_average, 2))


# =====================================================================
# SECTION 14: COUNT EVEN AND ODD MARKS
# =====================================================================

# Even numbers have a remainder of zero
# when divided by two.
#
# Odd numbers have a non-zero remainder.
#
# We process every mark in the dataset.

print("\n" + "=" * 75)

print("SECTION 14: EVEN AND ODD MARKS")

print("=" * 75)


even_count = 0

odd_count = 0


for marks in students.values():

    for mark in marks:

        if mark % 2 == 0:

            even_count += 1

        else:

            odd_count += 1


print("Even Marks:", even_count)

print("Odd Marks:", odd_count)


# =====================================================================
# SECTION 15: CALCULATE TOTAL NUMBER OF EXAMINATION MARKS
# =====================================================================

# We calculate the total marks obtained
# by all students across all subjects.

print("\n" + "=" * 75)

print("SECTION 15: TOTAL EXAMINATION MARKS")

print("=" * 75)


overall_total = 0

for marks in students.values():

    for mark in marks:

        overall_total += mark


print("Total Examination Marks:", overall_total)


# =====================================================================
# SECTION 16: CALCULATE PASS PERCENTAGE
# =====================================================================

# Formula:
#
# Pass Percentage =
# (Number of Passed Students / Total Students) * 100
#
# We use len() to count students.

print("\n" + "=" * 75)

print("SECTION 16: PASS PERCENTAGE")

print("=" * 75)


total_students = len(students)

pass_percentage = (len(passed_students) / total_students) * 100

print("Total Students:", total_students)

print("Passed Students:", len(passed_students))

print("Pass Percentage:", round(pass_percentage, 2), "%")


# =====================================================================
# SECTION 17: GENERATE INDIVIDUAL PERFORMANCE REPORTS
# =====================================================================

# We combine the information collected earlier.
#
# Each student receives a complete performance report.

print("\n" + "=" * 75)

print("SECTION 17: INDIVIDUAL PERFORMANCE REPORTS")

print("=" * 75)


for student_name in students:

    print("\nStudent Name:", student_name)

    print("Total Marks:", student_totals[student_name])

    print("Average:", round(student_averages[student_name], 2))

    print("Grade:", student_grades[student_name])

    if student_averages[student_name] >= 50:

        print("Result: PASS")

    else:

        print("Result: FAIL")


# =====================================================================
# SECTION 18: DISPLAY SUBJECT-WISE STUDENT PERFORMANCE
# =====================================================================

# We display each student's marks for every subject.
#
# enumerate() gives the index and subject.
#
# The index helps us access the correct mark
# from each student's marks list.

print("\n" + "=" * 75)

print("SECTION 18: SUBJECT-WISE PERFORMANCE")

print("=" * 75)


for student_name, marks in students.items():

    print("\nStudent:", student_name)

    for index, subject in enumerate(subjects):

        print(subject, ":", marks[index])


# =====================================================================
# SECTION 19: CLASS PERFORMANCE CLASSIFICATION
# =====================================================================

# We classify the entire class using its average.
#
# This is a simple rule-based evaluation.

print("\n" + "=" * 75)

print("SECTION 19: CLASS PERFORMANCE")

print("=" * 75)


if class_average >= 85:

    print("Class Performance: EXCELLENT")

elif class_average >= 75:

    print("Class Performance: VERY GOOD")

elif class_average >= 65:

    print("Class Performance: GOOD")

elif class_average >= 50:

    print("Class Performance: SATISFACTORY")

else:

    print("Class Performance: NEEDS IMPROVEMENT")


# =====================================================================
# SECTION 20: CREATE A REUSABLE ANALYSIS FUNCTION
# =====================================================================

# Functions allow us to reuse code.
#
# This function receives a list of marks
# and calculates its total and average.
#
# We use a loop inside the function.

print("\n" + "=" * 75)

print("SECTION 20: REUSABLE ANALYSIS FUNCTION")

print("=" * 75)


def analyze_marks(marks):

    total = 0

    for mark in marks:

        total += mark

    average = total / len(marks)

    return total, average


# Test the function with Ali's marks.

ali_total, ali_average = analyze_marks(students["Ali"])


print("Ali's Total:", ali_total)

print("Ali's Average:", round(ali_average, 2))


# =====================================================================
# SECTION 21: BASIC AI PREDICTION ERROR ANALYSIS
# =====================================================================

# This is an introductory Machine Learning example.
#
# Actual values represent real outcomes.
# Predicted values represent model predictions.
#
# MAE = Mean Absolute Error
#
# Formula:
#
# MAE = SUM(|Actual - Predicted|) / n
#
# We calculate each prediction error using a loop.

print("\n" + "=" * 75)

print("SECTION 21: AI PREDICTION ERROR ANALYSIS")

print("=" * 75)


actual_values = [100, 200, 300, 400, 500]

predicted_values = [90, 210, 280, 390, 520]


total_error = 0


for actual, predicted in zip(actual_values, predicted_values):

    error = actual - predicted

    absolute_error = abs(error)

    total_error += absolute_error

    print("Actual:", actual)

    print("Predicted:", predicted)

    print("Absolute Error:", absolute_error)


mae = total_error / len(actual_values)


print("\nMean Absolute Error:", mae)


# =====================================================================
# SECTION 22: FINAL MANAGEMENT REPORT
# =====================================================================

# We summarize the most important results
# from our analysis.
#
# This section combines information
# calculated throughout the project.

print("\n" + "=" * 75)

print("             FINAL MANAGEMENT REPORT")

print("=" * 75)


print("Total Students:", total_students)

print("Total Subjects:", len(subjects))

print("Overall Class Average:", round(class_average, 2))

print("Pass Percentage:", round(pass_percentage, 2), "%")

print("Highest Performer:", highest_student)

print("Lowest Performer:", lowest_student)

print("Best Performing Subject:", best_subject)

print("Weakest Performing Subject:", weakest_subject)

print("Passed Students:", len(passed_students))

print("Failed Students:", len(failed_students))

print("Even Marks:", even_count)

print("Odd Marks:", odd_count)

print("Total Examination Marks:", overall_total)

print("AI Model Mean Absolute Error:", mae)


# =====================================================================
# SECTION 23: PROJECT CONCLUSION
# =====================================================================

print("\n" + "=" * 75)

print("PROJECT COMPLETED SUCCESSFULLY!")

print("=" * 75)

print("We successfully processed the student dataset.")

print("We calculated individual student performance.")

print("We evaluated academic grades.")

print("We analyzed subject performance.")

print("We calculated statistical measurements.")

print("We introduced a basic AI prediction error metric.")

print("\nTHANK YOU FOR USING THE SYSTEM!")

print("=" * 75)


# =====================================================================
# END OF DAY 012 - CHALLENGE.PY
# =====================================================================
