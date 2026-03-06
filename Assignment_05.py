#Assignment-05 

#QUESTION 1: Working with Lists
# Create a list called numbers containing at least 8 integers.
# Using a for loop, do the following:
# Print all numbers in the list.
# Print the sum of all numbers.
# Print only the even numbers.
# Requirements:
# Use at least one loop.
# Use conditional statements.
# Display clear output.

numbers = [2,3,4,5,6,7,8,9]   #list of 8 integers.
total = 0   #First the total Sum is 0.

print('Numbers:', end=' ')  #for formatting, end='' prevents new line.
for num in numbers:      #Runing loop on all the values in numbers list.
    print(num, end=' ')     #Prints the number list.
    total += num     #Do the sum of all numbers and store it in total variable.
print()  #To move on next line.

print('Even:', end=' ')  #For formatting
for num in numbers:   #Runing loop on all the values of numbers list.
    if num % 2 == 0:    # If number divided by 2 gives remainder 0, it means the number is even
        print(num, end=' ')  #Prints all the even numbers in 1 line.
print()           
print(f"Total Sum: {total}")  #Prints Total Sum of numbers list.

#QUESTION 2: Dictionary Basics
# Create a dictionary called student with the following keys:
# name
# age
# course
# marks (must store a list of 3 marks)
# Using loops:
# Print all keys and their values.
# Calculate the average of the marks.
# Display whether the student Passed (average ≥ 50) or Failed.
# Requirements:
# Dictionary must contain a list.
# Use loops to calculate the average.

student = {"Name": "Simra",  # Dictionary storing student information and a list of marks
           "Age": 19,
           "Course": "Python",
           "Marks": [80, 90, 75]}

for key, value in student.items():  #Runing loop through all the items of dictionary.
    print(f'{key} -> {value}')   #Prints student details.

total = 0   #Total marks is 0 at first
for mark in student["Marks"]:   #Runing loop on Marks of list in dictionary.
    total += mark    #Sum all the marks and store it in total variable.
average = total / len(student["Marks"])   #Dividing the total marks with the length of Marks list and stores it in average variable.
print(f'Average is: {round(average,2)}')   #Prints the total average of marks with round of by 2.

if average >= 50:   #Checking if Average % is greater than 50 student is passed.
    print('You passed')

else:   #Lower than 50% student failed.
    print('You failed')     

#QUESTION 3: List of Dictionaries
# Create a list called employees.
# Each employee must be stored as a dictionary containing:
# name
# department
# salary
# Using loops:
# Print details of all employees.
# Find the employee with the highest salary.
# Calculate the total salary expense.
# Requirements:
# Minimum 3 employees.
# Use comparison logic.
# Use loops to process data.

employees = [{'Employee': 1,    #Storing 3 employee details of dictionaries in a list.
              'Name': "Hamza",
              "Department": "IT",
              "Salary": 70000},
              {'Employee': 2,
               'Name': "Fasih",
              "Department": "Software Eng",
              "Salary": 65000},
              {'Employee': 3,
               'Name': "Saira",
              "Department": "HR",
              "Salary": 60000}]

total_salary = 0    #First total salary expense is 0 later we will use it to add the all salaries in it inside loop.
highest_salary = 0    #First highest salary is 0 then we will use it inside loop to find the employee that has highest salary. 
highest_employee = ""   #This empty string is for storing the name of employee which has highest salary.

for employee in employees:   #Telling the loop to run on list.
    for key, value in employee.items():  # Loop through each key-value pair inside the employee dictionary
        print(f'{key} -> {value}')  #printing the details
    print('----')    #To see each employee data clearly.

    total_salary += employee["Salary"]   #Here employee means dictionaries that has the keys name Salary we are telling it to sum all the salaries and store it in total_salary variable.

    if employee["Salary"] > highest_salary:   #Checking if any employee has highest salary or not
        highest_salary = employee["Salary"]   #if finds highest salary than other employees store that value in highest_salary variable.
        highest_employee = employee['Name']   #The employee that has highest salary we are telling it to pick that employee name and store it in highest_employee variable.

