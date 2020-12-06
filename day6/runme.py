import re

DEBUG = False

class filethingy:

    def __init__(self, filename):
        self.values = []
        f = open(filename, 'r')
        for line in f:
            self.values.append(line.strip())
        print("input: ", self.values)



class part1:
    """class to solve the problem at hand
    """

    def __init__(self, filename):
        self.result = 0  # Highest Seat ID
        self.mydata = filethingy(filename)
        self.groups = []


    def solve(self):
        thisgroup = ''
        self.mydata.values.append('')
        for boardingPass in self.mydata.values:
            print(boardingPass)
            if boardingPass == '':
                thiscount = len(set(thisgroup))
                self.result = self.result + thiscount
                print(f"Adding {thiscount} for {thisgroup}")
                thisgroup = ''
            else:
                thisgroup = thisgroup + boardingPass.strip()

        print(f'count: {self.result}')
        return(self.result)

class part2:
    """class to solve the problem at hand
    """

    def __init__(self, filename):
        self.result = 0  # Highest Seat ID
        self.mydata = filethingy(filename)
        self.groups = []


    def solve(self):
        allanswers = set('')
        self.mydata.values.append('')
        newpass = True
        for boardingPass in self.mydata.values:
            if newpass:
                allanswers = set(boardingPass)
                # print(f"allanswers starts as {allanswers}")
            if boardingPass == '':
                thiscount = len(set(allanswers))
                self.result = self.result + thiscount
                print(f"Adding {thiscount} for {allanswers}")
                allanswers = set('')
                newpass = True
            else:
                newpass = False
                allanswers = allanswers.intersection(boardingPass.strip())
                print(f"handling: {boardingPass}: {allanswers}")

        print(f'count: {self.result}')
        return(self.result)

# test = filethingy('testinput.txt')

# mything = part1('testinput.txt')
# test1 = mything.solve()
# mything = part1('input.txt')
# part1 = mything.solve()

mything = part2('testinput.txt')
test2 = mything.solve()
mything = part2('input.txt')
part2 = mything.solve()