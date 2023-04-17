import random

print('''
game rules 
variables = rock,paper,scissors
rock vs paper --- paper wins
paper vs scissors ----- scissors wins
Scissors vs rock ------ rock wins
''')
tied=0
user_score=0
comp_score=0
for i in range(0,5):
    user_choice=input('enter ur option:')
    options=['rock','paper','scissors']
    comp_choice=random.choice(options)

    #print('user choice is ',user_choice)
    #print('computer choice is',comp_choice)

    if(user_choice==comp_choice):
        tied+=1

    elif(user_choice=='rock' and comp_choice=='paper'):
        comp_score+=1

    elif(user_choice=='paper' and comp_choice=='scissors'):
        comp_score +=1

    elif (user_choice=='scissors' and comp_choice=='rock'):
        comp_score +=1
    else:
        user_score+=1


if user_score > comp_score:
    print("score= ",user_score,'user win the game')
else:
    print("score= ",comp_score,'computer win the game')
print('total match tied ',tied)
print()
print('thankyou for participating the game')