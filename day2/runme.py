import re

DEBUG = False

class filethingy:

    values = []

    def __init__(self, filename):
        self.values = []
        f = open(filename, 'r')
        for line in f:
            self.values.append(line)

        print("input: ", self.values)


class findvalid:
    """class to solve the problem at hand
    """
    
    def __init__(self, filename):
        self.result = 0  # Count of valid passwords
        self.mydata = filethingy(filename)

    def solve(self):
        for item in self.mydata.values:
            parsed = list(re.findall(r'(\d+)-(\d+).([a-z]):.([a-z]+)', item))[0]
            isValid = self.testValid(parsed[0], parsed[1], parsed[2], parsed[3])
            print(isValid)
            if isValid:
                self.result += 1
        return self.result

    def testValid(self, lownum, highnum, letter, password):
        print(f"{lownum}, {highnum}, {letter}, {password}")
        count = password.count(letter)
        print(f"count: {count}")
        if int(lownum) <= count <= int(highnum):
            return True
        else:
            return False

# mything = find2020s()
# mything.getfirstresult()
test = filethingy('testinput.txt')

mything2 = findvalid('input.txt')
mything2.solve()
print(mything2.result)