#start
s=input("Enter string")
L=s.split()
a=0
for x in L:
    if x.upper() in "IS":
        a=a+1
print("the word is appears",a,"times")
#end
        
