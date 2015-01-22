__author__ = 'Binary_Ninja'

from tkinter import *
import Board

class GUI(Frame):

    def __init__(self, master = NONE):
        Frame.__init__(self,master)
        Label(self, text="hello there")
        self.board = Board.Board()
        self.__labels = {}
        for r in range(self.board.height):
            for c in range(self.board.width):
                Label(self, text = self.board.get_square(c,r).value, bd=2, relief=RAISED).grid(row=r, column=c, sticky=N+S+E+W)
                self.columnconfigure(c,weight=1)
                self.rowconfigure(r,weight=1)

    def move_board(self,x,y):
        self.board.move(x,y)

#def move_board(gui,x,y):
 #   gui.move_board(x,y)


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


