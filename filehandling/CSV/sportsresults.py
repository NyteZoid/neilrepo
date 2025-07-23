#start

import csv

def Accept():
    with open("Result.csv","w",newline="") as F:
        obj = csv.writer(F)
        obj.writerow(["St_Id","St_Name","Game_Name","Result"])
        n = int(input("How many records do you want to enter"))
        for x in range(n):
            St_Id = int(input("Enter student id: "))
            St_Name = input("Enter student name: ")
            Game_Name = input("Enter game name: ")
            Result = input("Enter result: ")
            data = [St_Id,St_Name,Game_Name,Result]
            obj.writerow(data)

def wonCount():
    with open("Result.csv","r",newline="") as F:
        obj = csv.reader(F)
        next(obj)
        c=0
        for x in obj:
            if x[3].upper() == "WON":
                c=c+1
        print(c)

Accept()
wonCount()

#end