import itertools
import re
import time

from collections import Counter

class data:

    def __init__(self, filename):
        self.lines = []
        f = open(filename, 'r')
        # row = 0
        for row, line in enumerate(f):
            self.lines.append(line.strip())
            
        # print(f"input: {self.lines} with {len(self.lines)} rows")


class machine:

    def __init__(self, filename):
        self.data = data(filename)
    
    def runProgram(self):
        total = sum([self._calculate(x) for x in self.data.lines])
        return total
    
    def _findrParen(self, line):
        """Finds the first left paren and then returns the index of the matching right paren"""
        countParen = 0
        for i, c in enumerate(line):
            if c == '(':
                countParen += 1
            if c == ')':
                countParen -= 1
                if countParen == 0:
                    return (i)


    def _calculate(self, line):
        digit = re.compile('^(\d+)$')
        # line = line.replace(' ', '')
        print(f"Calculating: {line}")

        if digit.match(line):
            return int(line)

        while '(' in line:
            lParen = line.find('(')
            rParen = self._findrParen(line)
            if lParen > 0:
                lStuff = line[0:lParen]
            else:
                lStuff = ''
            pStuff = line[lParen+1:rParen]
            if rParen < len(line):
                rStuff = line[rParen+1:]
            else:
                rParen = ''
            print(f"{lStuff} | {pStuff} | {rStuff}")
            pValue = self._calculate(pStuff)
            line = lStuff + str(pValue) + rStuff
            print(f"Line is now: {line}")

        rvalue = 0

        while '*' in line:
            spot = line.find('*')
            lStuff = line[0:spot-1]
            rStuff = line[spot+1:]
            lvalue = self._calculate(lStuff)
            rvalue = self._calculate(rStuff)
            rvalue = lvalue * rvalue
            line = str(rvalue)
            print(f"From multiplication: {line}")
            return self._calculate(line)
        
        ops = line.split(' ')
        if '' in ops:
            ops.remove('')
        
        print(f"Got here with : {ops}")
        state = 's'
        for value in ops:
            if digit.match(value):
                if state == 's':
                    rvalue = int(value)
                elif state == '+':
                    rvalue += int(value)
                elif state == '*':
                    print(f"Shouldn't be any plusses here")
                    exit()
                    # rvalue *= int(value)
                else:
                    print(f"{value} not a valid state!")
                    exit()
            else:
                state = value
        print(f"Finished calculating: {rvalue}")

        return rvalue


input = data('testinput.txt')
print("-----------------")

myMachine = machine('testinput.txt')
finalState = myMachine.runProgram()
print(f"Final State: {finalState}")

# myMachine = machine('testinput2.txt')
# finalState = myMachine.runProgram()
# print(f"Final State: {finalState}")

myMachine = machine('input.txt')
finalState = myMachine.runProgram()
print(f"Final State: {finalState}")