numbers = []
preambleN = 25
with open('input/day9.txt') as f:
    for line in f:
        numbers.append(int(line))

def valid(number, preamble):
    for i in range(preambleN):
        if preamble[i] < number:
            for j in range(i + 1, preambleN):
                if preamble[i] + preamble[j] == number:
                    return True
    return False

def firstNonValid():
    for i in range(preambleN, len(numbers)):
        if not valid(numbers[i], numbers[i - preambleN : i]):
            return numbers[i]

partOne = firstNonValid()
print(partOne)

def contiguousSet(inumber):
    contSet = []
    for number in numbers:
        contSet.append(number)
        while sum(contSet) > inumber:
            contSet.pop(0)
        if sum(contSet) == inumber:
            return min(contSet) + max(contSet)
    return -1

partTwo = contiguousSet(partOne)
print(partTwo)