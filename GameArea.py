from Tile import Tile
import numpy as np


class GameArea:
    """This class instantiate a game area with the following parameters:
    - player_1: the first player
    -player_2: the second player"""
    def __init__(self):
        k = 1
        #Creating an empty game area
        self.gamearea = np.empty([3, 3], dtype=Tile)
        self.emptytile = self.gamearea[1][1]
        #Creating initial game area
        for i in range(3):
            for j in range(3):
                if i == 1 and j == 1:
                    self.gamearea[i][j] = Tile(i, j, k)
                    k += 1
                else:
                    self.gamearea[i][j] = Tile(i, j, k)
                    self.gamearea[i][j].createSquareToken()
                    k += 1
    #Display the game area
    def displayGameArea(self):
        board = ""
        for i in range(3):
            for j in range(3):
                if self.gamearea[i][j].isSquareToken():
                    board += "■ "
                else:
                    board += "▢ "
            board += "\n"
        print(board)

