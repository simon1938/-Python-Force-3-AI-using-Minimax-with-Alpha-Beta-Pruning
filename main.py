from GameArea import GameArea
from Player import Player
from CircleToken import CircleToken
import GameMode as gm
import NewMinmax as ai
from tkinter import *

#Choice of game mode
mode = gm.start()

#Creation of players
player_1 = Player(0, "R")
player_2 = Player(1, "B")

#Assigning ai to players
if mode == 2 or mode == 3:
    player_2.isia = True
if mode == 3:
    player_1.isia = True

player = [player_1, player_2]

#Creation of the game board
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
round = 0
check = "0"

while check == "0":
    if player[round].isia == True:
        board=ai.findBestMove(board, player[round])
    else:
        check = gm.next_round(board, player[round])
    board.displayGameArea()
    if round == 0:
        round = 1
    else:
        round = 0
exit()

