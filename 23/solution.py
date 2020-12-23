import copy

def move_cups(cups, num_cups, num_turns):

    # establish a circular list (a dict where the value of a key is the next key)
    # and pre-fill with the provided values
    ring = {i: i+1 for i in range(1, num_cups)}
    ring[num_cups] = cups[0]
    for i in range(len(cups)-1):
        ring[cups[i]] = cups[i+1]
    if num_cups > len(cups):
        ring[cups[-1]] = max(cups)+1
    else:
        ring[cups[-1]] = cups[0]

    current_cup = cups[0]
    
    for i in range(num_turns):
        # find the cups which need to be moved
        to_be_moved = [ring[current_cup], ring[ring[current_cup]], ring[ring[ring[current_cup]]]]
        ring[current_cup] = ring[ring[ring[ring[current_cup]]]]
        destination = current_cup - 1 if current_cup != 1 else num_cups
        while destination in to_be_moved:
            destination -= 1
            if destination < 1:
                destination = num_cups
        old = ring[destination]
        ring[destination] = to_be_moved[0]
        ring[to_be_moved[2]] = old
        current_cup = ring[current_cup]
    
    return ring

def part1(cups):
    ring = move_cups(cups, len(cups), 100)
    curr = 1
    solution = ""
    for i in range(len(cups)-1):
        curr = ring[curr]
        solution += str(curr)
    return solution

def part2(cups):
    ring = move_cups(cups, 1000000, 10000000)
    return ring[1] * ring[ring[1]]    

if __name__ == "__main__":
    
    with open('23/input.txt') as inputfile:
        inputlines = inputfile.read()
        #inputlines = "389125467" # sample input
        cups = [int(a) for a in inputlines]

    print(f"Part 1 solution: {part1(copy.copy(cups))}")
    print(f"Part 2 solution: {part2(copy.copy(cups))}")