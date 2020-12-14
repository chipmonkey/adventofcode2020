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
        self.ones = '0'*36
        self.zeros = '0'*36
    
    def runProgram(self):
        for line in self.input.lines:
            # print(f"processing: {line}")
            if 'mask' in line:
                self._getmask(line)
            elif 'mem' in line:
                self._runMem(line)
        print(f"Program has run.  Final state is: {self.state}")
        total = self._sumState()
        return(total)
    
    def _getmask(self, line):
        line = line.replace('mask = ', '')
        self.ones = line
        self.ones = self.ones.replace('X', '0')
        self.ones = int(self.ones, 2)

        self.zeros = line
        self.zeros = self.zeros.replace('X', '1')
        self.zeros = int(self.zeros, 2)

        print(f"getmask: {line} ({self.ones}, {self.zeros})")
    
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
            print(f'self.state: {self.state}')
        applyOnes = value | self.ones
        print(f"applyOnes {applyOnes} : {str(bin(applyOnes))}")
        forceZeros = applyOnes & self.zeros
        print(f"Mem result is: {forceZeros} - {str(bin(forceZeros))}")
        self.state[address] = forceZeros
    
    def _sumState(self):
        print(f"Total from {self.state}")
        print(self.state.values())
        total = sum(self.state.values())
        return(total)

    


input = code('testinput.txt')
print("-----------------")

myMachine = machine('testinput.txt')
finalState = myMachine.runProgram()
print(f"Final State: {finalState}")

myMachine = machine('input.txt')
finalState = myMachine.runProgram()
print(f"Final State: {finalState}")
# print(f"Testing countOccupiedRays(4, 3)")
# print(input.lines[4][3])
# result = input.countOccupiedRays(4,3)
# print(f"result: {result}")
# # input.printPage(input.lines)
# # input.printPage(input.lines)
# # input.iterate1()
# # print(f"Testing countOccupiedAdjacent(2,2)")
# # result = input.countOccupiedAdjacent(2,2)
# # print(f"result: {result}")
# # print(f"Step 2")
# # input.iterate1()

# input = code('testinput.txt')
# input.solve()

# # myMachine = machine('testinput.txt')
# # myMachine.solve()

# # myMachine = machine('testinput2.txt')
# # myMachine.solve()

# myMachine = code('input.txt')
# myMachine.solve()
