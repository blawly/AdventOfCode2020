cupstr = '653427918'
cups = []
for cup in cupstr:
    cups.append(int(cup))
current = cups[0]

for i in range(100):

    pickup = []
    for j in range(3):
        pickup.append(cups.pop((cups.index(current) + 1) % (9 - j)))

    destination = current - 1
    while destination not in cups:
        if destination == 0:
            destination = 9
        else:
            destination -= 1

    for cup in pickup[::-1]:
        cups.insert(cups.index(destination) + 1, cup)

    current = cups[(cups.index(current) + 1) % 9]

partOne = ''
for i in range(8):
    partOne += str(cups[(cups.index(1) + 1 + i) % 9])
print(partOne)