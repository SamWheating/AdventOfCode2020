with open('7/input.txt') as inputfile:
    rows = inputfile.read().split("\n")

def part1():
    rules = []
    for row in rows:
        words = row.split(" ")
        outer = words[0] + words[1]
        inners = []
        for i in range(3, len(words)):
            if words[i][:3] == "bag":
                inners.append(words[i-2]+words[i-1])
        rules.append({"inner": inners, "outer": outer})
    inner = {"shinygold"}
    while True:
        firstsize = len(inner)
        old_inner = list(inner)
        for rule in rules:
            for inner_bag in old_inner:
                if inner_bag in rule["inner"]:
                    inner.add(rule["outer"])
        if len(inner) == firstsize:
            return len(inner)-1
          
def part2():
    recipes = {}  # unresolved bags (unknown size) and they're makeup ex. {"blue": {"red": 1, "yellow": 2}}
    bag_sizes = {}  # resolved bags (known size) and their size ex: {"blue": 6, "yellow": 9}
    for row in rows:
        words = row.split(" ")
        if words[-2] == "other":
            bag_sizes["".join(words[:2])] = 1
        else:
            outer = "".join(words[:2])
            recipes[outer] = {}
            for i in range(3, len(words)):
                if words[i][:3] == "bag":
                    type = "".join(words[i-2]+words[i-1])
                    count = int(words[i-3])
                    recipes[outer][type] = count
    while True:
        for bag in recipes:
            ingredients = recipes[bag].keys()
            if set(recipes[bag].keys()).issubset(set(bag_sizes.keys())): # can we resovle this one?
                size = 1    # the size of the outer bag
                for ingredient in recipes[bag]: # the total size of all the inner bags
                    size += (bag_sizes[ingredient]*recipes[bag][ingredient])
                bag_sizes[bag] = size
        
        # check if we're done
        if "shinygold" in bag_sizes:
            return bag_sizes["shinygold"] - 1

        # removed resolved entries from recipes
        for bag in bag_sizes:
            if bag in recipes:
                del recipes[bag]

if __name__ == "__main__":
    print(f"Part 1 solution: {part1()}")
    print(f"Part 2 solution: {part2()}")
