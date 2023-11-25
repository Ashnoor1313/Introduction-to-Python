import random

choices = ['Rock','Paper','Scissors']

computer = random.choice(choices)
print(choices)

player = input('player: ')
print('computer :',computer)

if player == computer:
    print('Tie')

elif player == 'Rock':
    if computer == 'Paper':
        print('You win')
    elif  computer == 'Scissors':
        print('You win')   

elif player == 'Paper':
    if computer == 'Rock':
        print('You lose') 
    elif computer == 'Scisscor':
        print('You lose')        


elif player == 'Scissors':
    if computer == 'Rock':
        print('You lose')
    elif computer == 'Paper':
        print('You win')

else:
    print('wrong choice') 
