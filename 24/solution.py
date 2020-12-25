import copy

def flip_tiles(tiles):
    flipped = set()
    for tile in tiles:
        ne = 0
        e = 0
        # based on
        # https://catlikecoding.com/unity/tutorials/hex-map/part-1/hexagonal-coordinates/axial-diagram.png
        for move in tile:
            if move == 'nw':
                ne += 1
                e -= 1
            if move == 'se':
                ne -= 1
                e += 1
            if move == 'w': e -= 1
            if move == 'e': e += 1
            if move == 'ne': ne += 1
            if move == 'sw': ne -= 1
        tile = (e, ne)
        if tile in flipped:
            flipped.remove(tile)
        else:
            flipped.add(tile)
    return flipped


def part1(tiles):
    return len(flip_tiles(tiles))

def adjacent_tiles(tiles, coord):
    adjacent = 0
    neighbours = [(1,0), (1,-1), (0,-1), (-1,0), (-1,1), (0,1)]
    for neighbour in neighbours:
        if (coord[0] + neighbour[0], coord[1] + neighbour[1]) in tiles:
            adjacent += 1
    return adjacent

def part2(tiles):
    # tiles is now just a set of coords in which the tiles have flipped
    tiles = flip_tiles(tiles)
    for i in range(100):
        new_tiles = set()
        max_e = max([item[0] for item in tiles])
        min_e = min([item[0] for item in tiles])
        max_ne = max([item[1] for item in tiles])
        min_ne = min([item[1] for item in tiles])
        for e in range(min_e-1, max_e+2):
            for ne in range(min_ne-1, max_ne+2):
                coord = (e, ne)
                adjacent = adjacent_tiles(tiles, coord)
                if coord in tiles:
                    if adjacent in [1,2]: new_tiles.add(coord)
                else:
                    if adjacent == 2: new_tiles.add(coord)
        tiles = new_tiles
    return len(tiles)


def parseline(line):
    tile = []
    while len(line) > 0:
        if line[0] in ['s', 'n']:
            tile.append(line[:2])
            line = line[2:]
        elif line[0] in ['e', 'w']:
            tile.append(line[0])
            line = line[1:]
        else:
            raise Exception
    return tile
        

if __name__ == "__main__":
    
    with open('24/input.txt') as inputfile:
        inputlines = inputfile.read().split("\n")
        tiles = [parseline(line) for line in inputlines]


    print(f"Part 1 solution: {part1(tiles)}")
    print(f"Part 2 solution: {part2(tiles)}")