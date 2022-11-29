from Tile import Tile
from Player import Player
import numpy as np

#gameArea is a board of Tile
class GameArea:
    def __init__(self,player1: Player, player2: Player) -> None:
        self.gamearea = np.empty([3, 3], dtype=Tile)
        for i in range(3):
            for j in range(3):
                if i == 1 and j == 1:
                    self.gamearea[i][j] = Tile(i, j, False)
                else:
                    self.gamearea[i][j] = Tile(i, j, True)

    #Afficher le plateau de jeu sur la console

    #data class GameArea
        # Variable to keep track of where the empty tile is
        self.emptyTile = self.gamearea[1][1]
        # Liste to store the players of the game
        self.players = [player1, player2]
        # variable that stores the number of the player if he wins
        self.winner = None
    # data class GameArea

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