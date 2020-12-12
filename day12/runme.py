import re
import time

class input:

    def __init__(self, filename):
        self.linesOriginal = []
        f = open(filename, 'r')
        for line in f:
            self.linesOriginal.append(line.strip())
        self.lines = self.linesOriginal
        print(f"input: {self.lines} ")

    
class ship:

    def __init__(self, filename):
        self.input = input(filename)
        self.x = 0
        self.y = 0
        self.wayX = 10
        self.wayY = -1
    
    def solve(self):
        for line in self.input.lines:
            print(f"Executing {line}")
            self._execute(line)
            print(f"Ship is: ({self.x}, {self.y}) waypoint is: ({self.wayX}, {self.wayY}")
        print("hello")
        return (abs(self.x) + abs(self.y))
    
    def _execute(self, line):
        lineParts = list(re.findall(r'([NSEWLRF])(\d+)', line)[0])
        # print(f"lineParts: {lineParts}")
        operator = lineParts[0]
        quantity = int(lineParts[1])


        if operator == 'N':
            self.wayY = self.wayY - quantity
        elif operator == 'S':
            self.wayY = self.wayY + quantity
        elif operator == 'E':
            self.wayX = self.wayX + quantity
        elif operator == 'W':
            self.wayX = self.wayX - quantity
        elif operator == 'L':
            if quantity % 90 != 0:
                print(f"{quantity} is not divisible by 90")
                exit("This should not be")
            rotations = quantity // 90 % 4
            print (f"Rotating: {rotations} to the Left")
            if rotations == 0:
                pass
            if rotations == 1:
                tempX = self.wayX
                self.wayX = self.wayY
                self.wayY = -1 * tempX
            elif rotations == 2:
                self.wayX = -1 * self.wayX
                self.wayY = -1 * self.wayY
            elif rotations == 3:
                tempX = self.wayX
                self.wayX = -1 * self.wayY
                self.wayY = tempX
        elif operator == 'R':
            if quantity % 90 != 0:
                print(f"{quantity} is not divisuble by 90")
                exit("This should not be")
            rotations = quantity // 90 % 4
            print (f"Rotating: {rotations} to the Right")
            if rotations == 0:
                pass
            if rotations == 1:
                tempX = self.wayX
                self.wayX = -1 * self.wayY
                self.wayY = tempX
            elif rotations == 2:
                self.wayX = -1 * self.wayX
                self.wayY = -1 * self.wayY
            elif rotations == 3:
                tempX = self.wayX
                self.wayX = self.wayY
                self.wayY = -1 * tempX
        elif operator == 'F':
            self.x = self.x + quantity * self.wayX
            self.y = self.y + quantity * self.wayY
        else:
            exit("Bad Operator")
        

# myship = ship('testinput.txt')
# result = myship.solve()
# print(f"result: {result}")

myship = ship('input.txt')
result = myship.solve()
print(f"result: {result}")