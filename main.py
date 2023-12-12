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

  