from dataclasses import dataclass
import math

input_file = "./day8/data.txt"

def part1(steps, network_map, first_step, end_step):
    count = 0
    current_step = first_step
    while not current_step.endswith(end_step):
        step = steps[count % len(steps)]
        if step == "L":
            current_step = network_map[current_step][0]
        elif step == "R":
            current_step = network_map[current_step][1]
        count += 1
    return count

def are_nodes_finished(nodes):
    for node in nodes:
        if not node.endswith("Z"):
            return False
    return True

def part2(steps, network_map):
    start_nodes = [step for step in network_map.keys() if step.endswith("A")]

    node_steps = []
    for node in start_nodes:
        count = 0
        current_step = node
        while not current_step.endswith("Z"):
            step = steps[count % len(steps)]
            if step == "L":
                current_step = network_map[current_step][0]
            elif step == "R":
                current_step = network_map[current_step][1]
            count += 1
        node_steps.append(count)

    return math.lcm(*node_steps)

def parse_data_to_map(data):
    steps = data[0]

    network_map = {}
    for i in range(2, len(data)):
        dat = data[i].split("=")
        network_map[dat[0].strip()] = dat[1].strip().replace("(", "").replace(")", "").replace(" ", "").strip().split(',')

    return steps, network_map

def main():
    with open(input_file) as f:
        data = f.read().splitlines()

    steps, network_map = parse_data_to_map(data)

    p1 = part1(steps, network_map, "AAA", "ZZZ")
    print(p1)

    p2 = part2(steps, network_map)
    print(p2)

if __name__ == "__main__":
    main()