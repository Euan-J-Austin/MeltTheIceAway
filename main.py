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
# import math as m

# def calculator(d):
#   for v in d.split(','):
#       print(m.sqrt(2*50*int(v)/30))

# calculator(input('ENTER A LIST OF COMMA-SEPARATED VALUES:'))

"""
7. _Write a program which takes 2 digits, X,Y as input and generates a 2-dimensional array. The element value in the i-th row and j-th column of the array should be i _ j.*

Note: i=0,1.., X-1; j=0,1,¡­Y-1. Suppose the following inputs are given to the program: 3,5

Then, the output of the program should be:
[[0, 0, 0, 0, 0], [0, 1, 2, 3, 4], [0, 2, 4, 6, 8]]
"""

#X determines rows, Y determines columns
#[0,0,0,0,0] as 0 row mutiplied by 0-4 columns
#[0,1,2,3,4,5] as 1 row by 0-4 columns

# def twoDimArr(i):
#   x,y= int(i.split(',')[0]), int(i.split(',')[1])
#   out = []
#   row, col = 0, 0
#   temp = []
#   while x > 0:
#     while len(temp) <= y-1:
#       temp.append(row*col)
#       col += 1
#     out.append(temp)
#     temp = []
#     row += 1
#     col = 0
#     x += -1
#   return print(out)

# twoDimArr(input('ENTER TWO DIGITS:'))

#darkprinx's solution

# x,y = map(int,input().split(','))
# lst = [[i*j for j in range(y)] for i in range(x)]
# print(lst)

"""
8  Write a program that accepts a comma separated sequence of words as input and prints the words in a comma-separated sequence after sorting them alphabetically.

"""

# def sort_words(w):
#   print(sorted(l.upper() for l in w.split(',')))

# sort_words(input('Enter comma-separated words:'))

"""
9. Write a program that accepts sequence of lines as input and prints the lines after making all characters in the sentence capitalized.

Suppose the following input is supplied to the program:

Hello world
Practice makes perfect

Then, the output should be:

HELLO WORLD
PRACTICE MAKES PERFECT
"""

# out = ""

# def capSeq(x):
#   global out
#   if x != "":
#     out = out + x.upper() + "\n"
#     return capSeq(input("ENTER. CARR. RETURN TO PRINT:"))
#   else:
#     return print(out)

# capSeq(input("ENTER. CARR. RETURN TO PRINT:"))

# '''Soltuion by: hajimalung baba
# '''
# def inputs():
#     while True:
#         string = input()
#         if not string:
#             return
#         yield string

# print(*(line.upper() for line in inputs()),sep='\n')

"""
10 Write a program that accepts a sequence of whitespace separated words as input and prints the words after removing all duplicate words and sorting them alphanumerically.

Suppose the following input is supplied to the program:

hello world and practice makes perfect and hello world again
Then, the output should be:

again and hello makes perfect practice world.
"""

# def my_func(x):
#   return print(' '.join(sorted((v for v in {w.lower() for w in x.split()}))))

# my_func(input("ENTER: "))

"""
11. Write a program which accepts a sequence of comma separated 4 digit binary numbers as its input and then check whether they are divisible by 5 or not. The numbers that are divisible by 5 are to be printed in a comma separated sequence.

Example:

0100,0011,1010,1001
Then the output should be:

1010
Notes: Assume the data is input by console.
"""

# def bin_five(s):
#   return print(','.join([bin(x)[2:] for x in (filter(lambda x: x%5 == 0, [int(x, 2) for x in s.split(',')]))]))

# bin_five(input("ENTER:"))

"""
12.Write a program, which will find all such numbers between 1000 and 3000 (both included) such that each digit of the number is an even number.The numbers obtained should be printed in a comma-separated sequence on a single line.
"""

# x = range(1000, 3001)
# out = []

# for n in x:
#   length_n = len(str(n))
#   score = 0
#   for v in str(n):
#     if int(v)%2 == 0:
#       score += 1
#     else:
#       pass
#   if score == length_n:
#     out.append(n)
#   else: 
#     pass

# print(out)

"""
13. Write a program that accepts a sentence and calculate the number of letters and digits.

Suppose the following input is supplied to the program:

hello world! 123
Then, the output should be:

LETTERS 10
DIGITS 3
"""


# def count_ld(x):
#   return print(f'LETTERS {len([v for v in x if ord(v) in range(65, 91) or ord(v) in range(97,123)])}\nDIGIT {len([v for v in x if ord(v) in range(48,58)])}')

# count_ld(input("ENTER: "))

"""

I'm happy with this solution, used unicode integer values to isolate all letters, lower and upper case, in the Latin alphabet and the digits 0-9 which saved on detailed solution to distinguishing between numbers in string format and integers; how to deal with punctuation 

"""

"""
14 Write a program that accepts a sentence and calculate the number of upper case letters and lower case letters.

Suppose the following input is supplied to the program:

Hello world!
Then, the output should be:

UPPER CASE 1
LOWER CASE 9

"""

def what_case(x):
  chars = [v for v in x if ord(v) in range(65, 91) or ord(v) in range(97,123)]
  upper = len([i for i in chars if i.isupper()])
  lower = len(chars) - upper
  return print(f'UPPER CASE {upper}\nLOWER CASE {lower}')

what_case(input("ENTER:"))

    
  
  
    