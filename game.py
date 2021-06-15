import random

class Field:

    num = None
    starter = True
    shaded = False

    def __init__(self, num, starter = False, shaded = False):
        self.num = num
        self.starter = starter
        self.shaded = shaded

class Game:
    megoldottTabla = [[0 for i in range(9)] for j in range(9)]
    feladatTabla = [[Field(0) for i in range(9)] for j in range(9)]
    lives = 3
    help = 5
    def __init__(self, mode):
        
        """
        Args:
            mode (string): Ez határozza meg, hogy milyen nehézségi fokon fogunk játszani.
        """
        
        self.tablageneralas()
        self.kezdotablaKeszites(mode)

    def tablageneralas(self):
        
        """
        Ebben a függvényben generáljuk a táblát a generateGrid függvény segítségével. Ha elér egy adott számú próbálkozáshoz (esetünkben 28),
        akkor újra kezdi a tábla generelását. Erre azért van szükség, mivel adott számú próbálkozással sem találja meg a sudoku szabályainak megfelelő számot
        valószínű, hogy nem létezik helyes szám az adott pozícióba. 
        """
        
        keres = True
        while keres:
            szamok = [1,2,3,4,5,6,7,8,9]
            random.shuffle(szamok)
            self.megoldottTabla[3][3:6] = szamok[0:3]
            self.megoldottTabla[4][3:6] = szamok[3:6]
            self.megoldottTabla[5][3:6] = szamok[6:9]

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
                self.megoldottTabla = [[0 for i in range(9)] for j in range(9)]
        #self.kiir()


    def _generateGrid(self,x1,x2,y1,y2):
        
        """
        Véletlenszerű számokkal próbálja meg feltölteni a paraméterek által jelölt résztáblát a sudoku szabályai alapján. 

        Args:
            x1 (int): a generálandó 3x3-as négyzet x tengelyen lévő első koordinátája
            x2 (int): a generálandó 3x3-as négyzet x tengelyen lévő utolsó koordinátája
            y1 (int): a generálandó 3x3-as négyzet y tengelyen lévő első koordinátája
            y2 (int): a generálandó 3x3-as négyzet y tengelyen lévő utolsó koordinátája

        Raises:
            UserWarning: Jelzi a tábla generáló függvénynek, hogy elértük a maximum megengedett próbálkozásaink számát.  
        """

        for i in range(x1,x2):
            for j in range(y1,y2):
                hiba = 0
                while True:
                    rand = random.randint(1,9)
                    if self._checkTable(i, j, rand):
                        self.megoldottTabla[i][j] = rand
                        break
                    else:
                        hiba+=1
                        if hiba == 28:
                            raise UserWarning()

    def _checkTable(self,x,y,num):
        """
        A függvény ellenőrzi, hogy a sudoku szabályai alapján egy adott szám beilleszthető-e egy adott mezőbe.

        Args:
            x (int): annak a mezőnek az x koordinátája amelyet módosítani szeretnénk
            y (int): annak a mezőnek az y koordinátája amelyet módosítani szeretnénk
            num (int): a táblába beillesztendő szám

        Returns:
            bool: érték ha igaz: beilleszthető
                  érték ha hamis: nem beilleszthető
        """
        if num in self.megoldottTabla[x]:
            return False
        if num in [x[y] for x in self.megoldottTabla]:
            return False
        if x<3:
            if y<3:
              square=[self.megoldottTabla[i][0:3] for i in range(0,3)]
            elif y<6:
              square=[self.megoldottTabla[i][3:6] for i in range(0,3)]
            else:  
              square=[self.megoldottTabla[i][6:9] for i in range(0,3)]
        elif x<6:
            if y<3:
              square=[self.megoldottTabla[i][0:3] for i in range(3,6)]
            elif y<6:
              square=[self.megoldottTabla[i][3:6] for i in range(3,6)]
            else:  
              square=[self.megoldottTabla[i][6:9] for i in range(3,6)]
        else:
            if y<3:
              square=[self.megoldottTabla[i][0:3] for i in range(6,9)]
            elif y<6:
              square=[self.megoldottTabla[i][3:6] for i in range(6,9)]
            else:  
              square=[self.megoldottTabla[i][6:9] for i in range(6,9)]
        if num in (square[0] + square[1] + square[2]):
            return False
        return True    

    # def check(self):
    #     for i in range(len(self.megoldottTabla)):
    #         sor=set()
    #         for j in range(len(self.megoldottTabla[i])):
    #             sor.add(self.megoldottTabla[i][j])
    #         if len(sor)!=9:
    #              return False    


    #     for i in range(len(self.megoldottTabla)):
    #         oszlop=set()
    #         for j in range(len(self.megoldottTabla[i])):
    #             oszlop.add(self.megoldottTabla[j][i])
    #         if len(oszlop)!=9:
    #             return False 

    #     for i in range(0,3):
    #         for j in range(0,3):
    #             negyzet=set()
    #             for k in range(0,3):
    #                 for l in range(0,3):
    #                     negyzet.add(self.megoldottTabla[i*3+k][j*3+l])
    #             if len(negyzet)!=9:
    #                 return False
    #     return True

    def kezdotablaKeszites(self, szint):
        """
        A megadott szint alapján hozza létre a megadott tábla alap tábláját. Szintenként eltér, hogy hány számot rakunk bele a kezdő táblánkba.

        Args:
            szint (string): eldönti milyen szinten szeretnénk játszani
        """
        elofordulas = []
        if szint == "kezdo":
            elofordulas=[3,1,2,4,3,5,4,3,2]
        elif szint == "halado":
            elofordulas=[3,1,2,2,3,4,3,3,1]
        else:
            elofordulas=[2,4,3,1,0,2,3,1,1]
        random.shuffle(elofordulas)
        for i in range(9):
            ssz = 0 # sorszám
            db = 0 # hány db-t talált már meg a mátrixban a bejárás
            poz = []
            for j in range(elofordulas[i]):
                rand = random.randint(1, 9)
                while rand in poz:
                    rand = random.randint(1, 9)
                poz.append(rand)
            poz.sort()
            for x in range(9):
                for y in range(9):
                    if self.megoldottTabla[x][y] == i+1:
                        db+=1
                        if ssz<len(poz) and db == poz[ssz]:
                            self.feladatTabla[x][y] = Field(i+1, True)
                            ssz+=1
        #self.kiirFeladat()
        
    
    # def kiir(self):
    #     for i in range(len(self.megoldottTabla)):
    #         print(self.megoldottTabla[i])

    # def kiirFeladat(self):
    #     for i in range(len(self.feladatTabla)):
    #         for j in range (len(self.feladatTabla)):
    #             print(self.feladatTabla[i][j].num, end = ' ')
    #         print()

    def beir(self, x, y, num):
        """
        A függvény eldönti, hogy a szám amit be akarunk írni a táblába, beírható-e a táblába vagy sem és vizsgálja, hogy hány hiba lehetőségünk maradt.

        Args:
            x (int): annak a mezőnek az x koordinátája amelybe az adott számot írni szeretnénk
            y (int): annak a mezőnek az y koordinátája amelybe az adott számot írni szeretnénk
            num (int): a szám amit az adott mezőbe írni szeretnénk

        Returns:
            int: a számok döntik el, hogy helyes-e a szám és bekerülhet-e a mezőbe, helytelen-e a szám és hibázhatunk-e még vagy helytelen-e a szám és már nem hibázhatunk.
                 Az utolsó eshetőségben a játék véget ér. A függvény ezt jelzi a 2-es visszatérési értékkel, amelyet a program a későbbiekben lekezel.
        """
        if self.megoldottTabla[x][y] == num:
            self.feladatTabla[x][y].num = num
            return 0 # helyes szám kerül a mezőbe
        else:
            self.lives -=1
            if self.lives == 0:
                return 2 # helytelen szám és elfogyott az életünk
            return 1 # helytelen szám, de még van életünk
    
    def help(self, x, y):
        """
        A játék során ha elakadunk kérhetünk segítséget. A függvény meghívásakor a kiválasztott mezőn megjelenik a helyes szám.

        Args:
            x (int): annak a mezőnek az x koordinátája amelybe az adott számot írni szeretnénk segítségképp
            y (int): annak a mezőnek az y koordinátája amelybe az adott számot írni szeretnénk segítségképp
        """
        self.feladatTabla[x][y].num = self.megoldottTabla[x][y]