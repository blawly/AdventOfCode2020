class Tile:
    def __init__(self, tid, tdata):
        self.tid = tid
        self.tdata = tdata
        self.tborders = self.borders()
        
    def borders(self):
        top = tdata[0]
        bottom = tdata[len(tdata) - 1]
        left = ''
        right = ''
        for line in tdata:
            left += line[0]
            right += line[len(line) - 1]
        return (top, right, bottom, left)

    def matches(self, tiles):
        matches = 0
        for border in self.tborders:
            for tile in tiles:
                if (
                    tile.tid != self.tid and 
                    (any(border == mborder for mborder in tile.tborders) or
                    any(border == mborder[::-1] for mborder in tile.tborders))
                ):
                    matches += 1
        return matches

with open('input/day20.txt') as f:
    rawTiles = f.read().split('\n\n')

tiles = []
for tile in rawTiles:
    tid = int(tile.split()[1].split(':')[0])
    tdata = []
    for line in tile.split('\n')[1:]:
        tdata.append(line)
    tiles.append(Tile(tid, tdata))

# Part One
cornerProduct = 1
for tile in tiles:
    if tile.matches(tiles) == 2:
        cornerProduct *= tile.tid
print(cornerProduct)