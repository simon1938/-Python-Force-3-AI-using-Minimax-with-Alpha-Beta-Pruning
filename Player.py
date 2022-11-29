class Player:
    """
    Instanciate a player with the following parameters:
     - playerNumber: number of the player, playerNumber = 0 or 1
     - color: color of the player (white or black)
     - pawns: table of the player's pawn on the board
    """

    def __init__(self, numberplayer: int = 0, color: bool = 0) -> None:
        self.numberplayer = numberplayer
        self.color = color
        self.pawns = []

    # returns true if the player has a circular pawn available
    def isCircularPawnAvailable(self) -> bool:
        return len(self.pawns) < 3

    """
    This function represents the action of placing a circular pawn.
    The function reduces the amout of circular pawns the player has and returns 
    the color of the circular pawn.
    """

    def placeCircularPawn(self) -> bool:
        return self.color

    # returns the number of circular pawns the player hasn't placed on the board
    def getNumberOfCircularPawnsAvailable(self) -> int:
        return 3 - len(self.pawns)

    # returns the player number
    def getPlayerNumber(self) -> int:
        return self.numberplayer