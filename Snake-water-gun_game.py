# Now we are going to make our first project 
# SNAKE , WATER & GUN
'''
0 for snake 
1 for water
2 for gun
Basic idea we are taking for making game
'''
import random

computer=random.choice([0, 1, 2])
my_choice=input("Enter your choice ")
game_dict={'s':0,"w":1,'g':2}
rev_dict={0:"snake",1:'water',2:'gun'}
my_num=game_dict[my_choice]
print(f"You chose {rev_dict[my_num]}\nComputer chose {rev_dict[computer]}")

if(computer==my_num):
    print('It is a draw')
else:
    if(computer==0 and my_num==1):
        print("You lose")
    elif(computer==0 and my_num==2):
        print("You win") 
    elif(computer==1 and my_num==0):
        print("You win") 
    elif(computer==1 and my_num==2):
        print("You lose")
    elif(computer==2 and my_num==0):
        print("You lose") 
    elif(computer==2 and my_num==1):
        print("You win")
    else:
        print("Something went wrong")
print("my 1st project of Snake,Water & Gun is ready")
                 