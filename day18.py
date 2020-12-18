def sliceByParetheses(expression, start):
    depth = 0
    for i in range(start, len(expression)):
        if expression[i] == '(':
            depth += 1
        elif expression[i] == ')':
            depth -= 1
        if depth == 0:
            return expression[start + 1 : i]

def parenthesizePluses(expression):
    i = 0
    while i < len(expression):
        if expression[i] == '+':
            depth = 0
            for j in range(i - 1, - 1, - 1):
                if expression[j] == ')':
                    depth += 1
                elif expression[j] == '(':
                    depth -= 1
                if expression[j] not in '+*' and depth == 0:
                    start = j
                    break
            for j in range(i + 1, len(expression)):
                if expression[j] == '(':
                    depth += 1
                elif expression[j] == ')':
                    depth -= 1
                if expression[j] not in '+*' and depth == 0:
                    end = j + 1
                    break
            expression = expression[: start] + '(' + expression[start : end] + ')' + expression[end :]
            i += 1
        i += 1
    return(expression)
    
def solve(expression):
    result = 0
    operator = ''
    i = 0
    while i < len(expression):
        if expression[i] == '(':
            subExpression = sliceByParetheses(expression, i)
            i += len(subExpression) + 1
            operand = solve(subExpression)
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

partTwo = 0
for expression in expressions:
    partTwo += solve(parenthesizePluses(expression))
print(partTwo)