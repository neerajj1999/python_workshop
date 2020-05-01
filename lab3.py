# # 1. WAP to demonstrate while loop with else statement.
# # sol:-
# n = int(input("Enter the number "))
# while n<=10:
#     print("Python is easy")
#     break
# else:
#     print("learn python")
#     # /////////////////////////////////////////////////////////////////////////////////////////
# #
# # 2. Print 1st 5 even numbers (use break statement).
#
# # sol:-
# num = 10
# var = 1
# for number in range(var,num +1):
#     if(number % 2==0):
#         print("{0}".format(number))
#
# # ////////////////////////////////////////////////////////////////////////////////////////////
# # 3. Print 1st 4 even numbers (use continue statement).
#
# # sol:-
# num = 10
# var = 1
# for number in range(var,num +1):
#     if(number % 2==0):
#         print("{0}".format(number))
#         continue
#
# # //////////////////////////////////////////////////////////////////////////////////////////////
# # 4. WAP to demonstrate Pass statements.
#
# # sol:-
# num =int(input("enter the number: "))
# if num>5:
#     pass
#     print("python if fun")
# else:
#     print("Python is love")
# # ////////////////////////////////////////////////////////////////////////////////////////////////
# # 5. Write a Python program to calculate the length of a string. 
#
# # sol:-
# t = {'a' , 'b' , 'c', 'd', 'e', 'f' }
# print(len(t))
# # ///////////////////////////////////////////////////////////////////////////////////////////////////
# # 6. Write a Python program to count the number of characters
# # (character frequency) in a string
# # sol:-
#
# string = "Character frequency"
# print(len(string))
# # //////////////////////////////////////////////////////////////////////////////////////////////////
# # 7. Write a Python program to get a string made of the first 2 and the
# # last 2 chars from a given a string. If the string length is less than 2,
# # return instead of the empty string.
# # sol:-
# str = "Python"
# if (len(str) < 2):
#     print(str)
# else:
#     print(str[0:2] + str[-2:])
# # //////////////////////////////////////////////////////////////////////////////////////////////////
#
# # 8. Write a Python program to get a string from a given string where
# # all occurrences of its first char have been changed to &#39;$&#39;, except the
# # first char itself
# # sol:-
#
# def change_char(str1):
#     char = str1[0]
#     length = len(str1)
#     str1 = str1.replace(char, '$')
#     str1 = char + str1[1:]
#
#     return str1
#
# print(change_char('python_is_popular_programing'))
# # /////////////////////////////////////////////////////////////////////////////////////////////////
# # 9. Write a Python program to get a single string from two given
# # strings, separated by a space and swap the first two characters of
# # each string. 
#
# # sol:-
#
# def chars_mix_up(a, b):
#   new_a = b[:2] + a[2:]
#   new_b = a[:2] + b[2:]
#
#   return new_a + ' ' + new_b
# print(chars_mix_up('python','language'))
# # /////////////////////////////////////////////////////////////////////////////////////////////////
# # 10. Write a Python program to add &#39;ing&#39; at the end of a given string
# # (length should be at least 3). If the given string already ends with
# # &#39;ing&#39; then add &#39;ly&#39; instead. If the string length of the given string is
# # less than 3, leave it unchanged
#
# # sol:-
# def string(char):
#     length = len(char)
#     if length > 2:
#         if char[-3:] == 'ing':
#             char += 'ly'
#         else:
#             char += 'ing'
#     return char
# print(string('ab'))
# print(string('python'))
# print(string('begging'))