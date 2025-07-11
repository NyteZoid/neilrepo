#start
F=open("file.txt")
L=F.readlines()
for x in L:
    y=x.split()
    for n in y:
        if "#" in n:
            print(n)
F.close()
#end
