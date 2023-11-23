"""1. Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5, between 2000 and 3200 (both included).The numbers obtained should be printed in a comma-separated sequence on a single line."""

#print([x for x in range(2000,3201) if x%7==0 and x%5!=0])
"""2. Write a program which can compute the factorial of a given numbers.The results should be printed in a comma-separated sequence on a single line.Suppose the following input is supplied to the program: 8 Then, the output should be:40320

4! = 4 * 3 * 2 * 1 = 24"""

# x = int(input("Enter number: "))
# cm = x #current_multiplicand
# out = x

# while cm > 1:
#   cm += -1
#   out = out*cm

# print(out)

# Improved syntax for harshraj22's solution
# def shortFact(x): return 1 if x <= 1 else x*shortFact(x-1)
# print(shortFact(int(input())))
"""3. With a given integral number n, write a program to generate a dictionary that contains (i, i x i) such that is an integral number between 1 and n (both included). and then the program should print the dictionary.Suppose the following input is supplied to the program: 8"""

# n = int(input('Enter integral: '))
# out = {}

# for v in range(1,n+1):
#   out.update({str(v):v*v})

# print(out)

#yurbika's solution corrected by Developer-47
# num = int(input("Number: "))
# print(dict(enumerate([i*i for i in range(1, num+1)], 1)))

"""4. Write a program which accepts a sequence of comma-separated numbers from console and generate a list and a tuple which contains every number.Suppose the following input is supplied to the program:"""

#out=[]

#for v in input('IN: '):
  #if v == ',':
    #continue
  #else:
    #out.append(v)
    
#print(out, tuple(out))

"""5. Define a class which has at least two methods:
getString: to get a string from console input
printString: to print the string in upper case.
Also please include simple test function to test the class methods."""

# class Capitalise:
#   def getString():
#     x = input('ENTER: ')
#     return(x)
#   def printString():
#     out = Capitalise.getString()
#     return print(str(out).upper())
  
# x = Capitalise
# x.printString()

"""
6. Write a program that calculates and prints the value according to the given formula:

Q = Square root of [(2 _ C _ D)/H]
Following are the fixed values of C and H:

C is 50. H is 30.

D is the variable whose values should be input to your program in a comma-separated sequence.For example Let us assume the following comma separated input sequence is given to the program

"""
import math as m

def calculator(d):
  for v in d.split(','):
      print(m.sqrt(2*50*int(v)/30))

calculator(input('ENTER A LIST OF COMMA-SEPARATED VALUES:'))

"""
7. _Write a program which takes 2 digits, X,Y as input and generates a 2-dimensional array. The element value in the i-th row and j-th column of the array should be i _ j.*

Note: i=0,1.., X-1; j=0,1,¡­Y-1. Suppose the following inputs are given to the program: 3,5

Then, the output of the program should be:
[[0, 0, 0, 0, 0], [0, 1, 2, 3, 4], [0, 2, 4, 6, 8]]
"""
  
  
  
  
  
    