from copy import deepcopy

from GameArea import GameArea
from Player import Player
from GameMode import isWinnerIA
from move import move
from Tile import Tile
import CONSTANT


def checktwocirclealldirection(player):

  listecoord = rec_circletoken_coordonnées(player.circletoken)
  listX = []
  listY = []
  listD = []
  x = -1
  y = -2
  compteurX = 0
  compteurY = 0
  compteurD = -1
  compteurD2 = -1

  #check for two in a row and in a column
  for coord in listecoord:
      # On récupère la coordonnée x1 du circle token coord
      x1 = coord[0]
      # Si cette coordonnée x1 est déja dans la liste listX
      if x1 in listX:
          # alors un autre circle token a la même coordonnée x donc appartient à la même colonne
          compteurY = compteurY + 1
      else:
          # sinon on l'ajoute à la liste des coordonnées x
          listX.append(x1)
      # On récupère la coordonnée y1 du circle token coord
      y1 = coord[1]
      # Si cette coordonnée y1 est déja dans la liste listY
      if y1 in listY:
          # alors un autre circle token a la même coordonnée y donc appartient à la même ligne
          compteurX = compteurX + 1
      else:
          # sinon on l'ajoute à la liste des coordonnées y
          listY.append(y1)

  #check for two in a left diagonal
  for coord in listecoord:
      # Si les coordonnées x et y sont les mêmes
      if coord[1] == coord[0]:
          # alors cela signifie que le circle token coord appartient à la diagonale gauche
          compteurD += 1

  #check for two in a right diagonal
  for coord in listecoord:
      # Si les le circle token a pour coordonnée [2, 0] ou [1, 1] ou [0, 2]
      if (coord[0] == 0 and coord[1] == 2) or (coord[0] == 2 and coord[1] == 0) or (coord[0] == 1 and coord[1] == 1):
          # alors cela signifie que le circle token coord appartient à la diagonale droite
          compteurD2 += 1

  #la fonction retourne ligne colonne diagonalegauche diagonaledroite (monte a droite)
  return compteurY, compteurX, compteurD, compteurD2

# returns a list of coordinates corresponding to the coordinates of the circletokens of the player on the board
def rec_circletoken_coordonnées(player_token):
    coordonnées = []

    # Si le player au moins 1 token sur le board
    if len(player_token) >= 1:
        x0 = player_token[0].get_X()
        y0 = player_token[0].get_Y()
        coordonnées.append([x0, y0])
    # Si le player au moins 2 tokens sur le board
    if len(player_token) >= 2:
        x1 = player_token[1].get_X()
        y1 = player_token[1].get_Y()
        coordonnées.append([x1, y1])
    # Si le player a 3 tokens sur le board
    if len(player_token) == 3:
        x2 = player_token[2].get_X()
        y2 = player_token[2].get_Y()
        coordonnées.append([x2, y2])
    return coordonnées

# Checking if row can be complete by player or opponent
def evaluate(board,ismax,player_id):

    # The player_id is the id of the player who we want to will
    # The ismax is just to know if is the turn of the max or min player
    if player_id == 0:
        thegoodplayer = board.player_1
        thebadplayer = board.player_2
    elif player_id == 1:
        thegoodplayer = board.player_2
        thebadplayer = board.player_1

    # For the max player
    # Initialization of weights for two circle tokens in the same direction
    tab_two_circle_token_all_direction = checktwocirclealldirection(thegoodplayer)
    val_evaluate = 0
    # Pour chacune des directions (colonne, ligne, diagonale gauche, diagonale droite)
    for val_one_direction in tab_two_circle_token_all_direction:
        # Si une de ces directions contient deux circle token (donc est égale à 1)
        if (val_one_direction == 1):
            val_evaluate = val_evaluate + 1

    # Initialization of the weight according to the number of tokens compared to the other player
    val_nb_jeton = 0
    # si thegoodplayer a plus de jeton que thebadplayer
    if (thegoodplayer.circletoken_id >= thebadplayer.circletoken_id):
        val_nb_jeton = 4

    # For the min player
    # Initialization of weights for two circle tokens in the same direction
    tab_two_circle_token_all_direction_bad = checktwocirclealldirection(thebadplayer)
    val_evaluate_bad = 0
    # Pour chacune des directions (colonne, ligne, diagonale gauche, diagonale droite)
    for val_one_direction_bad in tab_two_circle_token_all_direction_bad:
        # Si une de ces directions contient deux circle token (donc est égale à 1)
        if (val_one_direction_bad == 1):
            val_evaluate_bad = val_evaluate_bad - 1

    # Initialization of the weight according to the number of tokens compared to the other player
    val_nb_jeton_bad = 0
    # si thebadplayer a plus de jeton que thegoodplayer
    if (thebadplayer.circletoken_id >= thegoodplayer.circletoken_id):
        val_nb_jeton_bad = -4

    # So thegoodplayer is the player who we want to win
    # thebadplayer is the player who we want to lose
    # they depend of the player_id
    if ismax == 1:
        if isWinnerIA(board, thegoodplayer):
            return 10
        elif isWinnerIA(board, thebadplayer):
            return -10
        elif val_nb_jeton != 0 and val_evaluate != 0:
            val_evaluate = val_evaluate + val_nb_jeton
            return val_evaluate
        elif val_nb_jeton is not None:
            return val_nb_jeton
        elif val_evaluate != 0:
            return val_evaluate
        else:
            return 0

    elif ismax == 0:
        if isWinnerIA(board, thegoodplayer):
            return 10
        elif isWinnerIA(board, thebadplayer):
            return -10
        elif val_nb_jeton_bad != 0 and val_evaluate_bad != 0:
            val_evaluate_bad = val_evaluate_bad + val_nb_jeton_bad
            return val_evaluate_bad
        elif val_nb_jeton_bad is not None:
            return val_nb_jeton_bad
        elif val_evaluate_bad != 0:
            return val_evaluate_bad
        else:
            return 0

