from dataclasses import dataclass
import math
from functools import lru_cache
from itertools import product, groupby
import time

input_file = "./day13/data.txt"

def calc_points(puzzle, index0, index1):
    points = 1
    while index0 >= 0 and index1 < len(puzzle):
        if puzzle[index0] == puzzle[index1]:
            points += 1
            index0 -= 1
            index1 += 1
        else:
            return 0
    return points
    
def get_possible_middles(rows):
    middles = []
    for idx, row in enumerate(rows):
        if idx == 0 or idx == len(rows)-1:
            continue
        if row == rows[idx-1] and row != rows[idx+1]:
            middles.append(idx)
    return middles


def part1(puzzles):
    sum = 0
    for p in puzzles:
        middles = get_possible_middles(p)
        for m in middles:
            points = calc_points(p, m-1, m)
        
            if points > 0:
                sum += (points * 100)
                break
        else:
            rp = rotate(p)
            middles = get_possible_middles(rp)
            for m in middles:
                points = calc_points(rp, m-1, m)
                if points > 0:
                    sum += points
                    break
    return sum

def rotate(puzzle):
    newPuzzle = ["" for _ in range(len(puzzle[0]))]
    for i, l in enumerate(puzzle):
        for j, c in enumerate(l):
            newPuzzle[j] += c
    return newPuzzle


def main():
    with open(input_file) as f:
        rows = f.read().splitlines()

    
    puzzles = []

    chunkIndex = 0
    for row in rows:
        if row == "":
            chunkIndex += 1
            continue
        if len(puzzles) <= chunkIndex:
            puzzles.append([])
        puzzles[chunkIndex].append(row)

    p1 = part1(puzzles)
    print(p1)


if __name__ == "__main__":
    main()
