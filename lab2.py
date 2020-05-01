# #Q1. Check whether a number is even or odd
# sol:-

# number = int(input("Enter the Number :   "))
# if number % 2 == 0:
#     print("The Number is Even.")
# else:
#     print("The Number is Odd.")

# //////////////////////////////////////////////////////////////////////////////////////////


# # Q2. Check whether an entered year is leap year or not.
# sol:-

# year = int(input("Enter the Days: "))
# if year == 365:
#     print('The year is non-leap year')
# elif year == 366:
#     print('The year is a leap year ')
# else:
#     print('The value is incorrect')

# ////////////////////////////////////////////////////////////////////////////////////////////
# # Q3. Write a program to check whether a character is vowel or
# # consonants.
# sol:

# vowel = ('a','e','i','o','u')
# word= str(input("Enter the Letter :  "))
# if word.lower() in vowel:
#     print("The word is Vowel ")
# else:
#     print("The word is consonent ")
# ////////////////////////////////////////////////////////////////////////////////////////////

# # Q4. Write a program to find the smallest of two numbers.
# sol:-

# digit_first = int(input('Enter the first number: '))
# digit_second = int(input('Enter the second number: '))
# if digit_first > digit_second:
#     print(digit_second)
# elif digit_first < digit_second:
#     print(digit_first)
# else:
#     print(' The number is same')

# ////////////////////////////////////////////////////////////////////////////////////////////////
# # Q5. Find the Factorial of a Number
# sol:-
# var = int(input(' Enter the number '))
# factorial = 1
# if var == 0:
#     print('The Factorial is 1')
# elif var <0:
#     print('The factorial is not exist')
# else:
#     for i in range(1,var + 1):
#         factorial = factorial* i
#     print("the factorial is ",factorial)

# ////////////////////////////////////////////////////////////////////////////////////////////////
# # Q6. Write a program to print this patterns
# # *
# # * *
# # * * *
# # * * * *

# sol:-

# num = int(input("Enter the number of rows"))
# for i in range(0,num):
#     for j in range(0,num-i-1):
#         print(end= " ")
#     for j in range(0,i+1):
#         print("*",end=" ")
#     print()

# //////////////////////////////////////////////////////////////////////////////////////////////////////////

# # Q7. Write a program to print this series
# # 1 1 2 3 5 8 13
# sol:-

# list = [1,1,2,3,5,8,13]
# a,b,c,d,e,f,g = list
# print(a,b,c,d,e,f,g)

# ////////////////////////////////////////////////////////////////////////////////////////////////
# # Q8. Check whether a number is prime or not
# sol:-

# num = int(input("Enter the number: "))
# if (num > 1):
#     for i in range(1,num):
#         if(num%2 ==0):
#             print(num,"the number is not prime number")
#             break
#         else:
#             print("The number is a prime number")
#             break
# ///////////////////////////////////////////////////////////////////////////////////////////////
# # Q9. Make a Simple Calculator.
# sol:-

# def add(x,y):
#     return x +y
#
# def subtract(x, y):
#     return x -y
#
# def multiply(x,y):
#     return x*y
#
# def division(x,y):
#     return x/y
# print("//// Choice of operation////")
# print("1.Add")
# print("2.Subtract")
# print("3.Multiply")
# print("4.Division")
# valu1 = float(input("Enter the First number: "))
# valu2 = float(input("Enter the Second number: "))
# choice = int(input("Enter the Choice: "))
#
#
# if choice == 1:
#     print(valu1 ,"+" , valu2, "=" , add(valu1, valu2))
# elif choice == 2:
#     print(valu1, "-" ,valu2, "=", subtract(valu1, valu2))
#
# elif choice == 3:
#     print(valu1, "*", valu2, "=", multiply(valu1,valu2))
#
# elif choice == 4:
#     print(valu1, "/", valu2, " = ", division(valu1 ,valu2 ))
#
# else:
#     print("INVALID")