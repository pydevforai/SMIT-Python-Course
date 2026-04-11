#SECTION C
# Functions
# Function design, scope, arguments, advanced function features
# C1  Function Basics & Return Values
# Write the following standalone utility functions, each with a docstring:
# is_prime(n) — returns True if n is prime, False otherwise
# celsius_to_all(c) — returns a tuple of (fahrenheit, kelvin)
# count_vowels(text) — returns the count of vowels in a string
# power(base, exp=2) — returns base raised to exp. Default exponent is 2.
# Call each function with at least one test case and print the result.

#Part1
def is_prime(n):
    if n < 2:
        return False
    # Check for factors from 2 to the square root of n
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

print(is_prime(3))

#Part2
def celsius_to_all(c):
    F = (c * 1.8) + 32
    K = c + 273.15
    return f"({F}°F, {K}°K)"

result = celsius_to_all(25)
print(result)

#Part3
def count_vowels(text):
    count = 0
    for char in text.lower():
        if char in "aeiou":
            count += 1
    return f"Count of vowels: {count}"

result = count_vowels("learning")
print(result)

#Part4
def power(base, exp=2):
    return base ** exp

print(power(5))
print(power(2, 3))    

#C2  Using *args and **kwargs
# Write a function generate_report(**student_info) that accepts keyword arguments and prints a formatted report card. It must:
# Accept fields: name, roll_no, marks (a list), subjects (a list)
# Compute the average of marks internally
# Print each field on its own line
# Print the grade based on average (use your B1 grade logic)

# Also write total_marks(*args) that accepts any number of integers and returns their sum.

# generate_report(
#     name="Sana Khan",
#     roll_no="CS-101",
#     subjects=["Math", "Physics", "Python"],
#     marks=[85, 78, 92]
# )

def generate_report(**student_info):
    name = student_info["name"]
    roll_no = student_info["roll_no"]
    subjects = student_info["subjects"]
    marks = student_info["marks"]

    average = sum(marks)/len(subjects)
    if average > 70:
        grade = "A"
    elif average >= 60 and average < 70:
        grade = "B"
    elif average >= 50 and average < 60:
        grade = "C"
    else:
        grade = "Fail"

    return f"Name = '{name}'\nRoll_number = '{roll_no}'\nSubjects = {subjects}\nMarks = {marks}\nAverage: {average}\nGrade: {grade}"

result = generate_report(name="Sana Khan", roll_no="CS-101", subjects=["Math", "Physics","Python"],marks=[85, 78, 92]) 
print(result) 

#Part2
def total_marks(*args):
    total = sum(args)
    return f"Total sum: {total}" 

result = total_marks(32, 54, 65, 76)
print(result)   

#C3  Lambda, map, filter, sorted
# Given this list (do not modify it):
# students = [
#     {"name": "Ali",   "marks": 55, "city": "Karachi"},
#     {"name": "Sara",  "marks": 90, "city": "Lahore"},
#     {"name": "Umar",  "marks": 45, "city": "Karachi"},
#     {"name": "Hina",  "marks": 78, "city": "Islamabad"},
#     {"name": "Bilal", "marks": 63, "city": "Lahore"},
# ]

# Using lambda, map, filter, and sorted — NO for loops:
# Create a list of just names using map
# Filter only students who passed (marks >= 50) using filter
# Sort students by marks descending using sorted
# Use map to create list of strings like "Ali - 55 marks"
# Use filter to get only students from Karachi

# Print the result of each operation.

students = [
    {"name": "Ali",   "marks": 55, "city": "Karachi"},
    {"name": "Sara",  "marks": 90, "city": "Lahore"},
    {"name": "Umar",  "marks": 45, "city": "Karachi"},
    {"name": "Hina",  "marks": 78, "city": "Islamabad"},
    {"name": "Bilal", "marks": 63, "city": "Lahore"},
]

# 1. List of just names using map
names = list(map(lambda student: student["name"], students))

# 2. Students who passed using filter
passed_students = list(filter(lambda student: student["marks"] >= 50, students))

# 3. Sort students by marks descending using sorted
sorted_students = sorted(students, key=lambda student: student["marks"], reverse=True)

# 4. List of strings like "Ali - 55 marks" using map
student_strings = list(map(lambda student: f'{student["name"]} - {student["marks"]} marks', students))

# 5. Students from Karachi using filter
karachi_students = list(filter(lambda student: student["city"] == "Karachi", students))

print("Names:", names)
print("Passed Students:", passed_students)
print("Sorted by Marks Desc:", sorted_students)
print("Student Strings:", student_strings)
print("Karachi Students:", karachi_students)

#C4  Recursion
# Part 1 — Fibonacci (2 marks):
# Write fibonacci(n) recursively. Print the first 10 Fibonacci numbers.

# Part 2 — Factorial (2 marks):
# Write factorial(n) recursively. Handle n=0 and negative input gracefully.

# Part 3 — Flatten a nested list (2 marks):
# Write flatten(lst) that takes a deeply nested list and returns a flat list using recursion.
# flatten([1, [2, [3, 4], 5], [6, 7]])
# Expected: [1, 2, 3, 4, 5, 6, 7]

# Part 1 - Fibonacci
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

print("First 10 Fibonacci numbers:")
for i in range(10):
    print(fibonacci(i), end=" ")

print()


# Part 2 - Factorial
def factorial(n):
    if n < 0:
        return "Factorial is not defined for negative numbers"
    elif n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

print("\nFactorial of 5:", factorial(5))
print("Factorial of 0:", factorial(0))
print("Factorial of -3:", factorial(-3))


# Part 3 - Flatten a nested list
def flatten(lst):
    result = []

    for item in lst:
        if isinstance(item, list):
            result.extend(flatten(item))
        else:
            result.append(item)

    return result

nested_list = [1, [2, [3, 4], 5], [6, 7]]
print("\nFlatten list:", flatten(nested_list))
