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

# def what_case(x):
#   chars = [v for v in x if ord(v) in range(65, 91) or ord(v) in range(97,123)]
#   upper = len([i for i in chars if i.isupper()])
#   lower = len(chars) - upper
#   return print(f'UPPER CASE {upper}\nLOWER CASE {lower}')

# what_case(input("ENTER:"))
"""
15. Write a program that computes the value of a+aa+aaa+aaaa with a given digit as the value of a.

Suppose the following input is supplied to the program:

9
Then, the output should be:

11106
"""

# def adder(a):
#   return print(sum(int(a*i) for i in range(1,5)))

# adder('9')
"""
16 Use a list comprehension to square each odd number in a list. The list is input by a sequence of comma-separated numbers. >Suppose the following input is supplied to the program:

1,2,3,4,5,6,7,8,9
Then, the output should be:

1,9,25,49,81
"""

# l = [1,2,3,4,5,6,7,8,9]

# out = [x*x for x in l if x%2 != 0]

# print(out)
"""
17

Write a program that computes the net amount of a bank account based a transaction log from console input. The transaction log format is shown as following:

D 100
W 200
D means deposit while W means withdrawal.
Suppose the following input is supplied to the program:

D 300
D 300
W 200
D 100
Then, the output should be:

500
"""

# def inputs():
#     while True:
#         string = input()
#         if not string:
#             break
#         yield string

# print('£', sum([int(i[1:]) if i[0] == 'D' else -int(i[1:]) for i in [line for line in inputs()]]))
"""
18

Question:
A website requires the users to input username and password to register. Write a program to check the validity of password input by users.

Following are the criteria for checking the password:

At least 1 letter between [a-z]
At least 1 number between [0-9]
At least 1 letter between [A-Z]
At least 1 character from [$#@]
Minimum length of transaction password: 6
Maximum length of transaction password: 12
Your program should accept a sequence of comma separated passwords and will check them according to the above criteria. Passwords that match the criteria are to be printed, each separated by a comma.

Example

If the following passwords are given as input to the program:

ABd1234@1,a F1#,2w3E*,2We3345
Then, the output of the program should be:

ABd1234@1

"""

# passwords = ['ABd1234@1','a F1#','2w3E*','2We3345']

# def checker(password):

#   counter = set({})
#   out = []

#   if len(password) in range(6,13):
#     for p in password:
#       for w in p:
#         if ord(w) in range(48,58):
#           counter.add('number')
#         if ord(w) in range(65,91):
#           counter.add('upper')
#           pass
#         if ord(w) in range(97,123):
#           counter.add('lower')
#           pass
#         if ord(w) in range(35,37) or ord(w) == 64:
#           counter.add('special')

#   if len(counter) == 4:
#       out.append(password)

#   return out

# print(list(filter(checker, passwords)))
"""
19
You are required to write a program to sort the (name, age, score) tuples by ascending order where name is string, age and score are numbers. The tuples are input by console. The sort criteria is:

1: Sort based on name
2: Then sort based on age
3: Then sort by score
The priority is that name > age > score.

If the following tuples are given as input to the program:

Tom,19,80
John,20,90
Jony,17,91
Jony,17,93
Json,21,85
Then, the output of the program should be:

[('John', '20', '90'), ('Jony', '17', '91'), ('Jony', '17', '93'), ('Json', '21', '85'), ('Tom', '19', '80')]

"""

# def inputs():
#     while True:
#         string = input()
#         if not string:
#             break
#         yield string

# print([tuple(str(x).capitalize().split(',')) for x in sorted([line.upper() for line in inputs()])])
"""
20. Question:
Define a class with a generator which can iterate the numbers, which are divisible by 7, between a given range 0 and n.

Suppose the following input is supplied to the program:

7
Then, the output should be:

0
7
14
Hints:
Consider use class, function and comprehension.
"""

# class luckySeven():
#   def __init__(self, limit):
#     self.limit = limit
#   def generator(self):
#     for y in (x for x in range(0,self.limit+1) if x%7 == 0):
#       print(y)

# luckySeven(int(input("Enter limit:"))).generator()
"""
Question 21
Question:
A robot moves in a plane starting from the original point (0,0). The robot can move toward UP, DOWN, LEFT and RIGHT with a given steps. The trace of robot movement is shown as the following:

UP 5
DOWN 3
LEFT 3
RIGHT 2
The numbers after the direction are steps. Please write a program to compute the distance from current position after a sequence of movement and original point. If the distance is a float, then just print the nearest integer. Example: If the following tuples are given as input to the program:

UP 5
DOWN 3
LEFT 3
RIGHT 2
Then, the output of the program should be:

2
"""
# import math as m

