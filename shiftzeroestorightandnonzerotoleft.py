#wap to input a list of numbers and shifts all the zeroes to the right and all the non zero numbers to the left

#start
L=eval(input("Enter a list"))
Lnew=[]
for x in L:
    if x!=0:
        Lnew.append(x)
for x in L:
    if x==0:
        Lnew.append(x)
print(Lnew)
#end
        
