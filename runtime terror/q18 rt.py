#start

n = int(input("Enter a number: "))
s = n**2

a = n%10
b = s%10

if a == b:
    print("Automorphic number")
else:
    print("Not automorphic number")

#end
