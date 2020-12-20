import copy
import math

def part1(tiles):
    # the corner pieces will only have one matching top / bottom edge
    corners = []
    edges = [] # all possible flips and rotations

    solution = 1

    for tile in tiles.values():
        #print("tile: ", tile)
        l = [row[0] for row in tile]
        lr = l[::-1]
        r = [row[-1] for row in tile]
        rr = r[::-1]
        t = tile[0]
        tr = t[::-1]
        b = tile[-1]
        br = b[::-1]
        edges.extend([l, lr, r, rr, t, tr, b, br])

    num_unmatched = {} # number of panels with <key> unmatched edges
    num_edge_matches = {} # number of matches each edge has in the universal edge set (1 = external, 2 = conclusive internal, 3 = inconclusive internal)

    for ID, tile in tiles.items():
        l = [row[0] for row in tile]
        t = list(tile[0])
        r = [row[-1] for row in tile]
        b = list(tile[-1])
        unmatched = 0
        for edge in [l,t,r,b]:
            matches = edges.count(edge)
            num_edge_matches[matches] = num_edge_matches.get(matches, 0) + 1
            if matches == 1:
                unmatched += 1
        if unmatched == 2:
            solution *= int(ID)
        num_unmatched[unmatched] = num_unmatched.get(unmatched, 0) + 1

    # print(num_unmatched) # we have exactly 40 edges, 4 corners and 100 internal squares
    # print(num_edge_matches) # there are 48 edges without a match (12 / side)
    # thus we know that there is a single 12x12 layout which satisfies this

    return solution

def rotate_ccw(tile):
    new = []
    for col in range(len(tile[0])):
        new.append([row[-(col+1)] for row in tile])
    return new

def mirror(tile):
    new = []
    for row in tile:
        new.append(row[::-1])
    return new

def get_top_left_corner_tile(tiles):
    edges = []
    for tile in tiles.values():
        l = [row[0] for row in tile]
        lr = l[::-1]
        r = [row[-1] for row in tile]
        rr = r[::-1]
        t = tile[0]
        tr = t[::-1]
        b = tile[-1]
        br = b[::-1]
        edges.extend([l, lr, r, rr, t, tr, b, br])
    # if a tile has an edge-match, it should be present in edges 16 times (to account for all rotations)
    # if a tile does not have an edge-match (outside edge) it should be present in edges 8 times.
    for ID, tile in tiles.items():
        l = [row[0] for row in tile]
        r = [row[-1] for row in tile]
        t = tile[0]
        b = tile[-1]
        if edges.count(l) == 8 and edges.count(t) == 8 and edges.count(r) == 16 and edges.count(b) == 16:
            return ID

def get_transformed_variants(ID, tile):
    variants = {}
    for i in range(4):
        tile_modified = tile
        title = str(ID) + 'o'
        for j in range(i):
            tile_modified = rotate_ccw(tile_modified)
            title += 'r'
        variants[title] = tile_modified
    for i in range(4):
        tile_modified = mirror(tile)
        title = str(ID) + 'm'
        for j in range(i):
            tile_modified = rotate_ccw(tile_modified)
            title += 'r'
        variants[title] = tile_modified
    return variants

def find_snakes(image):
    # find all occurences of a 'snake'
    # check every spot in the image to see if is the top left pixel of a snake

    snake_template = [
                    ['.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','#','.'],
                    ['#','.','.','.','.','#','#','.','.','.','.','#','#','.','.','.','.','#','#','#'],
                    ['.','#','.','.','#','.','.','#','.','.','#','.','.','#','.','.','#','.','.','.']
                ]

    count = 0

    for y in range(len(image) - len(snake_template) + 1):
        for x in range(len(image[0])  - len(snake_template[0]) + 1):
            is_snake = True
            for snake_y in range(len(snake_template)):
                for snake_x in range(len(snake_template[0])):
                    if snake_template[snake_y][snake_x] == "#":
                        if image[y + snake_y][x+snake_x] != "#":
                            is_snake = False
            if is_snake:
                count += 1

    return count


