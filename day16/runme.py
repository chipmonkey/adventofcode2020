import itertools
import numpy as np
import re
import time

from collections import Counter

class data:

    def __init__(self, filename):
        self.lines = []
        self.types = {}
        self.tickets = []
        self.goodtickets = []
        f = open(filename, 'r')
        state = 'types'
        for line in f:
            print(f"processing: {state} for {line}")
            if line.strip() == 'your ticket:':
                state = 'your ticket'
                continue
            elif line.strip() == 'nearby tickets:':
                state = 'nearby tickets'
                continue

            # File Sections:
            if state == 'types' and line.strip() != '':
                type, min1, max1, min2, max2 = re.findall(r'(\w+): (\d+)-(\d+) or (\d+)-(\d+)', line)[0]
                self.types[type] = [int(min1), int(max1), int(min2), int(max2)]
                print(f'types: {type} {min1}, {max1}, {min2}, {max2}')
            
            elif state == 'your ticket' and line.strip() != '':
                self.myticket = list(map(int, line.split(',')))
                print(f"my ticket: {self.myticket}")

            elif state == 'nearby tickets' and line.strip() != '':
                thisticket = list(map(int, line.split(',')))
                print(f"this ticket: {thisticket}")
                self.tickets.append(thisticket)
            
            self.lines.append(line.strip())
            
        self.nLines = len(self.lines)
        print(f"input: {self.lines} dimensions ({self.nLines})")
        print(f"self.types: {self.types}")
        print(f"self.myticket: {self.myticket}")
        print(f"self.tickets: {self.tickets}")

    def testvalid(self, ticket):
        result = 0
        for testNumber in ticket:
            # print(f"testNumber: {testNumber}")
            valid = False
            for mytype in self.types:
                print(f"mytype: {mytype} - {self.types[mytype]}")
                if self.types[mytype][0] <= testNumber <= self.types[mytype][1]:
                    valid = True
                if self.types[mytype][2] <= testNumber <= self.types[mytype][3]:
                    valid = True
            if not valid:
                result = result + testNumber
                print(f"{testNumber} is NOT VALID ({result})")
            else:
                print(f"{testNumber} is Valid for {mytype}")

        return result
    
    def getPossibleCases(self, columnIndex):
        possibleClasses = list(self.types.keys())
        print(f"Possible Classes: {possibleClasses}")
        for ticket in self.tickets:
            testNumber = ticket[columnIndex]
            for mytype in self.types:
                if not (self.types[mytype][0] <= testNumber <= self.types[mytype][1] or \
                    self.types[mytype][2] <= testNumber <= self.types[mytype][3]) and \
                    mytype in possibleClasses:
                    print(f"{testNumber} in column {columnIndex} not valid for {mytype}")
                    possibleClasses.remove(mytype)
        return possibleClasses

    @staticmethod
    def printPage(lines):
        for x, i in enumerate(lines):
            print(x, i)


class machine:

    def __init__(self, filename):
        self.input = data(filename)
        self.goodtickets = []
        self.potential = [0]*len(self.input.myticket)
        print(f"potential: {self.potential}")

    def runProgram(self):
        result = 0
        for idx, myticket in enumerate(self.input.tickets):
            thisResult = self.input.testvalid(myticket)
            result += thisResult
            if thisResult == 0:
                self.goodtickets.append(idx)

        print(f"Good Tickets: {self.goodtickets}")
        return(result)
    
    def runPart2(self):
        for columnIdx in range(len(self.input.myticket)):
            print(f"column: {columnIdx}")
            pCases = self.input.getPossibleCases(columnIdx)
            print(f"Column: {columnIdx} has pc: {pCases}")
            self.potential[columnIdx] = pCases
        
        self._resolvePotential()
        result = self._productByKey('departure')
        return result

    def _isResolved(self):
        resolved = True
        for column in self.potential:
            if len(column) > 1:
                resolved = False
        return resolved

    
    def _resolvePotential(self):
        while not self._isResolved():
            singles = [x[0] for x in self.potential if len(x) == 1]
            print(f"singles: {singles}")
            for i, column in enumerate(self.potential):
                if len(column) > 1:
                    for sing in singles:
                        print(f"removing {sing} from column: {column}")
                        if sing in self.potential[i]:
                            self.potential[i].remove(sing)
                        else:
                            print(f"{sing} is not in {self.potential[i]}")
            print(f"self.potential: {self.potential}")
    
    def _productByKey(self, key):
        result = 0
        indexes = [i for i, v in enumerate(self.potential) if key in v]
        print(f"indexes for {key}: {indexes}")
        rvalues = [x for x in self.input.myticket]
        print(f"rvalues: {rvalues}")
        result = np.prod(rvalues)
        return result

# input = data('testinput.txt')
# print("-----------------")

# myMachine = machine('testinput.txt')
# finalState = myMachine.runProgram()
# print(f"Final State: {finalState}")

# myMachine = machine('input.txt')
# finalState = myMachine.runProgram()
# print(f"Final State: {finalState}")


myMachine = machine('testinput2.txt')
finalState = myMachine.runProgram()
print(f"Final State: {finalState}")
partTwo = myMachine.runPart2()
print(f"Part 2: {partTwo}")



myMachine = machine('input.txt')
finalState = myMachine.runProgram()
print(f"Final State: {finalState}")
partTwo = myMachine.runPart2()
print(f"Part 2: {partTwo}")