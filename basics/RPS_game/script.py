# import library
import random

# functions and indentation
def get_choices():
    # variables
    player_choice = input('Enter a choice (rock, paper, scissor): ') # input functions
    options = ['rock', 'paper', 'scissors' ] # list
    computer_choice = random.choice(options)
    # dictionary
    choices = {
        'player':player_choice,
        'computer': computer_choice
    }
    
    return choices

# arguments in function
def check_win(player, computer):
    # concatenation and f - strings
    print(f'your choice: {player}\ncomputer choice: {computer}')
    # if statement
    if player == computer:
        return 'It\'s a tie!'
    elif player == 'rock':
        # refactoring
        if computer == 'scissors':
            return 'Rock smashes scissors! You win'
        else:
            return 'Paper covers rock! you lose'
    elif player == 'paper':
        if computer == 'rock':
            return 'Paper covers rock! You win'
        else:
            return 'Scissors cut paper! you lose'
    elif player == 'scissors':
        if computer == 'paper':
            return 'Scissors cut paper! You win'
        else:
            return 'Rock smashes scissors! you lose'
    

# assigning the return value of a function to a variable
choices = get_choices() # function call
p_choice = choices['player']
c_choice = choices['computer']

result = check_win(p_choice, c_choice)
print(result)