# def inputs():
#     while True:
#         string = input()
#         if not string:
#             break
#         yield string

# print("EXAMPLE INPUT:\nUP 5\nDOWN 3\nRIGHT 2\nLEFT 3\n")

# d = [int(y[1]) for y in [x.split(' ') for x in inputs()]]

# distance = m.sqrt((d[0] - d[1])**2 + (d[2] - d[3])**2)

# print(round(distance))
"""
QUESTION 22

Question:
Write a program to compute the frequency of the words from the input. The output should output after sorting the key alphanumerically.

Suppose the following input is supplied to the program:

New to Python or choosing between Python 2 and Python 3? Read Python 2 or Python 3.

Then, the output should be:

2:2
3.:1
3?:1
New:1
Python:5
Read:1
and:1
between:1
choosing:1
or:2
to:1

"""

# input = "New to Python or choosing between Python 2 and Python 3? Read Python 2 or Python 3."

# print({x: input.count(x) for x in sorted(input.split(' '))})
"""
23

Write a method which can calculate square value of number


"""

# class Calculator:
#   def get_number():
#     return(input('ENTER NUMBER: '))
#   def print_squared():
#     return print(int(Calculator.get_number())**2)

# m = Calculator
# m.print_squared()
"""
24

Python has many built-in functions, and if you do not know how to use it, you can read document online or find some books. But Python has a built-in document function for every built-in functions.

Please write a program to print some Python built-in functions documents, such as abs(), int(), raw_input()

And add document for your own function
"""

# def doc_printer():
#   """Prints __doc__ information"""
#   print(abs.__doc__)
#   print(int.__doc__)
#   print(doc_printer.__doc__)

# doc_printer()
"""
25

Question:
Define a class, which have a class parameter and have a same instance paramete

"""
# import math as m

# class Triangle:
#   def __init__(self, opposite, adjacent):
#     self.opposite = opposite
#     self.adjacent = adjacent
#   def hypotenuse(self):
#     return print(round(m.sqrt(self.opposite**2 + self.adjacent**2), 2))

# t1 = Triangle(5,7)

# t1.hypotenuse()
"""
26

Function to sum two numbers
"""

# def sumOf(a,b):
#   return print(int(a)+int(b))

# sumOf(1,2)
"""
27

Function to convert int to str
"""

# def toString(a):
#   return print(str(a))

# toString(12345)
"""
28

Define a function that can receive two integer numbers in string form and compute their sum and then print it in console.
"""

# def printSum(a,b):
#   return print(int(a)+int(b))

# printSum(input("Enter A:"), input("Enter B:"))
"""
29

Define a function that can accept two strings as input and concatenate them and then print it in console.

"""

# def concatStrings(a,b):
#   return print(a+b)

# concatStrings(input("A:"),input("B:"))
"""
30

Define a function that can accept two strings as input and print the string with maximum length in console. If two strings have the same length, then the function should print all strings line by line.

"""

# def printLongest(a, b):
#   if len(a) == len(b):
#     print(f"{a}\n{b}")
#   elif len(a) > len(b):
#     print(a)
#   else:
#     print(b)

# printLongest(input(""),input(""))

#yuan1z solution ...func = lambda a,b: print(max((a,b),key=len)) if len(a)!=len(b) else print(a+'\n'+b)
"""
31

Define a function which can print a dictionary where the keys are numbers between 1 and 20 (both included) and the values are square of keys.


"""

# def squaredDictionary():
#   return print({x: x**2 for x in range(1,21)})

# squaredDictionary()
"""
32

Define a function which can generate a dictionary where the keys are numbers between 1 and 20 (both included) and the values are square of keys. The function should just print the keys only.
"""

# def squaredDictKeys():
#   return print({x: x**2 for x in range(1,21)}.keys())

# squaredDictKeys()
"""
33 

Define a function which can generate and print a list where the values are square of numbers between 1 and 20 (both included).

"""

# print([x**2 for x in range(1,21)])
"""
34

Define a function which can generate a list where the values are square of numbers between 1 and 20 (both included). Then the function needs to print the first 5 elements in the list.

"""

# print([x**2 for x in range(1,21)][:5])
"""
34

Define a function which can generate a list where the values are square of numbers between 1 and 20 (both included). Then the function needs to print the last 5 elements in the list.

"""

