import math

with open('12/input.txt') as inputfile:
    inputlines = inputfile.read().split("\n")

# using EAST-NORTH coordinates
DIRECTIONS = {"N": [0,1], "S": [0,-1], "E": [1,0], "W": [-1,0]}

def part1():
    # order of bearings while turning right:
    bearings = ["E", "S", "W", "N"]
    bearing = "E"
    position = [0,0]
    for instruction in inputlines:
        letter = bearing if instruction[0] == "F" else instruction[0]
        number = int(instruction[1:])
        if letter in DIRECTIONS:
            position = [position[i] + number*DIRECTIONS[letter][i] for i in [0,1]]
        else:
            turns = (number / 90) if letter == "R" else -(number / 90)
            bearing = bearings[int((bearings.index(bearing) + turns)) % 4]
    return abs(position[0]) + abs(position[1])

# helper to perform a 2d clockwise rotation of a coordinate
def rotate(coordinate, degrees):
    rad = math.radians(degrees)
    return [
        round(math.cos(rad) * coordinate[0] + math.sin(rad) * coordinate[1]),
        round(-math.sin(rad) * coordinate[0] + math.cos(rad) * coordinate[1])
    ]

def part2():
    position = [0,0]
    waypoint = [10, 1]
    for instruction in inputlines:
        letter = instruction[0]
        number = int(instruction[1:])
        if letter == "F": 
            position = [position[i] + number * waypoint[i] for i in [0,1]]
        elif letter in DIRECTIONS:
            waypoint = [waypoint[i] + number*DIRECTIONS[letter][i] for i in [0,1]]
        else:
            if letter == "L": number *= -1 # counterclockwise = negative clockwise
            waypoint = rotate(waypoint, number)
    return abs(position[0]) + abs(position[1])

if __name__ == "__main__":
    print(f"Part 1 solution: {part1()}")
    print(f"Part 2 solution: {part2()}")
