with open('input/day15.txt') as f:
    numbers = []
    for number in f.read().split(','):
        numbers.append(int(number))
starterCount = len(numbers)

occurrences = dict()
for i in range(29999999):
    if numbers[i] not in occurrences.keys():
        occurrences[numbers[i]] = []
    occurrences[numbers[i]].append(i)
    if len(occurrences[numbers[i]]) > 2:
        occurrences[numbers[i]].pop(0)
    if i >= starterCount - 1:
        if len(occurrences[numbers[i]]) < 2:
            numbers.append(0)
        if len(occurrences[numbers[i]]) == 2:
            numbers.append(occurrences[numbers[i]][1] - occurrences[numbers[i]][0])

print(numbers[2019])
print(numbers[29999999])