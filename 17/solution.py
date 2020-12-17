def surrounding_3d(cubes, coord):
    """
    counts the active cubes immediately surrounding a cube.
    cubes is a set of 3d tuples, coordinate is a single 3d tuple (x,y,z)
    """
    count = 0
    cx,cy,cz = coord
    for x in [cx-1, cx, cx+1]:
        for y in [cy-1, cy, cy+1]:
            for z in [cz-1, cz, cz+1]:
                if (x,y,z) == coord: continue
                elif (x,y,z) in cubes: count += 1
    return count

def surrounding_4d(cubes, coord):
    """
    counts the active cubes immediately surrounding a cube.
    cubes is a set of 4d tuples, coordinate is a single 4d tuple (x,y,z,w)
    """
    count = 0
    cx,cy,cz,cw = coord
    for x in [cx-1, cx, cx+1]:
        for y in [cy-1, cy, cy+1]:
            for z in [cz-1, cz, cz+1]:
                for w in [cw-1, cw, cw+1]: 
                    if (x,y,z,w) == coord: continue
                    elif (x,y,z,w) in cubes: count += 1
    return count

def print_board_3d(cubes):
    x_min = min([cube[0] for cube in cubes])
    x_max = max([cube[0] for cube in cubes])
    y_min = min([cube[1] for cube in cubes])
    y_max = max([cube[1] for cube in cubes])
    z_min = min([cube[2] for cube in cubes])
    z_max = max([cube[2] for cube in cubes])
    for z in range(z_min, z_max+1):
        print(f"z = {z}")
        for y in range(y_min, y_max+1):
            row = ""
            for x in range(x_min, x_max+1):
                if (x,y,z) in cubes: row += "#"
                else: row += "."
            print(row)
        print("\n")
    print("\n")

def part1(inputlines):
    cubes = set()
    for y, row in enumerate(inputlines):
        for x, letter in enumerate(row):
            if letter == "#":
                cubes.add((x,y,0))

    #print_board_3d(cubes)

    for i in range(6):
        new_cubes = set()
        for x in range(min([cube[0] for cube in cubes])-1, max([cube[0] for cube in cubes])+2):
            for y in range(min([cube[1] for cube in cubes])-1, max([cube[1] for cube in cubes])+2):
                for z in range(min([cube[2] for cube in cubes])-1, max([cube[2] for cube in cubes])+2):
                    count = surrounding_3d(cubes, (x,y,z))
                    if (x,y,z) in cubes:
                        if count == 2:
                            new_cubes.add((x,y,z))
                    if count == 3:
                        new_cubes.add((x,y,z))
        cubes = new_cubes
        #print_board_3d(cubes)
    
    return len(cubes)

def part2(inputlines):
    cubes = set()
    for y, row in enumerate(inputlines):
        for x, letter in enumerate(row):
            if letter == "#":
                cubes.add((x,y,0,0))

    for i in range(6):
        new_cubes = set()
        for x in range(min([cube[0] for cube in cubes])-1, max([cube[0] for cube in cubes])+2):
            for y in range(min([cube[1] for cube in cubes])-1, max([cube[1] for cube in cubes])+2):
                for z in range(min([cube[2] for cube in cubes])-1, max([cube[2] for cube in cubes])+2):
                    for w in range(min([cube[3] for cube in cubes])-1, max([cube[3] for cube in cubes])+2):
                        count = surrounding_4d(cubes, (x,y,z,w))
                        if (x,y,z,w) in cubes:
                            if count == 2:
                                new_cubes.add((x,y,z,w))
                        if count == 3:
                            new_cubes.add((x,y,z,w))
        cubes = new_cubes
    
    return len(cubes)

if __name__ == "__main__":
    
    with open('17/input.txt') as inputfile:
        inputlines = inputfile.read().split("\n")

    print(f"Part 1 solution: {part1(inputlines)}")
    print(f"Part 2 solution: {part2(inputlines)}")