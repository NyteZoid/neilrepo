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
    def newrec():
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
    def delrec():
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
    def updrec():
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

while True:
    m = int(input("Press 1 to insert any new records\nPress 2 to delete any existing records\nPress 3 to update any existing records\nPress 4 to exit: "))
    if m == 1:
        insert()
    elif m == 2:
        delete()
    elif m == 3:
        update()
    elif m == 4:
        break
    else:
        print("Invalid choice")

#end
