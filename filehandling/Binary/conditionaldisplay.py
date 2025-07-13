#start

import pickle

def disp_Detail():
    F=open("emp.dat","rb")
    try:
        while True:
            data=pickle.load(F)
            if data[2]<25000:
                print(data)
    except:
        F.close()

#end