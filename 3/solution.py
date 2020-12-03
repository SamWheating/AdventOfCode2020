with open('3/input.txt') as inputfile:
    inputlines = inputfile.read().split("\n")
    parsed = [line for line in inputlines]

def traverse(path, right, down):
    pos = 0
    result = 0
    width = len(parsed[0])
    row_idx = 0
    while(row_idx) < len(parsed):
        if parsed[row_idx][pos] == "#":
            count += 1
        pos = (pos + right) % width
        row_idx += down 
    return count

def part1():

    return traverse(parsed, 3, 1)

def part2():

    result = traverse(parsed, 1, 1)
    result *= traverse(parsed, 3, 1)
    result *= traverse(parsed, 5, 1)
    result *= traverse(parsed, 7, 1)
    result *= traverse(parsed, 1, 2)

    return result 

if __name__ == "__main__":
    print(f"Part 1 solution: {part1()}")
    print(f"Part 2 solution: {part2()}")