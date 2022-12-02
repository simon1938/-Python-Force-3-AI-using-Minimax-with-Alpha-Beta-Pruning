from GameArea import GameArea
from Player import Player
import GameMode as gm
from tkinter import *
""""
class canva(Canvas):

    def __init__(self):

        # Variables

        self.cases = []  # Cases déjà remplies
        self.listerouge = []  # Liste des cases rouges
        self.listejaune = []  # Liste des cases jaunes
        self.fonce = "navy blue"


        self.canva = Canvas.__init__(self, width=165*3, height=165*3, bg=self.fonce, bd=0)
        self.grid(row=1, columnspan=5)


        # Création des cases

        self.ovals = []
        for y in range(10, 165*3, 55*3):
            for x in range(10, 165*3, 55*3):
                self.ovals.append(self.create_rectangle(x, y, x + 50*3, y + 50*3, fill="white"))


if __name__ == "__main__":
    window = Tk()
    window.title("Puissance 4")
    window.config(bg="navy blue")
    canva = canva()
    window.mainloop() """

player_1 = Player(1, "R")
player_2 = Player(2, "B")
board = GameArea(player_1, player_2)
board.displayGameArea()
for i in range(5):
    gm.next_round(board, player_1)
    board.displayGameArea()
    gm.next_round(board, player_2)
    board.displayGameArea()
    """


board.displayGameArea()
board.addCircleToken(0,1,player_2)
board.displayGameArea()
board.moveSquareToken(board.gamearea[0][1])
board.displayGameArea()
print(board.gamearea[1][1].squaretoken.circletoken.get_X())
print(board.gamearea[1][1].squaretoken.circletoken.get_Y())"""





#gm.start()
"""
#board.switchTokenPosition(board.gamearea[0][1], board.gamearea[1][1])
#board.switchTokenPosition(board.gamearea[1][1], board.gamearea[0][1])
board.moveSquareToken(board.gamearea[0][1])
board.displayGameArea()
board.moveSquareToken(board.gamearea[0][0])
board.displayGameArea()
board.moveSquareToken(board.gamearea[1][0])
board.displayGameArea()
board.moveSquareToken(board.gamearea[2][0])
board.displayGameArea()
board.moveSquareToken(board.gamearea[2][1])
board.displayGameArea()
board.moveSquareToken(board.gamearea[2][2])
board.displayGameArea()
board.moveSquareToken(board.gamearea[1][2])
board.displayGameArea()
board.moveSquareToken(board.gamearea[0][2])
board.displayGameArea()
board.moveSquareToken(board.gamearea[0][1])
board.displayGameArea()
board.moveSquareToken(board.gamearea[1][1])
board.displayGameArea()

print(board.gamearea[0][0].pos_X,board.gamearea[0][0].pos_Y, board.gamearea[0][0].tile_id)
print(board.gamearea[1][0].pos_X,board.gamearea[1][0].pos_Y,board.gamearea[1][0].tile_id)
print(board.gamearea[2][0].pos_X,board.gamearea[2][0].pos_Y,board.gamearea[2][0].tile_id)
print(board.gamearea[0][1].pos_X,board.gamearea[0][1].pos_Y,board.gamearea[0][1].tile_id)
print(board.gamearea[1][1].pos_X,board.gamearea[1][1].pos_Y,board.gamearea[1][1].tile_id)
print(board.gamearea[2][1].pos_X,board.gamearea[2][1].pos_Y,board.gamearea[2][1].tile_id)
print(board.gamearea[0][2].pos_X,board.gamearea[0][2].pos_Y,board.gamearea[0][2].tile_id)
print(board.gamearea[1][2].pos_X,board.gamearea[1][2].pos_Y,board.gamearea[1][2].tile_id)
print(board.gamearea[2][2].pos_X,board.gamearea[2][2].pos_Y,board.gamearea[2][2].tile_id)"""