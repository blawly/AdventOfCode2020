f = open("day7.txt")
rules = dict()
for line in f:
    words = line.split()
    ruleDict = dict()
    if words[4] != "no":
        for i in range(4, len(words), 4):
            ruleDict[words[i + 1] + words[i + 2]] = int(words[i])
    rules[words[0] + words[1]] = ruleDict
#Part One
def canContain(color, rules):
    for k, v in rules.items():
        if color in v:
            ableColors.add(k)
            ableColors.union(canContain(k, rules))
    return ableColors
ableColors = set()
print(len(canContain("shinygold", rules)))
#Part Two
def bagsInside(color, rules):
    bags = 0
    for k, v in rules[color].items():
        bags += v + v * bagsInside(k, rules)
    return bags
print(bagsInside("shinygold", rules))