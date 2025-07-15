#start

import pickle as pk

def save():    #not part of the question
    with open("STUDENT.dat","wb") as F:
        z = int(input("How many records do you want to insert? "))
        for x in range(z):
            admno = int(input("Enter admission number: "))
            name = input("Enter name: ")
            prcntg = float(input("Enter percentage: "))
            data = [admno,name,prcntg]
            pk.dump(data,F)

def countRec():
    with open("STUDENT.dat","rb") as F:
        c=0
        try:
            while True:
                data = pk.load(F)
                if data[2] > 75:
                    print(data)
                    c=c+1
        except:
            print(c,"students have scored above 75%")

save()
countRec()

#end