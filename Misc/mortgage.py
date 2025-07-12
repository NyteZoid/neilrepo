#start

pv=float(input("Enter principal amount"))
i=float(input("Enter interest rate"))
y=float(input("Enter number of years"))
r=i/100/12
n=y*12
pmt=(pv*r*((1+r)**n))/(((1+r)**n)-1)
print("Your monthly payment is",pmt)

#end