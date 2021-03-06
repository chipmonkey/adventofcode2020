import itertools
import re
import time

class code:

    def __init__(self, filename):
        self.lines = []
        f = open(filename, 'r')
        for line in f:
            self.lines.append(line.strip())
        self.nLines = len(self.lines)
        print(f"input: {self.lines} dimensions ({self.nLines})")


    @staticmethod
    def printPage(lines):
        for x, i in enumerate(lines):
            print(x, i)


class machine:

    def __init__(self, filename):
        self.input = code(filename)
        self.state = {}
        self.floats = {}
        self.ones = '0'*36
        self.zeros = '0'*36
        self.floatmask = 0
    
    def runProgram(self):
        for line in self.input.lines:
            # print(f"processing: {line}")
            if 'mask' in line:
                self._getmask(line)
            elif 'mem' in line:
                self._runMem(line)
        print(f"Program has run.  Final state is: {self.state}")
        total = self._sumState()
        part2 = self._sumStateWithFloats()
        print(f"total: {total}, part2: {part2}")
        return(total)

    def _getmask(self, line):
        line = line.replace('mask = ', '')
        self.ones = line
        self.ones = self.ones.replace('X', '0')
        self.ones = int(self.ones, 2)

        self.zeros = line
        self.zeros = self.zeros.replace('X', '1')
        self.zeros = int(self.zeros, 2)

        self.floatmask = line
        self.floatmask = self.floatmask.replace('1', '0')
        self.floatmask = self.floatmask.replace('X', '1')

        print(f"getmask: {line} ({self.ones}, {self.zeros}, {self.floatmask})")

    def _runMem(self, line):
        """ Parse a mem line into an address and a value
        and apply that value with self.mask to the self.state dict
        using address as the self.state dict key
        """
        thing = list(re.findall('mem\[(\d+)\] = (\d+)$', line)[0])
        print(f"thing: {thing}")
        address = thing[0]
        value = int(thing[1])
        print(f"value: {value} : {str(bin(value))}")
        if address not in self.state:
            self.state[address] = 0
            self.floats[address] = 0
            print(f'self.state: {self.state}')
        applyOnes = value | self.ones
        print(f"applyOnes {applyOnes} : {str(bin(applyOnes))}")
        forceZeros = applyOnes & self.zeros
        print(f"Mem result is: {forceZeros} - {str(bin(forceZeros))}")
        self.state[address] = forceZeros
        self.floats[address] = self.floatmask

    def _sumState(self):
        print(f"Total from {self.state}")
        print(self.state.values())
        total = sum(self.state.values())
        return(total)

    def _sumStateWithFloats(self):
        print("Sum State With Floats...")
        total = 0
        for key in self.state.keys():
            print(f"key: {key}")
            floatIndexes = [k for k, v in enumerate(self.floats[key]) if v == '1']
            print(f"float Indexes for {self.floats[key]} are: {floatIndexes}")
            explode = str(bin(self.state[key]))[2:].rjust(36, '0')
            print(f"exploding: {explode}")
            for bit in itertools.product('01', repeat=len(floatIndexes)):
                # print(f"bit: {bit}")
                this = explode
                for a, b in zip(bit, floatIndexes):
                    # print(f"put {a} in position {b}")
                    this = this[:b] + str(a) + this[b:-1]
                    total = total + int(this, 2)
            print(f"Running total: {total}")
                
                # print(f"bit: {bit}")
                # for i, idx in enumerate(floatIndexes):
                #     this = explode
                #     print(f"idx: {idx}, i: {i}: bit[i]: {bit[i]}")
                #     this = this[:idx] + bit[i] + this[idx:-1]
                #     print(f"this: {this} - value: {int(this, 2)}")
                #     total = total + int(this, 2)
                # print(f"Running total: {total}")
        return total



input = code('testinput.txt')
print("-----------------")

myMachine = machine('testinput2.txt')
finalState = myMachine.runProgram()
print(f"Final State: {finalState}")

myMachine = machine('input.txt')
finalState = myMachine.runProgram()
print(f"Final State: {finalState}")
