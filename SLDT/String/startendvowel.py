#start
s=input("Enter a sentence")
L=s.split()
for x in L:
    if x[0] in "AEIUOaeiou" and x[-1] in "AEIOUaeiou":
        print(x)
#end
