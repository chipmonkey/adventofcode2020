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
                type, min1, max1, min2, max2 = re.findall(r'([a-z ]+): (\d+)-(\d+) or (\d+)-(\d+)', line)[0]
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
        validTicket = True
        for testNumber in ticket:
            # print(f"testNumber: {testNumber}")
            if testNumber == 0:
                print(f"Working on a zero")
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
                validTicket = False
            else:
                print(f"{testNumber} in {ticket} is Valid for {mytype}")

        return result, validTicket
    
    def getPossibleCases(self, columnIndex):
        possibleClasses = list(self.types.keys())
        print(f"Possible Classes: {possibleClasses}")
        for ticket in self.tickets:
            testNumber = ticket[columnIndex]
            for mytype in self.types:
                if not (self.types[mytype][0] <= testNumber <= self.types[mytype][1] or \
                    self.types[mytype][2] <= testNumber <= self.types[mytype][3]) and \
                    mytype in possibleClasses:
                    if columnIndex == 13:
                        print(f"{testNumber} in {ticket} in column {columnIndex} not valid for {mytype}")
                    possibleClasses.remove(mytype)
        return possibleClasses

    @staticmethod
    def printPage(lines):
        for x, i in enumerate(lines):
            print(x, i)

    def fixTickets(self, goodtickets):
        print(f"Fixing: {goodtickets}")
        newTickets = []
        for i in goodtickets:
            newTickets.append(self.tickets[i])
        self.tickets = newTickets


class machine:

    def __init__(self, filename):
        self.input = data(filename)
        self.goodtickets = []
        self.potential = [0]*len(self.input.myticket)
        self.positions = [None for _ in self.input.myticket]

    def runProgram(self):
        result = 0
        for idx, myticket in enumerate(self.input.tickets):
            thisResult, isValid = self.input.testvalid(myticket)
            if isValid:
                self.goodtickets.append(idx)
            else:
                result += thisResult


        print(f"Good Tickets: {self.goodtickets}")
        return(result)
    
    def runPart2(self):
        self.input.fixTickets(self.goodtickets)
        for columnIdx in range(len(self.input.myticket)):
            pCases = self.input.getPossibleCases(columnIdx)
            if columnIdx == 13:
                print(f"Column: {columnIdx} has pc: {pCases}")
            self.potential[columnIdx] = pCases
        
        self._resolvePotential()
        result = self._productByKey('departure')
        return result

    # def _isResolved(self):
    #     resolved = True
    #     for column in self.potential:
    #         if len(column) > 1:
    #             resolved = False
    #     return resolved

    
    def _resolvePotential(self):
        didSomething = True
        while None in self.positions and didSomething:
            didSomething = False
            allOptions = {}
            singles = [x[0] for x in self.potential if len(x) == 1]
            print(f"singles: {singles}")
            for i, column in enumerate(self.potential):
                if len(column) == 1 and not self.positions[i]:
                    self.positions[i] = column[0]
                    print(f"Added {column[0]} to location {i} : {self.positions}")

                if len(column) > 1:
                    for thing in column:
                        if thing not in allOptions:
                            allOptions[thing] = 1
                        else:
                            allOptions[thing] = allOptions[thing] + 1
                    for sing in singles:
                        # print(f"removing {sing} from column: {column}")
                        if sing in self.potential[i] and len(self.potential[i]) > 1:
                            self.potential[i].remove(sing)
                            didSomething = True
                        # else:
                        #     print(f"{sing} is not in {self.potential[i]}")
            for x, v in allOptions.items():
                print(f"Alloptions[{x}] = {v}")
                if v == 1:
                    for i, column in enumerate(self.potential):
                        if i == 13:
                            print(f"testing: {column} for {x}")
                        if x in column:
                            self.positions[i] = x
                            self.potential[i] = [x]
                            didSomething = True
                            print(f"Because thing: removing {x} from position {i} {self.potential[i]}")

            print(f"allOptions: {allOptions}")
            print(f"self.undecided: {[x for x in self.potential if len(x) > 1]}")
    
    def _productByKey(self, key):
        result = 0
        indexes = [i for i, v in enumerate(self.potential) if key in ''.join(v)]
        print(f"really: {self.potential}")
        print(f"indexes for {key}: {indexes}")
        print(f"my ticket: {self.input.myticket}")
        rvalues = [self.input.myticket[i] for i in indexes]
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


# myMachine = machine('testinput2.txt')
# finalState = myMachine.runProgram()
# print(f"Final State: {finalState}")
# partTwo = myMachine.runPart2()
# print(f"Part 2: {partTwo}")



myMachine = machine('input.txt')
finalState = myMachine.runProgram()
print(f"Final State: {finalState}")
partTwo = myMachine.runPart2()
print(f"Part 2: {partTwo}")
# Fixed this stupid bug!
# print("And I don't know why there is one empty position but it tiees to value 179 and if you multiply my result by 179 you get the right answer")
# print("Because that's the only value that's missing and it must be a 'departure' value")
# print(f"resulting in: {partTwo * 179}")