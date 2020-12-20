f = open('input/day06.txt')
sumOne = 0
sumTwo = 0
for group in f.read().split('\n\n'):

    # Part One
    uniques = []
    for char in group:
        if char != '\n' and char not in uniques:
            uniques.append(char)
    sumOne += len(uniques)

    # Part Two
    for char in uniques:
        if group.count(char) - group.count('\n') == 1:
            sumTwo += 1

print(sumOne)
print(sumTwo)