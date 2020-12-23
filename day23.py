def shuffle(cups, iterations):
    length = len(cups)
    current = cups[0]
    for _ in range(iterations):
        pickup = []
        for i in range(3):
            pickup.append(cups.pop((cups.index(current) + 1) % (length - i)))
        destination = current - 1
        while destination not in cups:
            if destination == 0:
                destination = length
            else:
                destination -= 1
        for cup in pickup[::-1]:
            cups.insert(cups.index(destination) + 1, cup)
        current = cups[(cups.index(current) + 1) % length]

cupstr = '653427918'

cupsOne = []
for cup in cupstr:
    cupsOne.append(int(cup))

shuffle(cupsOne, 100)

partOne = ''
for i in range(8):
    partOne += str(cupsOne[(cupsOne.index(1) + 1 + i) % len(cupsOne)])
print(partOne)


cupsTwo = []
for cup in cupstr:
    cupsTwo.append(int(cup))
for i in range(len(cupsTwo), 1000001):
    cupsTwo.append(i)

shuffle(cupsTwo, 10000000)

partTwo = 1
for i in range(2):
    partTwo *= cupsTwo[(cupsTwo.index(1) + 1 + i) % len(cupsTwo)]
print(partTwo)