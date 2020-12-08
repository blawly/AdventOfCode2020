f = open("day8.txt")
ops = []
for line in f:
    ops.append(line.strip("\n").split())
#Part One
def findLoop():
    ip = 0
    acc = 0
    seq = []
    while True:
        if ip in seq:
            return [acc, True] #also returns True if an infinite loop is found
        if ip == len(ops):
            return [acc, False] #and False if no such loop is present anymore (for part two)
        seq.append(ip)
        if ops[ip][0] == "jmp":
            ip += int(ops[ip][1])
        elif ops[ip][0] == "acc":
            acc += int(ops[ip][1])
            ip += 1
        else:
            ip += 1
print(findLoop()[0])
#Part Two
def findError():
    for op in ops:
        if op[0] == "jmp":
            op[0] = "nop"
            res = findLoop()
            if not res[1]:
                return res[0]
            else:
                op[0] = "jmp"
        
        if op[0] == "nop":
            op[0] = "jmp"
            res = findLoop()
            if not res[1]:
                return res[0]
            else:
                op[0] = "nop"
print(findError())