print(f'Employee that has Highest Salary is: {highest_employee} -> {highest_salary}')  #Prints Employee name with highest salary.
print(f"Total Salary Expense: {total_salary}")  #prints Total salary expense.

#QUESTION 4: While Loop with User Input
# Ask the user to enter numbers.
# Store the numbers in a list.
# Stop when the user enters -1.
# After the loop ends:
# Print the complete list.
# Print the largest number.
# Print the smallest number.
# Requirements:
# Must use a while loop.
# Must store input in a list.
# Handle user input correctly.

numbers = []  #This is empty list we will need it to store numbers in it through loop.

while True:   #This means run the loop until the condition is True.
    user_input = int(input('Enter a number or (-1 to stop): '))  #takes user input in integer
    if user_input == -1:   #Checking if user input is equal to -1 if yes the loop will break and end.
        break
    else:
        numbers.append(user_input)   #Store the number in the list if it is not -1.

largest = numbers[0]   #To check the largest number in the same list we are supposing that the 1st index value of numbers list is the largest to compare it with other indexes values through loop.

smallest =  numbers[0]  #To find the smallest number in the list we use it in loop to compare.

index = 0   #Initializing index starts from 0 to use in the loop as iterator.

while index < len(numbers):  #Using nested loop because we want to find the max number in the same numbers list, loop will run until the iterator will be less than length of list.

    if numbers[index] > largest:   #Checking if any of the value on numbers list index is greater than largest.
        largest = numbers[index]    #if it finds greater value than largest we will update largest by storing that greater value in variable.

    if numbers[index] < smallest:   #This checks if there is any value smaller in the list.
        smallest = numbers[index]   #if finds smaller value than update smallest variable by storing that smaller value in it.

    index += 1   #Incrementing iterator becuase if we don't add this loop will not run it will not move to next index in the list.
    
print(f'Number of list: {numbers}') #All the prints will print the outputs in 3 lines.
print(f'Largest: {largest}')
print(f'Smallest: {smallest}')

#QUESTION 5: Word Frequency Counter
# Ask the user to enter a sentence.
# Convert the sentence into a list of words.
# Use a dictionary to count how many times each word appears.
# Print the word frequency clearly.
# Example Format (for understanding only):
# apple: 3
# banana: 2
# orange: 1
# Requirements:
# Use string splitting.
# Use a dictionary for counting.
# Use loops for processing.

sentence = input("Enter your sentence: ")  #takes user input
word_list = sentence.split()  #split sentence into substring words of list and store it into word_list variable
word_count = {}   #This is empty dictionary we will store words in it through loop.

for word in word_list:   #We are telling it to run loop on all the words in word_list
    if word in word_count:   #Here loop is checking if the word already exist in dict or not if yes it will increase the count by 1.
        word_count[word] += 1

    else:
        word_count[word] = 1   #Here this else will add the new word in dict and the count will be 1.

print(f'Word Count: {word_count}')   #At last we print the whole dict to see the count of each word.

#QUESTION 6: Nested Loops – Multiplication Table
# Using nested loops, print a multiplication table from 1 to 5.
# Expected Output Format:
# 1 2 3 4 5
# 2 4 6 8 10
# 3 6 9 12 15
# 4 8 12 16 20
# 5 10 15 20 25
# Requirements:
# Must use nested loops.
# Proper formatting required

for i in range(1, 6):  #i is for 5 rows and range(1,6) means numbers 1 to 5 because the stop value is excluded 
    for j in range(1, 6):  #j is for 5 columns same range logic as outer loop
        print(i * j, end=' ')  #i * j is doing this i[1]*j[1] = 1 and this multiplication goes until all the 5 tables prints, end=' ' prevent new line print output in 1 line.
    print() #this print moves loop to next line when 1 table completes. 
      