#with open('8/sample_input.txt') as inputfile:
with open('8/input.txt') as inputfile:
    inputlines = inputfile.read().split("\n")

# Part 1
def part1():
    accumulator = 0
    position = 0
    visited = set()
    while True:
        if position in visited:
            return accumulator
        visited.add(position)
        command = inputlines[position].split(" ")[0]
        number =  int(inputlines[position].split(" ")[1])
        if command == "acc":
            accumulator += number
            position += 1
            continue
        elif command == "jmp":
            position += number
            continue
        elif command == "nop":
            position += 1
            continue

# Part 2
def part2():
    # mutate one line of the program
    for spot in range(len(inputlines)):
        if inputlines[spot][:3] == "nop":
            inputlines[spot] = "jmp" + inputlines[spot][3:]
        elif inputlines[spot][:3] == "jmp":
             inputlines[spot] = "nop" + inputlines[spot][3:]
        else:
            continue

        accumulator = 0
        position = 0
        for i in range(len(inputlines)): # max of this many runs
            if position == len(inputlines):
                return accumulator
            command = inputlines[position].split(" ")[0]
            number =  int(inputlines[position].split(" ")[1])
            if command == "acc":
                accumulator += number
                position += 1
                continue
            elif command == "jmp":
                position += number
                continue
            elif command == "nop":
                position += 1
                continue

        # revert the earlier mutation
        if inputlines[spot][:3] == "nop":
            inputlines[spot] = "jmp" + inputlines[spot][3:]
        elif inputlines[spot][:3] == "jmp":
             inputlines[spot] = "nop" + inputlines[spot][3:]

if __name__ == "__main__":
    print(f"Part 1 solution: {part1()}")
    print(f"Part 2 solution: {part2()}")