# Define a list of two dimentions (list of coordinates) for where the token can be moved
def allmovecirculartokens(board):
    tab = []
    for col in range(3):
        for row in range(3):
            if (board.gamearea[row][col].squaretoken != None):
                if (board.gamearea[row][col].squaretoken.circletoken == None):
                    tab.append([row, col])

    return tab

def allmovesquaretokens(board, nbofsquaretoken):
    tab = []
    # Recovery of the tile on which there is no square token
    for i in range(3):
        for j in range(3):
            if not board.gamearea[i][j].isSquareToken():
                empty_tile = board.gamearea[i][j]
    if nbofsquaretoken == 1:
        # Recovery of square token ids that can be moved by 1 on the board
        temp = CONSTANT.moveable_1squaretoken[str(empty_tile.tile_id)]
    else:
        # Recovery of square token ids that can be moved by 2 on the board
        temp = CONSTANT.moveable_2squaretoken[str(empty_tile.tile_id)]

    # Recovery of the coordinates of each of the boxes that can be moved by 1
    for x in range(len(temp)):
        tab.append(CONSTANT.correlation[str(temp[x])])
    return tab

def get_possible_moves(board):

    allmove= move()
    allmove.place_token=[[]]
    allmove.place_token = allmovecirculartokens(board)
    allmove.move_tokens = [[]]
    allmove.move_tokens = allmovecirculartokens(board)
    allmove.move_square = allmovesquaretokens(board, 1)
    allmove.move_2square = allmovesquaretokens(board, 2)

    return allmove

# Make a hit
def make_move(board,litlemove,indexmove,ismax,player_id,circle_tokenid):
    if player_id == 0:
        thegoodplayer = board.player_1
        thebadplayer = board.player_2
    elif player_id == 1:
        thegoodplayer = board.player_2
        thebadplayer = board.player_1

        # Just for checking errors
    if board is None:
        print("board is none")

        # The indexmove is to select the type of move(0=place token,1=move token,2=move square 3 move 2square)
    if indexmove == 0:
        if ismax:
            # litlemove is a list of two dimentions (list of coordinates) for where the token can be moved
            board.addCircleToken(litlemove[0], litlemove[1], thegoodplayer)
        else:
            board.addCircleToken(litlemove[0], litlemove[1], thebadplayer)
    if indexmove == 1:
        if ismax:
            board.moveCircleToken(litlemove[0], litlemove[1], thegoodplayer, circle_tokenid)
        else:
            board.moveCircleToken(litlemove[0], litlemove[1], thebadplayer, circle_tokenid)
    if indexmove == 2:
        board.moveSquareToken(board.gamearea[litlemove[0]][litlemove[1]], True)
    if indexmove == 3:
        board.move2SquareToken(board.gamearea[litlemove[0]][litlemove[1]], True)

