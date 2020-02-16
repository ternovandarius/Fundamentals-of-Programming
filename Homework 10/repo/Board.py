class Board:
    def __init__(self):
        '''
        Initializes each Board object with a 7x6 matrix that will serve as the playing space.
        '''
        self.__playing_space=[['0' for i in range(7)] for j in range(6)]

    def __str__(self):
        '''
        Overrides the __str__ method in order to properly display the playing space.
        '''
        string="   1 2 3 4 5 6 7\n -----------------\n"
        for i in range (6):
            string = string + str(i) + "| "
            for j in range(7):
                string = string + str(self.__playing_space[i][j]) + " "
                if j==6:
                    string = string + "|\n"
        string = string + " -----------------"
        return string

    def clear_board(self):
        '''
        This function makes all the values in the matrix "0" in order to let the user play a new game.
        '''
        self.__playing_space = [['0' for i in range(7)] for j in range(6)]

    def fill_board(self):
        '''
        This function fills the board with "1" for test purposes.
        '''
        self.__playing_space = [['1' for i in range(7)] for j in range(6)]

    def verify_column(self, col):
        '''
        This function verifies if a specific column, "col", has any space left for another piece to be added.
        Input: col
        Preconditions: col - integer from 0 to 6
        Output: -1 or row
        Postconditions: -1 if there is no more room on the column, or row (which is the lowest row unoccupied on that column)
        '''
        row=-1
        for i in reversed(range(6)):
            if self.__playing_space[i][int(col)] == "0":
                row=i
                break
        return row

    def add_piece(self, piece):
        '''
        This function adds a piece to the playing space.
        Input: row, col, p
        Preconditions: row - integer from 0 to 6, col - integer from 0 to 7, p - "1"(if it's the player's move) or "2"(if it's the computer's move)
        Output: modifies one value of self.__playing_space with the value p
        Postconditions: -
        '''
        row=piece.get_row()
        col=piece.get_col()
        p=piece.get__p()
        self.__playing_space[int(row)][int(col)]=p

    def check_victory(self, p):
        '''
        This function checks vertically, horizontally and diagonally (2 ways upwards) whether there are four values p adjacent to each other.
        Input: p
        Preconditions: p - "1" for user piece or "2" for computer piece
        Output:True or False
        Postconditions: function returns True if it finds four adjacent p pieces, or False otherwise
        '''
        for i in reversed(range(6)):
            for j in range(7):
                c=0
                if self.__playing_space[i][j]==p:
                    #vertical check
                    if i>=3:
                        if self.__playing_space[i-1][j]==p:
                            if self.__playing_space[i-2][j]==p:
                                if self.__playing_space[i-3][j]==p:
                                    return True
                    #horizontal check
                    if j<=3:
                        if self.__playing_space[i][j+1]==p:
                            if self.__playing_space[i][j+2]==p:
                                if self.__playing_space[i][j+3]==p:
                                    return True
                    #diagonal check
                        #upwards to the right
                    if i>=3 and j<=3:
                        if self.__playing_space[i-1][j+1]==p:
                            if self.__playing_space[i-2][j+2]==p:
                                if self.__playing_space[i-3][j+3]==p:
                                    return True
                        #upwards to the left
                    if i>=3 and j>=3:
                        if self.__playing_space[i-1][j-1]==p:
                            if self.__playing_space[i-2][j-2]==p:
                                if self.__playing_space[i-3][j-3]==p:
                                    return True
        #if no 4 adjacent p were found, it returns false
        return False

    def check_if_near_victory(self, p):
        '''
        This function helps the computer check whether it, or the opponent is near victory vertically, horizontally(2 ways), or diagonally (4 ways).
        For the horizontal check, in order to avoid a case like |0011100| which can no longer be blocked, the function can also return
        a position that blocks a formation of 2 horizontal pieces.
        Input: p
        Preconditions: p - "1" for user piece or "2" for computer piece
        Output: [i, j]
        Postconditions: i = row, j = col; i and j can be -1 if no near victory case exists
        '''
        for i in reversed(range(6)):
            for j in range(7):
                c=0
                if self.__playing_space[i][j]==p:
                    #vertical check
                    if i>=3:
                        if self.__playing_space[i-1][j]==p:
                            if self.__playing_space[i-2][j]==p:
                                if self.__playing_space[i-3][j]=="0":
                                    return [i-3, j]
                    if j<=3:
                        if self.__playing_space[i][j+1]==p:     #horizontal to the right
                            if self.__playing_space[i][j+2]==p:
                                if self.__playing_space[i][j+3]=="0":
                                    if i<=4:
                                        if self.__playing_space[i+1][j+3]!="0":
                                            return [i, j+3]
                                    else:
                                        return [i, j+3]
                            else:
                                if self.__playing_space[i][j+2]=="0":
                                    if i<=4:
                                        if self.__playing_space[i+1][j+2]!="0":
                                            return [i, j+2]
                                    else:
                                        return [i, j+2]
                    if j>=3:
                        if self.__playing_space[i][j-1]==p:     #horizontal to the left
                            if self.__playing_space[i][j-2]==p:
                                if self.__playing_space[i][j-3]=="0":
                                    if i<=4:
                                        if self.__playing_space[i+1][j-3]!="0":
                                            return [i, j-3]
                                    else:
                                        return [i, j-3]
                            else:
                                if self.__playing_space[i][j-2]=="0":
                                    if i<=4:
                                        if self.__playing_space[i+1][j-2]!="0":
                                            return [i, j-2]
                                    else:
                                        return [i, j-2]
                    if i>=3 and j<=3:
                        if self.__playing_space[i-1][j+1]==p:
                            if self.__playing_space[i-2][j+2]==p:
                                #then it has determined that the player is close to winning, but needs to see if spaces under are occupied
                                if self.__playing_space[i-3][j+3]=="0":
                                    if self.__playing_space[i-2][j+3]==p or self.__playing_space[i-2][j+3]=="1":
                                        return [i-3, j+3]
                    if i>=3 and j>=3:
                        if self.__playing_space[i-1][j-1]==p:
                            if self.__playing_space[i-2][j-2]==p:
                                #see if spaces below are occupied, if not, try to fill them
                                if self.__playing_space[i-3][j-3]=="0":
                                    if self.__playing_space[i-2][j-3]==p or self.__playing_space[i-2][j-3]=="1":
                                        return [i-3, j-3]
                    if i <= 2 and j <= 3:   ##diagonal down-right
                        if self.__playing_space[i + 1][j + 1] == p:
                            if self.__playing_space[i + 2][j + 2] == p:
                                # see if spaces below are occupied, if not, try to fill them
                                if self.__playing_space[i + 3][j + 3] == "0":
                                    if self.__playing_space[i + 2][j + 3] == p or self.__playing_space[i + 2][j + 3] == "1":
                                        return [i + 3, j + 3]
                    if i <= 2 and j >= 3:
                        if self.__playing_space[i + 1][j - 1] == p:
                            if self.__playing_space[i + 2][j - 2] == p:
                                # see if spaces below are occupied, if not, try to fill them
                                if self.__playing_space[i + 3][j - 3] == "0":
                                    if self.__playing_space[i + 2][j - 3] == p or self.__playing_space[i + 2][j - 3] == "1":
                                        return [i + 3, j - 3]
        return [-1, -1]

    def check_if_draw(self):
        '''
        This function checks whether the entire board is filled up with pieces and no player has won.
        Output: returns False if no "0"s (free spaces) are on the top row, or True otherwise (indicating a draw)
        '''
        for j in range(7):
            if self.__playing_space[0][j] == "0":
                return False
        return True