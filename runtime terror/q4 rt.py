#start

import random

n = int(input("How many rounds do you want to play: "))

for x in range(n):
    c = input("Enter rock/paper/scissor: ")
    d = random.choice(["rock","paper","scissor"])
    if c == "rock":
        if d == "rock":
            print("Computer chose", d)
            print("Tie")
        elif d == "paper":
            print("Computer chose", d)
            print("You lose")
        elif d == "scissor":
            print("Computer chose", d)
            print("You win")
    elif c == "paper":
        if d == "rock":
            print("Computer chose", d)
            print("You win")
        elif d == "paper":
            print("Computer chose", d)
            print("Tie")
        elif d == "scissor":
            print("Computer chose", d)
            print("You lose")
    elif c == "scissor":
        if d == "rock":
            print("Computer chose", d)
            print("You lose")
        elif d == "paper":
            print("Computer chose", d)
            print("You win")
        elif d == "scissor":
            print("Computer chose", d)
            print("Tie")

#end

            

        
    
