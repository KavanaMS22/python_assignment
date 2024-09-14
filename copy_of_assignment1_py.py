# -*- coding: utf-8 -*-
"""Copy of assignment1.py

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1RQbytteOWv-tE_Eh6ERe6Ls_gkd0SPMb

Name: Kavana M S
Date: 11-09-2024

1a) variable: variable is a memory location used to stores values
"""

name="kavana" #name is a variable
print(name)

"""1 b) A variable is a memory location used to  store a value whereas the constant is a fixed value. Python does not contain any constants.

2a) 1. Integer
"""

num=int(input("enter a number")) #integer variable
print(num)

"""2a) 2. Float"""

a=float(input("enter a number")) #float variable
print(a)

"""2a)3.String"""

b=str(input("enter a string of characters")) #string variable
print(b)

"""2a)4. Boolean"""

a=10
b=20
c=a==b
print(bool(c)) #boolean variable

"""2b)"""

a=10
print("type of a is",{type(a)}) # integer variable
b=9.5
print("type of b is",{type(b)}) # float variable
c="kavana"
print("type of c is",{type(c)}) # string variable
d=[1,2,3]
print("type of d is",{type(d)}) # list variable
e=(1,2,3)
print("type of e is",{type(e)}) # tuple variable
f=True
print("type of f is",{type(f)}) # boolean variable

"""3a) 1. Addition: it is a arithmetic operator used to add two inputs"""

a=10
b=20
c=a+b #addition operator
print(c)

"""3a)2. Subtraction:it is a arithmetic operator used to subtract two inputs"""

a=20
b=20
c=a-b #subtraction operator
print(c)

"""3a)3. Multiplication: it is a arithmetic operator used to multiply two inputs"""

a=2
b=20
c=a*b #multiplication operator
print(c)

"""3a)4. Division: it is a arithmetic operator used to divide two inputs"""

a=20
b=2
c=a/b #division operator
print(c)

"""3a)5.Floor Division: it is a arithmetic operator which divides the first number by another number and rounds down the result to the nearest whole number"""

a=51
b=4
c=a//b #floor division operator
print(c)

"""3a) 6.Modulus: it is a arithmetic operator that gives the remainder"""

a=10
b=3
c=a%b #modulus operator
print(c)

"""3a)7.Exponentiation: number multiplied as many times as its power"""

a=2**4
print(a) #exponentiation operator

"""3b) Area of a rectangle"""

length=int(5)
width=int(10)
area=length*width
print(area)

"""4a)1. Equal to: it is a comparison operator which says both the inputs are equal"""

a=2
b=2
c=a==b #equal to operator
print(c)

"""4a)2.Not equal to: it is a comparison operator which says both the inputs are
 not equal
"""

a=2
b=3
c=a!=b #not equal to operator
print(c)

"""4a)3.Greater than:it is used to compare two values.

"""

a=5
b=4
print(a>b) #greater than operator

"""4a)4.Less than: it is used to compare two values."""

a=4
b=5
print(a<b) #less than operator

"""4a)5.Greater than or equal to: it is used to compare two values."""

a=5
b=4
print(a>=b) #greater than or equal to operator

"""4a)6.Less than or equal to:it is used to compare two values."""

a=4
b=5
print(a<=b) #less than or equal to operator

"""4b)"""

num = int(input("enter a number"))
if num>0:
  if num%2 ==0:
    print("number is positive and even")
  else:
    print("number is positive and odd")
elif num==0:
  print("number is zero")
else:
  print("number is negative")

"""5a)Type casting is the conversion of one data type into another.Implicit type casting is done by the program itself whereas the explicit type casting is conversion done by the programmer using built-in functions"""

a=3
b=4
c=a*b
print(c)
print({type(c)}) # implicit operator

a=3
b=float(a) # explicit operator
print(b)

"""5b)1. Float to an integer"""

a=3.5
b=int(a) #type casting float to integer
print(b)

"""5b)2. Integer to a string"""

a=300
b=str(a) #type casting integer to string
print(b)

"""5b)3.String to a float"""

a="300"
b=float(a)#type casting string to float
print(b)

"""6)1.Adds two numbers and print the result"""

a=10
b=25
c=a+b
print("the sum is",c)

"""6)2.Subtracts the second number from the first and prints the result"""

a=25
b=5
c=a-b
print("the result is",c)

"""6)3.Multiplies the two numbers and prints the result"""

a=5
b=5
c=a*b
print("the result is",c)

"""6)4.Divides the first number by the second and prints the result(handle division by zero)"""

a=25
b=5
c=a/b
print("the result is",c)

"""6)5.converts the sum of the numbers to a string and print the type of the result"""

a=22
b=29
c=a+b
d=str(c)
print(d)
print({type(d)})

