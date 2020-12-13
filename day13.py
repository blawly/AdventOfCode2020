import math

buses = []
with open('input/day13.txt') as f:
    timestamp = int(f.readline())
    i = 0
    for bus in f.readline().rstrip('\n').split(','):
        if bus != 'x':
            buses.append((i, int(bus)))
        i += 1

buses.sort(reverse = True, key = lambda x: x[1])

# Part One
minWait = (-1, buses[0][1])
for bus in buses:
    wait = math.ceil(timestamp / bus[1]) * bus[1] - timestamp
    if wait < minWait[1]:
        minWait = (bus[1], wait)
print(math.prod(minWait))

# Part Two
timestamp = buses[0][1] - buses[0][0]
adder = buses[0][1]
for bus in buses[1:]:
    while not ((timestamp + bus[0]) / bus[1]).is_integer():
        timestamp += adder
    adder *= bus[1]
print(timestamp)