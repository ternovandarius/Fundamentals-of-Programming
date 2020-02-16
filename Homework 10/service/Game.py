from random import *
from domain.PieceValidator import *

class Game:
    def __init__(self, board, validator):
        self.__board = board
        self.__validator = validator

    def print_game(self):
        '''
        This function prints the matrix representing the board.
        '''
        return self.__board

    def clear_board(self):
        '''
        This function clears the board for a new game.
        '''
        self.__board.clear_board()

    def fill_board(self):
        '''
        This function fills the board for testing purposes.
        '''
        return self.__board.fill_board()

    def make_move(self, move, p):
        '''
        This function checks whether a move is possible, and if it is, it adds the p piece to the board. It also returns
        True or False depending on whether the move was possible or not.
        Input: move, p
        Preconditions: move - int representing desired column, p - "1" for user piece or "2" for computer piece
        Output:
        '''
        move=int(move)
        if move < 0 or move > 6:
            print ("Invalid move! Select a column between 0 and 6.")
            return False
        else:
            row = self.__board.verify_column(move)
            if row != -1:
                piece=Piece(row, move, p)
                self.__validator.validate(piece)
                self.__board.add_piece(piece)
                return True
            else:
                print("Invalid move! No more space on the column.")
                return False

    def check_player_victory(self):
        '''
        This function returns True or False, depending on whether the player has won the game or not.
        '''
        return self.__board.check_victory("1")

    def check_computer_victory(self):
        '''
        This function returns True or False, depending on whether the computer has won the game or not.
        '''
        return self.__board.check_victory("2")

    def computer_move(self):
        '''
        This function represents the computer's tactics.
        It first checks whether it is close to victory, and if so, it makes the winning move.
        If not, it checks whether the player is close to victory and attempts to block them.
        If none of these cases are true, it moves randomly.
        '''
        #first checks if it is close to victory
        x=self.__board.check_if_near_victory("2")
        #if x is (-1, -1), then it is not, if not, it makes the winning move
        x[0]=int(x[0])
        x[1]=int(x[1])
        if x[0]!=-1:
            y=self.make_move(x[1], "2")
        else:
            x=self.__board.check_if_near_victory("1")
            x[0]=int(x[0])
            x[1]=int(x[1])
            if x[0]!=-1:
                y=self.make_move(x[1], "2")
            else:
                #if self.__board.check_if_no_computer_piece():
                a=randint(0, 6)
                b=False
                while b==False:
                    b=self.make_move(a, "2")

    def check_if_draw(self):
        '''
        This function checks whether the game is a draw.
        Output: returns True if draw, False otherwise
        '''
        return self.__board.check_if_draw()
