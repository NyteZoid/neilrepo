#start
def fact(n):
    F=1
    for x in range(1,n+1):
        F=F*x
    print(F)
fact(5)
fact(3)
p=int(input("Enter a number"))
fact(p)
#end
