# SECTION A
# Python Fundamentals
# Data types, variables, operators, string operations — Weeks 1 and 2

# A1  Variables, Types & Type Conversion
# You are processing student registration data entered by a user. The data comes in as raw strings:

# raw_name = "  ali raza  "
# raw_age = "21"
# raw_gpa = "3.75"
# raw_enrolled = "True"

# Write a Python script that:
# Cleans raw_name (remove extra spaces, convert to title case)
# Converts raw_age to an integer and raw_gpa to a float
# Converts raw_enrolled to a proper boolean
# Prints: Name: Ali Raza | Age: 21 | GPA: 3.75 | Enrolled: True

# Expected output: Name: Ali Raza | Age: 21 | GPA: 3.75 | Enrolled: True

raw_name = "  ali raza  "
raw_age = "21"
raw_gpa = "3.75"
raw_enrolled = "True"

name = raw_name.strip().title()
age = int(raw_age)
gpa = float(raw_gpa)
enrolled = bool(raw_enrolled)
print(f"Name: {name} | Age: {age} | GPA: {gpa} | Enrolled: {enrolled}")

#A2  String Operations & F-Strings
# Write a program that accepts a sentence from the user and performs these operations, printing each result:
# Count the total number of words
# Count how many times the letter 'a' appears (case-insensitive)
# Reverse the entire string
# Check if it is a palindrome (ignoring spaces and case)
# Replace every vowel (a e i o u) with *

# Test your program with: "Never odd or even"
# Hint: Use .split(), .count(), .replace(), and slicing [::-1]

sentence = input("Enter a sentence: ")
word_count = len(sentence.split())
print(f"Total word count {word_count}")

char_count = sentence.count("a")
print(f"Character_Count of 'a' {char_count}")

reverse = sentence[::-1]
print(f"Reverse String {reverse}")

if sentence[:] == sentence[::-1]:
    print(f"It's a palindrome")
else:
    print("Not a palindrome")

replace_vow = sentence.replace("a","*").replace("e","*").replace("i","*").replace("o","*").replace("u","*")
print(f"Replaceed String {replace_vow}")   

#A3  Arithmetic & Operators — Billing Calculator
# A shopkeeper needs a quick billing calculator. Write a program that takes:
# Item price (float), Quantity (int), Discount % (float), Tax rate (float)

# Calculate and print:
# Subtotal (price x quantity)
# Discount amount
# Amount after discount
# Tax amount (Pakistan GST 17%)
# Grand total (rounded to 2 decimal places)

# Sample: Price=500, Qty=3, Discount=10%, Tax=17% → Grand total: 1579.50

item_price = float(input("Enter item price: "))
quantity = int(input("Enter quantity: "))
discount = float(input("Enter discount percentage: "))
tax = float(input("Enter a tax percentage: "))

subtotal = item_price * quantity
discount_amount = (subtotal * discount)/ 100
amount_after_discount = subtotal - discount_amount
tax_amount = (amount_after_discount * tax)/100
grand_total = amount_after_discount + tax_amount

print(f"Subtotal: {subtotal}")
print(f"Discount amount: {discount_amount}")
print(f"Amount after discount: {amount_after_discount}")
print(f"Tax amount: {tax_amount}")
print(f"Grand total: {round(grand_total, 2)}")

#A4  Input Validation — Phone Number
# Write a program that collects and validates a Pakistani phone number. Rules:
# Must be exactly 11 digits
# Must start with 03
# Must contain only digits (no spaces, dashes, or letters)

# The program should:
# Ask the user to enter a phone number
# Check all three rules using string methods only (no import re)
# Print a clear message for each failed rule
# If valid, print: Valid phone number: 03XX-XXXXXXX (with dash after position 4)

phone_num = input("Enter phone number : ")

if len(phone_num) == 11 and phone_num.startswith("03") and phone_num.isnumeric():
    print(f"Valid Phone Number: {phone_num[:4]}-{phone_num[4:]}")

else:
    print("Invalid phone number")    