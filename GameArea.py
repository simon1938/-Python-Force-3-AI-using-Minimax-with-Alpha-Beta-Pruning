from Tile import Tile
import numpy as np

#gameArea is a board of Tile
class GameArea:
    def __init__(self):
        self.gamearea = np.empty([3, 3], dtype=Tile)
        for i in range(3):
            for j in range(3):
                if i == 1 and j == 1:
                    self.gamearea[i][j] = Tile(i, j, False)
                else:
                    self.gamearea[i][j] = Tile(i, j, True)

    #Afficher le plateau de jeu sur la console
    def displaygamearea(self):
        board = ""
        for i in range(3):
            for j in range(3):
                if self.gamearea[i][j].issquaretoken():
                    board += "■ "
                else:
                    board += "▢ "
            board += "\n"
        print(board)