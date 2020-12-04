import re

DEBUG = False

class filethingy:

    def __init__(self, filename):
        self.values = []
        f = open(filename, 'r')
        for line in f:
            self.values.append(line)

        print("input: ", self.values)



class traverseR3D1:
    """class to solve the problem at hand
    """
    
    def __init__(self, filename):
        self.result = 0  # Count of trees hit
        self.mydata = filethingy(filename)

    def solve(self):
        partials = [self.solvePartial(1, 1)]
        partials.append(self.solvePartial(3, 1))
        partials.append(self.solvePartial(5, 1))
        partials.append(self.solvePartial(7, 1))
        partials.append(self.solvePartial(1, 2))
        print(partials)

        result = 1
        for p in partials:
            result *= p
        print(f"result: {result}")
        return result


    def solvePartial(self, right, down):
        result = 0
        x = y = 0  # Starting coordinates
        while x < len(self.mydata.values):
            print(f"(x, y): ({x}, {y})")
            if self.mydata.values[x][y] == '#':
                print("Tree!")
                result += 1
            else:
                print("Not a tree")
            x += down
            y = (y + right) % (len(self.mydata.values[0])-1)
        print(f"Partial: {result}")
        return result


test = filethingy('testinput.txt')

mything2 = traverseR3D1('testinput.txt')
mything2.solve()

mything2 = traverseR3D1('input.txt')
day1 = mything2.solvePartial(3, 1)
day2 = mything2.solve()
