#start

import mysql.connector as sqlconn

myconn = sqlconn.connect(
    host="localhost",
    user="root",
    password="********",
    database="uwu"
)
if myconn.is_connected():
    print("Connection succesful")
else:
    print("Connection not succesful")

mycursor = myconn.cursor()

def show():
    mycursor.execute("SELECT * FROM STUDENT")
    data = mycursor.fetchall()
    count = mycursor.rowcount
    print("total no. of rows:",count)
    for row in data:
        print(row)

def insert():
    a = int(input("Do you wish to input any new records? Press 1 for yes, 2 for no: "))
    def newrec():
        if a == 1:
            sql = "INSERT INTO STUDENT (id,name,stream,marks) VALUES (%s,%s,%s,%s)"
            i = int(input("Enter student id: "))
            nm = input("Enter student name: ")
            st = input("Enter stream: ")
            mk = int(input("Enter marks: "))
            val = (i,nm,st,mk)
            mycursor.execute(sql,val)
            myconn.commit()
            show()
            b = int(input("Do you wish to input any more records? Press 1 for yes, 2 for no: "))
            if b == 1:
                newrec()
    newrec()

def delete():
    a = int(input("Do you wish to delete any existing records? Press 1 for yes, 2 for no: "))
    def delrec():
        if a == 1:
            d = int(input("Enter id of the student whose record you wish to delete: "))
            sql = "DELETE FROM STUDENT WHERE id = %s"
            val = (d,)
            mycursor.execute(sql,val)
            myconn.commit()
            show()
            b = int(input("Do you wish to delete any more records? Press 1 for yes, 2 for no: "))
            if b == 1:
                delrec()
    delrec()

def update():
    a = int(input("Do you wish to update any existing records? Press 1 for yes, 2 for no: "))
    def updrec():
        if a == 1:
            o = int(input("Enter id of the student whose marks you wish to update: "))
            n = input("Enter updated marks: ")
            sql = "UPDATE student SET  marks = %s WHERE id = %s"
            val = (n,o)
            mycursor.execute(sql,val)
            myconn.commit()
            show()
            b = int(input("Do you wish to update any more records? Press 1 for yes, 2 for no: "))
            if b == 1:
                updrec()
    updrec()

show()
insert()
delete()
update()

#end
