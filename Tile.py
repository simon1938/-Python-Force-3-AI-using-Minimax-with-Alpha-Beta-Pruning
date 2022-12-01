from SquareToken import SquareToken
class Tile:
    """This class instanciates a tile of the game area which can carry a square token or not with the following parameters:
     -  pos_X and pos_Y : row and column position of the tile
     -  tile_id : identifier of the tile"""
    def __init__(self, pos_X, pos_Y, tile_id):
        self.pos_X = pos_X
        self.pos_Y = pos_Y
        self.tile_id = tile_id
        self.squaretoken = None

    #Put a square token on the tile
    def setSquareToken(self, squaretoken):
        self.squaretoken = squaretoken

    #If it carries a square token it returns it otherwise it returns the None value
    def getSquareToken(self):
        return self.squaretoken

    #Check if the tile carries a square token
    def isSquareToken(self):
        if self.squaretoken is None:
            return False
        else:
            return True

    #Creates a square token and assigns it to the tile
    def createSquareToken(self):
        self.squaretoken = SquareToken()
        return self.squaretoken

    #Set the x coordinate
    def set_X(self, new_X):
        self.pos_X = new_X

    #Set the y ccordinate
    def set_Y(self, new_Y):
        self.pos_Y = new_Y

    #Get the x coordinate
    def get_X(self):
        return self.pos_X

    # Get the y coordinate
    def get_Y(self):
        return self.pos_Y