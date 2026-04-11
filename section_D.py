#SECTION D
# Data Structures, OOP & File Handling
# Lists, dicts, sets, tuples, classes, file I/O

# D1  List & Dictionary Operations
# You have a dictionary of products in a store:
# inventory = {
#     "Laptop":     {"price": 85000, "qty": 10, "category": "Electronics"},
#     "T-Shirt":    {"price": 1200,  "qty": 50, "category": "Clothing"},
#     "Headphones": {"price": 5500,  "qty": 20, "category": "Electronics"},
#     "Jeans":      {"price": 3200,  "qty": 30, "category": "Clothing"},
#     "Mouse":      {"price": 1800,  "qty": 15, "category": "Electronics"},
# }

# Write code to:
# Print the total inventory value (price x qty for each, summed)
# Find and print the most expensive item
# List all items in the "Electronics" category
# Apply a 10% discount to all items where price > 5000 (update dictionary)
# Print a sorted list of items by price (ascending)

inventory = {
    "Laptop":     {"price": 85000, "qty": 10, "category": "Electronics"},
    "T-Shirt":    {"price": 1200,  "qty": 50, "category": "Clothing"},
    "Headphones": {"price": 5500,  "qty": 20, "category": "Electronics"},
    "Jeans":      {"price": 3200,  "qty": 30, "category": "Clothing"},
    "Mouse":      {"price": 1800,  "qty": 15, "category": "Electronics"},
}

# Total inventory value
total_value = 0
for item in inventory:
    total_value += inventory[item]["price"] * inventory[item]["qty"]

print(f"Total inventory value: {total_value}")

# Most expensive item
most_expensive = max(inventory, key=lambda item: inventory[item]["price"])
print("Most expensive item:", most_expensive, inventory[most_expensive])

# Electronics items
print("Electronics items:")
for item in inventory:
    if inventory[item]["category"] == "Electronics":
        print(item)

# Apply 10% discount on items with price greater than 5000
for item in inventory:
    if inventory[item]["price"] > 5000:
        inventory[item]["price"] = inventory[item]["price"] * 0.90

print("Inventory after discount:")
for item in inventory:
    print(item, inventory[item])

# Sorted items by price in ascending order
sorted_items = sorted(inventory.items(), key=lambda x: x[1]["price"])

print("Sorted items by price:")
for item, details in sorted_items:
    print(item, details)


# D2  Sets & Tuples
section_a = {"Ali", "Sara", "Umar", "Hina", "Zara", "Kamran"}
section_b = {"Sara", "Bilal", "Hina", "Imran", "Zara", "Nadia"}

# Students in both sections
both_sections = section_a.intersection(section_b)
print("Students in both sections:", both_sections)

# Students only in Section A
only_section_a = section_a.difference(section_b)
print("Students only in Section A:", only_section_a)

# All unique students across both sections
all_students = section_a.union(section_b)
print("All unique students:", all_students)

# Students in exactly one section
one_section_only = section_a.symmetric_difference(section_b)
print("Students in exactly one section:", one_section_only)

# Tuple of three highest-scoring subjects
top_subjects = ("Math", "Physics", "Computer")
print("Top 3 subjects:", top_subjects)

# Tuples are immutable
try:
    top_subjects[0] = "English"
except TypeError as e:
    print("Tuple error:", e)


#D3  Object-Oriented Programming - Library System

# Part 1 - Book class
class Book:
    def __init__(self, title, author, isbn, is_available=True):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.is_available = is_available

    def __str__(self):
        return f"Title: {self.title}, Author: {self.author}, ISBN: {self.isbn}, Available: {self.is_available}"

    def __repr__(self):
        return self.__str__()

    def checkout(self):
        self.is_available = False

    def return_book(self):
        self.is_available = True


# Part 2 - Library class
class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def find_by_author(self, author):
        return [book for book in self.books if book.author == author]

    def available_books(self):
        return [book for book in self.books if book.is_available == True]

    def total_books(self):
        return len(self.books)


# Creating book objects
book1 = Book("Python Basics", "Ali Raza", "111")
book2 = Book("OOP in Python", "Sara Khan", "222")
book3 = Book("Data Structures", "Ali Raza", "333")
book4 = Book("Machine Learning", "Hina Ahmed", "444")

# Creating library object
library = Library()

# Adding books to library
library.add_book(book1)
library.add_book(book2)
library.add_book(book3)
library.add_book(book4)

# Checkout 2 books
book1.checkout()
book3.checkout()

print("Total books in library:", library.total_books())
print("Books by Ali Raza:", library.find_by_author("Ali Raza"))
print("Available books:")
for book in library.available_books():
    print(book)


# D4  File Handling
file_name = "students.txt"


def save_student(name, marks):
    with open(file_name, "a") as f:
        f.write(f"{name},{marks}\n")


def load_students():
    students = []
    try:
        with open(file_name, "r") as f:
            for line in f:
                name, marks = line.strip().split(",")
                students.append({"name": name, "marks": int(marks)})
    except FileNotFoundError:
        print("File not found")
    return students


def top_student():
    try:
        students = load_students()
        if len(students) == 0:
            return "No student record found"
        top = max(students, key=lambda student: student["marks"])
        return top["name"]
    except FileNotFoundError:
        return "File not found"


# Clear file before saving sample students
with open(file_name, "w") as f:
    pass

save_student("Ali", 85)
save_student("Sara", 92)
save_student("Umar", 78)
save_student("Hina", 95)
save_student("Zara", 88)

print("Loaded students:", load_students())
print("Top student:", top_student())
