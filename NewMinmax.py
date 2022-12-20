from copy import deepcopy

from GameArea import GameArea
from Player import Player
from GameMode import isWinner
from move import move

# Checking if row can be complete by player or opponent
def evaluate(board, ismax):

    if ismax == 1:

        if(isWinner(board,board.player_2)):
            return 10
        elif(isWinner(board,board.player_1)):
            return -10
        else:
            return 0
    else:

        if (isWinner(board, board.player_1)):
            return 10
        elif (isWinner(board, board.player_2)):
            return -10
        else:
            return 0

#Scans the game board and returns a list of coordinates of the tile on which a circletoken can be placed
def allmovecirculartokens(board):
    tab = [[]]
    for col in range(3):
        for row in range(3):
            if (board.gamearea[row][col].squaretoken != None):
                if (board.gamearea[row][col].squaretoken.circletoken == None):
                    tab.append([row, col])

    #Remove the first element of the list
    tab.pop(0)

    return tab
#
def get_possible_moves(board,ismax):

    allmove = move()
    allmove.place_token=[[]]
    allmove.place_token=allmovecirculartokens(board)
    allmove.move_tokens = [[]]
    allmove.move_tokens = allmovecirculartokens(board)

    # for col in range(3):
    #     for row in range(3):
    #          if(board.gamearea[row][col].squaretoken!=None):
    #             if(board.gamearea[row][col].squaretoken.circletoken==None):
    #                allmove.place_token.append([row,col])
    # allmove.place_token.pop(0)
    # allmove.move_tokens.pop(0)


    return allmove

def make_move(board,litlemove,indexmove,ismax,circle_tokenid):

    #just for checking errors
    if(board==None):
        print("board is none")

    #the indexmove is to select the type of move(0=place token,1=move token,2=move square 3 move 2square)
    if(indexmove==0):
        if ismax == 0:
            #litlemove is a list of two dimentions (list of coordinates) for where the token can be moved
            board.addCircleToken(litlemove[0],litlemove[1],board.player_1)
            #board.displayGameArea()
        else:
            board.addCircleToken(litlemove[0],litlemove[1],board.player_2)
            #board.displayGameArea()
    if(indexmove==1):
        if ismax == 0:
            board.moveCircleToken(litlemove[0],litlemove[1],board.player_1,circle_tokenid)
            #board.displayGameArea()
        else:
            board.moveCircleToken(litlemove[0],litlemove[1],board.player_2,circle_tokenid)
            #board.displayGameArea()






def minmax(state, depth, ismax):
    # Evaluate the board
    score = evaluate(state, ismax)
    # Si la profondeur maximale est atteinte
    if depth == 0:
        # Retourner le score
        return score

    # Récupération des coordonnées à tester
    listofmove = get_possible_moves(state, 1).move_tokens
    listofmove2 = get_possible_moves(state, 1).place_token

    print(listofmove)
    if ismax == 1:
        # Initialisation de la meilleur valeure
        bestValue = -5000
        # Test de déplacement de circletoken sur toutes les coordonnées disponibles du board
        for move in listofmove:
            # Pour chacun des circle token du board
            #for i in range(state.player_1.getnumberofcircletoken()):
            for i in range(3):
                # Création d'une copie du board
                newState = deepcopy(state)
                # Éxecution du coup
                make_move(newState, move, 1, ismax, i)
                # Appelle minmax sur le nouveau board
                value = minmax(newState, depth - 1, ismax)
                # Test de la valeure obtenue
                bestValue = max(bestValue, value)

        # Test de placement de circletoken sur toutes les coordonnées disponibles du board
        for move in listofmove2:
            # Création d'une copie du board
            newState = deepcopy(state)
            # Éxecution du coup
            make_move(newState, move, 0, ismax, -1)
            # Appelle minmax sur le nouveau board
            value = minmax(newState, depth - 1, ismax)
            # Test de la valeure obtenue
            bestValue = max(bestValue, value)

        return bestValue

    else:
        bestValue = 5000
        # Test de déplacement de circletoken sur toutes les coordonnées disponibles du board
        for move in listofmove:
            for i in range(3):
                # Création d'une copie du board
                newState = deepcopy(state)
                # Éxecution du coup
                make_move(newState, move, 1, ismax,i)
                # Appelle minmax sur le nouveau board
                value = minmax(newState, depth - 1, ismax)
                # Test de la valeure obtenue
                bestValue = min(bestValue, value)

        # Test de placement de circletoken sur toutes les coordonnées disponibles du board
        for move in listofmove2:
            newState = deepcopy(state)
            # Éxecution du coup
            make_move(newState, move, 0, ismax, -1)
            # Appelle minmax sur le nouveau board
            value = minmax(newState, depth - 1, ismax)
            # Test de la valeure obtenue
            bestValue = min(bestValue, value)

        return bestValue

