with open('input/day5.txt') as f:
    sids = []
    for line in f:
        sid = 0
        for char in line.rstrip('\n'):
            sid *= 2
            if char in ['B', 'R']:
                sid += 1
        sids.append(sid)

# Part One
maxid = 0
for sid in sids:
    if sid > maxid:
        maxid = sid
print(maxid)

# Part Two
for mysid in range(1024):
    if (mysid not in sids and
        mysid - 1 in sids and
        mysid + 1 in sids):
            print(mysid)