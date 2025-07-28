#start

st = []

def Push(Vehicle):
    for (k,v) in Vehicle.items():
        if v.upper()=="TATA":
            st.append(k)

def Pop():
    while len(st) > 0:
        print(st.pop())
    else:
        print("UNDERFLOW")

v = eval(input("Enter dictionary of car models and their manufacturers: "))
Push(v)
Pop()

#end
