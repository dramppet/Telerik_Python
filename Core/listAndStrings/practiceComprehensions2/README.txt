                                      Tuple

Task 1 - Tuple Unpacking
Parse a list of employee records like [("John", "Doe", "Manager"), ("Alice", "Smith", "Engineer")] and output on console full names with job titles in the following format.

employees = [("John", "Doe", "Manager"), ("Alice", "Smith", "Engineer")]
Output:

John Doe - Manager
Alice Smith - Engineer

Task 2 - Swapping Variables with Tuples
Swap the values of two variables without a helper variable.

Task 3 - Immutable Sorting
Given a list of tuples containing (name, age), sort the list by age, then by age.

Example:

data = [("Alice", 25), ("Bob", 20), ("Alice", 20), ("Charlie", 19)]
Output:

[('Charlie', 19), ('Alice', 20), ('Bob', 20), ('Alice', 25)]

Task 4 - Top N Elements by Value
You have a list of (item, count) tuples. Find the top 3 items with the highest counts.

data = [("apple", 10), ("banana", 30), ("cherry", 20), ("strawberry", 50)]
Output:

[("strawberry", 50), ("banana", 30), ("cherry", 20)]

Task 5 - Student Scores
Given students' test scores in the form of tuples like ("Alice", 89), calculate the average score.

scores = [("Alice", 80), ("Bob", 90),  ("Tod", 100)]
Output:

90.0

                                Dictionaries

Task 1 - Character Frequency Counter
Count the frequency of each character in a given string.

s = "hello"
Output:

{'h': 1, 'e': 1, 'l': 2, 'o': 1}

Task 2 - Word Frequency in Paragraph
Tokenize a paragraph and count how many times each word appears.

text = "Hello, World! Hello, Python, too!"
Output:

{'hello': 2, 'world': 1, 'python': 1, 'too': 1}

Task 3 - Inventory System
Track inventory where keys are product names and values are quantities. Update inventory as items are sold.

inventory = {"apple": 5, "banana": 3}
sales = ["apple", "banana", "apple", "apricot"]
Output:

Product not available
{'apple': 3, 'banana': 2}

Task 4 - Nested Dictionaries
Given student data, compute each student's average.

data = {
  "Alice": {"math": 90, "english": 85},
  "Bob": {"math": 78, "english": 88}}
Output:

{'Alice': 85.0, 'Bob': 77.5}

Task 5 - Lookup by Value
Given a dictionary of country codes, find which key maps to a given value.

d = {"us": "USA", "bg": "Bulgaria", "ca": "Canada"}
target_value = "Bulgaria"
Output:

Target value 'Bulgaria' exists: True

Task 6 - Merge Two Dictionaries
Combine two dictionaries. If a key exists in both, sum their values.

a = {"apple": 3, "banana": 1}
b = {"apple": 2, "cherry": 4}
Output:

{'apple': 5, 'banana': 1, 'cherry': 4}

Task 7 - Sort Dictionary by Value
Sort a dictionary of scores by value in descending order.

d = {"apple": 5, "banana": 2}
Output:

{'apple': 5, 'banana': 2}

                                          Dictionary Comprehensions

Task 1 - Square Numbers
Create a dictionary mapping numbers 1–10 to their squares.

Output:

{1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100}

Task 2 - Filter Even Numbers
From a list of numbers, create a dictionary of number → square for only even numbers.

lst = [1, 2, 3, 4, 5]
Output:

{2: 4, 4: 16}

Task 3 - Invert a Dictionary
Invert a dictionary: {a: 1, b: 2} → {1: a, 2: b}.

d = {"a": 1, "b": 2}
Output:

{1: a, 2: b}

Task 4 - Conditional Dictionary
Given a dictionary of items with prices, create a new one with only items costing over $20.

prices = {"pen": 10, "book": 25, "bag": 50}
Output:

{'book': 25, 'bag': 50}

Task 5 - Word Length Mapping
Given a list of words, map each word to its length.

words = ["hello", "world"]
Output:

{'hello': 5, 'world': 5}

Task 6 - Grade Categorization
From a dictionary of names to grades, create a dictionary mapping names to "Pass"/"Fail" based on a threshold.

grades = {"Alice": 85, "Bob": 55}
Output:

{'Alice': 'Pass', 'Bob': 'Fail'}

Task 7 - Character Count from String
Create a dictionary where each character in a string maps to its frequency.

s = "banana"
Output:

{'b': 1, 'n': 2, 'a': 3}
