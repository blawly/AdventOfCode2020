f = open("day3.txt")
lines = []
for line in f:
    lines.append(line)
#Part One
y = 0
trees = 0
for line in lines:
    if line != '':
        if line[y] == '#':
            trees += 1
        y += 3
        y = y % (len(line) - 1)
print(trees)
#Part Two
product = 1
slopes = [[1, 1], [1, 3], [1, 5], [1, 7], [2, 1]]
for slope in slopes:
    y = 0
    trees = 0
    for line in lines[::slope[0]]:
        if line != '':
            if line[y] == '#':
                trees += 1
            y += slope[1]
            y = y % (len(line) - 1)
    product *= trees
print(product)