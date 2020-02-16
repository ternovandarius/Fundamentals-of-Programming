from repo.Board import *
from domain.PieceValidator import *
from ui.Console import *

board = Board()
validator = Validator()
game = Game(board, validator)
console = Console(game)

console.start_ui()