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

