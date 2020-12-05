import re

DEBUG = False

maxSeatId = 0
allseats = []
f = open('input.txt', 'r')
for line in f:
    row = int(line[0:7].replace('F', '0').replace('B', '1'), 2)
    seat = int(line[7:10].replace('L', '0').replace('R', '1'), 2)
    id = row * 8 + seat
    if id > maxSeatId:
        maxSeatId = id
    allseats.append(id)

print(f'Max Seat ID: {maxSeatId}')

allseats.sort()

for i in range(min(allseats), max(allseats)):
    if i not in allseats:
        results = i

print(f'Solution: {results}')
