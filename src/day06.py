from enum import Enum
import re


class Action(Enum):
    TURN_ON = "turn on"
    TURN_OFF = "turn off"
    TOGGLE = "toggle"

    def apply(self, value):
        if self == Action.TURN_ON:
            return 1
        elif self == Action.TURN_OFF:
            return 0
        elif self == Action.TOGGLE:
            return 1 - value
        else:
            raise ValueError("unknown action")


class Instruction:
    def __init__(self, action, start, end):
        self.action = action
        self.start = start
        self.end = end

    def apply(self, grid):
        for x in range(self.start[0], self.end[0] + 1):
            for y in range(self.start[1], self.end[1] + 1):
                grid[x][y] = self.action.apply(grid[x][y])


def parse_line(line):
    # regex action coord_start "through" coord_end
    match = re.match(r"(.+) (\d+),(\d+) through (\d+),(\d+)", line)

    action = Action(match.group(1))
    start = (int(match.group(2)), int(match.group(3)))
    end = (int(match.group(4)), int(match.group(5)))
    return Instruction(action, start, end)


# create grid
grid = [[0 for _ in range(1000)] for _ in range(1000)]

# read input.txt and parse lines
with open("data/day06/input.txt", "r") as file:
    instructions = [parse_line(line) for line in file]

# apply instructions
for instruction in instructions:
    instruction.apply(grid)

# count lights
count_lights = sum(sum(row) for row in grid)
# print number of lights
print("total number of lights: {}".format(count_lights))
