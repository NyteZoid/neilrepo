#start
import pickle

def SAVE():
    F=open("stud.dat","wb")
    for x in range(3):
        r=int(input("Enter roll"))
        nm=input("Enter name")
        m=int(input("Enter marks"))
        data=[r,nm,m]
        pickle.dump(data,F)
    F.close()

def UPDATE():
    F=open("stud.dat","rb")
    c=0
    roll=int(input("Enter roll number to be updated"))
    try:
        while True:
            data=pickle.load(F)
            if data[0]==roll:
                data[2]=int(input("Enter new marks"))
                c=c+1
    except:
        if c>0:
            F.close()
            F=open("stud.dat","ab")
            pickle.dump(data,F)
            print("Succesful")
        else:
            print("Does not exist")
        F.close()
SAVE()
UPDATE()
#end
                