# print([x**2 for x in range(1,21)][-5:])
"""
35

Define a function which can generate a list where the values are square of numbers between 1 and 20 (both included). Then the function needs to print all values except the first 5 elements in the list.


"""

# print([x**2 for x in range(1,21)][5:])
"""
37

Define a function which can generate and print a tuple where the value are square of numbers between 1 and 20 (both included).

"""

# print(tuple([x**2 for x in range(1,21)]))
"""
38

With a given tuple (1,2,3,4,5,6,7,8,9,10), write a program to print the first half values in one line and the last half values in one line.
"""

# t = tuple([x for x in range (1,11)])

# print(f'{t[:5]}\n{t[5:]}')
"""
39

Write a program to generate and print another tuple whose values are even numbers in the given tuple (1,2,3,4,5,6,7,8,9,10).

"""

# t = tuple([x for x in range (1,11)])

# print(tuple([x for x in t if x%2 == 0]))
"""
40

Write a program which accepts a string as input to print "Yes" if the string is "yes" or "YES" or "Yes", otherwise print "No".
"""

# print("".join((['Yes' if input('ENTER:').lower() == 'yes' else 'No'])))
"""
41

Write a program which can map() to make a list whose elements are square of elements in [1,2,3,4,5,6,7,8,9,10].
"""

# o = list(map(lambda x: x**2, [x for x  in range(1,11)]))

# print(o)
"""
42 

Write a program which can map() and filter() to make a list whose elements are square of even number in [1,2,3,4,5,6,7,8,9,10].
"""

# o = list(map(lambda x: x**2, filter(lambda x: x%2 == 0, [x for x in range(1,11)])))

# print(o)
"""
43

Write a program which can filter() to make a list whose elements are even number between 1 and 20 (both included).
"""

# print(list(filter(lambda x: x%2 == 0, [x for x in range(1,21)])))
"""
44

Write a program which can map() to make a list whose elements are square of numbers between 1 and 20 (both included).
"""

# print(list(map(lambda x: x**2, [x for x in range(1,21)])))
"""
45

Define a class named American which has a static method called printNationality.

46

Define a class named American and its subclass NewYorker.

"""

# class American:
#   @staticmethod
#   def printNationality():
#     print("I'm American.")
# class newYorker(American):
#   def __init__(self, printNationality):
#       super().__init__()

# newYorker.printNationality()
"""
47

Define a class named Circle which can be constructed by a radius. The Circle class has a method which can compute the area.

"""

# import math

# class Circle:
#   def __init__(self, radius):
#     self.radius = int(radius)
#   def area(self):
#     return print(round(math.pi * self.radius**2, 2))

# Circle(input("Radius: ")).area()
"""
48 


Define a class named Rectangle which can be constructed by a length and width. The Rectangle class has a method which can compute the area.

"""

# class Rectangle:
#   def __init__(self, l, w):
#     self.length = l
#     self.width = w
#   def area(self):
#     return print(self.length*self.width)

# Rectangle(10,12).area()
"""
49

Define a class named Shape and its subclass Square. The Square class has an init function which takes a length as argument. Both classes have a area function which can print the area of the shape where Shape's area is 0 by default.

"""

# class Shape:
#   def __init__(self):
#     pass
#   def area(self):
#     return print(0)

# class Square(Shape):
#   def __init__(self, length = 0):
#       Shape.__init__(self)
#       self.l =length
#   def area(self):
#     return print(self.l*self.l)

# Square(9).area()
"""
50 Please raise a RuntimeError exception.
"""
# x = 1

# if x > 0:
#   raise Exception("Error.")
"""51

Write a function to compute 5/0 and use try/except to catch the exceptions."""

# def overZero():
#   return print(5/0)

# try:
#   overZero()
# except:
#    print("Zero-division error.")
"""
Question 52

Define a custom exception class which takes a string message as attribute.

To define a custom exception, we need to define a class inherited from Exception.
"""

# class OverZero(Exception):
# """
# Custom exception class.

# Returns error message if input greater than zero.
# """

#   def __init__(self, msg):
#     self.msg = msg
#   def message(self):
#     print(self.msg)

# x = int(input())

# if x > 0:
#   OverZero("Greater than zero. Too large!").message()
# if x <= 0:
#   OverZero("OK").message()

# help(OverZero)
"""
53

Assuming that we have some email addresses in the "username@companyname.com" format, please write program to print the user name of a given email address. Both user names and company names are composed of letters only.

"""

# e = "publiuscurtius@senate.im"

