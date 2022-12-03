import CONSTANT
def start():
    choice = 0
    level_choice = ["1", "2", "3"]
    print("What mode of game do you want ?")
    print("-(1): Player VS Player\n-(2): Player VS IA\n-(3): IA VS IA")
    while choice not in level_choice:
        choice = input()

def next_round(board, player):
    answer = choix(board, player)
    if answer == 1:
        check = 100
        print("You are going to add a circle token on the playing area :\n")
        while check != 1:
            if check == 0:
                print("Retry player" + str(player.player_id) + " :")

            coordinate_x = int(input("Choose the targeted x coordinate among (0,1,2) :\n"))
            while coordinate_x not in {0, 1, 2}:
                coordinate_x = int(input())

            coordinate_y = int(input("Choose the targeted y coordinate among (0,1,2) :\n"))
            while coordinate_y not in {0, 1, 2}:
                coordinate_y = int(input())
            check = board.addCircleToken(coordinate_x,coordinate_y,player)
        checkwinner = str(isWinner(board, player))
    elif answer == 2:
        print("You are going to move a circle token :\n")
        check = 0
        while check == 0:
            coordinate_x = int(input("Choose the targeted x coordinate among (0,1,2) :\n"))
            while coordinate_x not in {0, 1, 2}:
                coordinate_x = int(input())
            coordinate_y = int(input("Choose the targeted y coordinate among (0,1,2) :\n"))
            while coordinate_y not in {0, 1, 2}:
                coordinate_y = int(input())
            #Display the list of the available token_id
            print("Which circle token do you want to move :\n")
            circletoken = 100
            if len(player.circletoken) == 3:
                t0, t1, t2 = player.circletoken
                circletoken = int(input("-The first : " + str(t0.token_id) + "\n-The second : " + str(t1.token_id) + "\n-The third : " + str(t2.token_id) + "\n"))
            if len(player.circletoken) == 2:
                t0, t1 = player.circletoken
                circletoken = int(input("-The first : " + str(t0.token_id) + "\n-The second : " + str(t1.token_id) + "\n"))
            #If there are just one circle token
            if len(player.circletoken) == 1:
                circletoken = 0

            while circletoken not in {0, 1, 2}:
                circletoken = input()
            check = board.moveCircleToken(coordinate_x,coordinate_y,player,circletoken)
        checkwinner = str(isWinner(board, player))
    elif answer == 3:
        print("You are going to move 1 square token :\n")
        check = 100
        while check != 1:
            if check == 0:
                print("This move isn't possible !")
                print("Retry player" + str(player.player_id) + " :\n")
            coordinate_x = int(input("Choose the x coordinate of the token to move among (0,1,2) :\n"))
            while coordinate_x not in {0, 1, 2}:
                coordinate_x = int(input())
            coordinate_y = int(input("Choose the y coordinate of the token to move among (0,1,2) :\n"))
            while coordinate_y not in {0, 1, 2}:
                coordinate_y = int(input())
                print(coordinate_x,coordinate_y)
            check = board.moveSquareToken(board.gamearea[coordinate_x][coordinate_y])
        checkwinner = str(isWinner(board, player))
    else :
        check = 100
        while check != 1:
            if check == 0:
                print("This move isn't possible !")
                print("Retry player" + str(player.player_id) + " :\n")
            print("You are going to move 2 square token :\n")
            coordinate_x = int(input("Choose the x coordinate of the token to move among (0,1,2) :\n"))
            while coordinate_x not in {0, 1, 2}:
                coordinate_x = int(input())
            coordinate_y = int(input("Choose the y coordinate of the token to move among (0,1,2) :\n"))
            while coordinate_y not in {0, 1, 2}:
                coordinate_y = int(input())
            check = board.move2SquareToken(board.gamearea[coordinate_x][coordinate_y])
        checkwinner = str(isWinner(board, player))
    return checkwinner


def isWinner(board, player):
    combination = []
    check = 0
    if player.circletoken_id == 3:
        token_1, token_2, token_3 = player.circletoken
        id_1 = board.gamearea[token_1.get_X()][token_1.get_Y()].tile_id
        id_2 = board.gamearea[token_2.get_X()][token_2.get_Y()].tile_id
        id_3 = board.gamearea[token_3.get_X()][token_3.get_Y()].tile_id

        print(str(id_1) + str(id_2) + str(id_3))
        if id_1 < id_2:
            if id_2 < id_3:
                combination = [id_1, id_2, id_3]
            else:
                if id_1 > id_3:
                    combination = [id_3, id_1, id_2]
                else:
                    combination = [id_1, id_3, id_2]
        else:
            if id_1 < id_3:
                combination = [id_2, id_1, id_3]
            else:
                if id_3 > id_2:
                    combination = [id_2, id_3, id_1]
                else:
                    combination = [id_3, id_2, id_1]

        if combination in CONSTANT.winning_combination:
            print("Player " + str(player.player_id) + " YOU WIN")
            check = 1
        else:
            check = 0
    return check

def choix(board, player):

    print("Player " + str(player.player_id) + " it's your turn :")
    choice1, choice2, choice3, choice4 = ["-(1) : Add circle token\n", "-(2) : Move circle token\n",
                                          "-(3) : Move 1 square token\n", "-(4) : Move 2 square token\n"]
    if player.circletoken_id > 0:
        if player.circletoken_id <= 2 and board.emptytile.tile_id != 5:
            answer = int(input("What do you want to do for the next round?\n"
                               + choice1 + choice2 + choice3 + choice4))
            while answer not in {1, 2, 3, 4}:
                answer = int(input())
        elif player.circletoken_id == 3 and board.emptytile.tile_id != 5:
            answer = int(input("What do you want to do for the next round?\n"
                               + choice2 + choice3 + choice4))
            while answer not in {2, 3, 4}:
                answer = int(input())
        elif player.circletoken_id <= 2 and board.emptytile.tile_id == 5:
            answer = int(input("What do you want to do for the next round?\n"
                               + choice1 + choice2 + choice3))
            while answer not in {1, 2, 3}:
                answer = int(input())
        else:
            answer = int(input("What do you want to do for the next round?\n"
                               + choice2 + choice3))

            while answer not in {2, 3}:
                answer = int(input())
    else:
        if player.circletoken_id <= 2 and board.emptytile.tile_id != 5:
            answer = int(input("What do you want to do for the next round?\n"
                               + choice1 + choice3 + choice4))
            while answer not in {1, 3, 4}:
                answer = int(input())
        elif player.circletoken_id == 3 and board.emptytile.tile_id != 5:
            answer = int(input("What do you want to do for the next round?\n"
                               + choice3 + choice4))
            while answer not in {3, 4}:
                answer = int(input())
        elif player.circletoken_id <= 2 and board.emptytile.tile_id == 5:
            answer = int(input("What do you want to do for the next round?\n"
                               + choice1 + choice3))
            while answer not in {1, 3}:
                answer = int(input())
        else:
            answer = int(input("What do you want to do for the next round?\n"
                               + choice3))

            while answer not in {3}:
                answer = int(input())
    return answer