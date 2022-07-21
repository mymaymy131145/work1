print(" Welcome To My Quiz Game \n Interesting Game to Play")
Player = input(" Do you want to play the game? \n" )
if Player.lower() != 'yes':
    print("Good Bye")
    quit()  

name_player = input("Enter Your Name: ")

print("Let's Start the Game :) ",name_player)

score = 0

answer = input('How many eyes does a cat have ? \n ')
if answer.lower() == 'two':
    print("Correct")
    score += 1
else:
    print('Wrong')
 
answer = input('How many legs does a dog have? \n ')
if answer.lower() == 'four':
    print("Correct")
    score += 1
else:
    print('Wrong')

answer = input('The elephant is fat or skinny?\n ')
if answer.lower() == 'fat':
    print("Correct")
    score += 1
else:
    print('Wrong')

answer = input('How many days in a month? \n ')
if answer.lower() == (28,29,30,31):
    print("Correct")
    score += 1
else:
    print('Wrong')

answer = input('How many days are there in a week? \n ')
if answer.lower() == 'seven':
    print("Correct")
    score += 1
else:
    print('Wrong')
    
print("You got the " + str(score)+ " correct answers")
print("You got the " + str((score/5) *100)+ " correct answers")
