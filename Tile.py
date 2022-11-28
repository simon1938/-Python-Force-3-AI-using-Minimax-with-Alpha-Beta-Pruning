class Tile:
    def __init__(self, pos_X, pos_Y, squaretoken):
        self.pos_X = pos_X
        self.pos_Y = pos_Y
        self.squaretoken = squaretoken

    def issquaretoken(self):
        return self.squaretoken