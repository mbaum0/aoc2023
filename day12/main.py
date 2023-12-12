from dataclasses import dataclass
import math
import itertools

input_file = "./day12/data.txt"

def part1(grid):
    return grid

def main():
    grid = []
    with open(input_file) as f:
        data = f.read().splitlines()
        for i, line in enumerate(data):
            grid.append([c for c in line])


    p1 = part1(grid)
    print(p1)

    # p2 = part2(grid)
    # print(p2)


if __name__ == "__main__":
    main()

