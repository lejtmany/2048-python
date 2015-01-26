__author__ = 'Binary_Ninja'

from tkinter import *
import tkinter.messagebox
import Board
from BoardSquare import *

class GUI(Frame):

    def __init__(self, master = NONE):
        Frame.__init__(self,master)
        self.board = Board.Board()
        self.create_labels()
        self.__update_label_color()

    def create_labels(self):
        self.__labels = {}
        self.__string_vars = self.__generate_stringvars()
        for r in range(self.board.size):
            for c in range(self.board.size):
                label = Label(self, height=4,width=8,textvariable = self.__string_vars[self.board.get_square(c,r)], bd=2, relief=RAISED)
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
            if square.value == 1:
                self.__labels[square]["bg"] = "azure"
            elif square.value == 2:
                self.__labels[square]["bg"] = "misty rose"
            elif square.value == 4:
                self.__labels[square]["bg"] = "peach puff"
            elif square.value == 8:
                self.__labels[square]["bg"] = "palegreen1"
            elif square.value == 16:
                self.__labels[square]["bg"] = "slategray2"
            elif square.value == 32:
                self.__labels[square]["bg"] = "plum1"
            elif square.value == 64:
                self.__labels[square]["bg"] = "indianred1"
            elif square.value == 128:
                self.__labels[square]["bg"] = "firebrick3"
            elif square.value == 256:
                self.__labels[square]["bg"] = "darkorchid2"
            elif square.value == 512:
                self.__labels[square]["bg"] = "hotpink2"
            elif square.value == 1024:
                self.__labels[square]["bg"] = "cornflowerblue"
            elif square.value == 2048:
                self.__labels[square]["bg"] = "red4"
            elif square.value == BoardSquare.empty_value:
                self.__labels[square]["bg"] = "gray94"

    def __update_string_vars(self):
        for square in self.board.get_square_list():
            self.__set_string_var(self.__string_vars[square], square)

    def __set_string_var(self, str_var ,square):
         if square.value == BoardSquare.empty_value:
             str_var.set("")
         else:
            str_var.set(str(square.value))

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


