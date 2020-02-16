from service.Game import *
from domain.PieceValidator import *
from repo.Board import *
import unittest

class testgame(unittest.TestCase):
    board=Board()
    validator=Validator()
    game=Game(board, validator)

    def setUp(self):
        unittest.TestCase.setUp(self)

    def tearDown(self):
        unittest.TestCase.tearDown(self)

    def test1(self):
        x=self.game.make_move(2,"1")
        assert x == True
        self.game.make_move(2,"1")
        self.game.make_move(2,"1")
        self.game.make_move(2,"1")
        assert self.game.check_player_victory() == True
        self.game.clear_board()
        assert self.game.check_player_victory() == False
        self.game.make_move(2, "2")
        self.game.make_move(2, "2")
        self.game.make_move(2, "2")
        self.game.make_move(2, "2")
        assert self.game.check_computer_victory() == True
        self.game.fill_board()
        assert self.game.check_if_draw() == True
        self.game.clear_board()
        '''string = "   1 2 3 4 5 6 7\n -----------------\n"
        for i in range(6):
            string = string + str(i) + "| "
            for j in range(7):
                string = string + "0" + " "
                if j == 6:
                    string = string + "|\n"
        string = string + " -----------------"
        assert self.game.print_game() == string'''
        self.game.make_move(2, "1")
        self.game.make_move(2, "1")
        self.game.make_move(2, "1")
        self.game.computer_move()
        self.game.make_move(2, "1")
        assert self.game.check_player_victory() == False