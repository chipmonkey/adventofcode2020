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
        self.allcombinations = []
        self.totalCombinations = 0

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
    
    def _recurseiveThingy(self, currentvalue, thisList):
        if currentvalue is None:
            thisList = [0]
            self._recurseiveThingy(0, thisList)
        elif currentvalue == max(self.input.lines):
            print(f"Solution: {thisList} ending in {currentvalue}")
            self.totalCombinations += 1
        else:
            validValues = [x for x in self.input.lines if (currentvalue + 1 <= x <= currentvalue + 3)]
            # print(f"ValidValues for {currentvalue} are: {validValues}")
            oldList = thisList
            if validValues:
                for x in validValues:
                    print(f"Recursing {currentvalue}, {x}")
                    thisList = oldList
                    thisList.extend([x])
                    # print(f"This List is now: {thisList}")
                    self._recurseiveThingy(x, thisList)
            else:
                print(f"Failed list: {thisList}")
                return 0
        # print(f"Total Combinations: {self.totalCombinations}")
        return(self.totalCombinations)

    
    def _countNexts(self):
        for x in range(len(self.input.lines)-1):
            print(self.input.lines[x+1] - self.input.lines[x])

    def _countBranches(self):
        totalBranches = 1
        for i in range(len(self.input.lines)-1):
            currentValue = self.input.lines[i]
            validValues = [x for x in self.input.lines if (currentValue + 1 <= x <= currentValue + 3)]
            print(f"ValidValues for i {i} ({currentValue})== {len(validValues)}")
            totalBranches *= len(validValues)
        print(f"Total Branches: {totalBranches}")
        return totalBranches
        
        


# testinput = code('testinput.txt')

# testinput = code('testinput2.txt')

# myMachine = machine('testinput.txt')
# print(myMachine._countOnes())
# print(myMachine._countThrees())
# myMachine.solve()

# myMachine._countBranches()
# exit()

myMachine = machine('testinput2.txt')
# print(myMachine._countOnes())
# print(myMachine._countThrees())
# myMachine.solve()


myMachine = machine('input.txt')
# print(myMachine._countOnes())
# print(myMachine._countThrees())
# myMachine.solve()

# myMachine._countNexts()
totalCount = myMachine._recurseiveThingy(None, [0])
print(totalCount)

# print(f"Result is: {result}")
# myMachine.findContiguous()

# myMachine = machine('input.txt', 25)
# result = myMachine.runcode()
# print(f"Result is: {result}")
# myMachine.findContiguous()