# print(e.split('@')[0])
"""
54

Assuming that we have some email addresses in the "username@companyname.com" format, please write program to print the company name of a given email address. Both user names and company names are composed of letters only.

"""

# x = "username@companyname.com"

# print(x.split('@')[1].split('.')[0])
"""
55

Write a program which accepts a sequence of words separated by whitespace as input to print the words composed of digits only.
"""

# x = "2 cats and 3 dogs".split(' ')

# print([v for v in x if v.isdigit()])
"""
56

Print a unicode string "hello world".

"""

# print(u"Hello world")
"""
57

Write a program to read an ASCII string and to convert it to a unicode string encoded by utf-8.
"""

# print(input().encode('utf-8'))
"""
58

Write a special comment to indicate a Python source code file is in unicode.


"""

#-*- encoding: utf-8 -*-
"""
59

Write a program to compute 1/2+2/3+3/4+...+n/n+1 with a given n input by console (n>0).

"""

# import numpy as np

# def calculator(i):
#   if i > 0:
#     return print(round(sum([x/float(x+1) for x in np.arange(1,i+1,1)]),2))
#   else:
#     calculator(float(input("Enter integer greater than zero: ")))

# calculator(float(input("Enter integer greater than zero: ")))
"""
60

Write a program to compute:

f(n)=f(n-1)+100 when n>0
and f(0)=0
with a given n input by console (n>0).

"""

# def f(n):
#   if n == 0:
#     return 0
#   return f(n-1)+100

# print(f(int(input())))
"""
61

The Fibonacci Sequence is computed based on the following formula:

f(n)=0 if n=0
f(n)=1 if n=1
f(n)=f(n-1)+f(n-2) if n>1
Please write a program to compute the value of f(n) with a given n input by console.
"""

# def f(n):
#   if n == 0:
#     return 0
#   if n == 1:
#     return 1
#   return f(n-1)+f(n-2)

# print('Fibonacci sequence sums the two preceeding numbers usig the formula f(n-1)+f(n-2). For example, input of 7 returns 13 which is the sum of 5 (F(6)) and 3(F(5)).')

# print(f(int(input(""))))
"""
Question 62

The Fibonacci Sequence is computed based on the following formula:

f(n)=0 if n=0
f(n)=1 if n=1
f(n)=f(n-1)+f(n-2) if n>1
Please write a program to compute the value of f(n) with a given n input by console.

Example: If the following n is given as input to the program:

7
Then, the output of the program should be:

0,1,1,2,3,5,8,13

"""

# out = []

# for f in [n for n in range(0,int(input())+1)]:
#   if f == 0:
#     out.append(0)
#   elif f == 1:
#     out.append(1)
#   else:
#     out.append(out[-1]+out[-2])

# print(','.join(str(v) for v in out))
"""
63

Please write a program using generator to print the even numbers between 0 and n in comma separated form while n is input by console.

Example: If the following n is given as input to the program:

10
Then, the output of the program should be:

0,2,4,6,8,10
"""

#NB the use of a generator is unnecessary.  comprehension is superior.

# o = list((v for v in range(0, int(input()) + 1) if v % 2 == 0))

# print(','.join([str(v) for v in o]))
"""
64

Please write a program using generator to print the numbers which can be divisible by 5 and 7 between 0 and n in comma separated form while n is input by console.

Example: If the following n is given as input to the program:

100
Then, the output of the program should be:

0,35,70
"""

# o = list((v for v in range(0, int(input()) + 1) if v % 5 == 0 and v % 7 == 0))

# print(','.join([str(v) for v in o]))
"""
65 

Please write assert statements to verify that every number in the list [2,4,6,8] is even
"""

t = list(range(2, 9, 2))

for n in t:
  assert n % 2 == 0
"""
66

Please write a program which accepts basic mathematic expression from console and print the evaluation result.

Example: If the following n is given as input to the program:

35 + 3
Then, the output of the program should be:

38
"""

#NB I did not use eval. Eval presents a critical security risk as it allows the user to access one's computer

# import operator

# ops = {
#     '+' : operator.add,
#     '-' : operator.sub,
#     '*' : operator.mul,
#     '/' : operator.truediv,
#     '%' : operator.mod,
#     '^' : operator.xor,
# }

# x = input().split(' ')

# print(ops[x[1]](int(x[0]),int(x[2])))
"""
67

Question
Please write a binary search function which searches an item in a sorted list. The function should return the index of element to be searched in the list.

Hints
Use if/elif to deal with conditions.
"""

#Binary search identifies upper and lower bounds, examine middle elements is that correct? then forms new upper lower bound, new middle element etc

