#start
def index_list(L):
    Lnew=[]
    for n in range(len(L)):
        if L[n]%2==0:
            Lnew.append(n)
    print(Lnew)
index_list([1,2,3,4,5,6,7,8,9])
#end
            
