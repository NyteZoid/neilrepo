#start
def freq(s):
    u=0
    l=0
    for x in s:
        if x.isupper()==True:
            u=u+1
        elif x.islower()==True:
            l=l+1
    print(u,l)
freq("wELCome")
#end
