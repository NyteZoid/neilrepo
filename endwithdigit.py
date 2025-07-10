#start
s=input("Enter sentence")
L=s.split()
for x in L:
    if x[-1].isdigit()==True:
        print(x)
#end
