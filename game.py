import random

class Field:

    num = 0
    starter = True
    shaded = False

    def __init__(self, num):
        self.num = num

class Game:
    tabla = []
    def __init__(self):
        row = [1,2,3,4,5,6,7,8,9]
        for i in range(9):
            random.shuffle(row)
            self.tabla.append(row)
        print(self.tabla)

    def check(self):
        pass

