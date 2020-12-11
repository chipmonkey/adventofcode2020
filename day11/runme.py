import re
import time

class code:

    def __init__(self, filename):
        self.linesOriginal = []
        f = open(filename, 'r')
        for line in f:
            self.linesOriginal.append(line.strip())
        self.lines = self.linesOriginal
        self.maxX = len(self.lines)
        self.maxY = len(self.lines[0])
        print(f"input: {self.lines} dimensions ({self.maxX}, {self.maxY})")

    
    def countOccupiedAdjacent(self, x, y):
        xmin = 0 if x == 0 else x - 1
        ymin = 0 if y == 0 else y - 1
        xmax = self.maxX - 1 if x >= self.maxX - 1 else x + 1
        ymax = self.maxY - 1 if y >= self.maxY - 1 else y + 1
        # print(f"Counting for ({x}, {y}) as range x: ({xmin} - {xmax}) and y: ({ymin} - {ymax})")
        count = 0
        for xi in range(xmin, xmax+1):
            for yi in range(ymin, ymax+1):
                if xi != x or yi != y:
                    # print(f"position ({xi}, {yi}) has value {self.lines[xi][yi]}")
                    if self.lines[xi][yi] == '#':
                        count += 1
        # print(f"We counted {count} for ({x}, {y})")
        # time.sleep(1)
        return count
    
    def countOccupiedRays(self, x, y):
        """ Counts 1 if any seat is in a line in the 8 cardinal directions, otherwise 0"""
        # Right:
        count = 0
        for direction in ['N', 'NE', 'E', 'SE', 'S', 'SW', 'W', 'NW']:
        # for direction in ['NW']:
            thisCount = 0
            found = False
            xi = x
            yi = y
            while not found and 0 <= xi <= self.maxX and 0 <= yi <= self.maxY:
                if 'N' in direction:
                    xi = xi - 1
                elif 'S' in direction:
                    xi = xi + 1
                if 'E' in direction:
                    yi = yi + 1
                elif 'W' in direction:
                    yi = yi - 1
                # print(f"(xi, yi) is : ({xi}, {yi}) starting at ({x}, {y})")
                if 0 <= xi < self.maxX and 0 <= yi < self.maxY:
                    # print(f"Searching lines[{xi}][{yi}] which has {self.lines[xi][yi]}")
                    if self.lines[xi][yi] == '#':
                        thisCount += 1
                        found = True
                    if self.lines[xi][yi] == 'L':  # Exit if we find an empty seat first
                        found = True
            count = count + thisCount
            # print(f"Found: {thisCount} while moving {direction} - total: {count}")
        return(count)



    def countAllSeats(self):
        count = 0
        for x in self.lines:
            count = count + x.count('#')
        return(count)


    @staticmethod
    def printPage(lines):
        for x, i in enumerate(lines):
            print(x, i)
    
    @staticmethod
    def printCount(countLines):
        for x in range(0, len(countLines)):
            for y in range(0, len(countLines[0])):
                print(f"countLines[{x}][{y}] = {countLines[x][y]}")
    
    def iterate1(self):
        print("Lines coming in:")
        self.printPage(self.lines)

        countLines = [[None]*self.maxY for _ in range(self.maxX)]
        newLines = [[None]*self.maxY]*self.maxX
        for x in range(0, self.maxX):
            for y in range(0, self.maxY):
                thisCount = self.countOccupiedRays(x, y)
                countLines[x][y] = thisCount
                # print(f"Count updated for ({x}, {y}) to {thisCount}")
                # self.printPage(countLines)
                # if x == 0:
                #     newLines.append([None]*self.maxY)
                if self.lines[x][y] == 'L' and thisCount == 0:
                    # print(f"{x}, {y}")
                    newLines[x][y] = '#'
                elif self.lines[x][y] == '#' and thisCount >= 5:
                    newLines[x][y] = 'L'
                else:
                    newLines[x][y] = self.lines[x][y]
            newLines[x] = ''.join(newLines[x])
        print(f"CountLines:")
        self.printPage(countLines)
        print(f"NewLines:")
        self.lines = newLines
        self.printPage(self.lines)
        print("----")

    
    def solve(self):
        runCount = 0
        diff = True
        while diff:
            lastLines = self.lines
            self.iterate1()
            diff = [x for x, y in zip(lastLines, self.lines) if x != y]
            print(f"diff: {diff}")
            # time.sleep(2)
            runCount += 1
        print(f"Total runcount: {runCount}")
        print(f"Solution is: {self.countAllSeats()}")


class machine:

    def __init__(self, filename):
        self.input = code(filename)

input = code('testeight.txt')
print(f"Testing countOccupiedRays(4, 3)")
print(input.lines[4][3])
result = input.countOccupiedRays(4,3)
print(f"result: {result}")
# input.printPage(input.lines)
# input.printPage(input.lines)
# input.iterate1()
# print(f"Testing countOccupiedAdjacent(2,2)")
# result = input.countOccupiedAdjacent(2,2)
# print(f"result: {result}")
# print(f"Step 2")
# input.iterate1()

input = code('testinput.txt')
input.solve()

# myMachine = machine('testinput.txt')
# myMachine.solve()

# myMachine = machine('testinput2.txt')
# myMachine.solve()

myMachine = code('input.txt')
myMachine.solve()
