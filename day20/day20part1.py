import itertools
import numpy
import re
import time

from collections import Counter
import builtins as __builtin__

DEBUG = True

def print(*args, **kwargs):
    """ This is handy for these sorts of hacks...
    override print and assign the DEBUG flag...
    print only in DEBUG mode.
    Use the __builtin__.print() function to force print
    """
    if DEBUG:
        return __builtin__.print(*args, **kwargs)
    else:
        return 0

class data:

    def __init__(self, filename):
        self.tiles = {}
        self.tileEdgeValues = {}
        self.tileReverseValues = {}
        self.oneEdge = set([])
        self.twoEdges = set([])

        self.cornerIDs = []

        self._loadFile(filename)
        self._calculateEdges()
        self._findTwoEdgeThings()

        product = numpy.prod(list(map(int, self.cornerIDs)))
        print(f"product: {product}")

    
    def _loadFile(self, filename):
        f = open(filename, 'r')
        # row = 0
        state = 'none'
        tile = '1'
        thing = []
        for row, line in enumerate(f):
            print(f"parsing line {row}: {line}")
            if re.match(r'^Tile', line):
                print(f"Line is a tile marker")
                if state != 'none':
                    self.tiles[tile] = thing
                state = line.strip()
                tile = re.search(r'(\d+)', state)[0]
                print(f"tileNumber: {tile}")
                thing = []
            elif line.strip() != '':
                thing.append(line.strip())
            else:
                self.tiles[tile] = thing
        if tile not in self.tiles:
            self.tiles[tile] = thing
        print(f"tiles: {self.tiles}")
        print(f"----")

    def _oneOrTwo(self, value):
        if value in self.oneEdge:
            self.twoEdges.add(value)
            self.oneEdge.remove(value)
        else:
            self.oneEdge.add(value)

    def _calculateEdges(self):
        for tileKey, tile in self.tiles.items():
            tops = tile[0].replace('#', '1').replace('.', '0')
            top = int(tops, 2)
            self._oneOrTwo(top)
            topr = int(tops[::-1], 2)
            self._oneOrTwo(topr)

            bottoms = tile[-1].replace('#', '1').replace('.', '0')
            bottom = int(bottoms, 2)
            self._oneOrTwo(bottom)
            bottomr = int(bottoms[::-1], 2)
            self._oneOrTwo(bottomr)

            rights = ''.join([row[-1] for row in tile]).replace('#', '1').replace('.', '0')
            right = int(rights, 2)
            self._oneOrTwo(right)
            rightr = int(rights[::-1], 2)
            self._oneOrTwo(rightr)

            lefts = ''.join([row[0] for row in tile]).replace('#', '1').replace('.', '0')
            left = int(lefts, 2)
            self._oneOrTwo(left)
            leftr = int(lefts[::-1], 2)
            self._oneOrTwo(leftr)

            self.tileEdgeValues[tileKey] = [top, right, bottom, left]  # Clockwise from top just in case
            self.tileReverseValues[tileKey] = [topr, rightr, bottomr, leftr]
            print(f'tile: {tileKey} has {[top, topr, right, rightr, bottom, bottomr, left]}')
    
    def _findTwoEdgeThings(self):
        for tileKey, tile in self.tileEdgeValues.items():
            tilecount = 0
            for value in tile:
                if value in self.twoEdges:
                    tilecount += 1
            if tilecount == 2:
                self.cornerIDs.append(tileKey)
            print(f"tile: {tileKey} has edge count: {tilecount}")
        print(f"Corner Tiles: {self.cornerIDs}")


input = data('testinput.txt')
print("-----------------")

# myMachine = machine('testinput.txt')
# finalState = myMachine.runProgram()
# print(f"Final State: {finalState}")

# myMachine = machine('testinput2.txt')
# finalState = myMachine.runProgram()
# print(f"Final State: {finalState}")

myMachine = data('input.txt')
# finalState = myMachine.runProgram()
# __builtin__.print(f"Final State: {finalState}")
