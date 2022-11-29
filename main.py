from Token import Token
from Player import Player
from GameArea import GameArea
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


token = Token("rouge", 4, 5)
rep = token.gettokenposition()

print("La position du token est " + str(rep))
player1=Player(1,0)
player2=Player(2,1)
board = GameArea(player1,player2)
board.displaygamearea()
print("la position null est X="+str(board.emptyTile.getX())+"et Y="+str(board.emptyTile.getX()))
