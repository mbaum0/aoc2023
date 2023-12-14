from dataclasses import dataclass
import math
from functools import lru_cache
from itertools import product, groupby
import time

input_file = "./day14/data.txt"

def roll(grid, direction='up'):
    dy = 0
    dx = 0
    if direction == 'up':
        dy = -1
    elif direction == 'down':
        dy = 1
    elif direction == 'left':
        dx = -1
    elif direction == 'right':
        dx = 1
    
    for idy, y in enumerate(grid):
        if idy == 0:
            continue
        for idx, x in enumerate(y):
            if grid[idy][idx] == 'O':
                newY = idy + dy
                newX = idx + dx
                while (newY >= 0 and newY < len(grid) and newX >= 0 and newX < len(grid[0]) and grid[newY][idx] == '.'):
                    grid[newY-dy][idx-dx] = '.'
                    grid[newY][idx] = 'O'
                    newY += dy
                    newX += dx
    return grid

def sum_load(grid):
    sum = 0
    length = len(grid)
    for idy, y in enumerate(grid):
        for idx, x in enumerate(y):
            if grid[idy][idx] == 'O':
                sum +=  length - idy

    return sum

def part2(grid):
    cycles = 1000000000
    for i in range(cycles):
        grid = roll(grid, 'up')
        grid = roll(grid, 'left')
        grid = roll(grid, 'down')
        grid = roll(grid, 'right')
    sum = sum_load(grid)
    return sum

def part1(grid):
    grid = roll(grid)
    sum = sum_load(grid)
    return sum

def main():
    with open(input_file) as f:
        rows = f.read().splitlines()

    grid = []
    for row in rows:
        grid.append(list(row))

    # p1 = part1(grid)
    # print(p1)
    p2 = part2(grid)
    print(p2)



if __name__ == "__main__":
    main()
