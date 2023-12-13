from dataclasses import dataclass
import math
from functools import lru_cache
from itertools import product, groupby
import time

input_file = "./day13/data.txt"


def reflect(rows, index0, index1):
    if index0 < 0:
        return 0
    if index1 >= len(rows)-1:
        return index0 + 1
    if rows[index0] == rows[index1]:
        return 1 + reflect(rows, index0 - 1, index1 + 1)
    if rows[index0] != rows[index1] and abs(index0 - index1) > 1:
        # case where we think we found a middle but failed
        return -1 * index1
    else:
        return reflect(rows, index0+1, index1+1)


def part1(puzzles):
    sum = 0
    for p in puzzles:
        res = reflect(p, 1, 2)
        res *= 100
        if res < 0:
            rP = rotate(p)
            res = reflect(rP, 1, 2)
        sum += res
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
