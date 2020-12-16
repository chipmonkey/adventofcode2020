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
        self.total = 0
    
    def runProgram(self):
        for line in self.input.lines:
            # print(f"processing: {line}")
            if 'mask' in line:
                self.mask = line.split('=')[1].strip()
            elif 'mem' in line:
                self._runMem(line)
        print(f"Program has run.  Final state is: {self.state}")
        print(f"Final total is: {self.total}")
        return(self.total)

    def _runMem(self, line):
        """ Parse a mem line into an address and a value
        and apply that value with self.mask to the self.state dict
        using address as the self.state dict key
        """
        print(f"parsing: {line}")
        address, value = map(int, re.findall(r'mem\[(\d+)\] = (\d+)$', line)[0])
        addressstr = bin(address)[2:].rjust(36, '0')
        valuestr = bin(value)[2:].rjust(36, '0')
        print(f"valuestr: {valuestr}")
        print(f"address: {address}, value: {value}")
        # if address not in self.state:
        #     self.state[address] = '0'*36
        #     print(f'self.state: {self.state}')
        
        bitcount = self.mask.count('X')
        print(f"bitcount: {bitcount}")

        # forceOnes = ''.join([a if a != '1' else b for a, b in zip(self.mask, addressstr)])
        forceOnesMask = ''.join([b if a == '0' else a for a, b in zip(self.mask, addressstr)])
        print(f"forceOnesMask: {forceOnesMask}")

        # print(f"mask is : {self.mask}")
        for bits in itertools.product('01', repeat=bitcount):
            byield = iter(bits)
            newString = ''.join([next(byield) if a == 'X' else a for a, b in zip(forceOnesMask, valuestr)])
            newAddress = int(newString, 2)
            self.state[newAddress] = value
            self.total = self.total + int(newString, 2)  #NO NO NO
            # print(f"New string: {''.join(newString)} (decimal {int(newString, 2)}")

        # print(f"self.state: {self.state}")
        self.total = sum(self.state.values())
        print(f"result: {self.total}")
        return self.total

input = code('testinput.txt')
print("-----------------")

myMachine = machine('testinput2.txt')
finalState = myMachine.runProgram()
print(f"Final State: {finalState}")

myMachine = machine('input.txt')
finalState = myMachine.runProgram()
print(f"Final State: {finalState}")
