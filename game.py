import random
from time import sleep
import os

LIVE = "X"
DEAD = "-"

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
    height = 0
    width = 0
    array = []
    next_step = []
    
    def __init__(self, height, width):
        self.height = height
        self.width = width
        self.array = [[0 for x in range(width)] for x in range(height)]
        self.next_step = [[0 for x in range(width)] for x in range(height)]

        for i in range(0, self.height):
            for j in range(0, self.width):
                self.array[i][j] = Cell(i, j)

    def printArr(self):
        for i in range(0, self.height):
            for j in range(0, self.width):
                self.array[i][j].printState()
            print()

    def initGame(self):
        #game will randomly assign Alive to tiles, with a 5% chance for being alive
        for i in range(0, self.height):
            for j in range(0, self.width):
                val = random.random()
                if val <= 0.15:
                    self.array[i][j].alive = True
        self.next_step = self.array

    def checkNeighbors(self, x, y):
        count = 0

        above = -1
        below = 2
        left = -1
        right = 2

        if x == 0:
            above = 0
        if x == self.height-1:
            below = 1
        if y == 0:
            left  = 0
        if y == self.width-1:
            right = 1
    
        for xs in range(above, below):
            for ys in range(left, right):
                if xs == 0 and ys == 0:
                    continue
                if self.array[xs+x][ys+y].alive == True:
                    count += 1

        return count

    def runCheck(self):
        for i in range(0, self.height):
            for j in range(0, self.width):
                num = a.checkNeighbors(i, j)
                if self.array[i][j].alive:
                    if num < 2:
                        #under populated, so DIE
                        self.next_step[i][j].alive = False
                    elif num > 3:
                        #over populated, so DIE
                        self.next_step[i][j].alive = False
                    pass
                else:
                    if num == 3:
                        self.next_step[i][j].alive = True
        self.array = self.next_step

if __name__ == "__main__":
    a = Grid(40, 100)
    a.initGame()

    while True:
        sleep(0.05)
        os.system('clear')#if unix
        a.printArr()
        a.runCheck()
        print()
