from cgitb import reset
import random
import sys
import os

CHOICES = 'rpsq'
CHOICES2 = "qre"
list_computer=[]
list_user=[]
list_game_play_time=[]
player_choice = None
computer_choice = None



def get_player_choice():
    # Get user input and validate it is one of the choices above
    print('\nPick one choice from below ')
    player_choice = None
    while player_choice is None:
        player_choice = input('\n(R)ock \n(P)aper \n(S)cissors \n\n (Q)uit \n\nPick: ')
        if player_choice.lower() not in CHOICES:
            player_choice = None
    return player_choice.lower()


def get_computer_choice():
    # Have the computer pick one of the valid choices at random
    print('Computer picked a choice --- **')
    computer_choice = random.randint(0, 2)
    computer_choice = CHOICES[computer_choice]
    return computer_choice


def is_draw(player_choice, computer_choice):
    # Check if game was a draw
    if player_choice == computer_choice:
        return True


def print_winner(player_choice, computer_choice):
    # Check to see who won
    list_game_play_time.append(1)
   
    if player_choice == 'r' and computer_choice == 's':
        print('Player wins!')
        list_user.append(1)
    elif player_choice == 's' and computer_choice == 'p':
        print('Player wins!')
        list_user.append(1)
    elif player_choice == 'p' and computer_choice == 'r':
        print('Player wins!')
        list_user.append(1)
    else:
        print('Computer wins!')
        list_computer.append(1)
        print('%s beats %s' % (computer_choice, player_choice))


def play_game():
    # play the game
    computer_choice = get_computer_choice()
    player_choice = get_player_choice()

    if(player_choice == 'q'):
        print("you chose to quit the game")
        exit()
   
    if is_draw(player_choice, computer_choice):
        list_game_play_time.append(1)
        print("It's a draw, both players picked %s: " % player_choice)
    else:
        print("Computer picked: %s" % computer_choice)
        print("Player picked: %s" % player_choice)
        print_winner(player_choice, computer_choice)

    # print('computer list size %s and user list size %s game play time %s' %(len(list_computer),len(list_user),len(list_game_play_time)))


if __name__ == "__main__":
   i = True
   while i:
        if(len(list_computer) == 5 or len(list_user) == 5):
            i = False
            if len(list_computer) == 5:
                print("Computer Won !! ")
            elif len(list_user) == 5:
                print("You Won !! ")

            print('game play %s times' %(len(list_game_play_time)))   
            print("do you want Quit or Restart the game ?")
            player_choice = None
            while player_choice is None:
                player_choice = input('\n(Q)uit \nR(E)start \n\nPick: ')
                if player_choice.lower() not in CHOICES2:
                    player_choice = None
                if(player_choice == 'q'):
                    exit()
                elif(player_choice == 'e'):
                    # reset here
                    list_game_play_time.clear()
                    list_computer.clear()
                    list_user.clear()
                    i = True
                    play_game()                
                else:
                    player_choice = None
                    
                    
        
        else:
         play_game()
    


