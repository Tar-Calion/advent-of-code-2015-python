from enum import Enum
import re


class Action(Enum):
    TURN_ON = "turn on"
    TURN_OFF = "turn off"
    TOGGLE = "toggle"

    def apply_part1(self, value):
        if self == Action.TURN_ON:
            return 1
        elif self == Action.TURN_OFF:
            return 0
        elif self == Action.TOGGLE:
            return 1 - value
        else:
            raise ValueError("unknown action")

    def apply_part2(self, value):
        if self == Action.TURN_ON:
            return value + 1
        elif self == Action.TURN_OFF:
            return max(0, value - 1)
        elif self == Action.TOGGLE:
            return value + 2
        else:
            raise ValueError("unknown action")


class Instruction:
    def __init__(self, action, start, end):
        self.action = action
        self.start = start
        self.end = end

    def apply_part1(self, grid):
        for x in range(self.start[0], self.end[0] + 1):
            for y in range(self.start[1], self.end[1] + 1):
                grid[x][y] = self.action.apply_part1(grid[x][y])

    def apply_part2(self, grid):
        for x in range(self.start[0], self.end[0] + 1):
            for y in range(self.start[1], self.end[1] + 1):
                grid[x][y] = self.action.apply_part2(grid[x][y])


def parse_line(line):
    # regex action coord_start "through" coord_end
    match = re.match(r"(.+) (\d+),(\d+) through (\d+),(\d+)", line)

    action = Action(match.group(1))
    start = (int(match.group(2)), int(match.group(3)))
    end = (int(match.group(4)), int(match.group(5)))
    return Instruction(action, start, end)


# create grid
grid_part1 = [[0 for _ in range(1000)] for _ in range(1000)]

# read input.txt and parse lines
with open("data/day06/input.txt", "r") as file:
    instructions = [parse_line(line) for line in file]

# apply instructions
for instruction in instructions:
    instruction.apply_part1(grid_part1)

# count lights
count_lights = sum(sum(row) for row in grid_part1)
# print number of lights
print("total number of lights: {}".format(count_lights))

# create grid
grid_part2 = [[0 for _ in range(1000)] for _ in range(1000)]

# apply instructions
for instruction in instructions:
    instruction.apply_part2(grid_part2)

# count intensity
intensity = sum(sum(row) for row in grid_part2)
# print intensity
print("total intensity: {}".format(intensity))
