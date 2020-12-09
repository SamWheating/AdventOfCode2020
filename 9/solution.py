with open('9/input.txt') as inputfile:
    inputlines = inputfile.read().split("\n")
    inputlines = [int(line) for line in inputlines]

# Part 1
def part1():
    i = 25 # start after the preamble
    while i < len(inputlines):
        valid = False
        for a in range(i-25, i):
            if valid: break
            for b in range(i-25, i):
                if valid: break
                if inputlines[a] + inputlines[b] == inputlines[i]:
                    valid = True
        if not valid:
            return inputlines[i]
        i += 1

def part2():
    target = part1()
    for i in range(len(inputlines)):
        for j in range(len(inputlines)-i):
            if sum(inputlines[i:j]) == target:
                return min(inputlines[i:j]) + max(inputlines[i:j])
            if sum(inputlines[i:j]) > 177777905:
                break

if __name__ == "__main__":
    print(f"Part 1 solution: {part1()}")
    print(f"Part 2 solution: {part2()}")
