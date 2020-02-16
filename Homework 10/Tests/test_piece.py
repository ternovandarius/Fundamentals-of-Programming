from domain.PieceValidator import *
import unittest

class testpiece(unittest.TestCase):

    def setUp(self):
        unittest.TestCase.setUp(self)

    def tearDown(self):
        unittest.TestCase.tearDown(self)

    def test_piece(self):
        piece=Piece(0, 2, "1")
        assert piece.get_row()==0
        assert piece.get_col()==2
        assert piece.get__p()=="1"

    def test_validator(self):
        piece=Piece(0, 2, "1")
        validator=Validator()
        validator.validate(piece)
        self.assertRaises(Exception)