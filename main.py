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

round = 1
check = "0"

while check == "0":
    if round == 0:
        round = 1
    else:
        round = 0
    if player[round].isia == True:
        board, check = ai.findBestMove(board, player[round])
    else:
        check = gm.next_round(board, player[round])
    board.displayGameArea()
exit()

