
# ================================================================
# DAY 008 - PYTHON STRINGS
# CHALLENGE PROJECT: AI TEXT ANALYZER
#
# Bachelor's in Artificial Intelligence
# 90-Day Python Programming Journey
#
# PROJECT OBJECTIVE:
# Develop a text analyzer using Python string operations.
#
# CONCEPTS USED:
# 1. Variables
# 2. Strings
# 3. String Methods
# 4. Indexing and Slicing
# 5. String Cleaning
# 6. String Searching
# 7. String Counting
# 8. Lists
# 9. Loops
# 10. Conditional Statements
# 11. Functions
# 12. Exception Handling
#
# ================================================================


# ================================================================
# SECTION 1: PROJECT INTRODUCTION
# ================================================================

print("\n" + "=" * 70)

print("                 AI TEXT ANALYZER")

print("=" * 70)

print("Welcome to the Python AI Text Analyzer!")

print("This application analyzes text and extracts useful information.")

print("=" * 70)


# ================================================================
# SECTION 2: COLLECT USER INPUT
# ================================================================

# input() collects information from the user.
#
# strip() removes unnecessary spaces from the beginning
# and end of the input.
#
# We will check whether the user entered any text.

while True:

    user_text = input("\nEnter your text: ").strip()

    if user_text:

        break

    else:

        print("Error: Please enter some text.")


# ================================================================
# SECTION 3: CLEAN THE TEXT
# ================================================================

# Text cleaning is an important concept in NLP.
#
# NLP means Natural Language Processing.
#
# It allows computers to process and analyze human language.
#
# Here we perform basic text cleaning.

# Convert all text into lowercase.

clean_text = user_text.lower()

# Remove unnecessary spaces around the text.

clean_text = clean_text.strip()

# Display the cleaned text.

print("\n" + "=" * 70)

print("TEXT CLEANING")

print("=" * 70)

print("Original Text:", user_text)

print("Cleaned Text:", clean_text)


# ================================================================
# SECTION 4: CREATE A FUNCTION FOR TEXT ANALYSIS
# ================================================================

# A function is a reusable block of code.
#
# def is used to define a function.
#
# We create functions to organize our application.
#
# This function will perform the main analysis.

def analyze_text(text):

    # ------------------------------------------------------------
    # 4.1 COUNT CHARACTERS
    # ------------------------------------------------------------

    # len() counts the number of characters.
    #
    # Spaces and punctuation are included.

    total_characters = len(text)

    # Remove spaces to calculate characters without spaces.

    characters_without_spaces = len(text.replace(" ", ""))


    # ------------------------------------------------------------
    # 4.2 COUNT WORDS
    # ------------------------------------------------------------

    # split() separates text into individual words.
    #
    # It returns a list.

    words = text.split()

    total_words = len(words)


    # ------------------------------------------------------------
    # 4.3 COUNT SENTENCES
    # ------------------------------------------------------------

    # We count common sentence-ending punctuation marks.
    #
    # This is a basic approximation, not a complete
    # linguistic sentence detection system.

    sentence_count = 0

    for character in text:

        if character in ".!?":

            sentence_count += 1


    # ------------------------------------------------------------
    # 4.4 FIND FIRST AND LAST WORD
    # ------------------------------------------------------------

    # Check whether the words list contains anything.

    if total_words > 0:

        first_word = words[0]

        last_word = words[-1]

    else:

        first_word = "None"

        last_word = "None"


    # ------------------------------------------------------------
    # 4.5 FIND LONGEST AND SHORTEST WORD
    # ------------------------------------------------------------

    # max() with key=len finds the longest word.
    #
    # min() with key=len finds the shortest word.

    if total_words > 0:

        longest_word = max(words, key=len)

        shortest_word = min(words, key=len)

        longest_word_length = len(longest_word)

        shortest_word_length = len(shortest_word)

    else:

        longest_word = "None"

        shortest_word = "None"

        longest_word_length = 0

        shortest_word_length = 0


    # ------------------------------------------------------------
    # 4.6 COUNT VOWELS AND CONSONANTS
    # ------------------------------------------------------------

    # Vowels are a, e, i, o and u.
    #
    # We check every character in the text.
    #
    # Alphabetic characters that are not vowels
    # are counted as consonants.

    vowels = "aeiou"

    vowel_count = 0

    consonant_count = 0

    for character in text:

        if character.isalpha():

            if character in vowels:

                vowel_count += 1

            else:

                consonant_count += 1


    # ------------------------------------------------------------
    # 4.7 COUNT DIGITS
    # ------------------------------------------------------------

    # isdigit() checks whether a character is a digit.

    digit_count = 0

    for character in text:

        if character.isdigit():

            digit_count += 1


    # ------------------------------------------------------------
    # 4.8 COUNT SPECIAL CHARACTERS
    # ------------------------------------------------------------

    # A special character here means any character
    # that is not a letter, digit or whitespace.

    special_character_count = 0

    for character in text:

        if not character.isalnum() and not character.isspace():

            special_character_count += 1


    # ------------------------------------------------------------
    # 4.9 REVERSE THE TEXT
    # ------------------------------------------------------------

    # [::-1] reverses a string.

    reversed_text = text[::-1]


    # ------------------------------------------------------------
    # 4.10 RETURN RESULTS
    # ------------------------------------------------------------

    # return sends calculated results back to the caller.
    #
    # A dictionary stores information using key-value pairs.

    results = {

        "characters": total_characters,

        "characters_without_spaces": characters_without_spaces,

        "words": total_words,

        "sentences": sentence_count,

        "first_word": first_word,

        "last_word": last_word,

        "longest_word": longest_word,

        "longest_word_length": longest_word_length,

        "shortest_word": shortest_word,

        "shortest_word_length": shortest_word_length,

        "vowels": vowel_count,

        "consonants": consonant_count,

        "digits": digit_count,

        "special_characters": special_character_count,

        "reversed_text": reversed_text

    }

    return results