def part2(tiles):

    # pre-compute all transformed variants of each tile
    # start with a random corner at a random orientation 
    transformed_tiles = {}
    for ID, tile in tiles.items():
        transformed_tiles.update(get_transformed_variants(ID, tile))

    remaining_tiles = copy.deepcopy(transformed_tiles)

    # find the 'top left' tile-variant (is a corner, has matches on bottom and right)
    # this determines the orientation of every other tile
    top_left = get_top_left_corner_tile(transformed_tiles)
    top_left_base_id = top_left[:4]

    # remove all variants of the tile we've used from the remaining tiles
    for tile in list(remaining_tiles):
        if tile.startswith(top_left_base_id): del remaining_tiles[tile]

    # initialize our mapping with the top left corner
    tiles_per_side = int(math.sqrt(len(tiles)))
    mapping = [['' for i in range(tiles_per_side)] for i in range(tiles_per_side)]
    mapping[0][0] = top_left

    # complete the top row by matching right edge to left edge:
    for i in range(1,tiles_per_side):
        edge_tile = mapping[0][i-1]
        exposed_edge = [row[-1] for row in transformed_tiles[edge_tile]]
        next_tile = ''
        for tile in remaining_tiles:
            if [row[0] for row in remaining_tiles[tile]] == exposed_edge:
                next_tile = tile
                break
        mapping[0][i] = next_tile
        for tile in list(remaining_tiles):
            if tile.startswith(next_tile[:4]): del remaining_tiles[tile]

    # complete all the other rows by matching the top edge to the bottom edge above
    for row in range(1,tiles_per_side):
        for col in range(tiles_per_side):
            edge_tile = mapping[row-1][col]
            exposed_edge = transformed_tiles[edge_tile][-1]
            next_tile = ''
            for tile in remaining_tiles:
                if remaining_tiles[tile][0] == exposed_edge:
                    next_tile = tile
                    break
            mapping[row][col] = next_tile
            for tile in list(remaining_tiles):
                if tile.startswith(next_tile[:4]): del remaining_tiles[tile]

    # now mapping represents the correct transformed tile for each position
    # lets build the actual map
    edge_length = len(mapping) * len(transformed_tiles[mapping[0][0]])
    map = [['' for i in range(edge_length)] for i in range(edge_length)]
    for row in range(len(mapping)):
        for col in range(len(mapping[0])):
            tile_id = mapping[row][col]
            tile = transformed_tiles[tile_id]
            for tile_row in range(len(tile)):
                for tile_col in range(len(tile[0])):
                    y = row*len(tile) + tile_row
                    x = col*len(tile) + tile_col
                    map[y][x] = tile[tile_row][tile_col]

    # building the map without borders
    tile_size = len(tile)
    trimmed_map = []
    for i in range(len(map)):
        if i % tile_size == 0 or i % tile_size == tile_size-1:
            continue
        trimmed_row = []
        for j in range(len(map[i])):
            if j % tile_size == 0 or j % tile_size == tile_size-1:
                continue
            trimmed_row.append(map[i][j])
        trimmed_map.append(trimmed_row)

    num_waves = 0
    for row in trimmed_map:
        num_waves += row.count("#")
    
    for i in range(4):
        image = trimmed_map
        for rotate in range(i):
            image = rotate_ccw(image)
        flipped = mirror(image)
        if find_snakes(image) != 0:
            return num_waves - find_snakes(image)*15

if __name__ == "__main__":
    
    with open('20/input.txt') as inputfile:
        inputlines = inputfile.read().split("\n\n")
    tiles = {}
    for tile in inputlines:
        ID = int(tile[5:9])
        tiles[ID] = [list(row) for row in tile.split("\n")[1:]]

    sample = [[1,2], [3,4]]
    assert rotate_ccw(sample) == [[2,4], [1,3]]
    assert mirror(sample) == [[2,1], [4,3]]

    print(f"Part 1 solution: {part1(tiles)}")
    print(f"Part 2 solution: {part2(tiles)}")
