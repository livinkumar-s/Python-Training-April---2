# neweFile=open("teaxt.txt","x")
# print(neweFile)
# neweFile.close()

# file = open("teaxt.txt",'r')
# # content=file.read(5)
# # content=file.read(5)
# # content=file.read(5)
# # content=file.readline()
# # content=file.readline()
# # content=file.readline()
# content=file.readlines()[1]

# print(content)
# file.close()


# # Write
# file = open("text.txt","w")

# content='''Hello
# Hi
# Good morning'''

# file.write(content)

# file.close()


# Write
# file = open("text.txt","a")

# content='''
# Hello
# Hi
# Good morning'''

# file.write(content)

# file.close()

# try:
#     with open("text.txt") as t:
#         print(t.read(5))
#         print(t.tell())
#         t.seek(0)
#         print(t.read(5))
# except FileNotFoundError:
#     print("No File Found")

import os 
os.remove("text.txt")
