adapters = [0]
with open('input/day10.txt') as f:
    for line in f:
        adapters.append(int(line))
adapters.sort()

last = adapters[0]
oneJoltDiffs = 0
threeJoltDiffs = 1
for adapter in adapters[1::]:
    if adapter - last == 3:
        threeJoltDiffs += 1
    elif adapter - last == 1:
        oneJoltDiffs += 1
    last = adapter
partOne = oneJoltDiffs * threeJoltDiffs
print(partOne)