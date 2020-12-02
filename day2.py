f = open('day2.txt')
lines = [0 for x in range(1000)]
validOne = 0
validTwo = 0
for i in range(1000):
    lines[i] = f.readline()
    one = int(lines[i].split('-')[0])
    two = int(lines[i].split('-')[1].split(' ')[0])
    letter = lines[i].split(' ')[1].split(':')[0]
    word = lines[i].split(' ')[2]
    count = word.count(letter)
    if count in range(one, two + 1):
        validOne += 1
    if (word[one - 1] == letter and word[two - 1] != letter) != (word[one - 1] != letter and word[two - 1] == letter):
        validTwo += 1
print(validOne)
print(validTwo)