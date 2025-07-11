#start
L=eval(input("Enter list"))
E=[]
O=[]
for x in L:
    if x%2==0:
        E.append(x)
    elif x%2!=0:
        O.append(x)
print(E,O)
#end
