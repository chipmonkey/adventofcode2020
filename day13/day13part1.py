import re
import time

class input:

    def __init__(self, filename):
        self.linesOriginal = []
        f = open(filename, 'r')
        for line in f:
            self.linesOriginal.append(line.strip())
        self.lines = self.linesOriginal
        self.starttime = int(self.lines[0])
        self.busses = set(self.lines[1].split(','))
        self.busses.remove('x')
        print(f"input: {self.lines} ")
        print(f"starttime: {self.starttime}")
        print(f"busses: {self.busses}")

    
class machine:

    def __init__(self, filename):
        self.input = input(filename)
        self.bestbus = 0
        self.solution = 0
    
    def solve(self):
        i = self.input.starttime
        found = False
        while not found:
            if i % 1000 == 0:
                print(f"Checkpoint: {i}")
            for bus in self.input.busses:
                if i % int(bus) == 0:
                    found = True
                    self.solution = i
                    self.bestbus = int(bus)
            i = i + 1
        print(f"Happy solution : {self.solution} with bus: {self.bestbus}")
        print(f"{self.input.starttime}")
        return((self.solution - self.input.starttime) * self.bestbus)
        

testinput = input('testinput.txt')
myMachine = machine('testinput.txt')
result = myMachine.solve()
print(f"result: {result}")

myMachine = machine('input.txt')
result = myMachine.solve()
print(f"result: {result}")
