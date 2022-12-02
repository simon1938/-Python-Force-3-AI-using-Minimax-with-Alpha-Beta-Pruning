from Tile import Tile
import numpy as np
import CONSTANT


class GameArea:
    """This class instantiate a game area with the following parameters:
    - player_1: the first player
    -player_2: the second player"""
    def __init__(self, player_1, player_2):
        k = 1
        # Creating an empty game area
        self.gamearea = np.empty([3, 3], dtype=Tile)
        self.emptytile = self.gamearea[1][1]
        self.player_1 = player_1
        self.player_2 = player_2
        self.previous_empty_tile_id = 100
        self.previous2_empty_tile_id = 100
        # Creating initial game area
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
    # Display the game area
    def displayGameArea(self):
        board = ""
        for j in range(3):
            board += str(j) + " "
            for i in range(3):
                if self.gamearea[i][j].isSquareToken():
                    if self.gamearea[i][j].squaretoken.isCircleToken():
                        board += str(self.gamearea[i][j].squaretoken.circletoken.color) + str(self.gamearea[i][j].squaretoken.circletoken.token_id) + " "
                    else:
                        board += "■  "
                else:
                    board += "▢  "
            board +="\n"
        print("  0  1  2")
        print(board)

    # Swap the place of a square token with the empty tile
    def switchTokenPosition(self, tile_1, tile_2):

        if tile_1.tile_id != self.previous_empty_tile_id:
            self.previous_empty_tile_id = tile_2.tile_id
            # If tile_2 is the empty tile
            if tile_2.squaretoken is None:
                # If there are circle token on tile_1
                if tile_1.squaretoken.isCircleToken():
                    x = tile_2.get_X()
                    y = tile_2.get_Y()
                    # Change (x
                    tile_1.squaretoken.circletoken.set_X(x)
                    tile_1.squaretoken.circletoken.set_Y(y)
                    tile_2.setSquareToken(tile_1.squaretoken)
                    tile_2.squaretoken.tile_id = tile_1.squaretoken.tile_id
                    tile_1.squaretoken = None
                    self.emptytile = tile_1
                else:
                    tile_2.setSquareToken(tile_1.squaretoken)
                    tile_1.squaretoken = None
                    self.emptytile = tile_1
            # If tile_1 is the empty tile
            else:
                tile_1.setSquareToken(tile_2.squaretoken)
                tile_2.squaretoken = None
                self.emptytile = tile_1
        else:
            print("You cannot return to the position of the round before")


    # Checks if the square token can go on the empty tile and places it there if possible
    def moveSquareToken(self, squaretoken):
        # If the id of the empty tile is next to the square token
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

    # Move two square tokens if possible
    def move2SquareToken(self, squaretoken_1):
        if self.previous2_empty_tile_id != squaretoken_1.tile_id:
            self.previous2_empty_tile_id = self.emptytile.tile_id
            tile_id_squaretoken_2 = self.second_squaretokenid([squaretoken_1.tile_id, self.emptytile.tile_id])
            x,y = CONSTANT.correlation[str(tile_id_squaretoken_2)]
            self.previous_empty_tile_id = 100
            self.moveSquareToken(self.gamearea[x,y])
            self.moveSquareToken(squaretoken_1)
            self.previous_empty_tile_id = 100
        else:
            print("You cannot return to the position of the round before")

    # Returns the id of the tile between the empty tile and the one that will move
    def second_squaretokenid(self, search):
        liste = CONSTANT.ga_line
        for i in range(6):
            if search[0] in liste[i] and search[1] in liste[i]:
                new_liste = liste[i]
                x, y, z = new_liste
                if x not in search:
                    return x
                elif y not in search:
                    return y
                elif z not in search:
                    return z

    # Add a circle token on a square token if it does not yet have one
    def addCircleToken(self, x, y, player):
        if player.circletoken_id <= 2:
            # If the tile is not empty
            if self.gamearea[x][y].isSquareToken():
                # If the square token carries a circle token
                if not self.gamearea[x][y].squaretoken.isCircleToken():
                    self.gamearea[x][y].squaretoken.createCircletoken(x, y, player.color, player.player_id, player.circletoken_id)
                    # Store player circle tokens in a list
                    player.circletoken.append(self.gamearea[x][y].squaretoken.getCircleToken())
                    print(player.circletoken_id)
                    player.circletoken_id += 1
                    return 1
                else:
                    print("There is already a circle token on this square token\n")
                    return 0
            else:
                print("There is no square token on this tile\n")
                return 0
        else:
            print("All of this player's circle token are already on the game area\n")
            return 0

    # Moves a circle token onto another square token if there is no circle token on it yet
    def moveCircleToken(self, new_x, new_y, player, circletoken_id):
        # If there are a square token on the new tile
        if self.gamearea[new_x][new_y].isSquareToken():
            # If there are no circle token on the new square token
            if not self.gamearea[new_x][new_y].squaretoken.isCircleToken():
                token_to_move = player.circletoken[circletoken_id]
                x = token_to_move.get_X()
                y = token_to_move.get_Y()
                self.gamearea[x][y].squaretoken.setCircleToken(None)
                self.gamearea[new_x][new_y].squaretoken.setCircleToken(token_to_move)
            else:
                print("There are already a circle token on this quare token")
        else:
            print("There are no square tokens on this tile")
