'''
Task 2: Using the Math Module for Calculations
 
Problem Statement: Write a Python program that:
1.   Asks the user for a number as input.
2.   Uses the math module to calculate the:
o   Square root of the number
o   Natural logarithm (log base e) of the number
o   Sine of the number (in radians)

'''
from math import *
n = int(input("Enter a number: "))
def func(n):
    print("Square root: ", (n ** (1/2)))
    print("Logarithm: ", log(n))
    print("sine: ", sin(n))
func(n)
    
