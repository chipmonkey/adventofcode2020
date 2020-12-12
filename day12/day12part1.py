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
        self.direction = 0  # 0 = East, 1 = North, 2 = West, 3 = South
    
    def solve(self):
        for line in self.input.lines:
            print(f"Executing {line}")
            self._execute(line)
            print(f"Landing on ({self.x}, {self.y}) now pointing in direction: {self.direction}")
        print("hello")
        return (abs(self.x) + abs(self.y))
    
    def _execute(self, line):
        lineParts = list(re.findall(r'([NSEWLRF])(\d+)', line)[0])
        # print(f"lineParts: {lineParts}")
        operator = lineParts[0]
        quantity = int(lineParts[1])


        if operator == 'N':
            self.y = self.y - quantity
        elif operator == 'S':
            self.y = self.y + quantity
        elif operator == 'E':
            self.x = self.x + quantity
        elif operator == 'W':
            self.x = self.x - quantity
        elif operator == 'L':
            if quantity % 90 != 0:
                print(f"{quantity} is not divisible by 90")
                exit("This should not be")
            rotations = quantity // 90 % 4
            print (f"Rotating: {rotations} to the Left")
            self.direction = (self.direction + rotations) % 4
        elif operator == 'R':
            if quantity % 90 != 0:
                print(f"{quantity} is not divisuble by 90")
                exit("This should not be")
            rotations = quantity // 90 % 4
            print (f"Rotating: {rotations} to the Right")
            self.direction = (self.direction - rotations) % 4
        elif operator == 'F':
            if self.direction == 0:
                print("F0")
                self.x = self.x + quantity
            elif self.direction == 1:
                print("F1")
                self.y = self.y - quantity
            elif self.direction == 2:
                print("F2")
                self.x = self.x - quantity
            elif self.direction == 3:
                print("F3")
                self.y = self.y + quantity
            else:
                exit("Bad direction going Forward")
        else:
            exit("Bad Operator")
        

# myship = ship('testinput.txt')
# result = myship.solve()
# print(f"result: {result}")

myship = ship('input.txt')
result = myship.solve()
print(f"result: {result}")