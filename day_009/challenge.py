
# =================================================================
# DAY 009 - PYTHON STRING METHODS
# CHALLENGE PROJECT
#
# PROJECT: STUDENT INFORMATION & TEXT PROCESSING SYSTEM
#
# Bachelor's in Artificial Intelligence
# 90-Day Python Programming Journey
#
# OBJECTIVE:
# Build a student information system using Python string methods.
#
# CONCEPTS USED:
# 1. String Methods
# 2. String Cleaning
# 3. String Validation
# 4. User Input
# 5. Functions
# 6. Loops
# 7. Conditional Statements
# 8. Lists
# 9. Dictionaries
# 10. Exception Handling
# 11. F-Strings
#
# =================================================================


# =================================================================
# SECTION 1: PROJECT INTRODUCTION
# =================================================================

print("\n" + "=" * 70)

print("       STUDENT INFORMATION & TEXT PROCESSING SYSTEM")

print("=" * 70)

print("Welcome to our Student Management Application!")

print("This program collects, cleans and processes student information.")

print("=" * 70)


# =================================================================
# SECTION 2: CREATE A FUNCTION TO CLEAN TEXT
# =================================================================

# Functions allow us to reuse code.
#
# This function:
# 1. Removes unnecessary spaces.
# 2. Converts text into title case.
#
# strip() removes spaces from both ends.
# title() capitalizes the beginning of each word.

def clean_name(name):

    cleaned_name = name.strip()

    formatted_name = cleaned_name.title()

    return formatted_name


# =================================================================
# SECTION 3: CREATE A FUNCTION TO VALIDATE EMAILS
# =================================================================

# This function performs BASIC email-format checks.
#
# It does not guarantee that an email address exists.
#
# Checks:
# 1. The email must contain exactly one @.
# 2. The username must not be empty.
# 3. The domain must contain a dot.
# 4. The domain must not begin or end with a dot.
# 5. The email must not contain spaces.

def validate_email(email):

    # Convert the email into lowercase.
    # Remove unnecessary surrounding spaces.

    email = email.strip().lower()

    # An email should not contain whitespace.

    if any(character.isspace() for character in email):

        return False

    # There should be exactly one @ symbol.

    if email.count("@") != 1:

        return False

    # Split the email into username and domain.

    username, domain = email.split("@")

    # Username and domain must not be empty.

    if not username or not domain:

        return False

    # The domain should contain a dot.

    if "." not in domain:

        return False

    # The domain should not start or end with a dot.

    if domain.startswith(".") or domain.endswith("."):

        return False

    # The domain should not contain consecutive dots.

    if ".." in domain:

        return False

    return True


# =================================================================
# SECTION 4: COLLECT STUDENT NAME
# =================================================================

print("\nSTUDENT INFORMATION")

print("-" * 70)

# Keep requesting the name until the user enters valid text.

while True:

    raw_name = input("Enter your full name: ")

    # Clean unnecessary spaces.

    raw_name = raw_name.strip()

    # Check whether the user entered something.

    if raw_name == "":

        print("Error: Name cannot be empty.")

        continue

    # A basic name check:
    # Every character must be a letter or whitespace.

    if not all(character.isalpha() or character.isspace()
               for character in raw_name):

        print("Error: Name should contain letters and spaces only.")

        continue

    # Format the student's name.

    student_name = clean_name(raw_name)

    break


# =================================================================
# SECTION 5: COLLECT AND VALIDATE EMAIL
# =================================================================

# Continue asking until a basic valid email format is provided.

while True:

    raw_email = input("Enter your email address: ")

    # Remove surrounding spaces and convert to lowercase.

    student_email = raw_email.strip().lower()

    # Call the email validation function.

    if validate_email(student_email):

        print("Email format accepted.")

        break

    else:

        print("Invalid email format. Please try again.")


# =================================================================
# SECTION 6: COLLECT COUNTRY
# =================================================================

while True:

    raw_country = input("Enter your country: ")

    # Remove spaces.

    raw_country = raw_country.strip()

    # Validate that the field is not empty.

    if raw_country == "":

        print("Country cannot be empty.")

        continue

    # Format country using title case.

    student_country = raw_country.title()

    break


# =================================================================
# SECTION 7: COLLECT UNIVERSITY
# =================================================================

while True:

    raw_university = input("Enter your university: ")

    raw_university = raw_university.strip()

    if raw_university == "":

        print("University cannot be empty.")

        continue

    # Format the university name.

    student_university = raw_university.title()

    break


# =================================================================
# SECTION 8: COLLECT COURSE
# =================================================================

while True:

    raw_course = input("Enter your course: ")

    raw_course = raw_course.strip()

    if raw_course == "":

        print("Course cannot be empty.")

        continue

    # Format the course.

    student_course = raw_course.title()

    break


# =================================================================
# SECTION 9: COLLECT STUDENT AGE
# =================================================================

# input() always returns a string.
#
# int() converts numeric text into an integer.
#
# try and except handle invalid numeric input.

while True:

    try:

        student_age = int(input("Enter your age: "))

        # Check whether the age is reasonable.

        if 1 <= student_age <= 120:

            break

        else:

            print("Please enter an age between 1 and 120.")

    except ValueError:

        print("Invalid input. Please enter a whole number.")


# =================================================================
# SECTION 10: GENERATE STUDENT ID
# =================================================================

# We use zfill() to add zeros to the beginning of an ID.
#
# Example:
# "25".zfill(6) becomes "000025".

student_number = "9"

student_id = student_number.zfill(6)

print("\nStudent ID Generated:", student_id)


# =================================================================
# SECTION 11: STORE INFORMATION IN A DICTIONARY
# =================================================================

