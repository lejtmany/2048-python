__author__ = 'Binary_Ninja'

from tkinter import *
import tkinter.messagebox
import Board
from BoardSquare import *


class GUI(Frame):
    def __init__(self, master=NONE):
        Frame.__init__(self, master)
        self.__init_color_dict()
        self.board = Board.Board()
        self.create_labels()
        self.__update_values()
        self.__update_label_color()

    def __create_label(self, square):
        label = Label(self, height=4, width=8, bd=2, relief=RAISED, font="bold")
        label.grid(column=square.x, row=square.y, sticky=N + S + E + W)
        self.__labels[square] = label


    def create_labels(self):
        self.__labels = {}
        for square in self.board.get_square_list():
            self.__create_label(self.board.get_square(square.x, square.y))


    def move_board(self, x, y):
        self.board.move(x, y)
        self.__update_values()
        self.__update_label_color()
        if self.board.game_over:
            self.ask_play_again()

    def ask_play_again(self):
        if tkinter.messagebox.askyesno("Game Over", "Game Over! \n Play Again?"):
            self.board = Board.Board()
            self.create_labels()
        else:
            sys.exit()

    def __update_label_color(self):
        for square in self.board.get_square_list():
            self.__labels[square]["bg"] = self.__color_dict[square.value]

    def __update_values(self):
        for square in self.board.get_square_list():
            self.__labels[square]['text'] = square.value

    def __init_color_dict(self):
        self.__color_dict = {}
        self.__color_dict[1] = "thistle"
        self.__color_dict[2] = "misty rose"
        self.__color_dict[4] = "peach puff"
        self.__color_dict[8] = "palegreen1"
        self.__color_dict[16] = "slategray2"
        self.__color_dict[32] = "plum1"
        self.__color_dict[64] = "indianred1"
        self.__color_dict[128] = "firebrick3"
        self.__color_dict[256] = "darkorchid2"
        self.__color_dict[512] = "hotpink2"
        self.__color_dict[1024] = "cornflowerblue"
        self.__color_dict[2048] = "red4"
        self.__color_dict[4096] = "forest green"
        self.__color_dict[8192] = "RoyalBlue3"
        self.__color_dict[BoardSquare.empty_value] = "black"


if __name__ == '__main__':
    root = Tk()
    gui = GUI(root)
    gui.grid(sticky=N + S + E + W)
    root.bind("<Up>", lambda event: gui.move_board(0, -1))
    root.bind("<Down>", lambda event: gui.move_board(0, 1))
    root.bind("<Right>", lambda event: gui.move_board(1, 0))
    root.bind("<Left>", lambda event: gui.move_board(-1, 0))
    root.columnconfigure(0, weight=1)
    root.mainloop()


