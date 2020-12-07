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

    def getDirectParents(self, bagName):
        """Get list of bags which contain a given bag"""
        results = []
        for bag in self.bags:
            for innerbag in bag.contents:
                if bagName == innerbag['targetBag']:
                    print(f"Found {bagName} in {bag.bagName}")
                    results.append(bag)
        print(f"Direct results are {results}")
        return(results)
    
    def getDirectParentsFromList(self, bagNameList):
        """"""
        results = []
        for bag in bagNameList:
            results.extend(self.getDirectParents(bag))
        print(f"results are {results}")
        return(results)

    def __repr__(self):
        self.__str__()
    
    def __str__(self):
        for bag in self.bags:
            print(bag)


class part1:
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

        print("--------------------")
        findbags = self.myBags.getDirectParents('shiny gold bag')
        print(f"Findbags are {findbags}")
        solutionbags = []
        while findbags:
            findbagNames = [x.bagName for x in findbags]
            print(f"findbagNames: {findbagNames}")
            print(f"solutionbags: {solutionbags}")
            newbags = set(findbagNames) - set(solutionbags)
            solutionbags.extend(list(newbags))
            print(f"newbags: {newbags}")
            findbags = self.myBags.getDirectParentsFromList(newbags)
            print(f"New Find Bags: {findbags}")

        print(f"Solution should be : {solutionbags}")
        self.result = len(list(solutionbags))
        print(f"Results: {self.result}")
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

mything = part1('testinput.txt')
mything.solve()

mything = part1('input.txt')
part1result = mything.solve()
# # day2 = mything2.solve()
