from dataclasses import dataclass
import math
from functools import lru_cache
from itertools import product, groupby
import time

input_file = "./day13/data.txt"

def calc_points(puzzle, index0, index1):
    points = index1
    while index0 >= 0 and index1 < len(puzzle):
        if puzzle[index0] == puzzle[index1]:
            index0 -= 1
            index1 += 1
        else:
            return 0
    return points

def calc_points_smudge(puzzle, index0, index1):
    points = index1
    smudge_count = 0
    while index0 > 0 and index1 < len(puzzle):
        i0 = set(puzzle[index0])
        i1 = set(puzzle[index1])
        diff1 = i0.difference(i1)
        diff2 = i1.difference(i0)
        diff = len(diff1.union(diff2))
        if diff > 0:
            if smudge_count > 1 or diff > 1:
                return 0
            else:
                smudge_count += 1
                index0 -= 1
                index1 += 1

        elif puzzle[index0] == puzzle[index1]:
            index0 -= 1
            index1 += 1
        else:
            return 0
    if smudge_count == 1:
        return points
    return 0
    
def get_possible_middles(rows):
    middles = []
    for idx, row in enumerate(rows):
        if idx < 0 or idx == len(rows) -1:
            continue
        if row == rows[idx+1]:
            middles.append(idx)
    return middles

def part2(puzzles):
    sum = 0
    for idx, p in enumerate(puzzles):
        psum = 0
        middles = get_possible_middles(p)
        for m in middles:
            c = calc_points_smudge(p, m, m+1)
            if c > 0:
                psum += c *100
                break
        if psum == 0:
            rp = rotate(p)
            middles = get_possible_middles(rp)
            if len(middles) == 0:
                print("BAD")
            for m in middles:
                c = calc_points_smudge(rp, m, m+1)
                psum += c
        sum += psum
    return sum

def part1(puzzles):
    sum = 0
    for idx, p in enumerate(puzzles):
        psum = 0
        middles = get_possible_middles(p)
        for m in middles:
            c = calc_points(p, m, m+1)
            if c > 0:
                psum += c *100
                break
        if psum == 0:
            rp = rotate(p)
            middles = get_possible_middles(rp)
            if len(middles) == 0:
                print("BAD")
            for m in middles:
                c = calc_points(rp, m, m+1)
                psum += c
        sum += psum
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

    p2 = part2(puzzles)
    print(p2)


if __name__ == "__main__":
    main()
