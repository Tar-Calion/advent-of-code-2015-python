def visit_houses(data):
    # set with coordinates of visited houses
    visited = set()

    # current position
    x = 0
    y = 0

    # add starting position to set of visited houses
    visited.add((x, y))

    # iterate over all characters in data
    for char in data:
        # move santa
        if char == "^":
            y += 1
        elif char == "v":
            y -= 1
        elif char == ">":
            x += 1
        elif char == "<":
            x -= 1
        else:
            print("ERROR: unknown character")
            raise ValueError("unknown character")

        # add current position to set of visited houses
        visited.add((x, y))
    return visited


def visit_houses_and_count(data):
    visited_houses = visit_houses(data)
    return len(visited_houses)


def visit_houses_with_robot_santa_and_count(data):
    # divide data into two parts
    data_santa = data[::2]
    data_robo_santa = data[1::2]

    # visit houses
    visited_houses_santa = visit_houses(data_santa)
    visited_houses_robo_santa = visit_houses(data_robo_santa)

    # combine sets
    visited_houses = visited_houses_santa.union(visited_houses_robo_santa)
    return len(visited_houses)


# read input.txt
with open("data/day03/input.txt", "r") as file:
    # read everything
    data = file.read()

# part one
count_visited_houses = visit_houses_and_count(data)
# print number of visited houses
print("santa visits {} houses".format(count_visited_houses))

# part two
count_visited_houses_second_year = visit_houses_with_robot_santa_and_count(data)
# print number of visited houses
print("santa and robo santa visit {} houses".format(count_visited_houses_second_year))
