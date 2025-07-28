#start

Hotel = []

def Push_Cust(L):
    for x in L:
        if x[1].upper()=="DELUXE":
            Hotel.append(x[0])

def Pop_Cust():
    while len(Hotel) > 0:
        print(Hotel.pop())
    else:
        print("UNDERFLOW")

entry = eval(input("Enter list of lists of customer entries: "))
Push_Cust(entry)
Pop_Cust()
    
#end