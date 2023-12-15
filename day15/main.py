from dataclasses import dataclass
import math
from functools import lru_cache
from itertools import product, groupby
import time
import hashlib

input_file = "./day15/data.txt"

@dataclass
class Lens:
    label: str
    op: str
    pos: int


def hash_str(s):
    sum = 0
    for c in s:
        sum += ord(c)
        sum *= 17
        sum %= 256
    return sum

def part1(data):
    p1 = 0
    for d in data:
        p1 += hash_str(d)
    return p1

def part2(data):
    ## map of label -> (index,val)
    boxes = [{} for _ in range(256)]
    for d in data:
        if '=' in d:
            label, op = d.split('=')
        else:
            label, op = d.split('-')
            op = '-'
        box = hash_str(label)
        if op == '-':
            loc = boxes[box].pop(label, None)
            if loc is None:
                continue
            for k in boxes[box].keys():
                if boxes[box][k][0] > loc[0]:
                    new_loc = (boxes[box][k][0] - 1, boxes[box][k][1])
                    boxes[box][k] = new_loc
        else:
            if label in boxes[box]:
                boxes[box][label] = (boxes[box][label][0], op)
                continue
            boxes[box][label] = (len(boxes[box]) + 1, op)

    power_sum = 0
    for bidx, box in enumerate(boxes):
        for label in box:
            power = (1 + bidx) * box[label][0] * int(box[label][1])
            power_sum += power
    return power_sum



def main():
    with open(input_file) as f:
        data = f.read()

    data = data.replace('\n', '')

    data = data.split(',')
    p1 = part1(data)
    print(p1)

    p2 = part2(data)
    print(p2)

if __name__ == "__main__":
    main()
