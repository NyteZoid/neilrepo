#start
print("1:Factorial \n2:Fibonacci Series")
ch=int(input("Enter your choice"))
if ch==1:
    n=int(input("Enter number"))
    f=1
    for x in range(1,n+1):
        f=f*x
    print(f)
elif ch==2:
    n=int(input("Enter number of terms"))
    a=-1
    b=1
    for x in range(1,n+1):
        c=a+b
        print(c,end=",")
        a=b
        b=c
else:
    print("Invalid choice")
#end
