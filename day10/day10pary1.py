import re

class code:

    def __init__(self, filename):
        self.lines = []
        f = open(filename, 'r')
        for line in f:
            self.lines.append(int(line.strip()))
        print("input: ", self.lines)
        self.lines.sort()
        print("sorted: ", self.lines)
    
    def set_line(self, idx, newvalue):
        self.lines[idx] = newvalue


class machine:

    def __init__(self, filename):
        print(f'Hello: {filename}')
        self.input = code(filename)

    def solve(self):
        ones = self._countOnes()
        threes = self._countThrees()
        print(f"Solution: {ones * threes}")

    def _countOnes(self):
        count = 0
        if self.input.lines[0] == 1:
            count += 1   # Account for initial value
        for x in range(len(self.input.lines) - 1):
            print(f"x: {x}")
            print(f"comparing: {self.input.lines[x]} with {self.input.lines[x+1]}")
            if self.input.lines[x] == self.input.lines[x+1]-1:
                count += 1
        return count

    def _countThrees(self):
        count = 0
        if self.input.lines[0] == 3:
            print("Add one for step 1")
            count += 1   # Account for initial value
        for x in range(len(self.input.lines) - 1):
            print(f"x: {x}")
            if self.input.lines[x] == self.input.lines[x+1]-3:
                count += 1
            print(f"comparing: {self.input.lines[x]} with {self.input.lines[x+1]} - count: {count}")

        count += 1
        print("adding one for your thingy")

        return count


testinput = code('testinput.txt')

testinput = code('testinput2.txt')

myMachine = machine('testinput.txt')
print(myMachine._countOnes())
print(myMachine._countThrees())
myMachine.solve()


myMachine = machine('testinput2.txt')
print(myMachine._countOnes())
print(myMachine._countThrees())
myMachine.solve()


myMachine = machine('input.txt')
print(myMachine._countOnes())
print(myMachine._countThrees())
myMachine.solve()

# print(f"Result is: {result}")
# myMachine.findContiguous()

# myMachine = machine('input.txt', 25)
# result = myMachine.runcode()
# print(f"Result is: {result}")
# myMachine.findContiguous()
