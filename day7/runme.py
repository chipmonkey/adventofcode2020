import re

DEBUG = False

class filethingy:

    def __init__(self, filename):
        self.values = []
        f = open(filename, 'r')
        for line in f:
            self.values.append(line.strip())
        print("input: ", self.values)


class bagStruct:

    def __init__(self):
        self.bagName = ''
        self.contents = [] # list of bags
    
    def updateOrAdd(self, bagName, targetBag, targetQuantity):
        self.bagName = bagName
        newTarget = {'targetBag': targetBag, 'targetQuantity': targetQuantity}
        if self.contents and targetBag:
            self.contents.append(newTarget)
        elif targetBag:
            self.contents = [newTarget]
        # print(f"Updated {self.bagName} to: {self.contents}")
    
    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return(f"bagName: {self.bagName}: contents: {self.contents}")


class bagMap:
    """ Custom little class for mapping the ensuing tree structure"""

    def __init__(self):
        self.bags = []  # list of bags

    def add(self, newbag):
        if newbag not in self.bags:
            self.bags.append(newbag)

    def __repr__(self):
        self.__str__()
    
    def __str__(self):
        for bag in self.bags:
            print(bag)


class day1:
    """class to solve the problem at hand
    """

    def __init__(self, filename):
        self.result = 0  # Count of valid passports
        self.mydata = filethingy(filename)
        self.myBags = bagMap()

    def solve(self):
        for line in self.mydata.values:
            newline = self.parseLine(line)
            print(newline)
            self.myBags.add(newline)

        print(f"MyBags: {self.myBags.bags}")
        return self.result
    

    def parseLine(self, line):
        newbag = bagStruct()
        split1 = list(map(str.strip, line.split('contain')))
        thisbag = split1[0].rstrip('s')
        inbags = list(map(lambda s:s.replace('.', ''), split1[1].split(',')))
        inbags = list(map(str.strip, inbags))
        for myBag in inbags:
            print(f"searching {myBag}")
            x = re.search(r'^(\d+)', myBag)
            if x:
                quantity = x.group(0)
                print(f'quantity: {quantity}')
                targetBag = myBag.replace(x.group(0) + ' ', '')
            else:
                quantity = 0
                targetBag = myBag

            # print(f"quantity: {quantity}")
            targetBag = targetBag.rstrip('s')
            # print(f'targetBag: {targetBag}')
            newbag.updateOrAdd(thisbag, targetBag, quantity)

        print(f'bag: {thisbag} - to bags: {inbags}')

        return(newbag)


test = filethingy('testinput.txt')

mything = day1('testinput.txt')
mything.solve()

# mything = countValid('input.txt')
# day1 = mything.solve()
# # day2 = mything2.solve()
