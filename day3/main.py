schematic_file = "./day3/schematic.txt"
from dataclasses import dataclass

@dataclass
class Part:
    num: int
    row: int
    col: int
    width: int
    gears: list = None

@dataclass
class Gear:
    row: int
    col: int

def get_parts(schematic):
    parts = []
    for row, line in enumerate(schematic):
        c = ''
        for col in range(len(line)):
            if line[col].isdigit():
                c += line[col]
            else:
                if c != '':
                    parts.append(Part(int(c), row, col-len(c), len(c)))
                    c = ''
        if c != '':
            parts.append(Part(int(c), row, col-len(c)+1, len(c)))
    return parts

def get_adjacent_symbols(schematic, part):
    adjacent_symbols = []
    gears = []
    start_row = part.row - 1 if part.row > 0 else 0
    end_row = part.row + 2 if part.row + 2 < len(schematic) else len(schematic)
    start_col = part.col - 1 if part.col > 0 else 0
    end_col = part.col + part.width + 1 if part.col + part.width < len(schematic[0]) else len(schematic[0])
    for row in range(start_row, end_row):
        for col in range(start_col, end_col):
            if row == part.row and col >= part.col and col <= part.col + part.width - 1:
                continue
            adjacent_symbols.append(schematic[row][col])
            if schematic[row][col] == '*':
                gears.append(Gear(row, col))
    return adjacent_symbols, gears

def validate_part(symbols):
    return symbols.count('.') < len(symbols)

def part1(schematic):
    parts = get_parts(schematic)
    valid_parts = []
    for part in parts:
        symbols, _ = get_adjacent_symbols(schematic, part)
        if validate_part(symbols):
            valid_parts.append(part)
    return sum([part.num for part in valid_parts])
   

def part2(schematic):
    parts = get_parts(schematic)
    valid_parts = []
    for part in parts:
        symbols, gears = get_adjacent_symbols(schematic, part)
        if validate_part(symbols) and len(gears) > 0:
            part.gears = gears
            valid_parts.append(part)

    gear_map = {}
    for part in valid_parts:
        for gear in part.gears:
            if gear.row not in gear_map:
                gear_map[gear.row] = {}
            if gear.col not in gear_map[gear.row]:
                gear_map[gear.row][gear.col] = []
            gear_map[gear.row][gear.col].append(part.num)

    sum = 0
    for key, value in gear_map.items():
        for k, v in value.items():
            if len(v)  == 2:
                sum += (v[0] * v[1])
    return sum
    


with open(schematic_file, 'r') as f:
    schematic = [line.strip() for line in f.readlines()]
    print(part1(schematic))
    print(part2(schematic))