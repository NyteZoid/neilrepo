#start
s=input("Enter string")
v=0
c=0
u=0
l=0
for x in s:
    if x in "AEIOUaeiou":
        v=v+1
    elif x.isalpha():
        c=c+1
for x in s:
    if x.isupper():
        u=u+1
    elif x.islower():
        l=l+1
print(v,c,u,l)
#end
