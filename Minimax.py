'''import math
import GameArea from GameArea
import Node from Node
import Player from Player
import Tile from Tile

# Checking if row can be complete by player or opponent
def evaluate(b):
    for row in range(3):
        if (board[row][0] == board[row][1] and board[row][1] == board[row][2]):
            if (board[row][0]..squaretoken==player == player):
                return 10
            elif (board[row][0]..squaretoken==player == opponent):
                return -10

# Checking if columns can be complete by player or opponent
    for col in range(3):

        if (board[0][col] == board[1][col] and board[1][col] == board[2][col]):

            if (board[0][col]..squaretoken==player  == player):
                return 10
            elif (board[0][col]..squaretoken==player == opponent):
                return -10

# Checking if diagonal can be complete by player or opponent
    if (board[0][0] == board[1][1] and board[1][1] == board[2][2]):

        if (board[0][0]..squaretoken==player == player):
            return 10
        elif (board[0][0]..squaretoken==player == opponent):
            return -10

    if (board[0][2] == board[1][1] and board[1][1] == board[2][0]):

        if (board[0][2]..squaretoken==player == player):
            return 10
        elif (board[0][2]..squaretoken==player == opponent):
            return -10

    # else no win
    return 0




minimax function consider all the possibilities of a game an chose the most appropriate for the move play
the functon return the better score of a turn

def minimax(board, depth, isMax):
    score = evaluate(board)

    # If Maximizer has won the game
    if (score == 10):
        return score

    # If Minimizer has won the game
    if (score == -10):
        return score
    #no win but tree finished
    if (depth==0):
        return score

    # If this maximizer's turn
    if (isMax):
        best = -1000

        # Traverse all cells
        for i in range(3):
            for j in range(3):

                if(board).tile==emptytile:
                # Check if tile is empty
                elif (board[i][j].squaretoken==node):

                    board[i][j] = player
#resursivity minimax
                    best = max(best, minimax(board,depth + 1,not isMax))

                    # Undo the move
                    board[i][j] = '_'
        return best

    # If this minimizer's move
    else:
        best = 1000

        # Traverse all cells
        for i in range(3):
            for j in range(3):


                if(board).tile==emptytile:
                # Check if tile is empty
                elif (board[i][j].squaretoken==node):

                    board[i][j] = opponent

                    # Call minimax recursively and choose
                    # the minimum value
                    best = min(best, minimax(board, depth + 1, not isMax))

                    # Undo the move
                    board[i][j] = '_'

                #elsif compliqué sur le mouvement des tiles
                #elsif sur le déplacement des circletokens
        return best


# This will return the best possible move for the player with the minimax function
def findBestMove(board):
    bestVal = -1000
    bestMove = (-1, -1)

#place a token
    for i in range(3):
        for j in range(3):

            # Check if cell is empty
            if (board[i][j] == '_'):
                board[i][j] = player


                moveVal = minimax(board, 0, False)

                # Undo the move
                board[i][j] = '_'

                if (moveVal > bestVal):
                    bestMove = (i, j)
                    bestVal = moveVal

    return bestMove



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