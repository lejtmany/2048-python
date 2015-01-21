__author__ = 'Binary_Ninja'

from tkinter import *
import Board

class GUI(Frame):

    def __init__(self, master = NONE):
        Frame.__init__(self,master)
        Label(self, text="hello there")
        board = Board.Board()
        for r in range(board.height):
            for c in range(board.width):
                Label(self, text = board.get_square(c,r).value, bd=2, relief=RAISED).grid(row=r, column=c, sticky=N+S+E+W)
                self.columnconfigure(c,weight=1)
                self.rowconfigure(r,weight=1)

if __name__ == '__main__':
    root = Tk()
    gui = GUI(root).grid(sticky=N+S+E+W)
    root.columnconfigure(0, weight=1)
    root.mainloop()


