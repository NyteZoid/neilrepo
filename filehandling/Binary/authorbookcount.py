#start

import pickle as pk

def createFile():
    with open("books.dat","ab") as F:
        z=int(input("How many records do you want to input? "))
        for x in range(z):
            bookno = int(input("Enter book number: "))
            bookname = input("Enter book name: ")
            author = input("Enter author name: ")
            price = float(input("Enter price: "))
            data = [bookno,bookname,author,price]
            pk.dump(data,F)
            print("Record added succesfully")

def CountRec(Author):
    with open("books.dat","rb") as F:
        c=0
        try:
            while True:
                data = pk.load(F)
                if data[2] == Author:
                    c=c+1
        except:
            print("The author has written",c,"books in this list")

createFile()

s=input("Which author would you like to search? ")
CountRec(s)

#end