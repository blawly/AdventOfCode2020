f = open("day5.txt")
ids = []
for line in f:
    rowCode = line[0:7]
    colCode = line[7:10]
    row = 0
    for char in rowCode:
        row *= 2
        if char == 'B':
            row += 1
    col = 0
    for char in colCode:
        col *= 2
        if char == 'R':
            col += 1
    ids.append(row * 8 + col)
#Part One
maxid = 0
for pid in ids:
    if pid > maxid:
        maxid = pid
print(maxid)
#Part Two
for myid in range(1024):
    if (myid not in ids and 
        myid - 1 in ids and 
        myid + 1 in ids):
            print(myid)