# ================================================================
# SECTION 5: RUN THE ANALYSIS
# ================================================================

# Call the function and provide cleaned text.

analysis_results = analyze_text(clean_text)


# ================================================================
# SECTION 6: DISPLAY THE ANALYSIS REPORT
# ================================================================

print("\n" + "=" * 70)

print("                 TEXT ANALYSIS REPORT")

print("=" * 70)

# Display character information.

print("\nCHARACTER ANALYSIS")

print("-" * 70)

print("Total Characters:",
      analysis_results["characters"])

print("Characters Without Spaces:",
      analysis_results["characters_without_spaces"])

print("Vowels:",
      analysis_results["vowels"])

print("Consonants:",
      analysis_results["consonants"])

print("Digits:",
      analysis_results["digits"])

print("Special Characters:",
      analysis_results["special_characters"])


# Display word information.

print("\nWORD ANALYSIS")

print("-" * 70)

print("Total Words:",
      analysis_results["words"])

print("First Word:",
      analysis_results["first_word"])

print("Last Word:",
      analysis_results["last_word"])

print("Longest Word:",
      analysis_results["longest_word"])

print("Longest Word Length:",
      analysis_results["longest_word_length"])

print("Shortest Word:",
      analysis_results["shortest_word"])

print("Shortest Word Length:",
      analysis_results["shortest_word_length"])


# Display sentence information.

print("\nSENTENCE ANALYSIS")

print("-" * 70)

print("Total Sentences:",
      analysis_results["sentences"])


# Display reversed text.

print("\nREVERSED TEXT")

print("-" * 70)

print(analysis_results["reversed_text"])


# ================================================================
# SECTION 7: SEARCH FOR A WORD
# ================================================================

print("\n" + "=" * 70)

print("                 WORD SEARCH")

print("=" * 70)

# Ask the user which word they want to search for.

search_word = input("\nEnter a word to search for: ").strip().lower()

# Check that the user provided a search term.

if search_word:

    # Split the cleaned text into words.
    #
    # This search is case-insensitive.
    # It matches complete whitespace-separated words.

    words = clean_text.split()

    # Remove common punctuation from word boundaries.

    cleaned_words = [
        word.strip(".,!?;:\"'()[]{}")
        for word in words
    ]

    # Count exact matches.

    occurrences = cleaned_words.count(search_word)

    if occurrences > 0:

        print(f"\n'{search_word}' was found!")

        print("Occurrences:", occurrences)

    else:

        print(f"\n'{search_word}' was not found.")

else:

    print("No search word was entered.")


# ================================================================
# SECTION 8: DISPLAY WORDS INDIVIDUALLY
# ================================================================

print("\n" + "=" * 70)

print("                 INDIVIDUAL WORDS")

print("=" * 70)

# Enumerate provides both the position and the word.

words = clean_text.split()

for position, word in enumerate(words, start=1):

    print(f"Word {position}: {word}")


# ================================================================
# SECTION 9: TEXT SUMMARY
# ================================================================

print("\n" + "=" * 70)

print("                 FINAL TEXT SUMMARY")

print("=" * 70)

# Display a short summary based on word count.

total_words = analysis_results["words"]

if total_words < 10:

    print("Text Category: Short Text")

elif total_words < 50:

    print("Text Category: Medium Text")

else:

    print("Text Category: Long Text")


# Display the total number of words.

print(f"Your text contains {total_words} words.")

# Display the total number of characters.

print(
    f"Your text contains "
    f"{analysis_results['characters']} characters."
)


# ================================================================
# SECTION 10: FINAL PROJECT MESSAGE
# ================================================================

print("\n" + "=" * 70)

print("             AI TEXT ANALYZER COMPLETED")

print("=" * 70)

print("Text Collection: Completed")

print("Text Cleaning: Completed")

print("Character Analysis: Completed")

print("Word Analysis: Completed")

print("Sentence Analysis: Completed")

print("Vowel and Consonant Analysis: Completed")

print("Digit Analysis: Completed")

print("Special Character Analysis: Completed")

print("Word Searching: Completed")

print("Text Reversal: Completed")

print("Final Report: Completed")

print("\nCONGRATULATIONS!")

print("You successfully built your first Python Text Analyzer.")

print("=" * 70)


# ================================================================
# END OF DAY 008 - CHALLENGE.PY
# ================================================================
