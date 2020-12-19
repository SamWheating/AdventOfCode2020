import copy

# every "rule" represents a list of possible values
# so we can iteratively "resolve" rules into their list of acceptable values
def resolve_rules(rules):
    rules = copy.copy(rules)

    resolved_rules = {} # dict of rule : set(possible results)
    for rule in list(rules.keys()):
        if rules[rule] in ["\"a\"", "\"b\""]:
            resolved_rules[rule] = {rules[rule][1:-1]}
            del rules[rule]
    while len(rules) > 0:
        for rule in list(rules.keys()):

            # check if the rule is resolvable
            components = rules[rule].replace(" |", "").split(" ")
            if not all([component in resolved_rules for component in components]):
                continue

            # if we're here then the rule can be resolved with existing knowledge:
            if "|" in rules[rule].split(" "):
                divider = rules[rule].split(" ").index("|")
                combinations = [rules[rule].split(" ")[:divider], rules[rule].split(" ")[divider+1:]]
            else:
                combinations = [components]

            values = set()

            for combination in combinations:
                if len(combination) == 1:
                    values.update(resolved_rules[combination[0]])
                    continue
                for a in resolved_rules[combination[0]]:
                    for b in resolved_rules[combination[1]]:
                        values.add(a+b)

            resolved_rules[rule] = values
            del rules[rule]

    return resolved_rules      

def part1(rules, codes):
    valid = resolve_rules(rules)['0']
    count = 0
    return len([code for code in codes if code in valid])

def part2(rules, codes):
    # Adding cycles:
    # 8: 42 | 42 8 -> 42 42 42 42 42 etc
    # 11: 42 31 | 42 11 31 -> 42 42 31 31 etc
    # rules 8 and 11 are only used in rule 0 (8 11)
    # thus every valid code will be x strings from rule 42, followed by y strings from rule 31 with x > y

    rules = resolve_rules(rules)
    count = 0

    for code in codes:

        if len(code) % 8 != 0:
            continue
        if len(code) < 24:
            continue

        chunks = []
        for i in range(int(len(code)/8)):
            chunks.append(code[i*8:(i+1)*8])
        count_42 = 0
        count_31 = 0
        for i in range(len(chunks)):
            if chunks[i] in rules['42']: count_42 += 1
            else: break
        for i in range(1, len(chunks)):
            if chunks[-i] in rules['31']: count_31 += 1
            else: break
        if count_42 + count_31 >= len(chunks) and count_42 > count_31 and count_31 > 0:
            count += 1

    return count


if __name__ == "__main__":
    
    with open('19/input.txt') as inputfile:
        inputlines = inputfile.read().split("\n")
    
    rules = inputlines[:inputlines.index("")]
    parsed_rules = {}
    for rule in rules:
        parsed_rules[rule.split(": ")[0]] = rule.split(": ")[1]

    codes = inputlines[inputlines.index(""):]

    print(f"Part 1 solution: {part1(parsed_rules, codes)}")
    print(f"Part 2 solution: {part2(parsed_rules, codes)}")
