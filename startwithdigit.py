#start
s=input("Enter a sentence")
L=s.split()
for x in L:
    if x[-1].isdigit()==True:
        print(x)
#end
