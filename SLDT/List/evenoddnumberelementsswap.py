#start
L=eval(input("Enter list"))
if len(L)%2==0:
    for x in range(0,len(L),2):
        L[x],L[x+1]=L[x+1],L[x]
else:
    for x in range(0,len(L)-1,2):
        L[x],L[x+1]=L[x+1],L[x]
print(L)
#end

