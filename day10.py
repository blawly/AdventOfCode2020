adapters = [0]
with open('input/day10.txt') as f:
    for line in f:
        adapters.append(int(line))
adapters.sort()
adapters.append(max(adapters) + 3)

last = adapters[0]
oneJoltDiffs = 0
threeJoltDiffs = 0
for adapter in adapters[1::]:
    if adapter - last == 3:
        threeJoltDiffs += 1
    elif adapter - last == 1:
        oneJoltDiffs += 1
    last = adapter
partOne = oneJoltDiffs * threeJoltDiffs
print(partOne)

arrangements = [0] * (max(adapters) + 1)
arrangements[0] = 1
for adapter in adapters[1:]:
    arrangements[adapter] = arrangements[adapter - 1] + arrangements[adapter - 2] + arrangements[adapter - 3]
partTwo = arrangements[max(adapters)]
print(partTwo)