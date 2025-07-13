#start

import pickle as pk

def SAVE():
    F=open("cand.dat","wb")
    for x in range(3):
        cid=int(input("Enter candidate id"))
        cnm=input("Enter candidate name")
        des=input("Enter designation")
        exp=float(input("Enter experience"))
        data=[cid,cnm,des,exp]
        pk.dump(data,F)
    F.close()

def UPDATE():
    F=open("cand.dat","rb")
    newl=[]
    try:
        while True:
            data=pk.load(F)
            if data[3]>10:
                data[2]="Senior Manager"
            newl.append(data)
    except:
        F.close()
        F=open("cand.dat","wb")
        for x in newl:
            pk.dump(x,F)
        F.close()

def SEARCH():
    F=open("cand.dat","rb")
    try:
        while True:
            data=pk.load(F)
            if data[2]!="Senior Manager":
                print(data)
    except:
        F.close()

SAVE()
UPDATE()
SEARCH()

#end 


