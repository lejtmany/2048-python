__author__ = 'Binary Ninja'
from BoardSquare import *
import random
class Board:
    height = 4
    width = 4
    __squares = []

    def __init__(self):
        self.__generate_board_squares()

    def __generate_board_squares(self):
        for x in range(0,4):
            for y in range(0,4):
                self.__squares.append(BoardSquare(x, y, BoardSquare.empty_value))

    def pop_random_square(self):
        empty_squares = [square for square in self.__squares if square.value == BoardSquare.empty_value]
        return random.choice(empty_squares)

    def get_random_value(self):
        return random.randrange(1,3)

    def set_empty_square(self):
        random_square = self.pop_random_square()
        random_square.value = self.get_random_value()

    def move(self, x, y):
        self.combine_squares(x,y)
        self.shift_squares(x,y)

  #  def shift_squares(self, x, y):
       # if(get_square)

    def get_square(self, x, y):
        return [square for square in self.__squares if square.get_coordinates()['x'] == x and square.get_coordinates()['y'] == y]