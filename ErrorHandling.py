print(1)
print(2)
print(3)
print(4)
print(5)
# if True:
# print("Hello")
# print("A"+1)
# print(int("Hello"))
# print(b)

# try:
#     print(100/0)
# except TypeError:
#     print("Invalid concatination")

try:
    num1=int(input("Enter Number 1: "))
    num2=int(input("Enter Number 2: "))
    print(num1/num2)
except ValueError:
    print("Please provide valid input..!")
except ZeroDivisionError:
    print("Invalid expression...!")
finally:
    print("Final Statement")