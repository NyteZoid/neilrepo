#start
def frequency(L):
    f=0
    s=0
    for x in L:
        if x%5==0 and x%7==0:
            f=f+1
            s=s+1
        elif x%5==0:
            f=f+1
        elif x%7==0:
            s=s+1         
    print(f,s)
frequency([1,2,10,14,70,85])
#end
