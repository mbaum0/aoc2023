scratcher_file = "./day4/scratcher.txt"
from math import pow
from dataclasses import dataclass

@dataclass
class ScratchCard:
    id: int
    winning_numbers: list
    numbers: list
    count: int


def part2(games):
    for key in sorted(games):
        game = games[key]
        wins = get_matched_numbers_count(game)
        for i in range(1, wins+1):
            games[game.id + i].count += (1 * game.count)

    return get_scratchcard_count(games)
        

def get_scratchcard_count(games):
    sum = 0
    for key in games:
        sum += games[key].count

    return sum

def get_matched_numbers_count(game):
    wins = 0
    for number in game.numbers:
        wins += game.winning_numbers.count(number)
    
    return wins
        

def part1(games):
    points = 0
    for game in games:
        winning_numbers, plays = game
        wins = 0
        for play in plays:
            # count occurences of each play in winning numbers
            wins += winning_numbers.count(play)
        if (wins == 0):
            continue
            
        points += int(pow(2, wins-1))
    
    return points


with open(scratcher_file, 'r') as f:
    scratcher = [line.strip() for line in f.readlines()]
    games = []
    games2 = {}
    for line in scratcher:
        card_id = int(line.split(':')[0].split()[1])
        winning_numbers, plays = line.split(':')[1].split("|")
        winning_numbers = winning_numbers.split()
        winning_numbers = [int(num) for num in winning_numbers]
        plays = plays.split()
        plays = [int(num) for num in plays]
        games.append((winning_numbers, plays))
        games2[card_id] = ScratchCard(card_id, winning_numbers, plays, 1)
    print(part1(games))
    print(part2(games2))