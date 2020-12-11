import re

class code:

    def __init__(self, filename):
        self.linesOriginal = []
        f = open(filename, 'r')
        for line in f:
            self.linesOriginal.append(line.strip())
        self.lines = self.linesOriginal
        self.maxX = len(self.lines[0])
        self.maxY = len(self.lines)
        print(f"input: {self.lines} dimensions ({self.maxX}, {self.maxY})")

    
    def countOccupiedAdjacent(self, x, y):
        xmin = min(x-1, 0)
        xmax = max(x+1, self.maxX)
        ymin = min(y-1, 0)
        ymax = max(y-1, self.maxY)
        count = 0
        for xi in range(xmin, xmax):
            for yi in range(ymin, ymax):
                if xi != x or yi != y:
                    if self.lines[x][y] == '#':
                        count += 1
        return count

    @staticmethod
    def printPage(lines):
        for x, i in enumerate(lines):
            print(x, i)
    
    def iterate1(self):

        newLines = [[None]*self.maxY]*self.maxX
        for x in range(0, self.maxX):
            for y in range(0, self.maxY):
                thisCount = self.countOccupiedAdjacent(x, y)
                # if x == 0:
                #     newLines.append([None]*self.maxY)
                if self.lines[x][y] == 'L' and thisCount == 0:
                    # print(f"{x}, {y}")
                    newLines[x][y] = '#'
                elif self.lines[x][y] == '#' and thisCount >= 4:
                    newLines[x][y] = 'L'
                else:
                    newLines[x][y] = self.lines[x][y]
            newLines[x] = ''.join(newLines[x])
        print(f"NewLines:")
        self.printPage(newLines)
        print("----")
        self.lines = newLines



class machine:

    def __init__(self):
        self.input = code()

input = code('testinput.txt')
# input.printPage(input.lines)
# input.printPage(input.lines)
input.iterate1()

# myMachine = machine('testinput.txt')
# myMachine.solve()

# myMachine = machine('testinput2.txt')
# myMachine.solve()

# myMachine = machine('input.txt')
# myMachine.solve()
