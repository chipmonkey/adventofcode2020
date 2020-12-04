import re

DEBUG = False

class filethingy:

    def __init__(self, filename):
        newPassport = True
        thisPassport = ''
        self.values = []
        f = open(filename, 'r')
        for line in f:
            if line == '\n':
                self.values.append(thisPassport)
                thisPassport = ''
                newPassport = True
                continue
            elif newPassport:
                thisPassport = line.strip('\n')
                newPassport = False
            else:
                thisPassport = thisPassport + ' ' + line.strip('\n')
        if line != '\n':  # The last line matters!
            self.values.append(thisPassport)
        print("input: ", self.values)



class countValid:
    """class to solve the problem at hand
    """
    
    keys = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid', 'cid']

    def __init__(self, filename):
        self.result = 0  # Count of valid passports
        self.mydata = filethingy(filename)

    def solve(self):
        for passport in self.mydata.values:
            # print(f"{passport.split()}")
            numfields = len(passport.split())
            print(f"Number of fields: {numfields}")
            print(f"{passport}")
            isValid = True
            for myKey in self.keys:
                myValue = self.getValue(myKey, passport)
                if myKey != 'cid' and myValue is None:
                    print(f"Missing {myKey}")
                    isValid = False
            if isValid:
                self.result += 1
            print(f"So far: {self.result}")
        return self.result


    @staticmethod
    def getValue(myKey, passport):
        """return the value for myKey from passport if found
        otherwise return None"""
        rvalue = None
        # print(f"searching for {myKey} in {passport}")
        myFind = re.search(f'{myKey}:([#\w]+)', passport)
        # if myFind:
        #     print(f"Found: {myFind.group()}")
        return myFind


test = filethingy('testinput.txt')

mything = countValid('testinput.txt')
mything.solve()

mything = countValid('input.txt')
day1 = mything.solve()
# day2 = mything2.solve()
