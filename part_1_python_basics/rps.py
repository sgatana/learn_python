import random

game = ['Rock', 'Paper', 'Scissors']
entered_value = int(
    input('What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors\n'))
if (entered_value >= 3 or entered_value < 0):
    print('You typed an invalid number. You loose')
else:
    user_choice = game[entered_value]
    print(f'You choose {user_choice}')
    computer_choice = random.choice(game)
    print(f'Computer choose {computer_choice}')
    if (user_choice == computer_choice):
        print('No winner')
    elif (user_choice == 'Rock' and computer_choice == 'Scissors') or (user_choice == 'Scissors' and computer_choice == 'Paper') or (user_choice == 'Paper' and computer_choice == 'Rock'):
        print('You Win!')
    else:
        print('You loose!')
