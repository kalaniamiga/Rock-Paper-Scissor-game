from rock_paper_scissor import get_player_choice
import mock
import builtins

 

def test_user_input_r():
    with mock.patch.object(builtins, 'input', lambda _: 'R'):
        assert get_player_choice() == 'r'

def test_user_input_p():
    with mock.patch.object(builtins, 'input', lambda _: 'P'):
        assert get_player_choice() == 'p'

def test_user_input_s():
    with mock.patch.object(builtins, 'input', lambda _: 'S'):
        assert get_player_choice() == 's'

def test_user_input_q():
    with mock.patch.object(builtins, 'input', lambda _: 'Q'):
        assert get_player_choice() == 'q'

 