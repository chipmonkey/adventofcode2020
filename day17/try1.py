import itertools
import re
import time

from collections import Counter

class cube:

    def __init__(self, filename):
        """ self.cube is a list of (x, y, z) tuples which are active
        """
        self.cube = []
        values = []
        self.types = {}
        self.tickets = []
        f = open(filename, 'r')
        row = 0
        for line in f:
            values.append(line.strip())
            
        self.width = len(values[0])
        self.height = len(values)
        self.depth = 0
        print(f"input: {values} dimensions ({self.width} x {self.height} x {self.depth})")
        

        self.cube.append(values)

        self._shift(1)
        self.printCube()

    def _shift(self, d=1):
        """ Shifts a cube (+d, +d, +d) in 3-space
        """
        newwidth = self.width+d
        newHeight = self.height+d
        newDepth = self.depth+d
        newcube = [[''.join(['.' for x in range(self.width+d)]) for y in range(self.height+d)] for z in range(self.depth+d)]
        
        print(newcube)
        newrow = ''.join(['.']*self.width)
        newlines = [newrow]*self.height



    def printCube(self):
        print(f"Cube has ")
        for d in range(self.depth):
            for l in self.cube[d]:
                print(l)
            if d < self.depth:
                print("")


class machine:

    def __init__(self, filename):
        self.input = cube(filename)
    
    def runProgram(self):
        result = 0
        for myticket in self.input.tickets:
            result += self.input.testvalid(myticket)
        return(result)


input = cube('testinput.txt')
print("-----------------")

# myMachine = machine('testinput.txt')
# finalState = myMachine.runProgram()
# print(f"Final State: {finalState}")

# myMachine = machine('input.txt')
# finalState = myMachine.runProgram()
# print(f"Final State: {finalState}")