#This is the simple solution using the bisect module which performs a binary search

# import bisect

# import time

# import random

# import pandas as pd

# length_series = []
# bisect_times = []
# myfunc_times = []
# index_times = []

# x = 1

# while x < 7:

#   e = 10**x

#   length_series.append(e)

#   v = random.randint(0,e+1)

#   elements = [x for x in range(0,e)]

#   start = time.perf_counter()

#   def bisearch(v):
#     if v in elements:
#       return print(f'Index of value is {bisect.bisect_left(elements, v)}.')
#     else:
#       print('Value not in list. Search again.')
#       return bisearch(int(input()))

#   bisearch(v)

#   stop = time.perf_counter()

#   bisect_times.append(stop-start)

#   start = time.perf_counter()

#   def bounds(elements, v):
#     middle = elements[len(elements)// 2]
#     if v == middle:
#       return print(f'{v} is at index {elements.index(v)}.')
#     if v < middle:
#       return bounds(elements[:len(elements)//2], v)
#     if v > middle:
#       return bounds(elements[len(elements)//2:], v)

#   bounds(elements, v)

#   stop = time.perf_counter()

#   myfunc_times.append(stop-start)

#   start = time.perf_counter()

#   print(elements.index(v))

#   stop = time.perf_counter()

#   index_times.append(stop-start)

#   x += 1

# d = {'Bisect': bisect_times, 'My_Binary_Search': myfunc_times, 'Index': index_times}

# df = pd.DataFrame(data=d, index=length_series)

# print(df)

# print(df.describe())
"""

68

Please generate a random float where the value is between 10 and 100 using Python module.

"""

# import random

# print(round(random.uniform(10,100),2))
"""
69

Please generate a random float where the value is between 5 and 95 using Python module.

"""

# import random

# print(round(random.uniform(5,95),2))
"""
70

Please write a program to output a random even number between 0 and 10 inclusive using random module and list comprehension.
"""

# import random

# print(round(random.choice([x for x in range(0,11,2)]),2))
"""
71

Please write a program to output a random number, which is divisible by 5 and 7, between 10 and 150 inclusive using random module and list comprehension.
"""

# import random

# print(round(random.choice([x for x in range(10,151) if x%5 ==0 and x%7 == 0]),2))
"""
72
Please write a program to generate a list with 5 random numbers between 100 and 200 inclusive.
"""
# import random

# print(random.choices([x for x in range(100,201)], weights=[1]*101, k=5))
"""
73

Please write a program to randomly generate a list with 5 even numbers between 100 and 200 inclusive.

"""

# import random

# print(random.choices([x for x in range(100,201,2)], weights=[1]*51, k=5))
"""
74

Please write a program to randomly generate a list with 5 numbers, which are divisible by 5 and 7 , between 1 and 1000 inclusive.

"""

# import random

# print(random.sample([x for x in range(1,1001) if x%5 == 0 and x%7 ==0], 5))
"""

75

Please write a program to randomly print a integer number between 7 and 15 inclusive

"""

# import random

# print(random.randrange(5,17))
"""

76

Please write a program to compress and decompress the string "hello world!hello world!hello world!hello world!".

"""

# import zlib

# t = "hello world!hello world!hello world!hello world!"

# t_compressed = zlib.compress(str.encode(t))

# t_decompressed = zlib.decompress(t_compressed)

# print(str(t_decompressed.decode()))
"""
77

Please write a program to print the running time of execution of "1+1" for 100 times.

"""

# import time

# start = time.perf_counter()

# for x in range(0,100):
#   1+1

# stop = time.perf_counter()

# print(stop-start)
"""
78

Please write a program to shuffle and print the list [3,6,7,8].

"""

# import random

# x = [3,6,7,8]

# random.shuffle(x)

# print(x)
"""
79

Please write a program to generate all sentences where subject is in ["I", "You"] and verb is in ["Play", "Love"] and the object is in ["Hockey","Football"].

"""
# import random

# pronoun = ["I", "You"]
# verb = ["Play", "Love"]
# noun = ["Hockey", "Football"]

# print(pronoun[random.randint(0,1)] + " " + verb[ random.randint(0,1)] + " " + noun[random.randint(0,1)])
"""
80

Please write a program to print the list after removing even numbers in [5,6,77,45,22,12,24].
"""

# print([x for x in [5,6,77,45,22,12,24] if x%2 != 0 ])
"""
81

By using list comprehension, please write a program to print the list after removing numbers which are divisible by 5 and 7 in [12,24,35,70,88,120,155].
"""

