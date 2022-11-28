class Token:
    def __init__(self, color, pos_X, pos_Y):
        self.color = color
        self.pos_X = pos_X
        self.pos_Y = pos_Y

    def settokenposition(self, pos_X, pos_Y):
        self.pos_X = pos_X
        self.pos_Y = pos_Y

    def gettokenposition(self):
        return [self.pos_X, self.pos_Y]
