from Token import Token

class SquareToken(Token):

    def __init__(self, numberplayer: int = 0, color: bool = 1, id: int = 0, x: int = 0, y: int = 0) -> None:
        self.numberplayer = numberplayer
        self.color = color
        self.id = id
        self.x = x
        self.y = y

    def getColor(self) -> bool:
        return self.color


    def getPlayerNumber(self) -> int:
        return self.playerNumber