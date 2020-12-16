def part1(inputlines):
    # construct a master set of all valid numbers
    rules = inputlines[:inputlines.index("your ticket:")-1]
    valid_number = set()
    for rule in rules:
        valids = rule.split(": ")[1].split(" ")[0]
        for i in range(int(valids.split("-")[0]), int(valids.split("-")[1])+1):
            valid_number.add(i)
        valids = rule.split("or ")[1]
        for i in range(int(valids.split("-")[0]), int(valids.split("-")[1])+1):
            valid_number.add(i)
    
    # validate all tickets:
    nearby = inputlines[inputlines.index("nearby tickets:")+1:]
    errors = 0
    for ticket in nearby:
        for number in [int(num) for num in ticket.split(",")]:
            if number not in valid_number:
                errors += number
    return errors


def part2(inputlines):

    # first we'll build a list of rules which satisfy all tickets in general
    # as well as a mapping from rule name to a list of all acceptable values
    raw_rules = inputlines[:inputlines.index("your ticket:")-1]
    rules = {} # mapping of field name to set{valid numbers}
    valid_number = set()
    for rule in raw_rules:
        name = rule.split(":")[0]
        rules[name] = set()
        valids = rule.split(": ")[1].split(" ")[0]
        for i in range(int(valids.split("-")[0]), int(valids.split("-")[1])+1):
            valid_number.add(i)
            rules[name].add(i)
        valids = rule.split("or ")[1]
        for i in range(int(valids.split("-")[0]), int(valids.split("-")[1])+1):
            valid_number.add(i)
            rules[name].add(i)
        
    # obtain a list of "valid" tickets:
    nearby = inputlines[inputlines.index("nearby tickets:")+1:]
    valid_tickets = []
    for ticket in nearby:
        valid = True
        for number in [int(num) for num in ticket.split(",")]:
            if number not in valid_number:
                valid = False
        if valid:
            valid_tickets.append([int(num) for num in ticket.split(",")])

    # find which columns satisfy which rules:
    satisfied = {}
    for rule in rules:
        satisfied[rule] = []
        for col in range(len(valid_tickets[0])):
            valid = True
            for row in range(len(valid_tickets)):
                if valid_tickets[row][col] not in rules[rule]:
                    valid = False
                    break
            if valid:
                satisfied[rule].append(col)
    
    # use process of elimination to find which column corresponds to which rule
    rule_mapping = {} # maps rule to column ex {arrival_location: 2, wagon: 1}
    while True:
        for rule in satisfied:
            if len(satisfied[rule]) == 1:
                decided = satisfied[rule][0]
                rule_mapping[rule] = decided
        for rule in satisfied:
            if decided in satisfied[rule]:
                satisfied[rule].remove(decided)
        if len(rule_mapping) == len(rules):
            break
    
    # find the product of all "departure_{x}" fields on our ticket 
    my_ticket = inputlines[inputlines.index("your ticket:")+1]
    my_ticket = [int(num) for num in my_ticket.split(",")]

    solution = 1
    for rule in rule_mapping:
        if rule.startswith("departure"):
            solution *= my_ticket[rule_mapping[rule]]

    return solution
    

if __name__ == "__main__":
    
    with open('16/input.txt') as inputfile:
        inputlines = inputfile.read().split("\n")

    print(f"Part 1 solution: {part1(inputlines)}")
    print(f"Part 2 solution: {part2(inputlines)}")