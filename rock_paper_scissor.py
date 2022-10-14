"""This is code for Rock paper Scissor game"""
import random


CHOICES = 'rpsq'
CHOICES2 = "qre"
list_computer_wins=[]
list_user_wins=[]
list_game_play_time=[]
player_choice = None
computer_choice = None


def get_player_choice():
    '''Get user input and validate it is one of the choices below'''
    print('\nPlease pick one choice from below ') 
    player_choice = None
    while player_choice is None:
        player_choice = input('\n(R)ock \n(P)aper \n(S)cissors \n\n (Q)uit \n\nPick: ')
        if player_choice.lower() not in CHOICES:
            player_choice = None
    return player_choice.lower()

def get_computer_choice():
    '''let computer pick one choice'''
    computer_choice = random.randint(0, 2)
    computer_choice = CHOICES[computer_choice]
    print('Computer picked a choice --- **')
    return computer_choice


def is_draw(player_choice, computer_choice):
    '''return true if coputer choice is same as player choice'''
    if player_choice == computer_choice:
        return True


def print_winner(player_choice, computer_choice):
    '''condition check and increment relevent list according to the winner'''
    list_game_play_time.append(1)
    if player_choice == 'r' and computer_choice == 's':
        print('Player wins!')
        list_user_wins.append(1)
    elif player_choice == 's' and computer_choice == 'p':
        print('Player wins!')
        list_user_wins.append(1)
    elif player_choice == 'p' and computer_choice == 'r':
        print('Player wins!')
        list_user_wins.append(1)
    else:
        print('Computer wins!')
        list_computer_wins.append(1)
        print(f'{computer_choice} beats {player_choice}')


def play_game():
    '''play game '''
    computer_choice = get_computer_choice()
    player_choice = get_player_choice()

    if player_choice == 'q':
        print("you chose to quit the game")
        exit()
    if is_draw(player_choice, computer_choice):
        list_game_play_time.append(1)
        print(f"It's a draw, both players picked {player_choice}")
    else:
        print(f"Computer picked: {computer_choice}")
        print(f"Player picked: {player_choice}")
        print_winner(player_choice, computer_choice)

if __name__ == "__main__":
    i = True
    while i:
        if len(list_computer_wins) == 5 or len(list_user_wins) == 5:
            i = False
            if len(list_computer_wins) == 5:
                print("Computer Won !! ")
            elif len(list_user_wins) == 5:
                print("You Won !! ")
            print(f"Game play {(len(list_game_play_time))} times")
            print("Do you want Quit or Restart the game ?")
            player_choice_two = None
            while player_choice_two is None:
                player_choice_two = input('\n(Q)uit \nR(E)start \n\nPick: ')
                if player_choice_two.lower() not in CHOICES2:
                    player_choice_two = None
                if player_choice_two == 'q':
                    exit()
                elif player_choice_two == 'e':
                    # reset here
                    list_game_play_time.clear()
                    list_computer_wins.clear()
                    list_user_wins.clear()
                    i = True
                    play_game()
                else:
                    player_choice = None
        else:
            play_game()
            