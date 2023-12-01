from dataclasses import dataclass
import functools   

input_file = "./day7/input.txt"

@dataclass
class CardPlay():
    hand: str
    bet: int
    hand_dict: dict
    rank: int


def get_play_value(p):
    joker_count = p.hand.count('J')
    d = p.hand_dict

    # five of a kind
    for k in d:
        if d[k] == 5:
            return 10
        elif (d[k] + joker_count == 5) and k != 'J':
            return 10
        
    # four of a kind
    for k in d:
        if d[k] == 4 or (k != 'J' and d[k] + joker_count >= 4):
            return 9
        
    # full house
    three_count = 0
    two_count = 0
    for k in d:
        if d[k] == 3:
            three_count += 1
        if d[k] == 2:
            two_count += 1

    if three_count > 0 and two_count > 0:
        return 8

    # joker full house
    if three_count > 0 and joker_count > 0:
        return 8
    
    if two_count > 1 and joker_count > 0:
        return 8
    
    # three of a kind
    if three_count > 0 or (two_count > 0 and joker_count > 0) or joker_count > 1:
        return 7
    
    # two pair
    pair_count = 0
    for k in d:
        if d[k] >= 2:
            pair_count += 1
    
    if pair_count == 2 or (pair_count == 1 and joker_count > 0) or joker_count > 1:
        return 6
    
    # one pair
    if pair_count == 1 or joker_count > 0:
        return 5
    
    # high card
    return 0

def compare_hands(h1, h2):
    c_ranks = ['J', '2','3','4','5','6','7','8','9','T','Q','K','A']
    for c in range(len(h1)):
        if c_ranks.index(h1[c]) > c_ranks.index(h2[c]):
            return 1
        elif c_ranks.index(h1[c]) < c_ranks.index(h2[c]):
            return -1
    return 0


def compare_plays(p1, p2):
    if p1.rank > p2.rank:
        return 1
    elif p1.rank < p2.rank:
        return -1
    else:
        return compare_hands(p1.hand, p2.hand)

def group_cards(data):
    # group cards by char.
    res_dict = {}
    for c in data:
        if c in res_dict:
            res_dict[c] += 1
        else:
            res_dict[c] = 1
    return res_dict


def part1(plays):
    for play in plays:
        play.hand_dict = group_cards(play.hand)
        res = get_play_value(play)
        play.rank = res
    
    plays = sorted(plays, key=functools.cmp_to_key(compare_plays), reverse=True)

    sum = 0
    for idx, play in enumerate(plays):
        newRank = len(plays) - idx
        val = (newRank * play.bet)
        sum += val
    return sum

def main():
    with open(input_file) as f:
        data = f.read().splitlines()

    plays = []
    for d in data:
        a = d.split(' ')
        plays.append(CardPlay(a[0], int(a[1]), {}, 0))

    res = part1(plays)
    print(res)
    # res = part2(data)
    # print(res)

if __name__ == "__main__":
    main()