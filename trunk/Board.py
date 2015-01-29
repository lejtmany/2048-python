__author__ = 'Binary Ninja'
from BoardSquare import *
import random


class Board:
    size = 4

    def __init__(self):
        self.__squares = self.__generate_board_squares()
        self.__set_empty_square()
        self.game_over = False

    def __generate_board_squares(self):
        squares = []
        for x in range(4):
            for y in range(4):
                squares.append(BoardSquare(x, y, BoardSquare.empty_value))
        return squares

    def __set_empty_square(self):
        random_square = self.__get_random_square()
        random_square.value = self.__get_random_value()

    def __get_random_square(self):
        empty_squares = [square for square in self.__squares if square.value == BoardSquare.empty_value]
        return random.choice(empty_squares)

    def __get_random_value(self):
        return random.randrange(1, 3)

    def move(self, directionX, directionY):
        self.__move_squares(directionX, directionY)
        self.__check_game_over()
        if not self.game_over and self.__changed:
            self.__set_empty_square()

    def __move_squares(self, directionX, directionY):
        self.__changed = False
        self.__shift_squares(directionX, directionY)
        self.__combine_squares(directionX, directionY)
        # need to re-shift if open space left by combining
        self.__shift_squares(directionX, directionY)

    def __shift_squares(self, directionX, directionY):
        for i in range(Board.size):
            non_empty_squares = [square for square in self.__squares if square.value != BoardSquare.empty_value]
            for square in non_empty_squares:
                self.__try_shift_squares(square, directionX, directionY)

    def __try_shift_squares(self, square, directionX, directionY):
        adjacent_square = self.__get_adjacent_square(square, directionX, directionY)
        if adjacent_square is not None and adjacent_square.value == BoardSquare.empty_value:
            self.__shift_square(adjacent_square, square)

    def __shift_square(self, adjacent_square, square):
        adjacent_square.value, square.value = square.value, BoardSquare.empty_value
        self.__changed = True

    def __combine_squares(self, directionX, directionY):
        non_empty_squares = [square for square in self.__squares if square.value != BoardSquare.empty_value]
        #sort so that squares closer to wall moving towards combine first
        self.__sort_squares(directionX, directionY, non_empty_squares)
        for square in non_empty_squares:
            self.__try_combine_squares(square, directionX, directionY)

    def __sort_squares(self, directionX, directionY, non_empty_squares):
        if directionX:
            non_empty_squares.sort(key=lambda item: item.x * -directionX)
        elif directionY:
            non_empty_squares.sort(key=lambda item: item.y * -directionY)

    def __try_combine_squares(self, square, directionX, directionY):
        adjacent_square = self.__get_adjacent_square(square, directionX, directionY)
        if adjacent_square is not None and adjacent_square.value == square.value:
            self.__combine_square(adjacent_square, square)

    def __combine_square(self, adjacent_square, square):
        square.value = BoardSquare.empty_value
        adjacent_square.value *= 2
        self.__changed = True

    def __get_adjacent_square(self, square, directionX, directionY):
        coordinates = square.get_coordinates()
        adjacent_coordinates = coordinates['x'] + directionX, coordinates['y'] + directionY
        return self.get_square(adjacent_coordinates[0], adjacent_coordinates[1])

    def __check_game_over(self):
        if [square for square in self.__squares if square.value == BoardSquare.empty_value] == []:
            self.game_over = True
        else:
            self.game_over = False

    def get_square(self, x, y):
        matching = [square for square in self.__squares if
                    square.get_coordinates()['x'] == x and square.get_coordinates()['y'] == y]
        if matching:
            return matching[0]
        else:
            return None

    def get_square_list(self):
        return self.__squares