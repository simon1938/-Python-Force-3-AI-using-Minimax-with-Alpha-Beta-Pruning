
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




    # If this maximizer's turn
    if (isMax):
        best = -1000

        # Traverse all cells
        for i in range(3):
            for j in range(3):

                if(board.gamearea[i][j].squaretoken!=None):
                    if(board.gamearea[i][j].squaretoken.circletoken==None and board.player_1.circletoken_id<=3):
                        #
                        board.gamearea[i][j].squaretoken.createCircletoken(i, j, 'R', 0,board.player_1.circletoken_id + 1)
                        board.player_1.circletoken_id = board.player_1.circletoken_id + 1

                        board.player_1.circletoken.append(board.gamearea[i][j].squaretoken.circletoken)
                        #


                        best = max(best, minimax(board,depth + 1,not isMax))


                        # Undo the move
                        board.gamearea[i][j].squaretoken.circletoken=None
                        board.player_1.circletoken_id=board.player_1.circletoken_id-1
                        board.player_1.circletoken.pop(board.player_1.circletoken_id)
        print("le best score est "+str(best))
        board.displayGameArea()
        return best

    # If this minimizer's move
    else:
        best = 1000

        # Traverse all cells
        for i in range(3):
            for j in range(3):

                if (board.gamearea[i][j].squaretoken != None):
                    if (board.gamearea[i][j].squaretoken.circletoken == None and board.player_2.circletoken_id<3):


                        board.gamearea[i][j].squaretoken.createCircletoken(i, j, 'B', 1,board.player_1.circletoken_id + 1)
                        board.player_1.circletoken_id = board.player_1.circletoken_id + 1

                        board.player_1.circletoken.append(board.gamearea[i][j].squaretoken.circletoken)


                        print("nbcirlce"+str(board.player_2.circletoken_id))

                        best = min(best, minimax(board, depth + 1, not isMax))
                        board.displayGameArea()
                        # Undo the move
                        board.gamearea[i][j].squaretoken.circletoken=None
                        board.player_1.circletoken_id = board.player_1.circletoken_id - 1
                        board.player_1.circletoken.pop(board.player_1.circletoken_id)

        return best


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
                    board.gamearea[i][j].squaretoken.createCircletoken(i, j, 'R', 0, board.player_1.circletoken_id + 1)
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

if __name__ == '__main__':


    player_1 = Player(0, "R")
    player_2 = Player(1, "B")
    board = GameArea(player_1, player_2)
    board.addCircleToken(2,0,player_1)
    board.addCircleToken(0, 0, player_1)

    board.displayGameArea()
    bestMove = findBestMove(board)


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