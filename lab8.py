# # Q1:-
# class Triangle:
#     a=0
#     b=0
#     c=0
#     def create_triangle(self):
#         self.a=int(input("Enter The First Side"))
#         self.b=int(input("Enter The Second Side "))
#         self.c = int(input("Enter The Third Side "))
#     def printside(self):
#         print(self.a)
#         print(self.b)
#         print(self.c)
#
# tr=Triangle()
# tr.create_triangle()
# print("The Sides Of Triangle are")
# tr.printside()
#
# # /---------------------------------------------------------------------------------------/
# q2:
# class halwa:
#     a=""
#     def gets(self):
#         self.a=input("Enter The String")
#         return (self.a)
# ha=halwa()
# print("THE INPUT STRING IS" ,ha.gets())
#
# # /---------------------------------------------------------------------------------------------/
#
# q3:
# class Rectangle:
#     w=0.0
#     l=0.0
#     def calper(self):
#         self.l=int(input("Enter The Length"))
#         self.w=int(input("Enter The width"))
#         return (2*(self.l+self.w))
# r1=Rectangle()
# print("The Perimeter of Rectangle is",r1.calper())
# # /----------------------------------------------------------------------------------------------/
#
# q4:
# class Circle:
#     rad=0.0
#     def _init_(self):
#         self.rad=float(input("Enter The Radius"))
#     def areac(self):
#         return (3.14*self.rad*self.rad)
#     def perr(self):
#         return (2*3.14*self.rad)
# c1=Circle()
# print("The Area Of circle is" ,c1.areac())
# print("The Perimeter of rect is" , c1.perr())
#
# class Circle2:
#     rad=0.0
#     def _init_(self):
#         self.rad=float(input("Enter The Radius"))
#     def areac(self):
#         return (3.14*self.rad*self.rad)
#     def circum(self):
#         return (2*3.14*self.rad)
# c2=Circle2()
# print("The Area Of circle is" ,c2.areac())
# print("The Perimeter of rect is" , c2.perr())
#
# class Temp:
#     f=0.0
#     c=0.0
#     def convf(self):
#         self.f=int(input("Enter the Temp in F"))
#         return ((self.f-32)/1.8)
#     def convc(self):
#         self.c=int(input("Enter The Temp in c"))
#         return ((self.c*1.8)+32)
# te=Temp()
# print("The Conversion of F to C is",te.convf())
# print("The Conversion of C to F is", te.convc())
# /-----------------------------------------------------------------------------------------------/

# Q5:-
# # Write a Python program to demonstrate multiple Inheritance.
# #
# # class Class1:
# #     def m(self):
# #         print("Thor")
# #
# #
# # class Class2(Class1):
# #     def m(self):
# #         print("Captain America")
# #
# #
# # class Class3(Class1):
# #     def m(self):
# #         print("Thanos")
# #
# #
# # class Class4(Class2, Class3):
# #     def m(self):
# #         print("Iron Man")
# #
# #
# # obj = Class4()
# # obj.m()
# #
# # Class2.m(obj)
# # Class3.m(obj)
# # Class1.m(obj)
#