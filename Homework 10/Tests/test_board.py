from repo.Board import *
from domain.PieceValidator import *
import unittest

class testboard(unittest.TestCase):

    board=Board()

    def setUp(self):
        unittest.TestCase.setUp(self)

    def tearDown(self):
        unittest.TestCase.tearDown(self)

    def test1(self):
        assert self.board.verify_column(1)==5
        piece=Piece(5, 1, "1")
        self.board.add_piece(piece)
        assert self.board.verify_column(1)==4
        piece=Piece(4, 1, "1")
        self.board.add_piece(piece)
        assert self.board.verify_column(1)==3
        self.board.clear_board()
        assert self.board.verify_column(1)==5

    def test2(self):
        piece=Piece(5, 0, "1")
        self.board.add_piece(piece)
        piece=Piece(5, 1, "1")
        self.board.add_piece(piece)
        piece=Piece(5, 2, "1")
        self.board.add_piece(piece)
        assert self.board.check_if_near_victory("1")==[5, 3]
        piece=Piece(5, 3, "1")
        self.board.add_piece(piece)
        assert self.board.check_victory("1")==True
        self.board.fill_board()
        assert self.board.check_if_draw()==True