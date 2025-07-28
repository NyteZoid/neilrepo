#start

st = []

def Push(SItem):
    c=0
    for (k,v) in SItem.items():
        if v > 75:
            st.append(k)
            c=c+1
    print("The count of elements in the stack is",c)

s = eval(input("Enter dictionary of items: "))
Push(s)

#end