from dataclasses import dataclass
import math
import itertools

input_file = "./day11/data.txt"


class SpaceGrid:
    def __init__(self, grid):
        self.grid = grid
        self.width = len(grid[0])
        self.height = len(grid)

    def get(self, x, y):
        if x < 0 or x >= self.width or y < 0 or y >= self.height:
            return None
        return self.grid[y][x]
    
    def insert_row_at(self, row, y):
        self.grid.insert(y, row)
        self.height += 1

    def insert_col_at(self, col, x):
        for i, row in enumerate(self.grid):
            row.insert(x, col[i])
        self.width += 1

    def is_row_empty(self, y):
        for x in range(self.width):
            if self.get(x, y) != '.':
                return False
        return True
    
    def is_col_empty(self, x):
        for y in range(self.height):
            if self.get(x, y) != '.':
                return False
        return True
    
    def get_empty_rows_between_galaxies(self, g1, g2):
        count = 0
        lower = min(g1[1], g2[1])
        upper = max(g1[1], g2[1])
        for y in range(lower + 1, upper):
            if self.is_row_empty(y):
                count += 1
        return count
    
    def get_empty_cols_between_galaxies(self, g1, g2):
        count = 0
        lower = min(g1[0], g2[0])
        upper = max(g1[0], g2[0])
        for x in range(lower + 1, upper):
            if self.is_col_empty(x):
                count += 1
        return count
    
    def get_galaxies(self):
        galaxies = []
        for y in range(self.height):
            for x in range(self.width):
                if self.get(x, y) == '#':
                    galaxies.append((x, y))
        return galaxies
    
    def expand_space(self, amount):
        # insert into empty rows
        empty_rows = []
        for y in range(self.height):
            if self.is_row_empty(y):
                empty_rows.append(y)

        empty_cols = []
        # insert into empty cols
        for x in range(self.width):
            if self.is_col_empty(x):
                empty_cols.append(x)

        for i, y in enumerate(empty_rows):
            for j in range(amount):
                self.insert_row_at(['.'] * self.width, y + i + j)

        for i, x in enumerate(empty_cols):
            for j in range(amount):
                self.insert_col_at(['.'] * self.height, x + i + j)
    
    def get_all_galaxy_pairs(self):
        return list(itertools.combinations(self.get_galaxies(), 2))

    def __str__(self):
        return "\n".join(["".join(row) for row in self.grid])
    
def get_galaxy_distance(g1, g2):
    return abs(g1[0] - g2[0]) + abs(g1[1] - g2[1])



def part2(spaceGrid):
    pairs = spaceGrid.get_all_galaxy_pairs()
    sum = 0
    multiplier = 1000000-1
    for pair in pairs:
        sum += get_galaxy_distance(pair[0], pair[1]) 
        sum += (spaceGrid.get_empty_rows_between_galaxies(pair[0], pair[1])*multiplier) + (spaceGrid.get_empty_cols_between_galaxies(pair[0], pair[1])*multiplier)
    return sum


def part1(spaceGrid):
    sum = 0
    pairs = spaceGrid.get_all_galaxy_pairs()
    for pair in pairs:
        sum += get_galaxy_distance(pair[0], pair[1])
        sum += spaceGrid.get_empty_rows_between_galaxies(pair[0], pair[1]) + spaceGrid.get_empty_cols_between_galaxies(pair[0], pair[1])
    return sum

def main():
    grid = []
    with open(input_file) as f:
        data = f.read().splitlines()
        for i, line in enumerate(data):
            grid.append([c for c in line])

    spaceGrid = SpaceGrid(grid)

    p1 = part1(spaceGrid)
    print(p1)

    p2 = part2(spaceGrid)
    print(p2)


if __name__ == "__main__":
    main()
