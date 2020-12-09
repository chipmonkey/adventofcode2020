import re

class code:

    def __init__(self, filename):
        self.lines = []
        f = open(filename, 'r')
        for line in f:
            self.lines.append(int(line.strip()))
        print("input: ", self.lines)
    
    def set_line(self, idx, newvalue):
        self.lines[idx] = newvalue


class machine:

    def __init__(self, filename, preambleLength):
        print(f'Hello: {filename}')
        self.code = code(filename)
        self.preambleLength = preambleLength
        self.pointer = preambleLength
        self.currentList = self.code.lines[0:preambleLength]
        self.state = 'VALID'
        self.badValue = 0
        print(f"Current List: {self.currentList}")


    def runcode(self):
        
        while self.state == 'VALID' and self.pointer < len(self.code.lines):
            self.currentList = self.code.lines[self.pointer-self.preambleLength:self.pointer]
            self._validateNext()
            self.pointer = self.pointer + 1
        
        self.badValue = self.code.lines[self.pointer-1]
        return self.badValue

    def findContiguous(self):
        for idx, _ in enumerate(self.code.lines):
            runningTotal = 0
            runningCount = 0
            while runningTotal < self.badValue:
                runningTotal += self.code.lines[idx + runningCount]
                runningCount = runningCount + 1
            if runningTotal == self.badValue:
                print(f"Solution found at: {idx} with {runningCount} values")
                solutionValues = self.code.lines[idx:idx+runningCount]
                print(f"Min: {min(solutionValues)}, Max: {max(solutionValues)}")
                print(f"Which adds up to: {min(solutionValues)+max(solutionValues)}")
                break

    
    def _validateNext(self):
        thisTarget = self.code.lines[self.pointer]
        isValid = False
        for i in self.currentList:
            if (thisTarget - i) in self.currentList and (thisTarget - i) != thisTarget:
                isValid = True
        if isValid:
            pass
            # print(f"Valid : {thisTarget} is the sume of two values in {self.currentList}")
        else:
            print(f"Invalid! : {thisTarget} is not the sum of two values in {self.currentList}")
            self.state = 'Finished'



testinput = code('testinput.txt')

myMachine = machine('testinput.txt', 5)
result = myMachine.runcode()

print(f"Result is: {result}")
myMachine.findContiguous()

myMachine = machine('input.txt', 25)
result = myMachine.runcode()
print(f"Result is: {result}")
myMachine.findContiguous()
