import itertools
import re
import time

from collections import Counter

class code:

    def __init__(self, filename):
        self.lines = []
        f = open(filename, 'r')
        for line in f:
            self.lines.append(line.strip())
        self.nLines = len(self.lines)
        print(f"input: {self.lines} dimensions ({self.nLines})")
        self.numbers = list(map(int, self.lines[0].split(',')))
        print(f"numbers: {self.numbers}")


    @staticmethod
    def printPage(lines):
        for x, i in enumerate(lines):
            print(x, i)


class machine:

    def __init__(self, filename):
        self.input = code(filename)
        self.lastspoken = {}
        self.lastlastspoken = {}
        self.spoken = []
        self.counter = 0
    
    def runProgram(self):
        for num in self.input.numbers:
            self._speak(num)
        print(f"spoken: {self.spoken}")
        print(f"lastspoken: {self.lastspoken}")
        
        while self.counter <= 2020:
            previous = self.spoken[-1]
            # print(f"previous: {previous}")
            if previous not in self.lastlastspoken:
                self._speak(0)
            else:
                # print(f"{previous} was spoken before at {self.lastspoken[previous]} and earlier at {self.lastlastspoken[previous]}")
                value = self.lastspoken[previous] - self.lastlastspoken[previous]
                self._speak(value)
        
        print(f"solution: {self.spoken[2020-1]}")
            
            
    def _speak(self, number):
        if self.counter % 1000 == 0:
            print(f"{self.counter}: speaking: {number}")
        self.spoken.append(number)
        if number in self.lastspoken:
            self.lastlastspoken[number] = self.lastspoken[number]
        self.lastspoken[number] = self.counter
        self.counter += 1
        # print(f"self.lastspoken: {self.lastspoken}")
        # print(f"self.lastlastspoken: {self.lastlastspoken}")


input = code('testinput.txt')
print("-----------------")

myMachine = machine('testinput.txt')
finalState = myMachine.runProgram()
print(f"Final State: {finalState}")

# myMachine = machine('input.txt')
# finalState = myMachine.runProgram()
# print(f"Final State: {finalState}")
