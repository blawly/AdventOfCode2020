f = open('input/day7.txt')
#Dictionary for the rules, keys are bag colors
rules = dict()
for line in f:
    words = line.split()
    #Dictionaries for each rule, values for the main dictionary
    ruleDict = dict()
    if words[4] != 'no':
        for i in range(4, len(words), 4):
            ruleDict[words[i + 1] + words[i + 2]] = int(words[i])
    #Filling the main dictionary
    rules[words[0] + words[1]] = ruleDict
#Part One
def canContain(color):
    for k, v in rules.items():
        if color in v:
            ableColors.add(k)
            ableColors.union(canContain(k))
    return ableColors
ableColors = set()
print(len(canContain('shinygold')))
#Part Two
def bagsInside(color):
    bags = 0
    for k, v in rules[color].items():
        bags += v + v * bagsInside(k)
    return bags
print(bagsInside('shinygold'))