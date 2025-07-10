#start
s=input("Enter sentence")
L=s.split()
for x in L:
    if x[0] in "aeiouAEIOU" and x[-1] in "aeiouAEIOU":
        print(x)
#end
