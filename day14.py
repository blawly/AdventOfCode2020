def writeOne(address, data, memory):
    binData = f'{data:036b}'
    maskedData = ''
    for i in range(36):
        if mask[i] == 'X':
            maskedData += binData[i]
        else:
            maskedData += mask[i]
    memory[address] = int(maskedData, 2)

def writeTwo(address, data, memory):
    binAddress = f'{address:036b}'
    maskedAddress = ''
    for i in range(36):
        if mask[i] == '0':
            maskedAddress += binAddress[i]
        else:
            maskedAddress += mask[i]
    addresses = unmaskAddress(maskedAddress)
    for address in addresses:
        memory[address] = data

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

memOne = dict()
memTwo = dict()
mask = ''
with open('input/day14.txt') as f:
    for line in f:
        if line.split()[0] == 'mask':
            mask = line.split()[2].rstrip('\n')
        else:
            writeOne(int(line.split('[')[1].split(']')[0]), int(line.split()[2]), memOne)
            writeTwo(int(line.split('[')[1].split(']')[0]), int(line.split()[2]), memTwo)
print(sum(memOne.values()))
print(sum(memTwo.values()))
