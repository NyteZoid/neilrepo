#start

l1 = eval(input("Enter first row"))
l2 = eval(input("Enter second row"))
l3 = eval(input("Enter third row"))
l4 = eval(input("Enter fourth row"))
l5 = eval(input("Enter fifth row"))

l1[0] = 0
l2[1] = 0
l3[2] = 0
l4[3] = 0
l5[4] = 0

K = [l1,l2,l3,l4,l5]

for x in K:
    print(x[:], sep = " ")

#end

