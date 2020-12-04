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
    valids = ['']

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

        if myFind:
            x = myFind.group(1)
            if myKey == 'byr':
                myFind = re.search('(^\d{4})$', x)
                print(f'byr test for {myFind.group(1)} (also {x})')
                if myFind and (x < '1920' or x > '2002'):
                    print(f"could not validate byr for {x}")
                    myFind = None
            elif myKey == 'iyr':
                myFind = re.search('(^\d{4})$', x)
                if myFind and (x < '2010' or x > '2020'):
                    myFind = None
            elif myKey == 'eyr':
                myFind = re.search('(^\d{4})$', x)
                if myFind and (x < '2020' or x > '2030'):
                    myFind = None
            elif myKey == 'hgt':
                parsed = re.findall('(^\d{2,3})(cm|in)$', x)
                if parsed:
                    parsed = parsed[0]
                    print(f"Parsed: {parsed}")
                    height = parsed[0]
                    unit = parsed[1]
                    if isinstance(int(height[0]), int):
                        if unit == 'cm' and '150' <= height <= '193':
                            myFind = parsed[0] + parsed[1]
                        elif unit == 'in' and '59' <= height <= '76':
                            myFind = parsed[0] + parsed[1]
                        else:
                            myFind = None
                else:
                    myFind = None

            elif myKey == 'hcl':
                myFind = re.search('^#[0-9a-f]{6}$', x)
                print(f"hcl: {myFind} from {x}")
            elif myKey == 'ecl':
                myFind = re.search('^amb$|^blu$|^brn$|^gry$|^grn$|^hzl$|^oth$', x)
            elif myKey == 'pid':
                myFind = re.search('^\d{9}$', x)
            elif myKey == 'cid':
                pass
            else:
                myFind = None
        return myFind


test = filethingy('testinput.txt')

mything = countValid('testinput.txt')
mything.solve()

mything = countValid('input.txt')
day1 = mything.solve()
# day2 = mything2.solve()
