from dataclasses import dataclass
import math
from functools import lru_cache
from itertools import product, groupby
import time

input_file = "./day14/data.txt"

def roll(grid, direction='up'):
    dy = 0
    dx = 0
    startY = 0
    startX = 0
    endY = 0
    endX = 0
    if direction == 'up':
        dy = -1
        endY = len(grid)
        endX = len(grid[0])
    elif direction == 'down':
        dy = 1
        startY = len(grid) - 1
        endY = -1
        endX = len(grid[0])
    elif direction == 'left':
        dx = -1
        endY = len(grid)
        endX = len(grid[0])
    elif direction == 'right':
        dx = 1
        endY = len(grid)
        startX = len(grid[0]) - 1
        endX = -1

    deltaY = dy*-1 if dy != 0 else 1
    deltaX = dx*-1 if dx != 0 else 1
    for y in range(startY, endY, deltaY):
        row = grid[y]
        for x in range(startX, endX, deltaX):
            if grid[y][x] == 'O':
                newY = y + dy
                newX = x + dx
                while (newY >= 0 and newY < len(grid) and newX >= 0 and newX < len(grid[0]) and grid[newY][newX] == '.'):
                    grid[newY-dy][newX-dx] = '.'
                    grid[newY][newX] = 'O'
                    newY += dy
                    newX += dx
    return grid

def print_grid(grid):
    for y in grid:
        print(''.join(y))
    print()

def sum_load(grid):
    sum = 0
    length = len(grid)
    for idy, y in enumerate(grid):
        for idx, x in enumerate(y):
            if grid[idy][idx] == 'O':
                sum +=  length - idy

    return sum

def part2(grid):
    cycles = 1
    for i in range(cycles):
        grid = roll(grid, 'up')
        print_grid(grid)
        grid = roll(grid, 'left')
        print_grid(grid)
        grid = roll(grid, 'down')
        print_grid(grid)
        grid = roll(grid, 'right')
        print_grid(grid)
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
