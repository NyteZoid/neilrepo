#start

status = []

def Push_Element():
    L=eval(input("Enter list of lists: "))
    for x in L:
        if x[2].upper()=="GOA":
            status.append([x[0],x[1]])

def Pop_Element():
    while len(status) > 0:
        print(status.pop())
    else:
        print("Stack empty")
    
Push_Element()
Pop_Element()

#end