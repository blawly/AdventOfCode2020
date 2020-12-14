def writeOne(address, value, data):
    binValue = f'{value:036b}'
    maskedData = ''
    for i in range(36):
        if mask[i] == 'X':
            maskedData += binValue[i]
        else:
            maskedData += mask[i]
    data[address] = int(maskedData, 2)

def writeTwo(address, value, data):
    binAddress = f'{address:036b}'
    maskedAddress = ''
    for i in range(36):
        if mask[i] == '0':
            maskedAddress += binAddress[i]
        else:
            maskedAddress += mask[i]
    addresses = unmaskAddress(maskedAddress)
    for address in addresses:
        data[address] = value

def unmaskAddress(maskedAddress):
    floatCount = maskedAddress.count('X')
    unmasks = unmaskHelper(floatCount)
    addresses = []
    for unmask in unmasks:
        address = ''
        i = 0
        while i < floatCount:
            for char in maskedAddress:
                if char == 'X':
                    address += unmask[i]
                    i += 1
                else:
                    address += char
        addresses.append(address)
    return(addresses)

def unmaskHelper(floatCount):
    if floatCount == 0:
        unmasks = ['']
    else:
        unmasks = unmaskHelper(floatCount - 1)
        for _ in range(2 ** (floatCount - 1)):
            unmasks.append(unmasks[0] + '0')
            unmasks.append(unmasks[0] + '1')
            unmasks.remove(unmasks[0])
    return unmasks

dataOne = dict()
dataTwo = dict()
mask = ''
with open('input/day14.txt') as f:
    for line in f:
        if line.split()[0] == 'mask':
            mask = line.split()[2].rstrip('\n')
        else:
            writeOne(int(line.split('[')[1].split(']')[0]), int(line.split()[2]), dataOne)
            writeTwo(int(line.split('[')[1].split(']')[0]), int(line.split()[2]), dataTwo)
print(sum(dataOne.values()))
print(sum(dataTwo.values()))