def minmax(state, depth, ismax, player_id):
    if (player_id == 0):
        thegoodplayer = state.player_1
        thebadplayer = state.player_2
    elif (player_id == 1):
        thegoodplayer = state.player_2
        thebadplayer = state.player_1

    # evaluate the board
    score = evaluate(state, ismax, player_id)
    if(score==10):
        return score
    if(score==-10):
        return score
    # Si la profondeur maximale est atteinte
    if(depth==0):
        return score

    # Récupération des coordonnées à tester
    listofmove = get_possible_moves(state).move_tokens
    listofmove2 = get_possible_moves(state).place_token
    listofmove3 = get_possible_moves(state).move_square
    listofmove4 = get_possible_moves(state).move_2square
    if ismax:
        # Initialisation de la pire valeur
        bestValue = -5000

        # Test de déplacement d'un squaretoken sur toutes les coordonnées disponibles du board

        for move in listofmove2:
            # Création d'une copie du board
            newState = deepcopy(state)
            # Éxecution du coup
            make_move(newState, move, 0, True, player_id, -1)
            value = minmax(newState, depth - 1, False, player_id)
            # Test de la valeure obtenue
            bestValue = max(bestValue, value)

        # Test de déplacement de circletoken sur toutes les coordonnées disponibles du board(tout les moves)
        for move in listofmove:
            # Pour chacun des circle token du board
            for i in range(thegoodplayer.getnumberofcircletoken()):
                # Création d'une copie du board
                newState = deepcopy(state)
                # Execution du coup
                make_move(newState, move, 1, True, player_id, i)
                # Appelle de minmax sur le nouveau board
                value = minmax(newState, depth - 1, False, player_id)
                # Test de la valeure obtenue
                bestValue = max(bestValue, value)

        for move in listofmove3:
            # Création d'une copie du board
            newState = deepcopy(state)
            # Éxecution du coup
            make_move(newState, move, 2, True, player_id, -1)
            value = minmax(newState, depth - 1, False, player_id)
            #print("value", value)
            # Test de la valeure obtenue
            bestValue = max(bestValue, value)

        # Test de déplacement de deux squaretoken sur toutes les coordonnées disponibles du board
        for move in listofmove4:
            # Création d'une copie du board
            newState = deepcopy(state)
            # Éxecution du coup
            make_move(newState, move, 3, True, player_id, -1)
            value = minmax(newState, depth - 1, False, player_id)
            # Test de la valeure obtenue
            bestValue = max(bestValue, value)

        return bestValue

    else:
        # Initialisation de la pire valeur
        bestValue = 5000

        for move in listofmove2:
            # Création d'une copie du board
            newState = deepcopy(state)
            # Éxecution du coup
            make_move(newState, move, 0, False, player_id, -1)
            value = minmax(newState, depth - 1, True, player_id)
            # Test de la valeure obtenue
            bestValue = min(bestValue, value)

        for move in listofmove:
           for i in range(thebadplayer.getnumberofcircletoken()):
               # Création d'une copie du board
               newState = deepcopy(state)
               # Éxecution du coup
               make_move(newState, move, 1, False, player_id, i)
               # on appelle minmax sur le nouveau board
               value = minmax(newState, depth - 1, True, player_id)
               # Test de la valeure obtenue
               bestValue = min(bestValue, value)


        for move in listofmove3:
            # Création d'une copie du board
            newState = deepcopy(state)
            # Éxecution du coup
            make_move(newState, move, 2, False, player_id, -1)
            value = minmax(newState, depth - 1, True, player_id)
            # Test de la valeure obtenue
            bestValue = min(bestValue, value)

        # Test de déplacement de deux squaretoken sur toutes les coordonnées disponibles du board
        for move in listofmove4:
            # Création d'une copie du board
            newState = deepcopy(state)
            # Éxecution du coup
            make_move(newState, move, 3, False, player_id, -1)
            value = minmax(newState, depth - 1, True, player_id)
            # Test de la valeure obtenue
            bestValue = min(bestValue, value)

        return bestValue

