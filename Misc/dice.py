#start
import random
while True:
    x=random.randint(1,6)
    print(x)
    ch=input("Do you wish to continue? (y/n)")
    if ch not in "Yy":
        break
#end
