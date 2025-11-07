#start

s = input("Enter sentence: ")
if s[-1] in ".?!":
    print("Invalid sentence. Sentence must end with a punctuation")
L = s.split()
n = ""
for x in L:
    if x == x[::-1]:
        n = n + x + " "
    else:
        a = x + x[-2::-1] 
        n = n + a + " "

print(n)

#end 
        

