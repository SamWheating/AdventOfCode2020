
# evaluates an equation with no brackets form left to right
# ex. eval_eq([1, '+', 2]) -> 3 
def eval_eq_1(equation):
    if len(equation) == 1:
        return int(equation[0])
    if equation[1] == '*':
        new_eq = [int(equation[0]) * int(equation[2])]
        new_eq.extend(equation[3:])
        return eval_eq_1(new_eq)
    if equation[1] == '+':
        new_eq = [int(equation[0]) + int(equation[2])]
        new_eq.extend(equation[3:])
        return eval_eq_1(new_eq)

# evaluates an equation with no brackets form left to right
# but with all additions performed before any multiplications
# ex. eval_eq([5, '*', 1, '+', 2]) -> 15
def eval_eq_2(equation):
    print(equation)
    if len(equation) == 1:
        return int(equation[0])
    elif "+" in equation:
        first = equation.index("+")-1
        second = first + 2 
        sum = int(equation[first]) + int(equation[second])
        new_equation = equation[:first] + [sum] + equation[second+1:]
        return eval_eq_2(new_equation)
    elif equation[1] == '*':
        new_eq = [int(equation[0]) * int(equation[2])]
        new_eq.extend(equation[3:])
        return eval_eq_2(new_eq)

# Solves a long expression recursively by solving innermost parantheses on each iteration
def solve(equation, eval_method):
    print(f"solving {equation}")
    if ")" not in equation:
        return eval_method(equation)
    end = equation.index(")")
    start = end
    while equation[start] != "(":
        start -= 1
    new_equation = equation[:start] + [eval_method(equation[start+1:end])] + equation[end+1:]
    print(new_equation)
    return solve(new_equation, eval_method)

def part1(inputlines):
    total = 0
    for line in inputlines:
        total += solve(list(line.replace(" ", "")), eval_eq_1)
    return total

def part2(inputlines):
    total = 0
    for line in inputlines:
        total += solve(list(line.replace(" ", "")), eval_eq_2)
    return total

if __name__ == "__main__":
    
    with open('18/input.txt') as inputfile:
        inputlines = inputfile.read().split("\n")

    print(f"Part 1 solution: {part1(inputlines)}")
    print(f"Part 2 solution: {part2(inputlines)}")
