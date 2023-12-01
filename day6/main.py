from dataclasses import dataclass

race_file = "./day6/races.txt"


@dataclass
class Race():
    record: int
    time: int

def part1(races):
    ways_to_win = []
    for r, race in enumerate(races):
        ways_to_win.append(0)
        for duration in range(0, race.time):
            dist = get_race_dist(race.time, duration)
            if (dist > race.record):
                ways_to_win[r] += 1
            elif (ways_to_win[r] > 0):
                break
    
    # multiply all the ways to win
    total = 1
    for ways in ways_to_win:
        total *= ways

    return total

def get_race_dist(race_time, button_held_duration):
    return (race_time - button_held_duration) * button_held_duration

def part2(races):
    ways_to_win = []
    for r, race in enumerate(races):
        ways_to_win.append(0)
        for duration in range(0, race.time):
            dist = get_race_dist(race.time, duration)
            if (dist > race.record):
                ways_to_win[r] += 1
            elif (ways_to_win[r] > 0):
                break
    return ways_to_win[0]


def main():
    with open(race_file) as f:
        data = f.read().splitlines()

    times = data[0].split(':')[1].split()
    distances = data[1].split(':')[1].split()

    races = []

    for idx in range(len(times)):
        t = int(times[idx])
        d = int(distances[idx])
        races.append(Race(d, t))

    res = part1(races)
    print(res)
    res = part2(races)
    print(res)

if __name__ == "__main__":
    main()
