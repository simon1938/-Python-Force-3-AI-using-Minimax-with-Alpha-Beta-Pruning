# Correspondence between the identifier of the tiles and their coordinates x and y
correlation = {"1": [0, 0], "2": [1, 0],
               "3": [2, 0], "4": [0, 1],
               "5": [1, 1], "6": [2, 1],
               "7": [0, 2], "8": [1, 2],
               "9": [2, 2]}

# Line of the playing area allowing to deduce the segond square token when 2 square token moves
ga_line = [[1, 4, 7],
           [1, 2, 3],
           [3, 6, 9],
           [9, 8, 7],
           [4, 5, 6],
           [2, 5, 8]]

winning_combination = [[1, 2, 3],
                       [4, 5, 6],
                       [7, 8, 9],
                       [1, 4, 7],
                       [2, 5, 8],
                       [3, 6, 9],
                       [1, 5, 9],
                       [3, 5, 7]]

moveable_1squaretoken = {"1": [2, 4], "2": [1, 3, 5],
                         "3": [2, 6], "4": [1, 5, 7],
                         "5": [2, 4, 6, 8], "6": [3, 5, 9],
                         "7": [4, 8], "8": [5, 7, 9],
                         "9": [6, 8]}

moveable_2squaretoken = {"1": [3, 7], "2": [8],
                         "3": [1, 9], "4": [6],
                         "5": [], "6": [4],
                         "7": [1, 9], "8": [2],
                         "9": [3, 7]}
deep = 2