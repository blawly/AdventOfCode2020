def partOne():
    invalidSum = 0
    for ticket in tickets:
        for number in ticket:
            if not valid(number):
                invalidSum += number
    return invalidSum

def valid(number):
    for rule in rules.values():
        if number in range(rule[0][0], rule[0][1] + 1):
            return True
        elif number in range(rule[1][0], rule[1][1] + 1):
            return True
    return False

with open('input/day16.txt') as f:
    rules = dict()
    (rawRules, myRawTicket, rawTickets) = f.read().split('\n\n')
    for rule in rawRules.split('\n'):
        start1 = int(rule.split(':')[1].split()[0].split('-')[0])
        stop1 = int(rule.split(':')[1].split()[0].split('-')[1])
        start2 = int(rule.split(':')[1].split()[2].split('-')[0])
        stop2 = int(rule.split(':')[1].split()[2].split('-')[1])
        rules[rule.split(':')[0]] = ((start1, stop1), (start2, stop2))
    myTicket = []
    for number in myRawTicket.split('\n')[1].split(','):
        myTicket.append(int(number))
    tickets = []
    for ticket in rawTickets.split('\n')[1:]:
        thisTicket = []
        for number in ticket.split(','):
            thisTicket.append(int(number))
        tickets.append(thisTicket)

print(partOne())