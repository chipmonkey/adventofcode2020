f = open('input.txt', 'r')
values = []
for line in f:
    values.append(int(line))

print(values)

for x in range(len(values)-1):
    for y in range(x+1, len(values)):
        print(x,y, values[x] + values[y])
        if (values[x] + values[y]) == 2020:
            print(x, y, values[x], values[y], values[x]*values[y])
            print("hi")
            exit()