
from GameArea import GameArea
from Player import Player
from GameMode import isWinner
from Tile import Tile

# Checking if row can be complete by player or opponent
def evaluate(board : GameArea):

        if(isWinner(board,board.player_1)):
            return 10
        elif(isWinner(board,board.player_2)):
            return -10
        else:
            return 0


#minimax function consider all the possibilities of a game an chose the most appropriate for the move play
#the functon return the better score of a turn
#################################################################################################################
def minimax(board, depth, isMax):
    score = evaluate(board)

    # If Maximizer has won the game
    if (score == 10):
        return score

    # If Minimizer has won the game
    if (score == -10):
        return score
    #no win but tree finished
    if (depth==3):
        return 0


    w=2

    # If this maximizer's turn
    if (isMax):
        best = -1000

        # Traverse all cells
        for i in range(3):
            for j in range(3):
                for w in range(1):
                        if(board.gamearea[i][j].squaretoken!=None):
                            if(board.gamearea[i][j].squaretoken.circletoken==None and board.player_1.circletoken_id<=3):
                                #do move
                                board.gamearea[i][j].squaretoken.createCircletoken(i, j, 'R', 0,board.player_1.circletoken_id + 1)
                                board.player_1.circletoken_id = board.player_1.circletoken_id + 1

                                board.player_1.circletoken.append(board.gamearea[i][j].squaretoken.circletoken)
                                #


                                best = max(best, minimax(board,depth + 1,not isMax))


                                # Undo the move
                                board.gamearea[i][j].squaretoken.circletoken=None
                                board.player_1.circletoken_id=board.player_1.circletoken_id-1
                                board.player_1.circletoken.pop(board.player_1.circletoken_id)
                   # else:
                     #   best =max (domove(board, 2, i, j, True,depth),best)




                   # elif(w==1):
                        #for all move circular tokens do
                        #best = max(best, minimax(board, depth + 1, not isMax))
                        #undo move

        print("le best score est "+str(best))
        board.displayGameArea()
        return best

    # If this minimizer's move
    else:
        best = 1000

        # Traverse all cells
        for i in range(3):
            for j in range(3):
                for w in range(1):
                        if (board.gamearea[i][j].squaretoken != None):
                            if (board.gamearea[i][j].squaretoken.circletoken == None and board.player_2.circletoken_id<3):


                                board.gamearea[i][j].squaretoken.createCircletoken(i, j, 'B', 1,board.player_2.circletoken_id + 1)
                                board.player_2.circletoken_id = board.player_2.circletoken_id + 1

                                board.player_2.circletoken.append(board.gamearea[i][j].squaretoken.circletoken)


                                print("nbcirlces"+str(board.player_2.circletoken_id))

                                best = min(best, minimax(board, depth + 1, not isMax))
                                board.displayGameArea()
                                # Undo the move
                                board.gamearea[i][j].squaretoken.circletoken=None
                                board.player_2.circletoken_id = board.player_2.circletoken_id - 1
                                board.player_2.circletoken.pop(board.player_2.circletoken_id)
                   # else:
                      #  best = min(domove(board, 2, i, j, True, depth), best)


        return best

#################################################################################################################
# This will return the best possible move for the player with the minimax function
def findBestMove(board):
    bestVal = -1000
    bestMove = (-1, -1)
    p=1
#place a token
    for j in range(3):
        for i in range(3):

            if (board.gamearea[i][j].squaretoken != None):
                if (board.gamearea[i][j].squaretoken.circletoken == None and board.player_1.circletoken_id<3):

                    board.player_1.circletoken_id = board.player_1.circletoken_id + 1
                    board.gamearea[i][j].squaretoken.createCircletoken(i, j, 'R', 1, board.player_1.circletoken_id + 1)
                    board.player_1.circletoken.append(board.gamearea[i][j].squaretoken.circletoken)
                    board.displayGameArea()



                    moveVal = minimax(board, 0, False)

                    # Undo the move

                    board.gamearea[i][j].squaretoken.circletoken=None
                    board.player_1.circletoken_id = board.player_1.circletoken_id - 1
                    board.player_1.circletoken.pop(board.player_1.circletoken_id)


                    if (moveVal > bestVal):
                        bestMove = (i, j)
                        bestVal = moveVal

    print("The values of the best Move is :", bestVal)
    print()

    return bestMove

