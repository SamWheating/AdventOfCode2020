with open('1/input.txt') as inputfile:
    inputlines = inputfile.read().split("\n")
    numbers = [int(number) for number in inputlines]

# Part 1
def part1():
    for number1 in numbers:
        for number2 in numbers:
                if number1 + number2 == 2020:
                    return number1*number2

# Part 2
def part2():
    for number1 in numbers:
        for number2 in numbers:
            for number3 in numbers:
                if number1 + number2 + number3 == 2020:
                    return number1*number2*number3

if __name__ == "__main__":
    print(f"Part 1 solution: {part1()}")
    print(f"Part 2 solution: {part2()}")
