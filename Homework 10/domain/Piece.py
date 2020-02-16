class Piece():
    def __init__(self, row, col, p):
        self.__row=row
        self.__col=col
        self.__p=p

    def get_row(self):
        return self.__row

    def get_col(self):
        return self.__col

    def get__p(self):
        return self.__p