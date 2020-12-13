import re
import time
import numpy as np

# Must use python >= 3.8 for extended pow() call...

class input:

    def __init__(self, filename):
        self.linesOriginal = []
        f = open(filename, 'r')
        for line in f:
            self.linesOriginal.append(line.strip())
        self.lines = self.linesOriginal
        self.starttime = int(self.lines[0])
        self.buslist = self.lines[1].split(',')
        self.buslistNoX = [int(x) for x in self.buslist if x != 'x']
        self.busses = set(self.lines[1].split(','))
        self.busses.remove('x')
        self.busIndex = [self.buslist.index(str(n)) for n in self.buslistNoX]

        print(f"input: {self.lines} ")
        print(f"starttime: {self.starttime}")
        print(f"busses: {self.busses}")
        print(f"busIndex: {self.busIndex}")

    
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
    
    def part2(self):
        coeffs = []
        for i, x in enumerate(self.input.buslist):
            if x != 'x':
                print(f"The result % {x} must be {i}")
                coeffs.append([x, i])
        print(f"coeffs: {coeffs}")

        # a = np.array(coeffs)
        # b = np.array(targets)
        # x = np.linalg.solve(a, b)
        # x = np.linalg.lstsq(a, b)
        print(x)
        # madness = coeffs[0]
        result = self._linQuick(coeffs[0:2])
        print(result)
        nxBus = [int(x) for x in self.input.buslist if x != 'x']
        print(f"non-x busses: {nxBus}")
        totalProduct = int(np.prod(nxBus))
        print(f"Total non-x Product: {totalProduct}")

        gcdList = [totalProduct // x for x in nxBus]
        print(f"GCD List: {gcdList}")

        remainders = [ -self.input.busIndex[i] % self.input.buslistNoX[i] for i in range(len(self.input.buslistNoX)) ]

        print(f"remainders: {remainders}")


        residuals = [pow(gcdList[i], -1, nxBus[i]) * remainders[i] % nxBus[i] for i in range(len(self.input.buslistNoX))]
        print(f"residuals: {residuals}")

        result = 0
        for x, y in zip(residuals, gcdList):
            result += x * y

        print(f"result: {result}")

        result = result % totalProduct

        # c1 = coeffs[0]
        # for i, x in enumerate(coeffs[1:]):
        #     print(f"c1: {c1}, x: {x}, {[c1, x]}")
        #     c2 = self._linQuick([c1, x])
        #     print(f"c2: {c2}")
        #     c1 = [c2, 0]
        #     print(f"New best is: {c1}")

        return(result)

    def _linQuick(self, coeffs):
        """Solve exactly two coefficients of the form:
        x = c1*i+0   # Target 1 must be zero
        x = c2*j+b2
        where x, i, j are unknown.
        The solution will be a value k such that for all integers i > 0:
        x = c1*k*i
        x = c2*k*i+b2
        Returns c1*k
        """
        k = 1
        c1 = coeffs[0][0]
        c2 = coeffs[1][0]
        t2 = coeffs[1][1]
        print(f"c1: {c1}, c2: {c2}, t2: {t2}")
        found = False
        while not found:
            d = int(c1)*k
            r = int(d) % int(c2)
            print(f"testing: {k}: {d} % {c2} = {r}")
            if r == t2:
                found = True
                result = d
            k = k + 1
        return(result)
        

testinput = input('testinput.txt')
myMachine = machine('testinput.txt')
result = myMachine.solve()
print(f"result: {result}")
result2 = myMachine.part2()
print(f"result2: {result2}")

myMachine = machine('input.txt')
result = myMachine.solve()
print(f"result: {result}")
result2 = myMachine.part2()
print(f"result2: {result2}")
