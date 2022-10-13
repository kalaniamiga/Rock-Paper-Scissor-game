from rock_paper_scissor import get_player_choice
from rock_paper_scissor import get_computer_choice
from rock_paper_scissor import is_draw
from rock_paper_scissor import player_choice
from rock_paper_scissor import computer_choice
from rock_paper_scissor import print_winner


import mock
import builtins
import sys

 

def test_user_input_R():
    with mock.patch.object(builtins, 'input', lambda _: 'R' ):
        assert get_player_choice() == 'r'
        
def test_user_input_r():
    with mock.patch.object(builtins, 'input', lambda _: 'r'):
        assert get_player_choice() == 'r'

def test_user_input_P():
    with mock.patch.object(builtins, 'input', lambda _: 'P'):
        assert get_player_choice() == 'p'

def test_user_input_p():
    with mock.patch.object(builtins, 'input', lambda _: 'P'):
        assert get_player_choice() == 'p'

def test_user_input_S():
    with mock.patch.object(builtins, 'input', lambda _: 'S'):
        assert get_player_choice() == 's'

def test_user_input_s():
    with mock.patch.object(builtins, 'input', lambda _: 's'):
        assert get_player_choice() == 's'

def test_user_input_Q():
    with mock.patch.object(builtins, 'input', lambda _: 'Q'):
        assert get_player_choice() == 'q'

def test_user_input_q():
    with mock.patch.object(builtins, 'input', lambda _: 'Q'):
        assert get_player_choice() == 'q'

def test_computer_choice():
    assert get_computer_choice() == 'r' or 'p' or 's'

def test_player_wins(capsys):
    print_winner(player_choice,computer_choice) 
    if player_choice == 'r' and computer_choice == 's':
        captured = capsys.readouterr() 
        assert captured.out == "Player wins!"

def test_player_wins2(capsys):
    print_winner(player_choice,computer_choice) 
    if player_choice == 's' and computer_choice == 'p':
        captured = capsys.readouterr() 
        assert captured.out == "Player wins!"
 
def test_player_wins3(capsys):
    print_winner(player_choice,computer_choice) 
    if player_choice == 'p' and computer_choice == 'r':
        captured = capsys.readouterr() 
        assert captured.out == "Player wins!"

def test_player_wins3(capsys):
    print_winner(player_choice,computer_choice) 
    if player_choice == 's' and computer_choice == 'r':
        captured = capsys.readouterr() 
        assert captured.out == "Computer wins!"


test_user_input_R()
test_user_input_r()
