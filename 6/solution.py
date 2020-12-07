import string

with open('6/input.txt') as inputfile:
    groups = inputfile.read().split("\n\n")

def part1():
    count = 0
    for group in groups:
        count += len(set(group.replace("\n", "")))
    return count

def part2():
    count = 0
    for group in groups:
        intersection = set(string.ascii_lowercase)
        for person in group.split("\n"):
            intersection = intersection & set(person)
        count += len(intersection)
    return count

if __name__ == "__main__":
    print(f"Part 1 solution: {part1()}")
    print(f"Part 2 solution: {part2()}")
