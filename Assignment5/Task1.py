'''
Task 1: Create a Dictionary of Student Marks

Problem Statement: Write a Python program that:
1.   Creates a dictionary where student names are keys and their marks are values.
2.   Asks the user to input a student's name.
3.   Retrieves and displays the corresponding marks.
4.   If the student’s name is not found, display an appropriate message.

'''

dirct = {"Sowmya": 92, "Lahari": 82, "Sreenivas": 94, "Vasu": 20}
name = str(input("Enter the Student's name: "))
if name in dirct:
    print("{}'s marks: {}".format(name,dirct.get(name)))
else:
    print("Student not found.")
