#SECTION B
# Control Flow & Loops
# Conditional logic and loop constructs 
# marks

# B1  Grade Calculator with Nested Conditions
# Write a program that takes a student's marks (0-100) and assigns a grade and remark:
# 90-100: A+  Outstanding  |  80-89: A  Excellent  |  70-79: B  Good
# 60-69: C  Average  |  50-59: D  Pass  |  Below 50: F  Fail

# Additionally:
# If marks are below 0 or above 100, print an error and exit
# Print the grade and remark
# If failed, print: "Minimum marks to pass: 50. You need X more marks."

marks = int(input("Enter your marks: "))

if marks >= 90 and marks <= 100:
    grade = "A+"
    remark = "Outstanding"

elif marks >= 80 and marks < 90:
    grade = "A"
    remark = "Excellent"

elif marks >= 70 and marks < 80:
    grade = "B"
    remark = "Good"

elif marks >= 60 and marks < 70:
    grade = "C"
    remark = "Average"

elif marks >= 50 and marks < 60:
    grade = "D"
    remark = "Pass"

elif marks < 0 or marks > 100:
    print("invalid input")
    exit()    

else:
    grade = "F"
    remark = "Fail"
    print(f"Minimum marks to pass: 50")

print(f"Grade: {grade} {remark}") 

# B2  Pattern Printing with Nested Loops
# Using nested loops, print the following patterns. Accept n from input (use n=5 for demo):

# Part 1 — Right triangle (2 marks):
# *
# * *
# * * *
# * * * *
# * * * * *

# Part 2 — Multiplication table grid (3 marks):
#   1   2   3   4   5
#   2   4   6   8  10
#   3   6   9  12  15
#   4   8  12  16  20
#   5  10  15  20  25

# Hint: Use print(f"{val:4}", end="") for aligned columns.

#Part1
print("Part1")
for i in range(1,6): #outer loop for rows
    for j in range(1, i+1): #inner loop for columns
        print("*", end=" ")
    print() 

#Part2
print("Part2")
for i in range(1,6):
    for j in range(1, 6):
        print(f"{i*j:4}", end=" ")
    print()

#Write a program that asks the user to enter numbers one by one. The user types "done" to stop. After the loop, display:
# Total count of numbers entered
# Sum and average (rounded to 2 decimal places)
# Largest and smallest numbers
# Count of even vs odd numbers

# Handle the case where the user enters a non-numeric value — skip it and print a warning, but don't crash.
numbers = []
count_even = 0
count_odd = 0

while True:
    user_input = input("Enter a number or (done) to stop: ")
    if user_input.lower() == "done":
        break

    try:
        num = int(user_input)
    except ValueError:
        print("Warning! Invalid input, the value should be numeric.")
        continue

    numbers.append(num)
    if num % 2 == 0:
        count_even += 1
    else:
        count_odd += 1

if numbers:
    count = len(numbers)
    total = sum(numbers)
    average = total / count
    largest = max(numbers)
    smallest = min(numbers)

    print(f"Total count of numbers entered: {count}")
    print(f"Total sum: {total}")
    print(f"Average: {average:.2f}")
    print(f"Largest: {largest}")
    print(f"Smallest: {smallest}")
    print(f"Count Even: {count_even}")
    print(f"Count Odd: {count_odd}")
else:
    print("No valid numbers were entered.")
        
#Print numbers from 1 to 100 applying these rules:
# Divisible by 3 → Fizz
# Divisible by 5 → Buzz
# Divisible by both 3 and 5 → FizzBuzz
# Divisible by 7 → append Boom (or print Boom alone if no other label)
# Otherwise → print the number

# After printing all 100 numbers, print a summary showing how many times each label appeared.

# Keep track of how many times each label appears
total_fizz = 0
total_buzz = 0
total_fizzbuzz = 0
total_boom = 0

# Loop through numbers from 1 to 100
for i in range(1, 101):
    result = ""

    # Check if the number is divisible by both 3 and 5
    if i % 3 == 0 and i % 5 == 0:
        result += "FizzBuzz"
        total_fizzbuzz += 1
    # Check if the number is divisible by 3
    elif i % 3 == 0:
        result += "Fizz"
        total_fizz += 1
    # Check if the number is divisible by 3
    elif i % 5 == 0:
        result += "Buzz"
        total_buzz += 1
    # Check if the number is divisible by 7
    if i % 7 == 0:
        result += "Boom"
        total_boom += 1
    # If none of the conditions are true, print the number itself
    if result == "":
        print(i)
    else:
        print(result)

# Print the final summary of all labels counted
print("Summary of each label appeared")
print(f"Total Fizz: {total_fizz}")
print(f"Total Buzz: {total_buzz}")
print(f"Total FizzBuzz: {total_fizzbuzz}")
print(f"Total Boom: {total_boom}")
           