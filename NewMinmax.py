from copy import deepcopy

from GameArea import GameArea
from Player import Player
from GameMode import isWinner
from move import move

# Checking if row can be complete by player or opponent
def evaluate(board : GameArea):

        if(isWinner(board,board.player_1)):
            return 10
        elif(isWinner(board,board.player_2)):
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

    #the idexmove is to select the type of move(0=place token,1=move token,2=move square 3 move 2square)
    if(indexmove==0):
        if(ismax):
            #litlemove is a list of two dimentions (list of coordinates) for where the token can be moved
            board.addCircleToken(litlemove[0],litlemove[1],board.player_1)
            #board.displayGameArea()
        else:
            board.addCircleToken(litlemove[0],litlemove[1],board.player_2)
            #board.displayGameArea()
    if(indexmove==1):
        if(ismax):
            board.moveCircleToken(litlemove[0],litlemove[1],board.player_1,circle_tokenid)
            #board.displayGameArea()
        else:
            board.moveCircleToken(litlemove[0],litlemove[1],board.player_2,circle_tokenid)
            #board.displayGameArea()






def minmax(state, depth, ismax):

   #evaluate the board
   score = evaluate(state)
   if(score==10):
        state.displayGameArea()
        return score
   if(score==-10):
        state.displayGameArea()
        return score
   #To add a end of the tree
   if(depth==0):
        return 0
   state.displayGameArea()
   #listofmove =get_possible_moves(state, 1).place_token
   listofmove = get_possible_moves(state, 1).move_tokens

   if ismax:
            bestValue = -5000
            for move in listofmove:
                #print(listofmove)
                #state.displayGameArea()
                #copy du board
                #print("le nombre de jeton du joeur est"+str(state.player_1.getnumberofcircletoken()))
                for i in range(state.player_1.getnumberofcircletoken()):

                        newState = deepcopy(state)
                        #on joue le coup
                        #print("#############   "+str(i)+"   #############")
                        make_move(newState, move, 1, 1,i)
                        #print("deeep="+str(depth)+"player 1"+str(move)+"id_token="+str(i))
                        #on appelle minmax sur le nouveau board
                        value = minmax(newState, depth - 1, False)
                        bestValue = max(bestValue, value)

            return bestValue

   else:
        bestValue = 5000
        for move in listofmove:
          #print(listofmove)
          #state.displayGameArea()
          #copy du board
          #print("le nombre de jeton du joeur est" + str(state.player_1.getnumberofcircletoken()))
          for i in range(state.player_2.getnumberofcircletoken()):
                  #print("#############   " + str(state.player_1.getnumberofcircletoken()) + "   #############")
                  newState = deepcopy(state)
                  #on joue le coup
                  make_move(newState, move, 1, 0,i)
                  #print("deeep tour ="+str(depth)+"player 2"+str(move)+"id_token="+str(i))
                  #on appelle minmax sur le nouveau board
                  value = minmax(newState, depth - 1, True)
                  bestValue = min(bestValue, value)

        return bestValue

#permets de trouver le meilleur coup en utilisant minimax
#évalu de tous les coups possibles au premier tour avec minimax
#et renvois juste les coodonnées du meilleur coup
def findBestMove(board):
    bestVal = -1000
    bestMove = (-1, -1)
    indexmove=-1
    listofmove = get_possible_moves(board, 1).move_tokens
    listofmove2 = get_possible_moves(board, 1).place_token
    print(listofmove)

    for move in listofmove:
        # copy du board

        for i in range(board.player_1.getnumberofcircletoken()):
                newState = deepcopy(board)
                # on joue le coup
                make_move(newState, move, 1, 1,i)
                moveVal = minmax(newState, 3, False)
                print("moveVal=" + str(moveVal)+"move="+str(move)+"id_token="+str(i))


                if (moveVal > bestVal):
                    bestMove = move
                    bestVal = moveVal
                    indexmovea=i

    for move in listofmove2:
        # copy du board
        newState = deepcopy(board)
        # on joue le coup
        make_move(newState, move, 0, 1,-1)
        moveVal = minmax(newState, 3, False)
        print("moveVal=" + str(moveVal) + "move=" + str(move))
        if (moveVal > bestVal):
            bestMove = move
            bestVal = moveVal
            indexmovea = -1


    if(indexmovea!=-1):
        print("le meilleur coup est de bouger le token numero : R"+str(indexmovea)+" en position "+str(bestMove)+" \nThe values of minimax of the best Move is :"+str(bestVal))
    else:
        print("le meilleur coup est de placer un nouveau token en position " + str(bestMove) + " \nThe values of minimax of the best Move is :" + str(bestVal))


if __name__ == '__main__':
    player_1 = Player(0, "R")
    player_2 = Player(1, "B")
    board = GameArea(player_1, player_2)
    board.addCircleToken(0, 2, player_1)
    board.addCircleToken(2, 2, player_1)
    board.addCircleToken(2, 1, player_1)

    board.addCircleToken(0, 0, player_2)
    board.addCircleToken(2, 0, player_2)
    board.addCircleToken(0, 1, player_2)

    board.displayGameArea()
    print(allmovecirculartokens(board))
    print("hh"+str(get_possible_moves(board,1).move_tokens))
    print("hh" + str(get_possible_moves(board, 1).place_token))

    findBestMove(board)










