

LIVE = "X"
DEAD = "0"

class Cell:
    alive = False
    x = 0
    y = 0

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def printState(self):
        if self.alive:
            print(LIVE, end="")
        else:
            print(DEAD, end="")


class Grid:
    width = 0
    height = 0
    array = []  #must be initialized in __init__
    
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.array = [[0 for x in range(height)] for x in range(width)]

        for i in range(0, self.width):
            for j in range(0, self.height):
                self.array[i][j] = Cell(i, j)

    def printArr(self):
        for i in range(0, self.width):
            for j in range(0, self.height):
                self.array[i][j].printState()
            print()

    def initGame(self):
        #game will randomly assign Alive to tiles, with a 15% chance for being alive
        pass

    def checkNeighbors(self, x, y):
        #TODO implement
        pass


if __name__ == "__main__":
    a = Grid(4, 10)
    a.printArr()
