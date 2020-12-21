import copy
import math

def part1(inputlines):
    allergen_map = {}  # make a mapping of alergens to all possible ingredients
    all_ingredients = set()
    for line in inputlines:
        allergens = line.split("(contains ")[1][:-1].split(", ")
        ingredients = line.split(" (contains")[0].split(" ")
        all_ingredients.update(ingredients)
        for allergen in allergens:
            if allergen in allergen_map:
                allergen_map[allergen].append(set(ingredients))
            else:
                allergen_map[allergen] = [set(ingredients)]
        print(allergens)
    unresolved_ingredient_map = {} # maps allergen to possible ingredients
    resolved_ingredient_map = {}
    for allergen in allergen_map:
        possible_ingredients = allergen_map[allergen][0]
        for i in range(1, len(allergen_map[allergen])):
            possible_ingredients = possible_ingredients & allergen_map[allergen][i]
        unresolved_ingredient_map[allergen] = possible_ingredients

    while True:
        for allergen, ingredients in unresolved_ingredient_map.items():
            if len(ingredients) == 1:
                ingredient = list(ingredients)[0]
                resolved_ingredient_map[allergen] = ingredient
                for a in unresolved_ingredient_map:
                    unresolved_ingredient_map[a].discard(ingredient)
                break
        if len(resolved_ingredient_map) == len(unresolved_ingredient_map):
            break

    # now we know exactly which allergens in which ingredient
    print(resolved_ingredient_map)
    # print(all_ingredients)
    unsafe_ingredients = list(resolved_ingredient_map.values())
    safe_ingredients = set([ingredient for ingredient in all_ingredients if ingredient not in unsafe_ingredients])

    count = 0
    for line in inputlines:
        ingredients = line.split(" (contains")[0].split(" ")
        for ingredient in ingredients:
            if ingredient in safe_ingredients:
                count += 1

    return count


def part2(inputlines):
    allergen_map = {}  # make a mapping of alergens to all possible ingredients
    all_ingredients = set()
    for line in inputlines:
        allergens = line.split("(contains ")[1][:-1].split(", ")
        ingredients = line.split(" (contains")[0].split(" ")
        all_ingredients.update(ingredients)
        for allergen in allergens:
            if allergen in allergen_map:
                allergen_map[allergen].append(set(ingredients))
            else:
                allergen_map[allergen] = [set(ingredients)]
        print(allergens)
    unresolved_ingredient_map = {} # maps allergen to possible ingredients
    resolved_ingredient_map = {}
    for allergen in allergen_map:
        possible_ingredients = allergen_map[allergen][0]
        for i in range(1, len(allergen_map[allergen])):
            possible_ingredients = possible_ingredients & allergen_map[allergen][i]
        unresolved_ingredient_map[allergen] = possible_ingredients

    while True:
        for allergen, ingredients in unresolved_ingredient_map.items():
            if len(ingredients) == 1:
                ingredient = list(ingredients)[0]
                resolved_ingredient_map[allergen] = ingredient
                for a in unresolved_ingredient_map:
                    unresolved_ingredient_map[a].discard(ingredient)
                break
        if len(resolved_ingredient_map) == len(unresolved_ingredient_map):
            break
    
    allergens_sorted = sorted(list(resolved_ingredient_map.keys()))
    print(allergens_sorted)
    solution = ",".join(resolved_ingredient_map[allergen] for allergen in allergens_sorted)
    return solution

if __name__ == "__main__":
    
    with open('21/input.txt') as inputfile:
        inputlines = inputfile.read().split("\n")

    print(f"Part 1 solution: {part1(inputlines)}")
    print(f"Part 2 solution: {part2(inputlines)}")
