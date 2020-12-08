f = open('input/day1.txt')
numbers = [0 for x in range(200)]
for x in range(200):
    numbers[x] = int(f.readline())
    for y in range(x):
        # Part One
        if numbers[x] + numbers[y] == 2020:
            print(numbers[x] * numbers[y])
        # Part Two
        elif numbers[x] + numbers[y] < 2020:
            for z in range(y):
                if numbers[x] + numbers[y] + numbers[z] == 2020:
                    print(numbers[x] * numbers[y] * numbers[z])