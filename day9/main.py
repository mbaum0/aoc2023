from dataclasses import dataclass
import math
import itertools

input_file = "./day9/data.txt"

def get_next_sequence(sequence):
    next_sequence = []
    for i, num in enumerate(sequence):
        if i == len(sequence) - 1:
            break
        i0 = sequence[i]
        i1 = sequence[i+1]
        n = i1 - i0
        next_sequence.append(n)

    return next_sequence

def get_complete_sequence(sequence):
    complete_sequence = [sequence]
    while not all(item == 0 for item in sequence):
        sequence = get_next_sequence(sequence)
        complete_sequence.append(sequence)
    return complete_sequence

def extrapolate_future_value(sequence):
    len_sequence = len(sequence)
    # iterate over sequence from end to start
    for i in range(len_sequence-1, -1, -1):
        if i == len_sequence-1:
            sequence[i].append(0)
        else:
            next_val = sequence[i+1][-1] + sequence[i][-1]
            sequence[i].append(next_val)
    return sequence[0][-1]

def extrapolate_past_value(sequence):
    len_sequence = len(sequence)
    for i in range(len_sequence-1, -1, -1):
        if i == len_sequence-1:
            sequence[i].append(0)
        else:
            next_val = sequence[i][0] - sequence[i+1][0]
            sequence[i].insert(0, next_val)
    return sequence[0][0]

def part1(histories):
    sum = 0
    for h in histories:
        res = get_complete_sequence(h)
        next_val = extrapolate_future_value(res)
        sum += next_val
    return sum

def part2(histories):
    sum = 0
    for h in histories:
        res = get_complete_sequence(h)
        next_val = extrapolate_past_value(res)
        sum += next_val
    return sum
    

def main():
    with open(input_file) as f:
        histories = f.read().splitlines()

    histories = [list(map(int, history.split(' '))) for history in histories]

    p1 = part1(histories)
    print(p1)

    p2 = part2(histories)
    print(p2)

if __name__ == "__main__":
    main()