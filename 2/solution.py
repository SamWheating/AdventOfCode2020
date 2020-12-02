with open('2/input.txt') as inputfile:
    inputlines = inputfile.read().split("\n")
    parsed = []
    for line in inputlines:
        low = int(line.split("-")[0])
        high = int(line.split("-")[1].split(" ")[0])
        letter = line.split(" ")[1][:-1]
        password = line.split(":")[1][1:]
        parsed.append({
            "low": low,
            "high": high,
            "password": password,
            "letter": letter
        })

def validate_part1(data):
    occurences = data["password"].count(data["letter"])
    if occurences > data["high"]:
        return False
    if occurences < data["low"]:
        return False
    return True

def validate_part2(data):
    first_letter = data["password"][data["low"]-1]
    second_letter = data["password"][data["high"]-1]
    if [first_letter, second_letter].count(data["letter"]) == 1:
        return True
    return False

def part1():
    valid = 0
    for data in parsed:
        if validate_part1(data):
            valid += 1

    return valid

def part2():
    valid = 0
    for data in parsed:
        if validate_part2(data):
            valid += 1

    return valid

if __name__ == "__main__":
    print(f"Part 1 solution: {part1()}")
    print(f"Part 2 solution: {part2()}")
