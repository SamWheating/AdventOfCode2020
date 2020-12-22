import copy

def score_deck(deck):
    score = 0
    for i in range(len(deck)):
        multiplier = len(deck)-i
        score += deck[i] * multiplier
    return score

def part1(deck1, deck2):
    while True:
        top1 = deck1[0]
        top2 = deck2[0]
        if top1 > top2:
            deck2 = deck2[1:]
            deck1 = deck1[1:] + [top1, top2]
        elif top2 > top1:
            deck2 = deck2[1:] + [top2, top1]
            deck1 = deck1[1:]
        if min([len(deck1), len(deck2)]) == 0:
            break
    return score_deck(deck1+deck2)

def play_combat_recursive(deck1, deck2):
    # track previous sets of deck1+deck2 to detect loops
    seen_states = set()

    while True:

        if str(deck1) + "/" + str(deck2) in seen_states:
            winner = "p1"
            break
        seen_states.add(str(deck1) + "/" + str(deck2))
        top1 = deck1[0]
        top2 = deck2[0]
        if len(deck1[1:]) >= top1 and len(deck2[1:]) >= top2:
            subdeck1 = copy.copy(deck1)[1:top1+1]
            subdeck2 = copy.copy(deck2)[1:top2+1]
            winner, _ = play_combat_recursive(subdeck1, subdeck2) 
        else:
            winner = "p1" if top1 > top2 else "p2"

        if winner == "p1":
            deck1 = deck1[1:] + [top1, top2]
            deck2 = deck2[1:]
        elif winner == "p2":
            deck2 = deck2[1:] + [top2, top1]
            deck1 = deck1[1:]

        if min(len(deck1), len(deck2)) == 0:
            break

    return winner, deck1+deck2

def part2(deck1, deck2):
    winner, deck = play_combat_recursive(deck1, deck2)
    return score_deck(deck)

if __name__ == "__main__":
    
    with open('22/input.txt') as inputfile:
        inputlines = inputfile.read().split("\n")
        deck1 = [int(card) for card in inputlines[1:inputlines.index("")]]
        deck2 = [int(card) for card in inputlines[inputlines.index("")+2:]]

    print(f"Part 1 solution: {part1(deck1, deck2)}")
    print(f"Part 2 solution: {part2(deck1, deck2)}")