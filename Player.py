
class Player:
    """This class instantiate a player with the following parameters:
    - player_id : identifier of the player
    - player_color : the color assigns to the player token"""
    def __init__(self, player_id, color):
        self.player_id = player_id
        self.color = color
        self.circletoken = []
        self.circletoken_id = 0

    def getnumberofcircletoken(self):
        return len(self.circletoken)