# Fonction permettant de trouver le meilleur coup grâce à minmax
# Évaluation de tous les coups possibles au premier tour avec minmax
# Renvois des coodonnées du meilleur coup
def findBestMove(board, player):

    # Initialisation des valeurs par défauts
    bestVal = -1000
    bestMove = (-1, -1)
    indexmovea= -1

    # Récupération des coordonnées à tester
    listofmove = get_possible_moves(board, player.player_id).move_tokens
    listofmove2 = get_possible_moves(board, player.player_id).place_token

    # Test de déplacement de circletoken sur toutes les coordonnées disponibles du board
    for move in listofmove:
        # Pour chacun des circle token du board
        for i in range(player.getnumberofcircletoken()):
            # Création d'une copie du board
            newState = deepcopy(board)

            # Éxecution du coups sur la copie du tableau
            make_move(newState, move, 1, player.player_id, i)
            #newState.displayGameArea()
            # Test de la valeur du coup joué
            #print("Début")
            moveVal = minmax(newState, 0, player.player_id)
            #print("Fin")
            print("moveVal = " + str(moveVal)+" move = " + str(move)+" id_token = " + str(i))

            # Si la valeure de coup joué est meilleure que la valeure du meilleur coup
            if (moveVal > bestVal):
                # Le coup joué devient le meilleur coup
                bestMove = move
                # On garde en mémoire le meilleur coup possible
                best = deepcopy(newState)
                # La valeure du coup joué devient la valeure du meilleure coup
                bestVal = moveVal
                indexmovea = i

    for move in listofmove2:
        if(bestVal==10):
            break
        # copy du board
        newState = deepcopy(board)
        # on joue le coup

        make_move(newState, move, 0, player.player_id,-1)
        moveVal = minmax(newState, 0, player.player_id)
        print("moveVal = " + str(moveVal) + " move = " + str(move))
        if (moveVal > bestVal):
            bestMove = move
            best = deepcopy(newState)
            bestVal = moveVal
            indexmovea = -1

    """
    if(indexmovea!=-1):
        print("le meilleur coup est de bouger le token numero : R"+str(indexmovea)+" en position "+str(bestMove)+" \nThe values of minimax of the best Move is :"+str(bestVal))
    else:
        print("le meilleur coup est de placer un nouveau token en position " + str(bestMove) + " \nThe values of minimax of the best Move is :" + str(bestVal))
    """
    return best

if __name__ == '__main__':
    player_1 = Player(0, "R")
    player_2 = Player(1, "B")
    board = GameArea(player_1, player_2)
    board.moveSquareToken(board.gamearea[1][0])
    
    board.addCircleToken(0, 2, player_1)
    board.addCircleToken(1, 2, player_1)
    board.addCircleToken(0, 1, player_2)
    board.addCircleToken(1, 1, player_2)


    board.displayGameArea()

    board = findBestMove(board, player_1)
    board.displayGameArea()










