def find_allergens(inputlines):

    allergen_map = {}  # make a mapping of allergens to all possible ingredients
    for line in inputlines:
        allergens = line.split("(contains ")[1][:-1].split(", ")
        ingredients = line.split(" (contains")[0].split(" ")
        for allergen in allergens:
            if allergen in allergen_map:
                allergen_map[allergen].append(set(ingredients))
            else:
                allergen_map[allergen] = [set(ingredients)]

    unresolved_ingredient_map = {} # maps allergen to possible ingredients
    resolved_ingredient_map = {} # maps allergen to ingredients

    # find the intersection of ingredients for every recipe which contains this allergen
    for allergen in allergen_map:
        possible_ingredients = allergen_map[allergen][0]
        for i in range(1, len(allergen_map[allergen])):
            possible_ingredients = possible_ingredients & allergen_map[allergen][i]
        unresolved_ingredient_map[allergen] = possible_ingredients

    # iteratively solve mapping between ingredients and allergens
    while True:
        for allergen, ingredients in unresolved_ingredient_map.items():
            if len(ingredients) == 1:
                ingredient = list(ingredients)[0]
                resolved_ingredient_map[allergen] = ingredient
                for a in unresolved_ingredient_map:
                    unresolved_ingredient_map[a].discard(ingredient)
                break
        if len(resolved_ingredient_map) == len(unresolved_ingredient_map):
            return resolved_ingredient_map


def part1(inputlines):

    unsafe_ingredients = list(find_allergens(inputlines).values())

    count = 0
    for line in inputlines:
        ingredients = line.split(" (contains")[0].split(" ")
        count += len([a for a in ingredients if a not in unsafe_ingredients])

    return count


def part2(inputlines):
    
    resolved_ingredient_map = find_allergens(inputlines)
    allergens_sorted = sorted(list(resolved_ingredient_map.keys()))
    solution = ",".join(resolved_ingredient_map[allergen] for allergen in allergens_sorted)
    return solution

if __name__ == "__main__":
    
    with open('21/input.txt') as inputfile:
        inputlines = inputfile.read().split("\n")

    print(f"Part 1 solution: {part1(inputlines)}")
    print(f"Part 2 solution: {part2(inputlines)}")
