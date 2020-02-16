from service.Game import *

class Console:
    def __init__(self, game):
        self.__game=game

    def start_ui(self):
        while True:
            cmd=input("Input your command! <play> <instructions> or <exit>")
            if cmd == "play":
                self.__game.clear_board()
                while True:
                    print(self.__game.print_game())
                    ok=False
                    while ok==False:
                        cmd2=input("Please enter the column you want to add a piece to.")
                        if cmd2.isdigit():
                            ok=True
                            cmd2=int(cmd2)
                        else:
                            print("Please enter an integer!!")
                    x=self.__game.make_move(cmd2-1, "1")
                    if x != False:
                        if self.__game.check_player_victory():
                            print(self.__game.print_game())
                            print ("Victory for player!")
                            break
                        if self.__game.check_if_draw():
                            print("Draw!")
                            break
                        self.__game.computer_move()
                        if self.__game.check_computer_victory():
                            print(self.__game.print_game())
                            print("Victory for computer!")
                            break
                        if self.__game.check_if_draw():
                            print("Draw!")
                            break
            elif cmd == "instructions":
                print("The objective of the game is to be the first to place four pieces in a horizontal, vertical or diagonal line.\nThe pieces fall straight down, occupying the lowest free space on the column.\nIn this version of the game, 0 represents an empty space, 1 is the player's piece and 2 is the computer's piece")
            if cmd == "exit":
                return