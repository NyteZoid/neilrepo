#start
def countnow(places):
    L=places.values()
    for x in L:
        if len(x)>5:
            print(x.upper())
d=eval(input("Enter dictionary"))
countnow(d)
#end
