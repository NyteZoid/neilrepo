#start
s=input("Enter a sentence")
L=s.split()
for x in L:
    if x[0]==x[-1]:
        print(x)
#end
