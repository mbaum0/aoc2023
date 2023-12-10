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

VALID_UP_PIPES = [START_POINT, V_PIPE, RIGHT_DOWN_PIPE, LEFT_DOWN_PIPE]
VALID_DOWN_PIPES = [START_POINT, V_PIPE, RIGHT_UP_PIPE, LEFT_UP_PIPE]
VALID_RIGHT_PIPES = [START_POINT, H_PIPE, RIGHT_DOWN_PIPE, RIGHT_UP_PIPE]
VALID_LEFT_PIPES = [START_POINT, H_PIPE, LEFT_DOWN_PIPE, LEFT_UP_PIPE]
def get_starting_point(grid):
    for y, row in enumerate(grid):
        for x, col in enumerate(row):
            if col == START_POINT:
                return (x, y)
    return None

def get_next_point(grid, current_point, last_point):
    x = current_point[0]
    y = current_point[1]
    grid_width = len(grid[0])
    grid_height = len(grid)
    current_pipe = grid[y][x]

    if y > 0 and grid[y-1][x] in VALID_UP_PIPES:
        next_up = (x, y-1)
    else:
        next_up = None

    if y < grid_height -1 and grid[y+1][x] in VALID_DOWN_PIPES:
        next_down = (x, y+1)
    else:
        next_down = None

    if x > 0 and grid[y][x-1] in VALID_LEFT_PIPES:
        next_left = (x-1, y)
    else:
        next_left = None

    if x < grid_width - 1 and grid[y][x+1] in VALID_RIGHT_PIPES:
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
    

def get_area(path, grid):
    n = len(path)
    area = 0
    x = path[0][0]
    y = path[0][1]
    part = grid[y][x]

    for i in range(n - 1):
        x = path[i][0]
        y = path[i][1]
        part = grid[y][x]
        area += (path[i][0] * path[i + 1][1]) 
        area -= (path[i + 1][0] * path[i][1])

    area = abs(area) - n + 1
    area = (abs(area) / 2.0) + 1

    return area
    
def part2(data):
    starting_point = get_starting_point(data)
    previous_point = starting_point
    next_point = get_next_point(data, previous_point, None)
    path = [starting_point, next_point]
    while(next_point != starting_point):
        save_point = next_point
        next_point = get_next_point(data, next_point, previous_point)
        previous_point = save_point
        path.append(next_point)
    
    area = get_area(path, data)
    return area

        

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

    p2 = part2(grid)
    print(p2)


if __name__ == "__main__":
    main()