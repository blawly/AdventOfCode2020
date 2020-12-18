def subExpression(expression, start):
    depth = 0
    for i in range(start, len(expression)):
        if expression[i] == '(':
            depth += 1
        elif expression[i] == ')':
            depth -= 1
        if depth == 0:
            return expression[start + 1 : i]

def solve(expression):
    result = 0
    operator = ''
    i = 0
    while i < len(expression):
        if expression[i] == '(':
            subExp = subExpression(expression, i)
            i += len(subExp) + 1
            operand = solve(subExp)
            if operator == '*':
                result *= operand
            else:
                result += operand
        elif expression[i] in '+*':
            operator = expression[i]
        else:
            operand = int(expression[i])
            if operator == '*':
                result *= operand
            else:
                result += operand
        i += 1
    return result

with open('input/day18.txt') as f:
    expressions = []
    for line in f:
        expressions.append(line.replace(' ', '').rstrip('\n'))

partOne = 0
for expression in expressions:
    partOne += solve(expression)
print(partOne)