'''
Task 2: Write and Append Data to a File
 
Problem Statement: Write a Python program that:
1.   Takes user input and writes it to a file named output.txt.
2.   Appends additional data to the same file.
3.   Reads and displays the final content of the file.
'''


a = str(input("Enter text to write to the the file: "))
file1 = open('C:\\Users\\SreenivasKoda.AzureAD\\Desktop\\Python\\Dev_Python\\Dev_Python\\Assignment4\\output.txt', 'w')
content = file1.write(a)
print("Data successfully written to output.txt.")
file1.close()

b = str(input("Enter additional text to append: "))
c = ("\n"+ b)
file1 = open('C:\\Users\\SreenivasKoda.AzureAD\\Desktop\\Python\\Dev_Python\\Dev_Python\\Assignment4\\output.txt', 'a')
append = file1.write(c)
print("Data successfully appended.")
file1.close()

file1 = open('C:\\Users\\SreenivasKoda.AzureAD\\Desktop\\Python\\Dev_Python\\Dev_Python\\Assignment4\\output.txt', 'r')
result = file1.read()
print("Final content of output.txt:\n")
print(result)
file1.close()