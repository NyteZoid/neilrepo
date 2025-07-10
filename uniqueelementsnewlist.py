#start
L1=eval(input("Enter a list"))
L2=[]
for x in L1:
    if x not in L2:
        L2.append(x)
print(L2)
#end
