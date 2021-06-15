from game import Game
from tkinter import *
# from evenorodd import Evenorodd as EOO

class gameui:

    row = 0
    col = 0

    def __init__(self, window, mode):
        game = Game(mode)
        topFrame = Frame(window)
        topFrame.pack(side = TOP)
        leftFrame = Frame(window)
        leftFrame.pack(side = LEFT)
        rightFrame = Frame(window)
        rightFrame.pack(side = RIGHT)
        for i in range(9):
            for j in range(9):
                num = self.getCellText(i, j, game)
                if num == '':
                    Button(leftFrame, text = num, command=lambda row = i, col = j: self.tableButtonPress(row, col), height=2, width = 4).grid(row=i, column=j)
                else:
                    Label(leftFrame, text = num, height=2, width = 4).grid(row=i, column=j)

        for i in range(3):
            for j in range(1,4):
                Button(rightFrame, text=str(i*3+j), command=lambda num = i*3+j : print(row, ' ', col, ' ', num), height=2, width = 4).grid(row = i, column = j)

    def tableButtonPress(self, row, col):
        self.row = row
        self.col = col

    def getCellText(self, row, col, game):
        num = game.feladatTabla[row][col].num
        if num != 0:
            return str(num)
        else:
            return ''

class menuui:
    def __init__(self):
        window = Tk()
        window.title("Suduku")
        frame = Frame(window)
        frame.pack()
        label = Label(frame, text="Válassz egy nehézségi szintet:", fg="black")
        label.pack(side = TOP)
        kezdobutton = Button(frame, text="Kezdő", fg="black", command=lambda: self.switchFrame(frame, window, 'kezdo') )
        kezdobutton.pack(side= TOP)
        haladobutton = Button(frame, text="Haladó", fg="black" , command=lambda: self.switchFrame(frame, window, 'halado'))
        haladobutton.pack(side= TOP)  
        mesterbutton = Button(frame, text="Mester", fg="black", command=lambda: self.switchFrame(frame, window, 'mester'))
        mesterbutton.pack(side= TOP)  
        eoobutton = Button(frame, text="Páros vagy páratlan", fg="black", command=lambda: self.switchFrame(frame, window, 'eoo'))
        eoobutton.pack(side= TOP)
        window.mainloop()

    def switchFrame(self, frame, window, mode):
        frame.destroy()
        gameui(window, mode)
        


