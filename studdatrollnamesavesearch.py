#start
import pickle
F=open("stud.dat","ab")
for x in range(3):
    r=int(input("Enter roll no."))
    n=input("Enter name")
    data=[r,n]
    pickle.dump(data,F)
F.close()
F=open("stud.dat","rb")
c=0
roll=int(input("Enter roll no. to be searched"))
try:
    while True:
        data=pickle.load(F)
        if data[0]==roll:
            rec=data[1]
            c=c+1
except:
    if c>0:
        print(rec)
    else:
        print("Doesn't exist")
    F.close()
#end
            
