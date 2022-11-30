
class CircleToken():
    """This class instanciate a circle token with the following parameters:
    -  pos_X and pos_Y : row and column position of the token
    - color : color of the token
    - player_id : identifier of the player who owns the token
    - token_id : identifier of the token"""
    def __init__(self, pos_X, pos_Y, color, player_id, token_id):

        self.pos_X = pos_X
        self.pos_Y = pos_Y
        self.color = color
        self.player_id = player_id
        self.token_id = token_id