import mysql.connector

mySQLConnection=mysql.connector.connect(
    host="localhost",
    user="root",
    password="12345",
    database="contactsaver"
)

print("Connection successfull")

cursor=mySQLConnection.cursor()

# cursor.execute('''CREATE TABLE contacts (
#     id SERIAL PRIMARY KEY,
#     name VARCHAR(100) NOT NULL,
#     phone VARCHAR(20)
# );''')

# print("Table Created....!")


# cursor.execute('''insert into contacts (name, phone) values (%s,%s),
# (%s,%s),
# (%s,%s);''',['Alice','97976855654','Bob', '97976855655','Charlie', '97976855656'])
# mySQLConnection.commit()

# cursor.execute("SELECT * FROM contacts WHERE id=%s",[4])
# allData=cursor.fetchall()
# print(allData)

# print("records fetched...!")

def seeAllContacts():
    cursor.execute("SELECT * FROM contacts")
    allData=cursor.fetchall()
    for x,y,z in allData:
        print(f"Name: {y}, Mobile: {z}")
    print("-------------------------------------")
    print()

def addContacts():
    name = input("Enter Contact Name: ")
    phone = input("Enter Phone Number: ")
    cursor.execute("insert into contacts (name, phone) values (%s,%s)",[name,phone])
    mySQLConnection.commit()
    print("Contact added...!")
    print("-------------------------------------")
    print()

def updateContacts():
    strTerm=f"%{input("Search contact here: ")}%" #"%56%"
    cursor.execute("SELECT * FROM contacts WHERE name like %s OR phone like %s",[strTerm,strTerm])
    allData=cursor.fetchall()
    for x,y,z in allData:
        print(f"Name: {y}, Mobile: {z}, id: {x}")

    if len(allData)>0:
        id=int(input("Choose the id: "))
        name = input("Enter Contact Name: ")
        phone = input("Enter Phone Number: ")
        cursor.execute("update contacts set name=%s, phone=%s where id=%s",[name,phone,id])
        mySQLConnection.commit()
        print("Updated successfully...!")  
    else:
        print("No concact found") 
        updateContacts()

    print("-------------------------------------")
    print()


def deleteContacts():
    pass

while True:
    inp=int(input('''0--> Exit
1-->All Contacts
2-->Add a Contact
3-->Update Contact
4-->Delete Contact
Choose an option: '''))
    if inp==0:
        break
    elif inp==1:
        seeAllContacts()
    elif inp==2:
        addContacts()
    elif inp==3:
        updateContacts()
    elif inp==4:
        deleteContacts()
    else:
        print("Invalid input")
    