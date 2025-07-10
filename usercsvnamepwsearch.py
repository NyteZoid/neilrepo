#start
import csv

def SAVE():
    F=open("user.csv","w",newline="")
    obj=csv.writer(F)
    for x in range(3):
        userid=input("Enter user id")
        pw=input("Enter password")
        data=[userid,pw]
        obj.writerow(data)
    F.close()

def SEARCH():
    F=open("user.csv","r",newline="")
    obj=csv.reader(F)
    un=input("Enter userid to be searched")
    c=0
    for data in obj:
        if data[0].upper()==un.upper():
            p=data[1]
            c=c+1
    if c>0:
        print(p)
    else:
        print("User does not exist")
    F.close()

SAVE()
SEARCH()
#end
