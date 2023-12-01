game_file = "./day2/games.txt"

RED = 'red'
GREEN = 'green'
BLUE = 'blue'

def part1(games, maxRed, maxGreen, maxBlue):
    possible_games = []
    possible_sum = 0
    for idx, game in enumerate(games):
        res = parse_game(game)
        if res[RED] <= maxRed and res[GREEN] <= maxGreen and res[BLUE] <= maxBlue:
            possible_games.append(game)
            possible_sum += idx+1
    return possible_sum


def part2(games):
    min_requred = {RED: 0, GREEN: 0, BLUE: 0}
    parsed_games = []
    power_sum = 0
    for idx, game in enumerate(games):
        res = parse_game(game)
        parsed_games.append(res)
        game_power = res[RED] * res[GREEN] * res[BLUE]
        power_sum += game_power
    return power_sum
        
    


# parse a game into a tuple of rgb values which specify the maximum number of rbg marbles seen
# input example: Game 1: 2 green, 6 blue, 7 red; 12 green, 6 blue, 3 red; 5 red, 18 green, 4 blue
def parse_game(game):
    rgbMap = {RED: 0, GREEN: 0, BLUE: 0}
    game = game.split(':')[1]
    for round in game.split(';'):
        for marble in round.split(','):
            marble = marble.strip().split(' ')
            rgbMap[marble[1]] = max(rgbMap[marble[1]], int(marble[0]))
    return rgbMap


with open(game_file, 'r') as f:
    games = [line.strip() for line in f.readlines()]
    print(part1(games, 12, 13, 14))
    print(part2(games))