def domove(board,m,i,j,isMax,depth,best):

    if(m==1 and isMax==1):
        #place a token
        if (board.gamearea[i][j].squaretoken != None):
            if (board.gamearea[i][j].squaretoken.circletoken == None and board.player_1.circletoken_id <= 3):
                #
                board.gamearea[i][j].squaretoken.createCircletoken(i, j, 'R', 0, board.player_1.circletoken_id + 1)
                board.player_1.circletoken_id = board.player_1.circletoken_id + 1

                board.player_1.circletoken.append(board.gamearea[i][j].squaretoken.circletoken)
                #

                best2 = max(best, minimax(board, depth + 1, not isMax))

                # Undo the move
                board.gamearea[i][j].squaretoken.circletoken = None
                board.player_1.circletoken_id = board.player_1.circletoken_id - 1
                board.player_1.circletoken.pop(board.player_1.circletoken_id)
                return best2

    elif(m==1 and isMax==0):
        if (board.gamearea[i][j].squaretoken != None):
            if (board.gamearea[i][j].squaretoken.circletoken == None and board.player_2.circletoken_id <= 3):
                #
                board.gamearea[i][j].squaretoken.createCircletoken(i, j, 'B', 1, board.player_2.circletoken_id + 1)
                board.player_2.circletoken_id = board.player_2.circletoken_id + 1

                board.player_2.circletoken.append(board.gamearea[i][j].squaretoken.circletoken)
                #

                best2 = min(best, minimax(board, depth + 1, not isMax))

                # Undo the move
                board.gamearea[i][j].squaretoken.circletoken = None
                board.player_2.circletoken_id = board.player_2.circletoken_id - 1
                board.player_2.circletoken.pop(board.player_2.circletoken_id)
                return best2



    elif(m==2 and isMax):
        #move a token
        if (board.gamearea[i][j].squaretoken != None) :
            if(board.gamearea[i][j].squaretoken.circletoken != None):
                if(board.gamearea[i][j].squaretoken.circletoken.player_id==isMax):
                    #do move
                    listeofmove=allmovecirculartokens(board,i,j,isMax)
                    for index in range(len(listeofmove)):
                        ni=listeofmove[index][0]
                        nj=listeofmove[index][1]
                        board.gamearea.moveCircleToken(board.gamearea[i][j].squaretoken.circletoken, ni,nj, board.player_1,board.gamearea[i][j].squaretoken.circletoken.token_id)


                        best=minimax(board, depth + 1, not isMax)

                        # undo move
                        board.gamearea.moveCircleToken(board.gamearea[ni][nj].squaretoken.circletoken, i, j, board.player_1,board.gamearea[ni][nj].squaretoken.circletoken.token_id)
                        return best

                else:
                    # do move
                    listeofmove = allmovecirculartokens(board, i, j, isMax)
                    for index in range(len(listeofmove)):
                        ni = listeofmove[index][0]
                        nj = listeofmove[index][1]
                        board.gamearea.moveCircleToken(board.gamearea[i][j].squaretoken.circletoken, ni, nj, board.player_2,board.gamearea[i][j].squaretoken.circletoken.token_id)

                        best=minimax(board, depth + 1, not isMax)

                        #undo move
                        board.gamearea.moveCircleToken(board.gamearea[ni][nj].squaretoken.circletoken, i, j, board.player_2,board.gamearea[i][j].squaretoken.circletoken.token_id)
                        return best


  #  elif(m==3):
#move a square token with circle token
   # elif (m == 4):
#moven 2 square token
        #yen plus



def allmovecirculartokens(board,i,j,player):
    tab=[[]]
    for row in range(3):
        for col in range(3):
            if(row!=i or col!=j ):
                if(board.gamearea[row][col].squaretoken!=None):
                    if (board.gamearea[row][col].squaretoken.circletoken==None):
                        tab.append([row,col])

    print("le tableau est "+ str(print(tab))+"pas en "+str(i)+str(j))
    return tab.pop(0)










if __name__ == '__main__':
    player_1 = Player(0, "R")
    player_2 = Player(1, "B")
    board = GameArea(player_1, player_2)
    board.addCircleToken(2, 0, player_2)
    board.addCircleToken(2, 2, player_2)
    board.addCircleToken(1, 2, player_1)

    board.displayGameArea()



    board.displayGameArea()
    bestMove = findBestMove(board)
    board.displayGameArea()


    print("The Optimal Move is :")
    print("ROW:", bestMove[0], " COL:", bestMove[1])

'''

#pseudo code
def minimax(curDepth, nodeIndex,maxTurn, scores,targetDepth):

    if (curDepth == targetDepth):
        return scores[nodeIndex]

    if (maxTurn):
        return max(minimax(curDepth + 1, nodeIndex * 2,
                           False, scores, targetDepth),
                   minimax(curDepth + 1, nodeIndex * 2 + 1,
                           False, scores, targetDepth))

    else:
        return min(minimax(curDepth + 1, nodeIndex * 2,
                           True, scores, targetDepth),
                   minimax(curDepth + 1, nodeIndex * 2 + 1,
                           True, scores, targetDepth))


# Driver code
scores = [3, 5, 2, 9, 12, 5, 23, 23]




def findbestmove()
    # pseudo code
    function
    minimax(board, depth, isMaximizingPlayer):

    if current board state is a terminal state:
        return value
        of
        the
        board

    if isMaximizingPlayer:
        bestVal = -INFINITY
        for each move in board:
            value = minimax(board, depth + 1, false)
            bestVal = max(bestVal, value)
        return bestVal

    else:
        bestVal = +INFINITY
        for each move in board:
            value = minimax(board, depth + 1, true)
            bestVal = min(bestVal, value)
        return bestVal
'''