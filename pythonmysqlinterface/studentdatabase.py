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

def showTab():
    mycursor.execute("SELECT * FROM STUDENT")
    data = mycursor.fetchall()
    count = mycursor.rowcount
    print("total no. of rows:",count)
    for row in data:
        print(row)

def insTab():
    def newRec():
        sql = "INSERT INTO STUDENT (id,name,stream,marks) VALUES (%s,%s,%s,%s)"
        i = int(input("Enter student id: "))
        nm = input("Enter student name: ")
        st = input("Enter stream: ")
        mk = int(input("Enter marks: "))
        val = (i,nm,st,mk)
        mycursor.execute(sql,val)
        myconn.commit()
        showTab()
        b = int(input("Do you wish to input any more records? Press 1 for yes, 2 for no: "))
        if b == 1:
            newRec()
    newRec()

def delTab():
    def delRec():
        d = int(input("Enter id of the student whose record you wish to delete: "))
        stp = input("Press enter to confirm: ")
        if stp == "":
            sql = "DELETE FROM STUDENTS WHERE id = %s"
            val = (d,)
            mycursor.execute(sql,val)
            myconn.commit()
            showTab()
            b = int(input("Do you wish to delete any more records? Press 1 for yes, 2 for no: "))
            if b == 1:
                delRec()
    delRec()

def updTab():
    def updRec():
        o = int(input("Enter id of the student whose marks you wish to update: "))
        def updSpec():
            global s
            g = int(input("Which field do you wish to change?\nPress 1 for id\nPress 2 for name\nPress 3 for stream\nPress 4 for marks: "))
            if g == 1:
                s = "id"
            elif g == 2:
                s = "name"
            elif g == 3:
                s = "stream"
            elif g == 4:
                s = "marks"
            else:
                print("Invalid choice")
                updSpec()
        updSpec()
        n = input("Enter updated value: ")
        sql = f"UPDATE student SET {s} = %s WHERE id = %s"
        val = (n,o)
        mycursor.execute(sql,val)
        myconn.commit()
        showTab()
        b = int(input("Do you wish to update any more records? Press 1 for yes, 2 for no: "))
        if b == 1:
            updRec()
    updRec()

showTab()

while True:
    m = int(input("Press 1 to insert any new records\nPress 2 to delete any existing records\nPress 3 to update any existing records\nPress 4 to exit: "))
    if m == 1:
        insTab()
    elif m == 2:
        delTab()
    elif m == 3:
        updTab()
    elif m == 4:
        print("Thank you for using this app!")
        break
    else:
        print("Invalid choice")

#end

