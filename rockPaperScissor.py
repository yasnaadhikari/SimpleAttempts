import random

list = ['Rock', 'Paper', 'Scissors']
player1 = random.choice(list)

user = input("Enter your First Name: ", )

choice = {'S':'Scissors', 'R':'Rock', 'P':'Paper'}

chance = 'Y'

while chance!='N':

    player2 = input("Select one among [R] Rock, [P] Paper and [S] Scissors: ", )
    player2=player2.upper()

    print("Rock Paper Scissors - SHOOT!")

    print("The first Player chose ", player1)
    print("You chose ", choice[player2])
        
    if player1[0] == player2:
        print("Oops, Tie!") 

    elif player1[0]=='S' and player2=='R':
        print("Congratulations, You Win! ", user)
            
    elif player1[0]=='S' and player2=='P':
        print("Sorry, You Lost! ", user)
            
    elif player1[0]=='P' and player2=='R':
        print("Sorry, You Lost! ", user)

    elif player1[0]=='P' and player2=='S':
        print("Congratulations, You Win! ", user)

    elif player1[0]=='R' and player2=='P':
        print("Congratulations, You Win! ", user)

    elif player1[0]=='R' and player2=='S':
        print("Sorry, You Lost! ", user)
    
    chance = input("Do you want to try again? If 'Yes', Type Y and if 'No', Type N: ")
    chance = chance.upper()
    if chance == "N":
        break



