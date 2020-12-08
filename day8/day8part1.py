import re

class code:

    def __init__(self, filename):
        self.lines = []
        f = open(filename, 'r')
        for line in f:
            self.lines.append(line.strip())
        print("input: ", self.lines)


class machine:

    def __init__(self, filename):
        print(f'Hello: {filename}')
        self.originalcode = code(filename)
        self.code = self.originalcode
        self.accumulator = 0
        self.linePointer = 0
        self.linesExecuted = []
        self.ithMutation = 0

    def runcode(self):
        exitedProperly = False
        while self.linePointer < len(self.code.lines) and \
            not (self.linePointer in (self.linesExecuted)):
            self.linesExecuted.append(self.linePointer)
            print(f"lines executed: {self.linesExecuted} - Accumulator is: {self.accumulator}")
            self._parse(self.code.lines[self.linePointer])


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
    

myMachine = machine('testinput.txt')
myMachine.runcode()

myMachine = machine('input.txt')
myMachine.runcode()
