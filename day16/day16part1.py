import itertools
import re
import time

from collections import Counter

class data:

    def __init__(self, filename):
        self.lines = []
        self.types = {}
        self.tickets = []
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


    @staticmethod
    def printPage(lines):
        for x, i in enumerate(lines):
            print(x, i)


class machine:

    def __init__(self, filename):
        self.input = data(filename)
    
    def runProgram(self):
        result = 0
        for myticket in self.input.tickets:
            result += self.input.testvalid(myticket)
        return(result)


# input = data('testinput.txt')
# print("-----------------")

myMachine = machine('testinput.txt')
finalState = myMachine.runProgram()
print(f"Final State: {finalState}")

myMachine = machine('input.txt')
finalState = myMachine.runProgram()
print(f"Final State: {finalState}")
