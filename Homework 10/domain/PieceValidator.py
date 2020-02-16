from domain.Piece import *

class Validator():
    def __init__(self):
        pass

    def validate(self, piece):
        errormsg=""
        if int(piece.get_row())<0 or int(piece.get_row())>5 or int(piece.get_row())=="":
            errormsg = errormsg + "Invalid row!"
        if int(piece.get_col())<0 or int(piece.get_col())>6 or int(piece.get_col())=="":
            errormsg = errormsg + "Invalid column!"
        if errormsg!="":
            raise Exception(errormsg)