from dataclasses import dataclass
import math
from functools import lru_cache
from itertools import product, groupby
import time

input_file = "./day13/data.txt"


def reflect(rows, index0, index1):
    if index0 < 0 or index1 >= len(rows):
        return 1
    if rows[index0] == rows[index1]:
        return 1 + reflect(rows, index0 - 1, index1 + 1)
    else:
        return reflect(rows, index0+1, index1+1)


def part1(vPuzzles, hPuzzles):
    sum = 0
    for v in vPuzzles:
        sum += reflect(v, 0, 1)
    for h in hPuzzles:
        sum += reflect(h, 0, 1) * 100
    return sum


def main():
    with open(input_file) as f:
        rows = f.read().splitlines()

    
    puzzleChunks = []

    chunkIndex = 0
    for row in rows:
        if row == "":
            chunkIndex += 1
            continue
        if len(puzzleChunks) <= chunkIndex:
            puzzleChunks.append([])
        puzzleChunks[chunkIndex].append(row)

    
    verticalPuzzles = []
    horizontalPuzzles = []


    for i, chunk in enumerate(puzzleChunks):
        if i % 2 == 0:
            verticalPuzzles.append(chunk)
        else:
            horizontalPuzzles.append(chunk)

    # rotate vertical puzzles
    for idx, vp in enumerate(verticalPuzzles):
        newVP = ["" for _ in range(len(vp[0]))]
        for i, l in enumerate(vp):
            for j, c in enumerate(l):
                newVP[j] += c
        verticalPuzzles[idx] = newVP


    p1 = part1(verticalPuzzles, horizontalPuzzles)
    print(p1)


if __name__ == "__main__":
    main()
