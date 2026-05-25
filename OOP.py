class Bottle:
    name="Bottle"
    def __init__(self,color,capacity,status):
        self.color=color
        self.capacity=capacity
        self.status=status
    #instance methods
    def open(self): 
        self.status="opened"
        print("Bottle is opened..!")
    #instance methods
    def close(self):
        self.status="closed"
        print("Bottle is closed..!")
    #class method
    @classmethod
    def printName(cls):
        print(cls.name)
    # @staticmethod
    def dummy():
        print("Hello...!")


# 3 attributes 2 - methods

b1=Bottle("Red",3,"opened")
# b1.close() #Bottle.close(b1)
b1.dummy() # Botle.dummy()

# b1=Bottle()
# b2=Bottle()
# b3=Bottle()

# b1.open()
# print(b1.status)
# print(b2.status)

# a="Hello"
# b=[1,2,3,4]
# print(type(b1)) #<class "Bottle">

# b1=Bottle("Red",3,"opened")
# b2=Bottle("blue",5,"closed")

# b1.color="Pink"

# Bottle.name="Water Bottle"

# print(b1.name)
# print(b2.name)

# b1.dummy()

# b2.close()
# print(b1.status)

# class User:
#     def __init__(self, user,password):
#         self.username=user
#         self.__password=password 

#     def checkPass(self,enteredPass):
#         if self.__password==enteredPass:
#             print("Valid")
#         else:
#             print("invalid")

#     def changePass(self,oldPass,newPass):
#         if self.__password==oldPass:
#             self.__password=newPass
#             print("password changed")
#         else:
#             print("Invalid password")
    

# u1=User("Alen","12345")

# print(u1.username)
# print(u1.__password)

# u1.checkPass("12345")
# u1.changePass("12345","79045")
# u1.checkPass("12345")


# class Calculator:
#     def __init__(self):
#         self.version="1.0.0"
#     @staticmethod
#     def add(a,b):
#         print(a+b)
#     @staticmethod
#     def sub(a,b):
#         print(a-b)

# class SuperCalculator():
#     def __init__(self):
#         self.version="1.1.0"
#     @staticmethod
#     def mul(a,b):
#         print(a*b)

# class ScinceCalculator(SuperCalculator, Calculator):
#     def __init__(self):
#         self.version="1.2.0"
#     @staticmethod
#     def dev(a,b):
#         print(a/b)
#     @staticmethod
#     def add(a,b,c=0):
#         print(a+b+c)

# sc1=ScinceCalculator()
# sc1.add(3,3,30)

# class Cat:
#     @staticmethod
#     def sayHello():
#         print("Meoww")

# class Dog:
#     @staticmethod
#     def sayHello():
#         print("Barking")

# c1=Cat()
# d1=Dog()

# c1.sayHello()
# d1.sayHello()

# from abc import ABC, abstractmethod

# class Vehicle(ABC):
#     @abstractmethod
#     def start():
#         pass 

#     @abstractmethod
#     def stop():
#         pass 

# class Car(Vehicle):
#     def __init__(self):
#         self.name="Audi"
#     def start(self):
#         print("Car "+self.name+" is getting Started")
#     def stop(self):
#         print("Car "+self.name+" is getting Stopped")

# # v1 = Vehicle()
# c1=Car()
# c1.stop()