# Fonction permettant de trouver le meilleur coup grâce à minmax pour un joueur donné
# Évaluation de tous les coups possibles au premier tour avec minmax
# Renvois le board avec le meilleur coup effectué
def findBestMove(board, player):
    # Profondeur initiale
    deepinit = CONSTANT.deep

    # Initialisation de l'id du joueur avec qui l'on souhaite optimiser le coup avec minmax
    player_id = player.player_id

    if (player_id == 0):
        thegoodplayer = board.player_1
        thebadplayer = board.player_2
    elif (player_id == 1):
        thegoodplayer = board.player_2
        thebadplayer = board.player_1

    # Initialisation des valeurs par défauts
    bestVal = -1000
    bestMove = (-1, -1)
    indexmovea=-1

    # Récupération de la liste de move possible pour chaque type de coup
    listofmove = get_possible_moves(board).move_tokens
    listofmove2 = get_possible_moves(board).place_token
    listofmove3 = get_possible_moves(board).move_square
    listofmove4 = get_possible_moves(board).move_2square


    # Si le joueur n'a pas encore placé tous ses circletoken
    if player.circletoken_id < 3:
        # Test de placement des circletoken sur toutes les coordonnées disponibles du board
        for move in listofmove2:
            if bestVal == 10:
                break
            # Création d'une copie du board actuel
            newState = deepcopy(board)
            # Génere chaque état possible avec l'ajout d'un circletoken sur le board initial pour un player donné
            make_move(newState, move, 0, True, player_id, -1)
            # Récupération du poids associé à cet état
            moveVal = minmax(newState, deepinit, False, player_id)
            # Comparaison du poid obtenu pour cet état avec le meilleur poid
            if moveVal > bestVal:
                bestMove = move
                bestVal = moveVal
                indexmovea = -1

    # Si le joueur a déjà placé au moins un circletoken
    if player.circletoken_id > 0:
        # Test de déplacement de circletoken sur toutes les coordonnées disponibles du board
        for move in listofmove:
            # Pour chacun des circle token du board
            for i in range(thegoodplayer.getnumberofcircletoken()):
                # Création d'une copie du board
                newState = deepcopy(board)
                # Génere chaque état possible avec le déplacement d'un circletoken sur le board initial pour un player donné
                make_move(newState, move, 1, True, player_id, i)
                # Récupération du poids associé à cet état
                moveVal = minmax(newState, deepinit, False, player_id)
                # Comparaison du poid obtenu pour cet état avec le meilleur poid
                if moveVal > bestVal:
                    bestMove = move
                    bestVal = moveVal
                    indexmovea = i
                #if bestVal == 10:
                #    break

    # Test de déplacement d'un squaretoken sur toutes les coordonnées disponibles du board
    for move in listofmove3:
        # Création d'une copie du board
        newState = deepcopy(board)
        # Génere chaque état possible avec le déplacement d'un squaretoken sur le board initial pour un player donné
        make_move(newState, move, 2, True, player_id, -1)
        # Récupération du poids associé à cet état
        moveVal = minmax(newState, deepinit, False, player_id)
        # Comparaison du poid obtenu pour cet état avec le meilleur poid
        if moveVal > bestVal:
            bestMove = move
            bestVal = moveVal
            indexmovea = -2

    #Test de déplacement de deux squaretoken sur toutes les coordonnées disponibles du board
    for move in listofmove4:
        #if bestVal == 10:
        #    break
        # Création d'une copie du board
        newState = deepcopy(board)
        # Génere chaque état possible avec le déplacement de deux squaretoken sur le board initial pour un player donné
        make_move(newState, move, 3, True, player_id, -1)
        # Récupération du poids associé à cet état
        moveVal = minmax(newState,deepinit, False, player_id)
        newState.displayGameArea()
        print("Poid = " + str(moveVal))
        # Comparaison du poid obtenu pour cet état avec le meilleur poid
        if moveVal > bestVal:
            bestMove = move
            bestVal = moveVal
            indexmovea = -3


    if player_id == 0:
        colortoken = "Rouge"
    else:
        colortoken = "Bleu"

    if indexmovea == -1:
        print("le meilleur coup est de placer un nouveau token de couleur " + colortoken + " en position  " +
              str(bestMove) + " \nThe values of minimax of the best Move is : " + str(bestVal))
    elif indexmovea == -2:
        print("le meilleur coup est de bouger 1 square token ayant l'identifiant " +
              str(board.gamearea[bestMove[0]][bestMove[1]].tile_id) +
              " \nThe values of minimax of the best Move is : " + str(bestVal))
    elif indexmovea == -3:
        print("le meilleur coup est de bouger 2 square token ayant l'identifiant " +
              str(board.gamearea[bestMove[0]][bestMove[1]].tile_id) +
              " \nThe values of minimax of the best Move is : " + str(bestVal))
    else:
        print("le meilleur coup est de bouger le circle token numero : " +
              colortoken + str(indexmovea) + " en position " + str(bestMove) +
              " \nThe values of minimax of the best Move is : " + str(bestVal))

    print("Move effectué \n")
    check = "0"
    # if bestVal == 10:
    #     print("Fin du jeu miskine tu t'es fait fumer par une ia !")
    #     check = 1

    if indexmovea == -1:
        make_move(board, bestMove, 0, True, player_id, indexmovea)
    elif indexmovea == -2:
        make_move(board, bestMove, 2, True, player_id, -1)
    elif indexmovea == -3:
        make_move(board, bestMove, 3, True, player_id, -1)
    else:
        make_move(board, bestMove, 1, True, player_id, indexmovea)

    if isWinnerIA(board, thegoodplayer):
        print("Fin du jeu miskine tu t'es fait fumer par une ia !")
        check = "1"
    return board, check


if __name__ == '__main__':
    player_1 = Player(0, "R")
    player_2 = Player(1, "B")
    board = GameArea(player_1, player_2)
    board.moveSquareToken(board.gamearea[0][1])
    board.moveSquareToken(board.gamearea[0][0])
    board.addCircleToken(1, 1, player_1)
    board.addCircleToken(1, 2, player_1)
    board.addCircleToken(2, 0, player_1)
    board.addCircleToken(0, 2, player_2)
    board.addCircleToken(1, 0, player_2)
    board.move2SquareToken(board.gamearea[0][2], True)

    board.displayGameArea()
    #print(evaluate(board, 0, player_2.player_id))
    findBestMove(board, board.player_1)
    board.displayGameArea()









