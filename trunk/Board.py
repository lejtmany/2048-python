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

    def __get_random_square(self):
        empty_squares = [square for square in self.__squares if square.value == BoardSquare.empty_value]
        return random.choice(empty_squares)

    def __get_random_value(self):
        return random.randrange(1,3)

    def __set_empty_square(self):
        random_square = self.__get_random_square()
        random_square.value = self.__get_random_value()

    def move(self, deltaX, deltaY):
        self.__changed=False
        self.__shift_squares(deltaX,deltaY)
        self.__combine_squares(deltaX,deltaY)
        #need to re-shift if open space left by combining
        self.__shift_squares(deltaX,deltaY)
        self.__check_game_over()
        if not self.game_over and self.__changed:
            self.__set_empty_square()

    def __shift_squares(self, deltaX, deltaY):
        for i in range(Board.size):
            non_empty_squares = [square for square in self.__squares if square.value != BoardSquare.empty_value]
            for square in non_empty_squares:
               self.__try_shift_squares(square, deltaX, deltaY)

    def __try_shift_squares(self,square, deltaX, deltaY):
        adjacent_square = self.__get_adjacent_square(square, deltaX, deltaY)
        if adjacent_square is not None and adjacent_square.value == BoardSquare.empty_value:
            self.__shift_square(adjacent_square, square)

    def __shift_square(self, adjacent_square, square):
        adjacent_square.value, square.value = square.value, BoardSquare.empty_value
        self.__changed = True

    def __combine_squares(self, deltaX, deltaY):
        non_empty_squares = [square for square in self.__squares if square.value != BoardSquare.empty_value]
        self.__sort_squares(deltaX, deltaY, non_empty_squares)
        for square in non_empty_squares:
            self.__try_combine_squares(square, deltaX, deltaY)

    def __sort_squares(self, deltaX, deltaY, non_empty_squares):
        if deltaX:
            non_empty_squares.sort(key=lambda item: item.x * -deltaX)
        elif deltaY:
            non_empty_squares.sort(key=lambda item: item.y * -deltaY)

    def __try_combine_squares(self, square, deltaX, deltaY):
        adjacent_square = self.__get_adjacent_square(square, deltaX, deltaY)
        if adjacent_square is not None and adjacent_square.value == square.value:
            self.__combine_square(adjacent_square, square)

    def __combine_square(self, adjacent_square, square):
        square.value = BoardSquare.empty_value
        adjacent_square.value *= 2
        self.__changed = True

    def __get_adjacent_square(self,square,deltaX, deltaY):
        coordinates = square.get_coordinates()
        adjacent_coordinates = coordinates['x'] + deltaX, coordinates['y'] + deltaY
        return self.get_square(adjacent_coordinates[0], adjacent_coordinates[1])

    def __check_game_over(self):
        if [square for square in self.__squares if square.value == BoardSquare.empty_value] == []:
            self.game_over = True
        else:
            self.game_over = False

    def get_square(self, x, y):
        matching = [square for square in self.__squares if square.get_coordinates()['x'] == x and square.get_coordinates()['y'] == y]
        if matching: return matching[0]
        else: return None

    def get_square_list(self):
        return self.__squares