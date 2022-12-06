import numpy as np

stack = [
    ['N', 'W', 'B'],
    ['B', 'M', 'D', 'T', 'P', 'S', 'Z', 'L'],
    ['R', 'W', 'Z', 'H', 'Q'],
    ['R', 'Z', 'J', 'V', 'D', 'W'],
    ['B', 'M', 'H', 'S'],
    ['B', 'P', 'V', 'H', 'J', 'N', 'G', 'L'],
    ['S', 'L', 'D', 'H', 'F', 'Z', 'Q', 'J'],
    ['B', 'Q', 'G', 'J', 'F', 'S', 'W'],
    ['J', 'D', 'C', 'S', 'M', 'W', 'Z']
]


class Command:
    def __init__(self, command):

        self.command = command
        digits = [int(s) for s in str.split(command) if s.isdigit()]
        self.amount, self.source, self.target = digits
        self.move()

    def move(self):
        moving_boxes = []
        print(self.command)
        for num in range(self.amount):
            moving_num = stack[self.source - 1].pop(0)
            moving_boxes.insert(0, moving_num)

        for num in moving_boxes:
            stack[self.target - 1].insert(0, num)

def get_top():
    tops = []
    for row in stack:
        tops.append(row[0])
    return "".join(tops)


with open("./data/day5.txt", 'r') as f:
    commands = []
    for line in f.readlines()[10:]:
        commands.append(Command(line[:-1]))

    print(get_top())
