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
        print(f"Current List: {self.currentList}")


    def runcode(self):
        
        while self.state == 'VALID' and self.pointer < len(self.code.lines):
            self.currentList = self.code.lines[self.pointer-self.preambleLength:self.pointer]
            self._validateNext()
            self.pointer = self.pointer + 1

    
    def _validateNext(self):
        thisTarget = self.code.lines[self.pointer]
        isValid = False
        for i in self.currentList:
            if (thisTarget - i) in self.currentList and (thisTarget - i) != thisTarget:
                isValid = True
        if isValid:
            print(f"Valid : {thisTarget} is the sume of two values in {self.currentList}")
        else:
            print(f"Invalid! : {thisTarget} is not the sum of two values in {self.currentList}")
            self.state = 'Finished'




    def _parse(self, line):
        lineParts = list(re.findall(r'(\w{3}) ([+-])(\d+)', line)[0])
        print(f'parsed: {lineParts}')

        if lineParts[1] == '-':
            lineParts[2] = -1 * int(lineParts[2])

        if lineParts[0] == 'nop':
            self.linePointer += 1
        elif lineParts[0] == 'acc':
            self.linePointer += 1
            self.accumulator += int(lineParts[2])
        elif lineParts[0] == 'jmp':
            print(f"jump to {lineParts}")
            self.linePointer = self.linePointer + int(lineParts[2])
        else:
            print("Fail")
            exit
    
    def _mutate(self):
        """Creates self.code from self.originalcode
        by Mutating the ith "nop" or "jmp" command to the other"""

        j = 0
        self.code = code(self.filename)
        for idx, line in enumerate(self.originalcode.lines):
            # print(f"Iterating {idx} - {line}")
            lineParts = list(re.findall(r'(\w{3}) ([+-])(\d+)', line)[0])
            if lineParts[0] == 'nop':
                # print(f"Found nop in {j} - {self.code.lines[idx]}")
                # print(f"Should cause: {self.code.lines[idx].replace('nop', 'jmp')}")
                j = j + 1
                if j == self.ithMutation:
                    # print(f"Changing")
                    self.code.set_line(idx, self.code.lines[idx].replace('nop', 'jmp'))
            if lineParts[0] == 'jmp':
                j = j + 1
                if j == self.ithMutation:
                    self.code.set_line(idx, self.code.lines[idx].replace('jmp', 'nop'))
        
        print(f"New Program for {self.ithMutation}: {self.code.lines}")



testinput = code('testinput.txt')

myMachine = machine('testinput.txt', 5)
myMachine.runcode()

myMachine = machine('input.txt', 25)
myMachine.runcode()