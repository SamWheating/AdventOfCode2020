with open('5/input.txt') as inputfile:
    seats = inputfile.read().split("\n")

# sample input:
# seats = ["BFFFBBFRRR", "FFFBBBFRRR", "BBFFBBFRLL"]

# parsing rows:
# BFFFBBF -> 70 (binary, F=0, B=1)
# parsing cols:
# RLL -> 4 (binary, R=1, L=0)

def part1():
    max = 0
    for seat in seats:
        row = int(seat[:7].replace("F", "0").replace("B", "1"), 2)
        col = int(seat[7:].replace("L", "0").replace("R", "1"), 2)
        seat_num = 8*row + col
        if seat_num > max:
            max = seat_num
    return max

            
def part2():
    seat_nums = []
    for seat in seats:
        row = int(seat[:7].replace("F", "0").replace("B", "1"), 2)
        col = int(seat[7:].replace("L", "0").replace("R", "1"), 2)
        seat_num = 8*row + col
        seat_nums.append(seat_num)

    seat_nums.sort()
    
    for i in range(1, len(seat_nums)):
        if seat_nums[i]-2 == seat_nums[i-1]:
            return seat_nums[i]-1


if __name__ == "__main__":
    print(f"Part 1 solution: {part1()}")
    print(f"Part 2 solution: {part2()}")
