# a="Hello guys"

# print(a[-2:])
# print(a[:7])
# print(a[2:7])
# print(a[6:])
# print(a[:5])
# print(a[::-1])

# List 
# lis1= [
# 1,
# 2,
# 3,
# 2.2,
# 3.3,
# "Hi",
# "Hello",
# True,
# False,
# 2,2
# ]
# print(len(lis1))
# print(lis1[-4])
# print(lis1[5:6]) #[]

# lis1[2]=33
# print(lis1)


# newLis=[]

# for i in lis2:
#     if i not in newLis:
#         newLis.append(i)

# print(newLis)


# lis2.append(99)
# lis2.append(999)

# lis2.insert(5,0)
# lis2.extend([-1,-2,-3])

# lis2.append("Hello")
# lis2.remove(2)
# lis2.pop(2)
# lis2.pop()
# lis2= [234,234,24,2,2]

# lis2.pop()
# print(lis2.index(5))
# print(lis2.index(334))

# lis2.sort(reverse=1)

# print(lis2[::-1])

# print("A" not in "Apple")

# Tuple 

# t1=(1,2,3,4,3,2,1,"Hi","Good",True, False)

# t1[2]=33

# print(t1.index(1))
# print(t1.count(1))

# person1=("ken",45,"FED")
# name = person1[0]
# age = person1[1]
# job = person1[2]

# name,age,job=person1

# print(age)

# Set 

# set1={1,1,1,2,3,4,5,67,0}
# set2={3,4,5,6,7,8,9}
# set1.add(90)
# set1.remove(1)
# print(set1)
# print(set1[2])
# set1[4]=3
# for i in set1:
#     print(i)

# print(set1.union(set2))
# print(set1.intersection(set2))
# print(set1.difference(set2))
# print(set2.difference(set1))

# Dict 

# d1={
#     "name":"Leo",
#     "age":52,
#     "job":"FSD"
# }

# d1["age"]=20
# d1["isMarried"]=True

# del d1["age"]

# print(d1.keys())
# print(d1.values())
# print(d1.items())
# print(d1)

# Strings

# str1="Hello"
# str1[3]="x"
# str1=str1+"123" #new string
# print(str1)

# l1=[1,2,3,4,5]
# l1.append(9)
# print(l1)

person1=[
    1,
    2,
    3,
    [
        4,
        5,
        6,
        [
            "six",
            "seven",
            "eight"
        ]
    ]
]
# print(len(person1))
# print(person1[-1][-1][-1][-1])

# t1=(1,2,3,4,5)
# print(list(t1))

list1=[432,54,34,4,45,234,243,3,243,243,243]
print(list(set(list1)))