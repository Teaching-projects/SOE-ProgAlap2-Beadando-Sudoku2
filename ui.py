from game import Game
from tkinter import *
from tkinter import messagebox
from evenorodd import Evenorodd as EOO

class gameui:

    row = -1
    col = -1
    buttonArray = []

    def __init__(self, window, mode):
        #window.configure(bg ="lightgreen")
        game = None
        if mode == 'eoo':
            game = EOO()
        else:
            game = Game(mode)
        topFrame = Frame(window)
        topFrame.pack(side = TOP)
        hintButton = Button(topFrame, text = "Segítségek száma: 5")
        hintButton.pack(side = LEFT)
        lifeLabel = Label(topFrame, text = "Hibák száma: 3")
        lifeLabel.pack(side = RIGHT)
        hintButton.pack(side = LEFT)
        hintButton.configure(command = lambda: self.hintPressed(hintButton, game))
        if mode == 'eoo' :
            szoveg = "Szinezett mezők: "+game.szinezett
            szinezettLabel = Label(topFrame, text = szoveg)
            szinezettLabel.pack(side = RIGHT)
        leftFrame = Frame(window)
        leftFrame.pack(side = LEFT)
        rightFrame = Frame(window)
        rightFrame.pack(side = RIGHT)
        for i in range(9):
            for j in range(9):
                num = self.getCellText(i, j, game)
                if num == '':
                    self.buttonArray.append(Button(leftFrame, text = num, command=lambda row = i, col = j: self.tableButtonPress(row, col, game),borderwidth= 2, relief = "solid", height=2, width = 4))
                    self.buttonArray[i*9+j].grid(row=i, column=j)
                    if self.getCellShade(i, j, game) :
                        self.buttonArray[i*9+j].configure(bg = "lightgray")

                else:
                    Label(leftFrame, text = num, height=2, width = 4,borderwidth= 2, relief = "solid").grid(row=i, column=j )
                    self.buttonArray.append(Button(text = "tömb kitöltő"))
                
        for i in range(3):
            for j in range(1,4):
                Button(rightFrame, text=str(i*3+j), command=lambda num = i*3+j : self.numberButtonPress(num, game,lifeLabel, topFrame, leftFrame, rightFrame, window), height=2, width = 4).grid(row = i, column = j)

        

    def hintPressed(self, hintButton, game):
        if self.row != -1 and self.col != -1:
            num = game.help(self.row, self.col)
            if num != -1:
                self.buttonArray[self.row*9+self.col].configure(text = num)
                szoveg = "Segítségek száma: "+str(game.helpCount)
                hintButton.configure(text = szoveg)
            if self.getCellShade(self.row, self.col, game):
                self.buttonArray[self.row*9+self.col].configure(bg = 'lightgray')
            else:    
                self.buttonArray[self.row*9+self.col].configure(bg = 'SystemButtonFace')
            self.row = -1
            self.col = -1


    def tableButtonPress(self, row, col, game):
        self.row = row
        self.col = col
        for i in range(len(self.buttonArray)):
            if i == self.row*9+self.col:
                self.buttonArray[i].configure(bg = "lightblue")
            else:
                if self.getCellShade(i//9, i%9, game):
                    self.buttonArray[i].configure(bg = 'lightgray')
                else:    
                    self.buttonArray[i].configure(bg = 'SystemButtonFace')

    def getCellText(self, row, col, game):
        num = game.feladatTabla[row][col].num
        if num != 0:
            return str(num)
        else:
            return ''

    def getCellShade(self, row, col, game):
        return game.feladatTabla[row][col].shaded

    def numberButtonPress(self, num, game, lifeLabel, topFrame, leftFrame, rightFrame, window):
        if self.row != -1 and self.col != -1:
            kod = game.beir(self.row, self.col,num)
            self.buttonArray[self.row*9+self.col].configure(text = num)
            if kod == 0:
                if self.getCellShade(self.row, self.col, game):
                    self.buttonArray[self.row*9+self.col].configure(fg = "black", bg = 'lightgray')
                else:
                    self.buttonArray[self.row*9+self.col].configure(fg = "black", bg = 'SystemButtonFace')
            elif kod == 1:
                if self.getCellShade(self.row, self.col, game):
                    self.buttonArray[self.row*9+self.col].configure(fg = "red", bg = 'lightgray')
                else:
                    self.buttonArray[self.row*9+self.col].configure(fg = "red", bg = 'SystemButtonFace')
                szoveg = "Hibák száma: "+str(game.misstake)
                lifeLabel.configure(text = szoveg)
            elif kod == 2:
                self.buttonArray[self.row*9+self.col].configure(fg = "red", bg = 'SystemButtonFace')
                messagebox.showinfo(title = "Vesztettél", message = "Sajnálom, vesztettél!")
                window.destroy()
            elif kod == 3: 
                messagebox.showinfo(title = "Nyertél", message = "Gratulálok, nyertél!")
                window.destroy()
            self.row = -1
            self.col = -1


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
        


