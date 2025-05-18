# Going to make project name "PERFECT GUESS"

import random
x=random.randint(1,100)
guesses=1
y=-1
while(y!=x):
    y=int(input("Guess the number: "))
    if(y>x):
        print("Lower number please ")
        guesses+=1

    elif(y<x):
        print("Higher number please")
        

    else:
        print(f"you got the right number {y} in {guesses} number of guesses")
        break   
         

        
           


