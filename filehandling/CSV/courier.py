#start

import csv

def COURIER_ADD():
    with open("courier.csv","w",newline="") as F:
        obj = csv.writer(F)
        obj.writerow(["cid","s_name","source","destination"])
        n = int(input("How many records do you wish to input? "))
        for x in range(n):
            cid = int(input("Enter courier id"))
            s_name = input("Enter sender name")
            source = input("Enter source")
            destination = input("Enter destination")
            data = [cid,s_name,source,destination]
            obj.writerow(data)

def COURIER_SEARCH():
    with open("courier.csv","r",newline="") as F:
        obj = csv.reader(F)
        next(obj)
        d = input("Enter destinatiion")
        for x in obj:
            if x[3].upper() == d.upper():
                print(x)

COURIER_ADD()
COURIER_SEARCH()

#end