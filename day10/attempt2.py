import re

class code:

    def __init__(self, filename):
        self.lines = []
        f = open(filename, 'r')
        for line in f:
            self.lines.append(int(line.strip()))
        print("input: ", self.lines)
        self.lines.sort()
        print("sorted: ", self.lines)
    
    def set_line(self, idx, newvalue):
        self.lines[idx] = newvalue


class machine:

    def __init__(self, filename):
        print(f'Hello: {filename}')
        self.input = code(filename)
        self.hashcounts = {}

    def solve(self):
        testlines = self.input.lines
        testlines.reverse()
        testlines.append(0)
        print(f"Solving for: {testlines}")
        for thisValue in testlines:
            if thisValue == max(self.input.lines):
                self.hashcounts[thisValue] = 1
            if thisValue not in self.hashcounts:
                self.hashcounts[thisValue] = 0
                validValues = [x for x in self.input.lines if (thisValue + 1 <= x <= thisValue + 3)]
                for x in validValues:
                    if x not in self.hashcounts:
                         print(f"Why is {x} not in {self.hashcounts}?")
                    self.hashcounts[thisValue] += self.hashcounts[x]
        print(self.hashcounts)
               

myMachine = machine('testinput.txt')
myMachine.solve()

myMachine = machine('testinput2.txt')
myMachine.solve()

myMachine = machine('input.txt')
myMachine.solve()
