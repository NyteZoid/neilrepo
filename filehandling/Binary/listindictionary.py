#start
 
import pickle
def Copy_new():
    F=open("items.dat","rb")
    G=open("new_items.dat","wb")
    try:
        while True:
            data=pickle.load(F)
            for (k,v) in data:
                if v[1]>1000:
                    pickle.dump(data,G)
    except:
        F.close()
        G.close()

#end