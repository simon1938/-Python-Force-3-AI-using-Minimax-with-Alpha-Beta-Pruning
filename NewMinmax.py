from copy import deepcopy

from GameArea import GameArea
from Player import Player
from GameMode import isWinnerIA
from move import move

# Checking if row can be complete by player or opponent
def evaluate(board,ismax,player_id):

    #the player_id is the id of the player who we want to will
    #the ismax is just to know if is the turn of the max or min player

    players= [board.player_1, board.player_2]
    if(player_id==0):
        thegoodplayer = players[0]
        thebadplayer  =  players[1]
    elif(player_id==1):
        thegoodplayer = players[1]
        thebadplayer  =  players[0]
    #so thegoodplayer is the player who we want to will
    #thebadplayer is the player who we want to lose
    #they depend of the player_id

    if(ismax==1):
        if(isWinnerIA(board,thegoodplayer)):
            return 10
        elif(isWinnerIA(board,thebadplayer)):
            return -10
        else:
            return 0

    elif(ismax==0):
        if(isWinnerIA(board,thegoodplayer)):
            return 10
        elif(isWinnerIA(board,thebadplayer)):
            return -10
        else:
            return 0

#défine a list of two dimentions (list of coordinates) for where the token can be moved
def allmovecirculartokens(board):
    tab = [[]]
    for col in range(3):
        for row in range(3):
            if (board.gamearea[row][col].squaretoken != None):
                if (board.gamearea[row][col].squaretoken.circletoken == None):
                    tab.append([row, col])
    #remove the first element of the list
    tab.pop(0)

    return tab
#
def get_possible_moves(board,ismax):

    allmove= move()
    allmove.place_token=[[]]
    allmove.place_token=allmovecirculartokens(board)
    allmove.move_tokens = [[]]
    allmove.move_tokens = allmovecirculartokens(board)

    return allmove

def make_move(board,litlemove,indexmove,ismax,player_id,circle_tokenid):

    if(player_id==0):
        thegoodplayer = board.player_1
        thebadplayer = board.player_2
    elif(player_id==1):
        thegoodplayer = board.player_2
        thebadplayer = board.player_1


    #just for checking errors
    if(board==None):
        print("board is none")

    #the idexmove is to select the type of move(0=place token,1=move token,2=move square 3 move 2square)
    if(indexmove==0):
        if(ismax):
            #litlemove is a list of two dimentions (list of coordinates) for where the token can be moved
            board.addCircleToken(litlemove[0],litlemove[1],thegoodplayer)
            #board.displayGameArea()
        else:
            board.addCircleToken(litlemove[0],litlemove[1],thebadplayer)
            #board.displayGameArea()
    if(indexmove==1):
        if(ismax):
            #print("debugk"+str(litlemove)+" "+str(circle_tokenid)+"c'est le tour du joueur" +str(ismax))

            board.moveCircleToken(litlemove[0],litlemove[1],thegoodplayer,circle_tokenid)
            #board.displayGameArea()
        else:
            board.moveCircleToken(litlemove[0],litlemove[1],thebadplayer,circle_tokenid)
            #board.displayGameArea()






def minmax(state, depth, ismax,player_id):

   if (player_id == 0):
         thegoodplayer = state.player_1
         thebadplayer = state.player_2
   elif (player_id == 1):
         thegoodplayer = state.player_2
         thebadplayer = state.player_1

   # evaluate the board
   score = evaluate(state, ismax,player_id)
   if(score==10):

        return score
   if(score==-10):

        return score
   # Si la profondeur maximale est atteinte
   if(depth==0):
        return 0

   # Récupération des coordonnées à tester
   listofmove = get_possible_moves(state, 1).move_tokens
   listofmove2 = get_possible_moves(state, 1).place_token

   if ismax:
            # Initialisation de la pire valeur
            bestValue = -5000
            # Test de déplacement de circletoken sur toutes les coordonnées disponibles du board(tout les moves)
            for move in listofmove:
                # Pour chacun des circle token du board
                for i in range(thegoodplayer.getnumberofcircletoken()):
                        # Création d'une copie du board
                        newState = deepcopy(state)
                        #Execution du coup
                        make_move(newState, move, 1, True,player_id,i)
                        #on appelle minmax sur le nouveau board
                        value = minmax(newState, depth - 1, False,player_id)
                        # Test de la valeure obtenue
                        bestValue = max(bestValue, value)
            for move in listofmove2:
                # Création d'une copie du board
                newState = deepcopy(state)
                # Éxecution du coup
                make_move(newState, move, 0, True, player_id,-1)
                value = minmax(newState, depth - 1, False, player_id)
                # Test de la valeure obtenue
                bestValue = max(bestValue, value)

            return bestValue

   else:
        bestValue = 5000
        for move in listofmove:
          for i in range(thebadplayer.getnumberofcircletoken()):
                  # Création d'une copie du board
                  newState = deepcopy(state)
                  # Éxecution du coup
                  make_move(newState, move, 1, False,player_id,i)
                  #on appelle minmax sur le nouveau board
                  value = minmax(newState, depth - 1, True,player_id)
                  # Test de la valeure obtenue
                  bestValue = min(bestValue, value)


        for move in listofmove2:
            # Création d'une copie du board
            newState = deepcopy(state)
            # Éxecution du coup
            make_move(newState, move, 0, False,player_id, -1)
            value = minmax(newState, depth - 1, True,player_id)
            # Test de la valeure obtenue
            bestValue = min(bestValue, value)

        return bestValue

