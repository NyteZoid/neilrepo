#start

n = input("Enter number")
a = input("Enter old digit")
b = input("Enter new digit")
new = ""
for x in n:
    if x != a:
        new = new + x
    else:
        new = new + b

print(new)

#end
    
