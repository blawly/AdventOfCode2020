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

def contiguousSet(number):
    for i in range(len(numbers)):
        if numbers[i] < number:
            sumOfSet = numbers[i]
            smallest = numbers[i]
            largest = numbers[i]
            for j in range(i + 1, len(numbers)):
                sumOfSet += numbers[j]
                if numbers[j] < smallest:
                    smallest = numbers[i]
                elif numbers[j] > largest:
                    largest = numbers[j]
                if sumOfSet == number:
                    return smallest + largest
                elif sumOfSet > number:
                    break
    return -1

partTwo = contiguousSet(partOne)
print(partTwo)