import random

class Field:

    num = None
    starter = True
    shaded = False

    def __init__(self, num):
        self.num = num

class Game:
    tabla = [[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0]]
    def __init__(self):
        keres = True
        while keres:
            szamok = [1,2,3,4,5,6,7,8,9]
            random.shuffle(szamok)
            self.tabla[3][3:6] = szamok[0:3]
            self.tabla[4][3:6] = szamok[3:6]
            self.tabla[5][3:6] = szamok[6:9]

            try:
                self._generateGrid(0,3,3,6)
                self._generateGrid(6,9,3,6)
                self._generateGrid(3,6,0,3)
                self._generateGrid(3,6,6,9)
                self._generateGrid(0,3,0,3)
                self._generateGrid(0,3,6,9)
                self._generateGrid(6,9,0,3)
                self._generateGrid(6,9,6,9)
                keres = False
            except UserWarning:
                self.tabla = [[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0]]
        self.kiir()


    def _generateGrid(self,x1,x2,y1,y2):
        for i in range(x1,x2):
            for j in range(y1,y2):
                hiba = 0
                while True:
                    rand = random.randint(1,9)
                    if self._checkTable(i, j, rand):
                        self.tabla[i][j] = rand
                        break
                    else:
                        hiba+=1
                        if hiba == 28:
                            raise UserWarning()

    def _checkTable(self,x,y,num):
        if num in self.tabla[x]:
            return False
        if num in [ x[y] for x in self.tabla]:
            return False
        if x<3:
            if y<3:
              square=[self.tabla[i][0:3] for i in range(0,3)]
            elif y<6:
              square=[self.tabla[i][3:6] for i in range(0,3)]
            else:  
              square=[self.tabla[i][6:9] for i in range(0,3)]
        elif x<6:
            if y<3:
              square=[self.tabla[i][0:3] for i in range(3,6)]
            elif y<6:
              square=[self.tabla[i][3:6] for i in range(3,6)]
            else:  
              square=[self.tabla[i][6:9] for i in range(3,6)]
        else:
            if y<3:
              square=[self.tabla[i][0:3] for i in range(6,9)]
            elif y<6:
              square=[self.tabla[i][3:6] for i in range(6,9)]
            else:  
              square=[self.tabla[i][6:9] for i in range(6,9)]
        if num in (square[0] + square[1] + square[2]):
            return False
        return True    

    def check(self):
        for i in range(len(self.tabla)):
            sor=set()
            for j in range(len(self.tabla[i])):
                sor.add(self.tabla[i][j])
            if len(sor)!=9:
                return False    


        for i in range(len(self.tabla)):
            oszlop=set()
            for j in range(len(self.tabla[i])):
                oszlop.add(self.tabla[j][i])
            if len(oszlop)!=9:
                return False 


        for i in range(0,3):
            for j in range(0,3):
                negyzet=set()
                for k in range(0,3):
                    for l in range(0,3):
                        negyzet.add(self.tabla[i*3+k][j*3+l])
                if len(negyzet)!=9:
                    return False
        return True

    def kiir(self):
        for i in range(len(self.tabla)):
            print(self.tabla[i])