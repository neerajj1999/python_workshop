# # Q5:-
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
# # //////////////////////////////////////////////////////////////////////////////////////////////
#
#
# # Q4:-
# #   Write a Python program to demonstrate Inheritance and method overriding.
# #
# # class Parent1():
# #
# #     def show(self):
# #         print("Parent 1 statement ")
# #
# # class Parent2():
# #
# #     def display(self):
# #         print("Parent 2 statment ")
# #
# # class Child(Parent1, Parent2):
# #
# #     def show(self):
# #         print(" child statment ")
# #
# #
# # obj = Child()
# #
# # obj.show()
# # obj.display()
#
# #/////////////////////////////////////////////////////////////////////////////////////////////////////
#
# # Q3:-
# #    Write a Python program to demonstrate classes and their attributes.
#
# #
# # class Dog:
# #
# #     attr1 = "mamal"
# #     attr2 = "dog"
# #
# #     def fun(self):
# #         print("I'm a", self.attr1)
# #         print("I'm a", self.attr2)
# #
# # Rodger = Dog()
# #
# # print(Rodger.attr1, Rodger.attr2)
# # print(Rodger.fun())
#
# # //////////////////////////////////////////////////////////////////////////////////////////////////////////
# # Q2:-
# # Write a Python program to create a class Employee.Define two subclasses:Engineer and Manager.Every class should have method named printDesignation() that prints Engineer for Engineer class and Manager for Manager Class.
# #
# #
# # class Employee():
# #     name = "employee"
# #     def printdesignation(self):
# #         print("I'm a",self.name)
# #
# # class Engineer():
# #     name = "Engineer"
# #
# #     def printdesignation(self):
# #         print("I'm a",self.name)
# #
# # class Manager():
# #     name = "Manager"
# #
# #     def printdesignation(self):
# #         print("I'm a",self.name)
# #
# # com_1 = Employee()
# # print(com_1.printdesignation())
# #
# # com_2 =Manager()
# # print(com_2.printdesignation())
# #
# # com_3 = Engineer()
# # print(com_3.printdesignation())
#
# # \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
# #
# # Q1:-
# #      Write a Python program that has a class Animal with a method legs(). Create two
# # subclasses Tiger and Dog, access the method leg explicitly with class Dog and implicitly
# # with the class Tiger.
#
# class animal:
#     def legs(self):
#         print("Animals have four legs")
#
# class tiger(animal):
#     pass
#
# class dog(animal):
#     animal().legs()
#
# tiger().legs()
