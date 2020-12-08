import re

class code:

    def __init__(self, filename):
        self.lines = []
        f = open(filename, 'r')
        for line in f:
            self.lines.append(line.strip())
        print("input: ", self.lines)
    
    def set_line(self, idx, newvalue):
        self.lines[idx] = newvalue


class machine:

    def __init__(self, filename):
        print(f'Hello: {filename}')
        self.originalcode = code(filename)
        self.code = code(filename)
        self.accumulator = 0
        self.linePointer = 0
        self.linesExecuted = []
        self.ithMutation = 0
        self.filename = filename

    def runcode(self):
        exitedProperly = False
        while not exitedProperly:
            print(f"Testing Mutation: {self.ithMutation}")
            while self.linePointer < len(self.code.lines) and \
                not (self.linePointer in (self.linesExecuted)):
                self.linesExecuted.append(self.linePointer)
                print(f"lines executed: {self.linesExecuted} - Accumulator is: {self.accumulator}")
                self._parse(self.code.lines[self.linePointer])
            
            if self.linePointer == len(self.code.lines):
                exitedProperly = True
                print(f"Exited Properly with accumulator: {self.accumulator}")

            self.lastAccumulator = self.accumulator

            self._mutate()
            self.accumulator = 0
            self.linesExecuted = []
            self.linePointer = 0
            self.ithMutation += 1



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




myMachine = machine('testinput.txt')
myMachine.runcode()

myMachine = machine('input.txt')
myMachine.runcode()