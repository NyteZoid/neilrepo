#start
x=10
print(x)
def func():
    global x
    x=30
    print(x)
func()
print(x)
#end
