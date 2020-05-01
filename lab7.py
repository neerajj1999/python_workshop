# Q1:

# def multiply(x,y):
#     z = x*y
#     return z
# num1= int(input("Enter the first number: "))
# num2 = int(input("enter the Second Number: "))
#
# print("The Solution is : ",multiply(num1,num2))

# /*-----------------------------------------------------------------------------/
# Q2:

# def add(a,b):
#     add = a+b
#     return add
#
# n1 = int(input("Enter the first number: "))
# n2 = int(input("enter the second number : "))
# print("The Solution is : ",add(n1,n2))

# /*-----------------------------------------------------------------------------------/
# Q3:

# def factorial(f):
#     fact = 1
#     for i in range(1, f + 1):
#         fact = fact * i
#     return fact
# f1 = int(input('enter the Number:  '))
# print("factorial is : ",factorial(f1))

# /------------------------------------------------------------------------------------
# Q4:

# def Fibonacci(n):
#     if n < 0:
#         print("Incorrect input")
#     elif n == 1:
#         return 0
#     elif n == 2:
#         return 1
#     else:
#         return Fibonacci(n - 1) + Fibonacci(n - 2)
#
# t1 = int(input("Enter the number:  "))
# print("The solution is : ",Fibonacci(t1))

# /-------------------------------------------------------------------------------------
#Q5:
# def swap_numbers(a, b):
#     temp = a
#     a = b
#     b = temp
#
#     print("After Swapping two Number: num1 = {0} and num2 = {1}".format(a, b))
#
#
# num1 = float(input(" Please Enter the First Value : "))
# num2 = float(input(" Please Enter the Second Value : "))
#
# print("Before Swapping two Number: num1 = {0} and num2 = {1}".format(num1, num2))
# swap_numbers(num1, num2)
# /---------------------------------------------------------------------------------------
# Q6:

# def hcf(x, y):
#     if x > y:
#         smaller = y
#     else:
#         smaller = x
#     for i in range(1, smaller + 1):
#         if ((x % i == 0) and (y % i == 0)):
#             hcf = i
#     return hcf
#
#
# num1 = int(input("Enter first number: "))
# num2 = int(input("Enter second number: "))
# print("The H.C.F. is", hcf(num1, num2))
# /--------------------------------------------------------------------------------------
# Q7:
# ch = input("Enter any character: ")
#
# print("The ASCII value of char " + ch + " is: ",ord(ch))

# /---------------------------------------------------------------------------------------

# Q8:
# import math
# print("The value of square root of 7 : ")
# print (math.sqrt(7))
# /--------------------------------------------------------------------------------------

#Q9
# import datetime
# from datetime import date
# print ("Present date is : ",end="")
# print (date.today())
# /----------------------------------------------------------------------------------
# Q10:
# def greet(name,msg):
#    print("Hello",name + ', ' + msg)
#
# greet("Gareeb","Good morning!")
# /------------------------------------------------------------------------------------
#Q11:
# def divide(a, b):
#     return a / b
#w
# print(divide(8,9))
# # /---------------------------------------------------------------------------------------
# Q12

# def myFun(x, y=50):
#     print("x: ", x)
#     print("y: ", y)
#
# myFun(10)

# /------------------------------------------------------------------------------------------
# Q13
#
# def myFun(*argv):
#     for arg in argv:
#         print(arg)
#
#
# myFun('Hello', 'Welcome', 'to', 'gareeb people')
# /-------------------------------------------------------------------------------------

