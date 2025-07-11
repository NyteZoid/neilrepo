#start
L=eval(input("Enter list"))
for x in range(0,len(L),2):
    L[x],L[x+1]=L[x+1],L[x]
print(L)
#end
