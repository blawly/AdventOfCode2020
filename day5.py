f = open("day5.txt")
ids = []
for line in f:
    pid = 0
    for char in line.rstrip('\n'):
        pid *= 2
        if char in ['B', 'R']:
            pid += 1
    ids.append(pid)
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