# Fonction permettant de trouver le meilleur coup grâce à minmax pour un joueur donné
# Évaluation de tous les coups possibles au premier tour avec minmax
# Renvois le board avec le meilleur coup effectué
def findBestMove(board,player):

    #initialisation de l'id du joueur avec qui l'on souhaite optimiser le coup avec minmax
    player_id=player.player_id
    print("player id"+str(player_id))

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
    # Récupération des coordonnées à tester
    listofmove = get_possible_moves(board, 1).move_tokens
    listofmove2 = get_possible_moves(board, 1).place_token
    #print(listofmove)

    # Test de déplacement de circletoken sur toutes les coordonnées disponibles du board(tout les moves)
    for move in listofmove:
        # Pour chacun des circle token du board
        for i in range(thegoodplayer.getnumberofcircletoken()):
                print(str(move)+" "+str(i))
                # Création d'une copie du board
                newState = deepcopy(board)
                # Éxecution du coup
                make_move(newState, move, 1, True,player_id,i)#Move to move token
                #newState.displayGameArea()
                moveVal = minmax(newState, 2, False,player_id)
                # print("§§moveVal§§ = "+ str(moveVal)+" move="+str(move)+"id_token="+str(i))
                # print('#####'+str(moveVal)+" "+str(bestVal)+"#####")

                # Si la valeure de coup joué est meilleure que la valeure du meilleur coup
                if (moveVal > bestVal):
                    # Le coup joué devient le meilleur coup
                    bestMove = move
                    bestVal = moveVal
                    indexmovea=i
                if(bestVal==10):
                    break

    for move in listofmove2:
        if(bestVal==10):
            break
        # Création d'une copie du board
        newState = deepcopy(board)
        # Éxecution du coup
        make_move(newState, move,0,True, player_id,-1) #Move to place token
        moveVal = minmax(newState, 2, False,player_id)
        #print("moveVal = " + str(moveVal) + "move=" + str(move) + "id_token=" + str(i))
        # print('#####' + str(moveVal) + " " + str(bestVal) + "#####")
        if (moveVal > bestVal):
            bestMove = move
            bestVal = moveVal
            indexmovea = -1


    if(player_id==0):
        colortoken='R'
    else:
        colortoken='B'

    if(indexmovea!=-1):
        print("le meilleur coup est de bouger le token numero : "+colortoken+str(indexmovea)+" en position "+str(bestMove)+" \nThe values of minimax of the best Move is :"+str(bestVal))
    else:
        print("le meilleur coup est de placer un nouveau token de couleur "+colortoken+" en position  "+ str(bestMove) + " \nThe values of minimax of the best Move is :" + str(bestVal))


    print("move effectuer")
    if(indexmovea!=-1):
        make_move(board, bestMove, 1, True,player_id,indexmovea)
    else:
        make_move(board, bestMove, 0, True,player_id,-1)

    return board


if __name__ == '__main__':
    player_1 = Player(0, "R")
    player_2 = Player(1, "B")
    board = GameArea(player_1, player_2)
    board.addCircleToken(0, 0, player_2)
    board.addCircleToken(2, 0, player_1)
    board.addCircleToken(2, 2, player_1)
    board.addCircleToken(1, 2, player_1)

    board.displayGameArea()
    findBestMove(board,board.player_1)
    board.displayGameArea()









