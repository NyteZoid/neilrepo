#start
s=input("Enter sentence")
L=s.split()
d={}
for x in L:
    n=len(x)
    d.update({x:n})
print(d)
#end
