from dataclasses import dataclass
import math
from functools import lru_cache
from itertools import product, groupby
import time

input_file = "./day12/data.txt"

@dataclass
class SpringRecord:
    spring: str
    record: list
    combos: int


def part2(springs, gen_func):
    combo_sum = 0
    for s in springs:
        s.spring = '?'.join([s.spring for _ in range(5)])
        s.record = tuple(s.record * 5)

        s_sum = gen_func(s.spring, s.record)
        combo_sum += s_sum

    return combo_sum

def part1(springs, gen_func):
    combo_sum = 0
    for s in springs:
        s.combos = 0
        s.record = tuple(s.record)
        combo_sum += gen_func(s.spring, s.record)
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

@lru_cache
def gen_combos_rec(spring, record):
    if len(spring) == 0:
        return 1 if len(record) == 0 else 0
    if spring.startswith("."):
        return gen_combos_rec(spring.strip("."), record)
    if spring.startswith("?"):
        return gen_combos_rec(spring.replace("?", ".", 1), record) + gen_combos_rec(spring.replace("?", "#", 1), record)
    if spring.startswith("#"):
        if len(record) == 0:
            return 0
        if len(spring) < record[0]:
            return 0
        if any(c == '.' for c in spring[0:record[0]]):
            return 0
        if len(record) > 1:
            if len(spring) < record[0] + 1 or spring[record[0]] == '#':
                return 0
            return gen_combos_rec(spring[record[0]+1:], record[1:])
        else:
            return gen_combos_rec(spring[record[0]:], record[1:])

def gen_combos(spring, record):
    xs = [i for i, char in enumerate(spring) if char == '?']

    replacements = product(['#', '.'], repeat=len(xs))
    sum = 0
    for replacement in replacements:
        res = list(spring)
        for idx, char in zip(xs, replacement):
            res[idx] = char

        if validate_combo(''.join(res), record):
            sum += 1
    return sum

def main():
    grid = []
    with open(input_file) as f:
        rows = f.read().splitlines()

    records = []
    for r in rows:
        a = r.split(' ')
        r = a[1].split(',')
        sr = [int(i) for i in r]
        r = SpringRecord(a[0], sr, 0)
        records.append(r)

    print("Part 1 Slow:")
    start = time.time()
    p1 = part1(records, gen_combos)
    end = time.time()
    print("Result: %d, Time: %f" % (p1, end - start))

    print("Part 2 Slow:")
    start = time.time()
    p2 = part2(records, gen_combos)
    end = time.time()
    print("Result: %d, Time: %f" % (p2, end - start))
    
    print("Part 1 Fast:")
    start = time.time()
    p1 = part1(records, gen_combos_rec)
    end = time.time()
    print("Result: %d, Time: %f" % (p1, end - start))

    print("Part 2 Fast:")
    start = time.time()
    p2 = part2(records, gen_combos_rec)
    end = time.time()
    print("Result: %d, Time: %f" % (p2, end - start))



if __name__ == "__main__":
    main()

