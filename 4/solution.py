with open('4/input.txt') as inputfile:
    inputlines = inputfile.read().split("\n\n")
    parsed_input = [line.replace("\n", " ") for line in inputlines]
    print(parsed_input[0])

def part1():
    count = 0
    for passport in parsed_input:
        valid = 1
        terms = [item.split(":")[0] for item in passport.split(" ")]
        for term in ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]:
            if term not in terms:
                valid = 0
                break
        count += valid
    return count
            
def part2():
    count = 0

    passports = []

    # parse list of passports and check for all fields
    for passport in parsed_input:
        valid = True
        terms = {item.split(":")[0]:item.split(":")[1] for item in passport.split(" ")}
        for term in ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]:
            if term not in terms:
                valid = False
                break
        if valid:
            passports.append(terms)
    
    # check fields for validity
    for passport in passports:
        try:
            if not 1920 <= int(passport["byr"]) <= 2002:
                continue
            if not 2010 <= int(passport["iyr"]) <= 2020:
                continue
            if not 2020 <= int(passport["eyr"]) <= 2030:
                continue
            if passport["hgt"][-2:] not in ["in", "cm"]:
                continue
            if passport["hgt"][-2:] == "cm":
                if not 150 <= int(passport["hgt"][0:3]) <= 193:
                    continue
            if passport["hgt"][-2:] == "in":
                if not 59 <= int(passport["hgt"][0:2]) <= 76:
                    continue
            if passport["hcl"][0] != "#":
                continue
            if len(passport["hcl"]) != 7:
                continue
            for letter in passport["hcl"][1:]:
                if letter not in list("1234567890abcdef"):
                    continue
            if passport["ecl"] not in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]:
                continue
            if len(passport["pid"]) != 9:
                continue
            for letter in passport["pid"][1:]:
                if letter not in list("1234567890"):
                    continue
        except Exception:
            continue
        count += 1
    
    return count

if __name__ == "__main__":
    print(f"Part 1 solution: {part1()}")
    print(f"Part 2 solution: {part2()}")