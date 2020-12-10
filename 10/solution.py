with open('10/input.txt') as inputfile:
    inputlines = inputfile.read().split("\n")
    inputlines = [int(line) for line in inputlines]
    inputlines.sort()

# Part 1
def part1():
    gaps = {1: 1, 3: 1} 
    for i in range(1, len(inputlines)):
        gaps[inputlines[i] - inputlines[i-1]] += 1
    return gaps[1] * gaps[3]

def part2():
    adapters = [0] + inputlines
    adapters.reverse()  # highest -> lowest
    paths = [0] * len(adapters) # tracks the number of possible "paths" from each point in the sorted list
    paths[0] = 1 # there is only one possible path from the highest adapter to the device
    for i in range(1, len(adapters)):
        for j in range(1, min(3, i)+1):
            if adapters[i-j] <= adapters[i]+3:
                paths[i] += paths[i-j]
    return paths[-1]

if __name__ == "__main__":
    print(f"Part 1 solution: {part1()}")
    print(f"Part 2 solution: {part2()}")
