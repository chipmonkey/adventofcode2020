import re

DEBUG = False

class filethingy:

    def __init__(self, filename):
        self.values = []
        f = open(filename, 'r')
        for line in f:
            self.values.append(line.strip())
        print("input: ", self.values)



class getSeat:
    """class to solve the problem at hand
    """

    def __init__(self, filename):
        self.result = 0  # Highest Seat ID
        self.mydata = filethingy(filename)
        self.allseats = []


    def solve(self):
        for boardingPass in self.mydata.values:
            print(boardingPass)
            rowId = boardingPass[0:7]
            rowId = rowId.replace('F','0')
            rowId = rowId.replace('B','1')
            # print(rowId)
            row = int(rowId, 2)
            # print(int(rowId, 2))

            seatId = boardingPass[7:10]
            print(seatId)
            seatId = seatId.replace('L','0')
            seatId = seatId.replace('R','1')
            seat = int(seatId, 2)
            print(f'seat: {seat}')

            id = row * 8 + seat

            self.allseats.append(id)

        self.allseats.sort()

        for i in range(min(self.allseats), max(self.allseats)):
            if i not in self.allseats:
                results = i
                print(f"Solution: {i}")

        print(f'all seats: {self.allseats}')
        return(self.result)

            # numfields = len(passport.split())
            # print(f"Number of fields: {numfields}")
            # print(f"{passport}")
            # isValid = True
            # for myKey in self.keys:
            #     myValue = self.getValue(myKey, passport)
            #     if myKey != 'cid' and myValue is None:
            #         print(f"Missing {myKey}")
            #         isValid = False
            # if isValid:
            #     self.result += 1
            # print(f"So far: {self.result}")
        return self.result


test = filethingy('testinput.txt')

mything = getSeat('testinput.txt')
mything2 = getSeat('input.txt')
day1 = mything.solve()
day2 = mything2.solve()
