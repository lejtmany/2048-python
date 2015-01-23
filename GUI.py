__author__ = 'Binary_Ninja'

from tkinter import *
import Board

class GUI(Frame):

    def __init__(self, master = NONE):
        Frame.__init__(self,master)
        self.board = Board.Board()
        self.__string_vars = self.__generate_stringvars()
        for r in range(self.board.height):
            for c in range(self.board.width):
                Label(self, textvariable = self.__string_vars[self.board.get_square(c,r)], bd=2, relief=RAISED).grid(row=r, column=c, sticky=N+S+E+W)
                self.columnconfigure(c,weight=1)
                self.rowconfigure(r,weight=1)

    def move_board(self,x,y):
        self.board.move(x,y)
        self.__update_string_vars()

    def __generate_stringvars(self):
        string_vars = {}
        for square in self.board.get_square_list():
                board_str_var =  StringVar()
                string_vars[square] = board_str_var
                board_str_var.set(str(square.value))
        return string_vars

    def __update_string_vars(self):
        for square in self.board.get_square_list():
            self.__string_vars[square].set(square.value)

if __name__ == '__main__':
    root = Tk()
    gui = GUI(root)
    gui.grid(sticky=N+S+E+W)
    root.bind("<Up>", lambda event: gui.move_board(0,1))
    root.bind("<Down>", lambda event: gui.move_board(0,-1))
    root.bind("<Right>", lambda event: gui.move_board(1,0))
    root.bind("<Left>", lambda event: gui.move_board(-1,0))
    root.columnconfigure(0, weight=1)
    root.mainloop()


