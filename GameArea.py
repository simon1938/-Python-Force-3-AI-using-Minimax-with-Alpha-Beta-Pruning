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
        for j in range(3):
            for i in range(3):
                if i == 1 and j == 1:
                    self.gamearea[i][j] = Tile(i, j, k)
                    self.emptytile = self.gamearea[i][j]
                    k += 1
                else:
                    self.gamearea[i][j] = Tile(i, j, k)
                    self.gamearea[i][j].createSquareToken()
                    k += 1
                    print(self.gamearea[i][j].isSquareToken())
    #Display the game area
    def displayGameArea(self):
        board = ""
        for j in range(3):
            for i in range(3):
                if self.gamearea[i][j].isSquareToken():
                    board += "■ "
                else:
                    board += "▢ "
            board += "\n"
        print(board)

    #Swap the place of a square token with the empty tile
    def switchTokenPosition(self, tile_1, tile_2):
        #If tile_2 is the empty tile
        if tile_2.squaretoken is None:
            tile_2.setSquareToken(tile_1.squaretoken)
            tile_1.squaretoken = None
            self.emptytile = tile_1
        #If tile_1 is the empty tile
        else:
            tile_1.setSquareToken(tile_2.squaretoken)
            tile_2.squaretoken = None
            self.emptytile = tile_1


    def moveSquareToken(self, squaretoken):
        
        if self.emptytile.tile_id == 1:
            if squaretoken.tile_id in {2,4}:
                self.switchTokenPosition(squaretoken, self.emptytile)
        elif self.emptytile.tile_id == 2:
            if squaretoken.tile_id in {1,5,3}:
                self.switchTokenPosition(squaretoken, self.emptytile)
        elif self.emptytile.tile_id == 3:
            if squaretoken.tile_id in {2,6}:
                self.switchTokenPosition(squaretoken, self.emptytile)
        elif self.emptytile.tile_id == 4:
            if squaretoken.tile_id in {1,5,7}:
                self.switchTokenPosition(squaretoken, self.emptytile)
        elif self.emptytile.tile_id == 5:
            if squaretoken.tile_id in {2,4,6,8}:
                self.switchTokenPosition(squaretoken, self.emptytile)
        elif self.emptytile.tile_id == 6:
            if squaretoken.tile_id in {3,5,9}:
                self.switchTokenPosition(squaretoken, self.emptytile)
        elif self.emptytile.tile_id == 7:
            if squaretoken.tile_id in {4,8}:
                self.switchTokenPosition(squaretoken, self.emptytile)
        elif self.emptytile.tile_id == 8:
            if squaretoken.tile_id in {5,7,9}:
                self.switchTokenPosition(squaretoken, self.emptytile)
        else:
            if squaretoken.tile_id in {6,8}:
                self.switchTokenPosition(squaretoken, self.emptytile)
