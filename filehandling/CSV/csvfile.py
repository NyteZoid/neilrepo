#start
import csv
def save():
    with ("details.csv","w") as F:
        details=csv.writer(F)
        details.writerow(["Roll_No","Name","Marks"])
        while True:
            r=int(input("Enter roll no."))
            nm=input("Enter name")
            m=int(input("Enter marks"))
            ch=int(input("Enter 1 to continue, 2 to exit"))
            details.writerow[r,nm,m]
            if ch==2:
                break
save()
#end

