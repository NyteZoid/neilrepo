#start

stack = []

def showStack():
    print(stack)

def pushStack():
    def pushElem():
        n = int(input("What type of element do you wish to push?\nPress 1 for single element\nPress 2 for list\nPress 3 for dictionary: "))
        if n == 1:
            o = int(input("Which type of value do you wish to push?\nPress 1 for integer\nPress 2 for string: "))
            if o == 1:
                x = int(input("Enter number to be pushed: "))
            elif o == 2:
                x = input("Enter sentence to be pushed: ")
            else:
                print("Invalid choice")
            stack.append(x)
            print("Value pushed succesfully")
        elif n == 2:
            x = eval(input("Enter list to be pushed: "))
            stack.append(x)
            print("List pushed succesfully")
        elif n == 3:
            x = eval(input("Enter dictionary to be pushed: "))
            stack.append(x)
            print("Dictionary pushed succesfully")
        else:
            print("Invalid choice")
        b = int(input("Do you wish to push any more elements? Press 1 for yes, 2 for no: "))
        if b == 1:
            pushElem()
    pushElem()

def popStack():
    def popElem():
        n = int(input("How many elements do you wish to pop from the stack: "))
        for x in range(n):
            if len(stack) > 0:
                print(stack.pop(),"has been popped")
            else:
                print("Stack empty")
        showStack()
        b = int(input("Do you wish to pop any more elements? Press 1 for yes, 2 for no: "))
        if b == 1:
            popElem()
    popElem()

pushStack()

while True:
    m = int(input("Press 1 to push new elements\nPress 2 to pop existing elements\nPress 3 to display stack\nPress 4 to exit: "))
    if m == 1:
        pushStack()
    elif m == 2:
        popStack()
    elif m == 3:
        showStack()
    elif m == 4:
        print("Thanks for using this app")
        break
    else:
        print("Invalid choice")

#end