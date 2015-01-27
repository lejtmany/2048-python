__author__ = 'Binary_Ninja'

from tkinter import *
import tkinter.messagebox
import Board
from BoardSquare import *

class GUI(Frame):

    def __init__(self, master = NONE):
        Frame.__init__(self,master)
        self.__init_color_dict()
        self.board = Board.Board()
        self.create_labels()
        self.__update_label_color()

    def create_labels(self):
        self.__labels = {}
        self.__string_vars = self.__generate_stringvars()
        for r in range(self.board.size):
            for c in range(self.board.size):
                label = Label(self, height=4,width=8,textvariable = self.__string_vars[self.board.get_square(c,r)], bd=2, relief=RAISED, font="bold")
                label.grid(row=r, column=c, sticky=N+S+E+W)
                self.__labels[self.board.get_square(c,r)] = label
                self.columnconfigure(c,weight=1)
                self.rowconfigure(r,weight=1)

    def ask_play_again(self):
        if tkinter.messagebox.askyesno("Game Over", "Game Over! \n Play Again?"):
            self.board = Board.Board()
            self.create_labels()
        else:
            sys.exit()

    def move_board(self,x,y):
        self.board.move(x,y)
        self.__update_string_vars()
        self.__update_label_color()
        if self.board.game_over:
            self.ask_play_again()

    def __generate_stringvars(self):
        string_vars = {}
        for square in self.board.get_square_list():
                board_str_var =  StringVar()
                string_vars[square] = board_str_var
                self.__set_string_var(board_str_var, square)
        return string_vars

    def __update_label_color(self):
        for square in self.board.get_square_list():
            self.__labels[square]["bg"] = self.__color_dict[square.value]

    def __update_string_vars(self):
        for square in self.board.get_square_list():
            self.__set_string_var(self.__string_vars[square], square)

    def __set_string_var(self, str_var ,square):
         if square.value == BoardSquare.empty_value:
             str_var.set("")
         else:
            str_var.set(str(square.value))

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
        self.__color_dict[4096]="forest green"
        self.__color_dict[8192]="RoyalBlue3"
        self.__color_dict[BoardSquare.empty_value] = "black"

if __name__ == '__main__':
    root = Tk()
    gui = GUI(root)
    gui.grid(sticky=N+S+E+W)
    root.bind("<Up>", lambda event: gui.move_board(0,-1))
    root.bind("<Down>", lambda event: gui.move_board(0,1))
    root.bind("<Right>", lambda event: gui.move_board(1,0))
    root.bind("<Left>", lambda event: gui.move_board(-1,0))
    root.columnconfigure(0, weight=1)
    root.mainloop()