# A dictionary stores information using key-value pairs.
#
# Each key identifies a particular piece of information.
#
# This makes student information easy to organize.

student_information = {

    "Student ID": student_id,

    "Full Name": student_name,

    "Email": student_email,

    "Age": student_age,

    "Country": student_country,

    "University": student_university,

    "Course": student_course

}


# =================================================================
# SECTION 12: DISPLAY STUDENT REPORT
# =================================================================

print("\n" + "=" * 70)

print("                 STUDENT PROFILE REPORT")

print("=" * 70)

# Loop through dictionary items.
#
# items() returns the keys and their corresponding values.

for key, value in student_information.items():

    print(f"{key}: {value}")

print("=" * 70)


# =================================================================
# SECTION 13: TEXT ANALYSIS OF STUDENT NAME
# =================================================================

# We will analyze the student's name.
#
# String methods allow us to extract useful information.

print("\nSTUDENT NAME ANALYSIS")

print("-" * 70)

# Calculate the number of characters.

name_characters = len(student_name)

# Split the name into individual words.

name_words = student_name.split()

# Count the number of words.

name_word_count = len(name_words)

# Identify the first and last name.

first_name = name_words[0]

last_name = name_words[-1]

# Find the longest name component.

longest_name = max(name_words, key=len)

# Find the shortest name component.

shortest_name = min(name_words, key=len)

print("Full Name:", student_name)

print("Total Characters:", name_characters)

print("Total Name Parts:", name_word_count)

print("First Name:", first_name)

print("Last Name:", last_name)

print("Longest Name Part:", longest_name)

print("Shortest Name Part:", shortest_name)


# =================================================================
# SECTION 14: SEARCH STUDENT INFORMATION
# =================================================================

print("\n" + "=" * 70)

print("              STUDENT INFORMATION SEARCH")

print("=" * 70)

# Ask the user what they want to search for.

search_query = input("Enter information to search: ")

# Clean the search query.

search_query = search_query.strip().lower()

# Convert the student dictionary into searchable text.
#
# This allows us to check whether the query appears
# in any of the stored student information.

search_found = False

for key, value in student_information.items():

    # Convert each value into a string before searching.

    searchable_value = str(value).lower()

    if search_query and search_query in searchable_value:

        print(f"Match found in {key}: {value}")

        search_found = True

if not search_found:

    print("No matching student information was found.")


# =================================================================
# SECTION 15: EMAIL DOMAIN ANALYSIS
# =================================================================

print("\n" + "=" * 70)

print("                 EMAIL DOMAIN ANALYSIS")

print("=" * 70)

# partition() separates the email into three parts:
#
# 1. Username
# 2. @ symbol
# 3. Domain

email_parts = student_email.partition("@")

email_username = email_parts[0]

email_separator = email_parts[1]

email_domain = email_parts[2]

print("Email Username:", email_username)

print("Separator:", email_separator)

print("Email Domain:", email_domain)

# Check the domain ending.

if email_domain.endswith(".com"):

    print("Domain Ending: Commercial domain (.com)")

elif email_domain.endswith(".org"):

    print("Domain Ending: Organization domain (.org)")

elif email_domain.endswith(".edu"):

    print("Domain Ending: Education-related ending (.edu)")

else:

    print("Domain Ending:", email_domain.split(".")[-1])


# =================================================================
# SECTION 16: GENERATE FORMATTED STUDENT ID
# =================================================================

print("\n" + "=" * 70)

print("                 STUDENT ID FORMATTING")

print("=" * 70)

# Demonstrate zfill() with a different number.

registration_number = "125"

formatted_registration = registration_number.zfill(8)

print("Original Registration Number:", registration_number)

print("Formatted Registration Number:", formatted_registration)


# =================================================================
# SECTION 17: DISPLAY STUDENT NAME FORMATS
# =================================================================

print("\n" + "=" * 70)

print("                 NAME FORMATTING")

print("=" * 70)

# Demonstrate different formatting methods.

print("Original:", student_name)

print("Uppercase:", student_name.upper())

print("Lowercase:", student_name.lower())

print("Title Case:", student_name.title())

print("Swap Case:", student_name.swapcase())


# =================================================================
# SECTION 18: FINAL STUDENT SUMMARY
# =================================================================

print("\n" + "=" * 70)

print("                 FINAL STUDENT SUMMARY")

print("=" * 70)

# Create a list containing the student's information.

summary = [

    student_name,

    student_email,

    student_country,

    student_university,

    student_course

]

# Count how many information fields are stored.

total_fields = len(summary)

print("Student:", student_name)

print("Student ID:", student_id)

print("Age:", student_age)

print("University:", student_university)

print("Course:", student_course)

print("Total Information Fields:", total_fields)


# =================================================================
# SECTION 19: FINAL PROJECT MESSAGE
# =================================================================

print("\n" + "=" * 70)

print("     STUDENT INFORMATION SYSTEM COMPLETED SUCCESSFULLY")

print("=" * 70)

print("Student Data Collection: Completed")

print("Name Cleaning: Completed")

print("Email Validation: Completed")

print("Country Formatting: Completed")

print("University Formatting: Completed")

print("Course Formatting: Completed")

print("Student ID Generation: Completed")

print("Dictionary Storage: Completed")

print("Student Name Analysis: Completed")

print("Information Searching: Completed")

print("Email Domain Analysis: Completed")

print("Final Report Generation: Completed")

print("\nCONGRATULATIONS!")

print("You have successfully completed the Day 009 challenge.")

print("=" * 70)


# =================================================================
# END OF DAY 009 - CHALLENGE.PY
# =================================================================
