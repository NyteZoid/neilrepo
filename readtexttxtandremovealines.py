#start
def SAVE():
    F=open("save.txt","w")
    while True:
        s=input("Enter sentence")
        F.write(s+"\n")
        b=int(input("Enter 1 to write more, 2 to exit"))
        if b==2:
              break
    F.close()
    
def REWRITE():
    F=open("save.txt")
    G=open("newsave.txt","w")
    L=F.readlines()
    for x in L:
        if "a" not in x and "A" not in x:
            G.write(x)
    F.close()
    G.close()

SAVE()
REWRITE()
#end

