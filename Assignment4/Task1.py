'''
Task 1: Read a File and Handle Errors 
Problem Statement:  Write a Python program that:
1.   Opens and reads a text file named sample.txt.
2.   Prints its content line by line.
3.   Handles errors gracefully if the file does not exist.

'''

try:
    file1 = open('C:\\Users\\SreenivasKoda.AzureAD\\Desktop\\Python\\Dev_Python\\Dev_Python\\Assignment4\\sample.txt', 'r')
    print("Reading file content:\n")
    line = 1
    for i in file1:
        print("Line", line,":", i.strip() )
        line += 1 
    file1.close()
except:
    print("Error: The file 'sample.txt' was not found.")