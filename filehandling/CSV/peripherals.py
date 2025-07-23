#start

import csv

def Add_Device():
    with open("Peripheral.csv","w",newline="") as F:
        obj = csv.writer(F)
        obj.writerow(["P_id","P_name","Price"])
        n = int(input("How many records do you want to add? "))
        for x in range(n):
            P_id = int(input("Enter peripheral id: "))
            P_name = input("Enter peripheral name: ")
            Price = int(input("Enter peripheral price: "))
            data = [P_id,P_name,Price]
            obj.writerow(data)

def Count_Device():
    with open("Peripheral.csv","r",newline="") as F:
        obj = csv.reader(F)
        next(obj)
        for x in obj:
            if int(x[2]) < 1000:
                print(x)

Add_Device()
Count_Device()

#end