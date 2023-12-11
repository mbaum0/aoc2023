from dataclasses import dataclass
import math
import itertools

input_file = "./day11/data.txt"

def part1(data):
    return data


def main():
    with open(input_file) as f:
        data = f.read().splitlines()

    p1 = part1(data)
    print(p1)

    # p2 = part2(data)
    # print(p2)


if __name__ == "__main__":
    main()
