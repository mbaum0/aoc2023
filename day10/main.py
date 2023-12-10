from dataclasses import dataclass
import math
import itertools

input_file = "./day10/data.txt"

START_POINT = 'S'
H_PIPE = "-"
V_PIPE = "|"
RIGHT_DOWN_PIPE = "7"
LEFT_DOWN_PIPE = "F"
RIGHT_UP_PIPE = "J"
LEFT_UP_PIPE= "L"

VALID_PIPES = [START_POINT, H_PIPE, V_PIPE, RIGHT_DOWN_PIPE, LEFT_DOWN_PIPE, RIGHT_UP_PIPE, LEFT_UP_PIPE]
def get_starting_point(grid):
    for i, row in enumerate(grid):
        for j, col in enumerate(row):
            if col == START_POINT:
                return (i, j)
    return None

def get_next_point(grid, current_point, last_point):
    x = current_point[0]
    y = current_point[1]
    grid_width = len(grid[0])
    grid_height = len(grid)
    current_pipe = grid[y][x]


    if y > 0 and grid[y-1][x] in VALID_PIPES:
        next_up = (x, y-1)
    else:
        next_up = None

    if y < grid_height -1 and grid[y+1][x] in VALID_PIPES:
        next_down = (x, y+1)
    else:
        next_down = None

    if x > 0 and grid[y][x-1] in VALID_PIPES:
        next_left = (x-1, y)
    else:
        next_left = None

    if x < grid_width - 1 and grid[y][x+1] in VALID_PIPES:
        next_right = (x+1, y)
    else:
        next_right = None

    if current_pipe == START_POINT:
        if next_up is not None and next_up != last_point:
            return next_up
        elif next_down is not None and next_down != last_point:
            return next_down
        elif next_left is not None and next_left != last_point:
            return next_left
        elif next_right is not None and next_right != last_point:
            return next_right
        else:
            return None
    elif current_pipe == H_PIPE:
        if next_left is not None and next_left != last_point:
            return next_left
        elif next_right is not None and next_right != last_point:
            return next_right
        else:
            return None
    elif current_pipe == V_PIPE:
        if next_up is not None and next_up != last_point:
            return next_up
        elif next_down is not None and next_down != last_point:
            return next_down
        else:
            return None
    elif current_pipe == RIGHT_DOWN_PIPE:
        if next_down is not None and next_down != last_point:
            return next_down
        elif next_left is not None and next_left != last_point:
            return next_left
        else:
            return None
    elif current_pipe == LEFT_DOWN_PIPE:
        if next_down is not None and next_down != last_point:
            return next_down
        elif next_right is not None and next_right != last_point:
            return next_right
        else:
            return None
    elif current_pipe == RIGHT_UP_PIPE:
        if next_up is not None and next_up != last_point:
            return next_up
        elif next_left is not None and next_left != last_point:
            return next_left
        else:
            return None
    elif current_pipe == LEFT_UP_PIPE:
        if next_up is not None and next_up != last_point:
            return next_up
        elif next_right is not None and next_right != last_point:
            return next_right
        else:
            return None
    else:
        return None

        

def part1(data):
    starting_point = get_starting_point(data)
    previous_point = starting_point
    next_point = get_next_point(data, previous_point, None)
    steps = 1
    while(next_point != starting_point):
        steps += 1
        save_point = next_point
        next_point = get_next_point(data, next_point, previous_point)
        previous_point = save_point
    return steps/2
    

def main():
    grid = []
    with open(input_file) as f:
        data = f.read().splitlines()
        for i, line in enumerate(data):
            # split into array of chars
            grid.append([c for c in line])

    p1 = part1(grid)
    print(p1)


if __name__ == "__main__":
    main()