# def printSteps():
#     print(1)
#     print(2)
#     print(3)
#     print(4)
#     print(5)

# printSteps()
# printSteps()
# printSteps()

# print(90)
# printSteps()
# print(100)

# def sum(a,b):
#     print(a)
#     print(b)
#     print(a+b)

# sum(4,5)
# sum(44,59)

# sum(b=6,a=66)

# def mul(x,y=10):
#     print(x*y)

# mul(8,7)

# def addAll(a,b,c):
#     print(a+b+c)

# addAll(4,5,6,5)

# def addAll(*num):
#     ans=1
#     for i in num:
#         ans*=i 
#     print(ans)

# addAll(5,5,2,2)

# print(sum([1,2,3,4,5]))

# def getUserDetails(**person):
#     print(person)

# getUserDetails(name="Naveen",age=22,job="FED")


# def dummy():
#     print("Step1")
#     print("Step2")
#     print("Step3")
#     return "Stupid"
#     print("Step4")
#     print("Step5")

# ans=dummy()
# print(ans)

# def add(a,b):
#     print(a+b) 

# print(add(2,2))

# lis1=[1,2,3,2,1]
# lis2=[1,2,3,2,1]

# print(lis1 is not lis2)

# lis1.reverse()

# print(lis1[::-1])

# print(lis1)

# if lis1==lis1[::-1]:
#     print("Palindrome")
# else:
#     print("No Pal")

# a=10
# b=10

# print(lis1==lis2)
# print(a is b)


# a=15

# def func1():
#     # global a
#     a=6
#     print(a)

# func1()
# print(a)

# age=22

# def incAge():
#     global age
#     age=age+1 # trying to create new local scoped var with name age
#     print(age)

# incAge()
# incAge()
# incAge()
# incAge()
# incAge()
# print(age)

# def outer():
#     def inner1():
#         print("Hi from one..!")
#     def inner2():
#         print("Hi from 2")
    


# outer()


# def sayHello():
#     print("Hello")
#     sayHello()

# sayHello()

# import sys

# print(sys.getrecursionlimit())
# sys.setrecursionlimit(10000)

# def count(n):
#     if n==0:
#         print("Done")
#     else:
#         print(n)
#         count(n-1)

# count(5000)

# count(5) --> 5
# count(4)  --> 4
# 3 --> 3
# 2 --> 2
 # 1 --> 1
 # 0 --> Done