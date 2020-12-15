def part1(numbers, target):
    seen = {} # the last time we saw each number
    count_seen = {} # the number of times we've seen each number
    for number in numbers:
        seen[number] = numbers.index(number)
        count_seen[number] = 1
    step = len(numbers)
    last = numbers[-1]
    while True:
        if count_seen[last] == 1:
            new = 0 # first time seeing
        else:
            new = max((step-1) - seen[last],1)
        #print(step, new, seen)
        if new in count_seen:
            count_seen[new] += 1
        else:
            count_seen[new] = 1 
        seen[last] = step-1
        step += 1
        if step == target:
            return new
        last = new

if __name__ == "__main__":
    
    inputlines = [9,3,1,0,8,4]

    print(f"Part 1 solution: {part1(inputlines, 2020)}")
    print(f"Part 2 solution: {part1(inputlines, 30000000)}")