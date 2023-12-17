from dataclasses import dataclass
from functools import lru_cache

input_file = "./day16/data.txt"

def main():
    with open(input_file) as f:
        data = f.read()

    # make a grid
    grid = []
    for i, row in enumerate(data.split("\n")):
        grid.append(list(row))

    print(grid)

if __name__ == "__main__":
    main()
