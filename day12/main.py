from dataclasses import dataclass
import math
from itertools import product

input_file = "./day12/data.txt"

@dataclass
class SpringRecord:
    spring: str
    record: list
    combos: int

def part1(springs):
    combo_sum = 0
    for s in springs:
        s.combos = 0
        for c in gen_combos(s.spring):
            if validate_combo(c, s.record):
                s.combos += 1
        combo_sum += s.combos
    return combo_sum

def validate_combo(spring, record):
    last_group_size = 0
    record_idx = 0
    # get groups of broken springs
    groups = []
    for char in spring:
        if char == '#':
            last_group_size += 1
        else:
            if last_group_size > 0:
                groups.append(last_group_size)
                last_group_size = 0

    if last_group_size > 0:
        groups.append(last_group_size)


    if len(groups) != len(record):
        return False
    
    for group in groups:
        if group != record[record_idx]:
            return False
        record_idx += 1
    
    return True

def gen_combos(spring):
    possible = []

    xs = [i for i, char in enumerate(spring) if char == '?']

    replacements = product(['#', '.'], repeat=len(xs))

    for replacement in replacements:
        res = list(spring)
        for idx, char in zip(xs, replacement):
            res[idx] = char
        yield ''.join(res)

def main():
    grid = []
    with open(input_file) as f:
        rows = f.read().splitlines()

    records = []
    for r in rows:
        a = r.split(' ')
        #s = [c for c in a[0]]
        r = a[1].split(',')
        sr = [int(i) for i in r]
        r = SpringRecord(a[0], sr, 0)
        records.append(r)


    p1 = part1(records)
    print(p1)

    # p2 = part2(grid)
    # print(p2)


if __name__ == "__main__":
    main()

