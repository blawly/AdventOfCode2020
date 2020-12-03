f = open('day2.txt')
validOne = 0
validTwo = 0
for line in f:
    one = int(line.split('-')[0])
    two = int(line.split('-')[1].split(' ')[0])
    letter = line.split(' ')[1].split(':')[0]
    word = line.split(' ')[2]
    count = word.count(letter)
    #Part One
    if count in range(one, two + 1):
        validOne += 1
    #Part Two
    if (word[one - 1] == letter and word[two - 1] != letter) != (word[one - 1] != letter and word[two - 1] == letter):
        validTwo += 1
print(validOne)
print(validTwo)