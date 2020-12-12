instructions = []
with open('input/day12.txt') as f:
    for line in f:
        direction = line[0]
        value = int(line.rstrip('\n')[1:])
        instructions.append([direction, value])

class Ship:
    def __init__(self, position, waypoint, heading):
        self.position = position
        self.waypoint = waypoint
        self.heading = heading

    def move(self, direction, value, ship):
        if ship:
            pos = self.position
        else:
            pos = self.waypoint
        if direction in ['N', 0]:
            pos[1] += value
        elif direction in ['E', 90]:
            pos[0] += value
        elif direction in ['S', 180]:
            pos[1] -= value
        elif direction in ['W', 270]:
            pos[0] -= value

    def moveToWp(self, value):
        self.position = [self.position[0] + value * self.waypoint[0], self.position[1] + value * self.waypoint[1]]

    def turn(self, direction, value):
        if direction == 'L':
            self.heading = (self.heading - value) % 360
        elif direction == 'R':
            self.heading = (self.heading + value) % 360

    def rotate(self, direction, value):
        waypoint = self.waypoint.copy()
        if (direction == 'L' and value == 90) or (direction == 'R' and value == 270):
            self.waypoint[0] = 0 - waypoint[1]
            self.waypoint[1] = waypoint[0]
        elif (direction == 'L' and value == 270) or (direction == 'R' and value == 90):
            self.waypoint[0] = waypoint[1]
            self.waypoint[1] = 0 - waypoint[0]
        else:
            self.waypoint[0] = 0 - waypoint[0]
            self.waypoint[1] = 0 - waypoint[1]

    def instruct(self, instruction, partOne):
        if instruction[0] in 'NESW':
            self.move(instruction[0], instruction[1], partOne)
        elif instruction[0] in 'LR':
            if partOne:
                self.turn(instruction[0], instruction[1])
            else:
                self.rotate(instruction[0], instruction[1])
        elif instruction[0] == 'F':
            if partOne:
                self.move(self.heading, instruction[1], True)
            else:
                self.moveToWp(instruction[1])

# Part One
ship = Ship([0, 0], [0, 0], 90)
for instruction in instructions:
    ship.instruct(instruction, True)
print(abs(ship.position[0]) + abs(ship.position[1]))

# Part Two
ship = Ship([0, 0], [10, 1], 0)
for instruction in instructions:
    ship.instruct(instruction, False)
print(abs(ship.position[0]) + abs(ship.position[1]))