# Module 2: Basic Python Concepts
# Task 1: Perform Basic Mathematical Operations
'''
Task 2: Create a Personalized Greeting
Problem Statement: Write a Python program that:
1.  Takes a user's first name and last name as input.
2.  Concatenates the first name and last name into a full name.
3.  Prints a personalized greeting message using the full name.
'''

firstName = input("Enter your first name: ")
firstName = str(firstName)
lastName = input("Enter your last name: ")
lastName = str(lastName)
fullName = (firstName + lastName)
greeting = ("Hello, "+ fullName + "! Welcome to the Python program.")
print(greeting)