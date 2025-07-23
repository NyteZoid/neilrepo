#start

import csv

def SAVE():
    with open("Happiness.csv","w",newline="") as F:
        obj = csv.writer(F)
        obj.writerow(["city name","population","happy population"])
        n = int(input("How many records do you want to enter? "))
        for x in range(n):
            nm = input("Enter name of city: ")
            pop = int(input("Enter total population: "))
            hap = int(input("Enter happy population: "))
            data = [nm,pop,hap]
            obj.writerow(data)

def DISPLAY():
    with open("Happiness.csv","r",newline="") as F:
        obj = csv.reader(F)
        next(obj)
        for x in obj:
            if int(x[1]) > 5000000:
                print(x)

def COUNT():
    with open("Happiness.csv","r",newline="") as F:
        obj = csv.reader(F)
        next(obj)
        c = 0
        for x in obj:
            c=c+1
        print("There are",c,"records")

SAVE()
DISPLAY()
COUNT()

#end
        