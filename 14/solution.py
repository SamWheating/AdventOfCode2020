from copy import copy

# Returns an integer with a mask applied as per part 1
def apply_mask_1(mask, value):
    value = list('{0:036b}'.format(value))
    for i, letter in enumerate(mask):
        if letter in ["0", "1"]:
            value[i] = letter
    return int("".join(value), 2)

# Returns a "masked memory address" (a list of "1"s, "0"s and "X"s)
# as per part 2
def apply_mask_2(mask, value):
    value = list('{0:036b}'.format(value))
    for i, letter in enumerate(mask):
        if letter in ["1", "X"]:
            value[i] = letter
    return value

# takes a "masked memory address" (a list of "1"s, "0"s and "X"s) and recursively
# expands every possible address based on X being either "0" or "1".
# ex input: get_addresses(["0", "X", "X", "1"]) -> [1,3,5,7]
def expand_address(address):
    if address.count("X") == 0:
        return [int("".join(address), 2)]
    else:
        idx = address.index("X")
        a0 = copy(address)
        a1 = copy(address)
        a0[idx] = "0"
        a1[idx] = "1"
        result = []
        result.extend(expand_address(a0))
        result.extend(expand_address(a1))
        return result

def part1(inputlines):
    memory = {}
    mask = ""
    for line in inputlines:
        if line.split(" = ")[0] == "mask":
            mask = line.split(" = ")[1]
        else:
            address = int(line[line.index("[")+1:line.index("]")])
            value = int(line.split(" = ")[1])
            memory[address] = apply_mask_1(mask, value)
    return sum(memory.values())

def part2(inputlines):
    memory = {}
    mask = ""
    for line in inputlines:
        if line.split(" = ")[0] == "mask":
            mask = line.split(" = ")[1]
        else:
            value = int(line.split(" = ")[1])
            address = int(line[line.index("[")+1:line.index("]")])
            address = apply_mask_2(mask, address)
            addresses = expand_address(address)
            for address in addresses:
                memory[address] = value
    return sum(memory.values())

if __name__ == "__main__":
    
    with open('14/input.txt') as inputfile:
        inputlines = inputfile.read().split("\n")

    print(f"Part 1 solution: {part1(inputlines)}")
    print(f"Part 2 solution: {part2(inputlines)}")