def start():
    choice = 0
    level_choice = ["1", "2", "3"]
    print("What mode of game do you want ?")
    print("-(1): Player VS Player\n-(2): Player VS IA\n-(3): IA VS IA")
    while choice not in level_choice:
        choice = input()

def next_round(board, player):

    possibilities = [1, 2, 3]
    answer = int(input("What do you want to do for the next round?\n"
                   "-(1) : Add circle token\n"
                   "-(2) : Move circle token\n"
                   "-(3) : Move square token\n"))
    while answer not in possibilities:
        answer = input()

    if answer == 1:
        coordinate_x = int(input("You are going to add a new circle token, choose x among (0,1,2)"))
        while coordinate_x not in {0, 1, 2}:
            coordinate_x = int(input())

        coordinate_y = int(input("Choose y among (0,1,2)"))
        while coordinate_y not in {0, 1, 2}:
            coordinate_y = int(input())
        board.addCircleToken(coordinate_x,coordinate_y,player)
    elif answer == 2:
        coordinate_x = int(input("You are going to move a circle token, choose x among (0,1,2)"))
        while coordinate_x not in {0, 1, 2}:
            coordinate_x = int(input())
        coordinate_y = int(input("Choose y among (0,1,2)"))
        while coordinate_y not in {0, 1, 2}:
            coordinate_y = int(input())
        circletoken = int(input("Which token id choose among (0,1,2)"))
        while circletoken not in {0, 1, 2}:
            circletoken = input()
        board.moveCircleToken(coordinate_x,coordinate_y,player,circletoken)

