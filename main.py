from GameArea import GameArea
from Player import Player
import GameMode as gm
from tkinter import *

player_1 = Player(1, "R")
player_2 = Player(2, "B")
board = GameArea(player_1, player_2)
board.displayGameArea()
"""
board.addCircleToken(2,0,player_1)

board.displayGameArea()
board.moveCircleToken(2,1,player_1,0)

board.displayGameArea()

board.moveCircleToken(2,2,player_1,0)
board.displayGameArea()
"""
player = [player_1, player_2]
round = 0
check = "0"



while check == "0":
    check = gm.next_round(board, player[round])
    board.displayGameArea()
    if round == 0:
        round = 1
    else:
        round = 0
exit()



