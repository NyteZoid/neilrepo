#start
a=int(input("Enter the single digit no"))
b=int(input("Enter the multi digit no"))
s=0
while b>0:
    if b%10==a:
        s=s+1
    b=b//10
if s!=0:
    print("exists and appears",s,"times")
else:
    print("does not exist")
#end

