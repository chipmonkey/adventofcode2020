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
        self.myMin = 0
        self.myMax = 3
        self.types = {}
        self.tickets = []
        f = open(filename, 'r')
        # row = 0
        for row, line in enumerate(f):
            values.append(line.strip())
            for y, c in enumerate(line.strip()):
                if c == '#':
                    self.cube.append((y, row, 0, 0))
                    print(f"cube: {self.cube}")
            # row = row + 1
            
        print(f"input: {values} with cube min/max: {self.myMin}/{self.myMax}")
        print(f"cube: {self.cube}")
    
    def _getMinMax(self):
        self.myMin = min([min(x) for x in self.cube])
        self.myMax = max([max(x) for x in self.cube])
        print(f"new dimensions: {self.myMin}/{self.myMax}")


    def grow(self):
        newcube = []
        myMin = min([min(x) for x in self.cube])
        myMax = max([max(x) for x in self.cube])
        print(f"min: {myMin}, max: {myMax}")
        dim = [x for x in range(myMin-1, myMax+2)]
        # print(f"growing new cube to : {dim}")
        for xyz in itertools.product(dim, dim, dim, dim):
            neighbors = self._neighbors(xyz)
            if (neighbors == 2 or neighbors == 3) and xyz in self.cube:
                newcube.append(xyz)
            elif neighbors == 3:
                newcube.append(xyz)
        print(f"newcube: {newcube}")
        self.cube = newcube
        self._getMinMax()

    def _neighbors(self, xyz):
        neighbors = 0
        for x in range(xyz[0]-1, xyz[0]+2):
            for y in range(xyz[1]-1, xyz[1]+2):
                for z in range(xyz[2]-1, xyz[2]+2):
                    for w in range(xyz[3]-1, xyz[3]+2):
                        # print(f"testing: ({x}, {y}, {z}) in {self.cube}")
                        if (x, y, z, w) != xyz and (x, y, z, w) in self.cube:
                            neighbors += 1
        # print(f"Neighbors for ({xyz}) = {neighbors}")
        return neighbors


    def printCube(self):
        dim = [x for x in range(self.myMin, self.myMax)]
        print("dim: ", dim)
        for slice in range(self.myMin, self.myMax):
            for row in range(self.myMin, self.myMax):
                line = ''
                for x in range(self.myMin, self.myMax):
                    if (x, row, slice) in self.cube:
                        line = line + '#'
                    else:
                        # print(f"({x}, {row}, {slice}) is not in cube")
                        line = line + '.'
                print(line)
            print('----')




class machine:

    def __init__(self, filename):
        self.cube = cube(filename)
    
    def runProgram(self):
        self.cube.printCube()
        for i in range(6):
            self.cube.grow()
        self.cube.printCube()
        return len(self.cube.cube)


input = cube('testinput.txt')
print("-----------------")

myMachine = machine('testinput.txt')
# test = myMachine.cube._neighbors((1,1,0))  # works
# test = myMachine.cube._neighbors((-1, 0, 0))
# print(f"test: {test}")
finalState = myMachine.runProgram()
print(f"Final State: {finalState}")

# myMachine = machine('input.txt')
# finalState = myMachine.runProgram()
# print(f"Final State: {finalState}")