# print([x for x in [12,24,35,70,88,120,155] if x%5 !=0 or x%7 != 0])
"""
82

By using list comprehension, please write a program to print the list after removing the 0th, 2nd, 4th,6th numbers in [12,24,35,70,88,120,155].
"""

# l1 = [12,24,35,70,88,120,155]

# l2 = [l1[x] for x in range(0,7,2)]

# print([x for x in l1 if x not in l2])

# l3 = enumerate(l1)

# With enumerate

# print([v for (i,v) in enumerate([12,24,35,70,88,120,155]) if i not in [0,2,4,6]])

"""
83

By using list comprehension, please write a program to print the list after removing the 2nd - 4th numbers in [12,24,35,70,88,120,155].
"""

# print([v for (i, v) in enumerate([12,24,35,70,88,120,155]) if i not in [1,2,3]])

"""
84

By using list comprehension, please write a program generate a 3*5*8 3D array whose each element is 0.
"""

# array = [[[0 for x in range(5)] for x in range(3)] for x in range(8)]

# #[[[columns/length]rows/width]depth]

# print(array)

"""
85

By using list comprehension, please write a program to print the list after removing the 0th,4th,5th numbers in [12,24,35,70,88,120,155].
"""

# print([v for (i, v) in enumerate([12,24,35,70,88,120,155]) if i not in [0,4,5]])

"""
86
By using list comprehension, please write a program to print the list after removing the value 24 in [12,24,35,24,88,120,155].

"""

# print([v for v in [12,24,35,24,88,120,155] if v != 24])

"""
87
With two given lists [1,3,6,78,35,55] and [12,24,35,24,88,120,155], write a program to make a list whose elements are intersection of the above given lists.
"""

# print([v for v in [1,3,6,78,35,55] if v in [12,24,35,24,88,120,155]])

"""
88

With a given list [12,24,35,24,88,120,155,88,120,155], write a program to print this list after removing all duplicate values with original order reserved.
"""
# l = [12,24,35,24,88,120,155,88,120,155]

# l.reverse()

# print(set(l))

"""
89

Define a class Person and its two child classes: Male and Female. All classes have a method "getGender" which can print "Male" for Male class and "Female" for Female class.
"""

# class Person:
#   def __init__(self):
#     self.Gender = "Unknown."
#   def getGender(self):
#     return print(self.Gender)

# class Male(Person):
#   def __init__(self):
#     self.Gender = "Male."

# class Female(Person):
#   def __init__(self):
#     self.Gender = "Female."

# m, f = Male(), Female()

# m.getGender()
# f.getGender()


"""
90

Please write a program which count and print the numbers of each character in a string input by console.

Example: If the following string is given as input to the program:

abcdefgabc
Then, the output of the program should be:

a,2
c,2
b,2
e,1
d,1
g,1
f,1

"""

# x = input("ENTER:")

# d = {}

# for c in x:
#   d[c] = x.count(c)

# print(d)

"""
Question 91

Please write a program which accepts a string from console and print it in reverse order.

Example: If the following string is given as input to the program:*

rise to vote sir

Then, the output of the program should be:

ris etov ot esir

"""

# MY SOLUTION IS INCORRECT. I have reversed each word in place as opposed to reversing the entire string using string[::-1].

# print(' '.join([x[::-1] for x in input("ENTER:").split(' ')]))

"""
QUESTION 92
Please write a program which accepts a string from console and print the characters that have even indexes.

Example: If the following string is given as input to the program:

H1e2l3l4o5w6o7r8l9d
Then, the output of the program should be:

Helloworld
"""

# print(''.join([v for (i,v) in enumerate(input("ENTER:")) if i%2 == 0]))

"""
QUESTION 93

Please write a program which prints all permutations of [1,2,3]
"""
# import itertools

# for p in itertools.permutations([1,2,3]):
#   print(p)

"""
QUESTION 94
Write a program to solve a classic ancient Chinese puzzle: We count 35 heads and 94 legs among the chickens and rabbits in a farm. How many rabbits and how many chickens do we have?
"""

# R = 4 legs, 1 head
# C = 2 legs, 1 head
#As each animal can have only 1 head there must be 35 animals in total
#Find out what combination of legs fit for 35 heads/animals 

# r, c = 0, 0

# for x in range(2,95,2):
#   c += 1
#   r = (94-x)/4
#   if r + c == 35:
#     print(f"{int(r)} rabbits and {c} chickens.")


