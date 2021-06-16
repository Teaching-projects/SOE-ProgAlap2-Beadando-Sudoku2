from game import Game
from game import Field
import random

# class Field(Field):

#     shaded = False
    
#     def __init__(self,num, starter = False, shaded= False):
#         super().__init__(num, starter)
#         self.shaded = shaded


class Evenorodd(Game): 

    szinezett = ''

    def __init__(self):
        """
        Az inicializálás után a függvény "besatírozza" a páros vagy a páratlan mezőket.
        """
        super().__init__('halado')
        color = random.randint(0,1)
        if color == 0:
            self.szinezett = 'Párosak'
        else:
            self.szinezett = 'Páratlanok' 
        for i in range(9):
            for j in range(9):
                if self.megoldottTabla[i][j] % 2 == color:
                    self.feladatTabla[i][j].shaded = True

    
