__author__ = 'Binary Ninja'
import BoardSquare
class Board:
    height = 4
    width = 4
    __squares = []

    def __init__(self):
        Board.__generate_board_squares()

    def __generate_board_squares(self):
        for x in range(0,3):
            for y in range(0,3):
                Board.__squares.append(BoardSquare(BoardSquare.empty_value,x,y))

    def pop_random_square(self):
        empty_squares = []

