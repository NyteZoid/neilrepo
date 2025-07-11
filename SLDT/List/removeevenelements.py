#start
L=eval(input("Enter list"))
for x in L:
    if x%2==0:
        L.remove(x)
print(L)
#end
