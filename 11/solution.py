with open('11/input.txt') as inputfile:
    inputlines = inputfile.read().split("\n")

# Part 1
def part1():
    iter = 0
    board = [list(line) for line in inputlines]
    while True:
        newboard = [[0 for i in range(len(board[0]))] for j in range(len(board))]
        for row in range(len(board)):
            for col in range(len(board[0])):
                surrounding = 0
                # 3x3 conv summing filter (middle excluded)
                for row_offset in [-1,0,1]:
                    for col_offset in [-1, 0, 1]:
                        if (0 <= row + row_offset < len(board)) and (0 <= col + col_offset < len(board[0])) and not (row_offset == col_offset == 0):
                            if board[row+row_offset][col+col_offset] == "#":
                                surrounding += 1
                if board[row][col] == "L" and (surrounding == 0):
                    newboard[row][col] = "#"
                elif board[row][col] == "#" and (surrounding >= 4):
                    newboard[row][col] = "L"
                else:
                    newboard[row][col] = board[row][col]
        if board == newboard:
            count = 0
            for row in range(len(board)):
                for col in range(len(board[0])):
                    if board[row][col] == "#": 
                        count += 1
            return count
        board = newboard
        iter += 1

def first_chair(view):
    for chair in view:
        if chair == "#": return 1
        if chair == "L": return 0
    return 0

def part2():
    iter = 0
    board = [list(line) for line in inputlines]
    while True:
        newboard = [[0 for i in range(len(board[0]))] for j in range(len(board))]
        for row in range(len(board)):
            for col in range(len(board[0])):
                surrounding = 0
                
                # first chair to the right
                right = board[row][col+1:]
                surrounding += first_chair(right)

                # first chair to the left
                left = board[row][:col]
                left.reverse()
                surrounding += first_chair(left)

                #first chair up
                up = [board[i][col] for i in range(row)]
                up.reverse()
                surrounding += first_chair(up)

                #first chair down
                down = [board[i][col] for i in range(row+1, len(board))]
                surrounding += first_chair(down)

                # first chair up+right
                length = min(row, len(board[0])-(col+1))
                up_right = [board[row-i-1][col+i+1] for i in range(length)]
                surrounding += first_chair(up_right)

                # first chair down+right
                length = min(len(board)-(row+1), len(board[0])-(col+1))
                down_right = [board[row+i+1][col+i+1] for i in range(length)]
                surrounding += first_chair(down_right)

                # first chair up+left
                length = min(row, col)
                up_left = [board[row-i-1][col-i-1] for i in range(length)]
                surrounding += first_chair(up_left)

                # first chair down+left
                length = min(len(board)-(row+1), col)
                down_left = [board[row+i+1][col-i-1] for i in range(length)]
                surrounding += first_chair(down_left)

                if board[row][col] == "L" and (surrounding == 0):
                    newboard[row][col] = "#"
                elif board[row][col] == "#" and (surrounding >= 5):
                    newboard[row][col] = "L"
                else:
                    newboard[row][col] = board[row][col]

        if board == newboard:
            count = 0
            for row in range(len(board)):
                for col in range(len(board[0])):
                    if board[row][col] == "#": 
                        count += 1
            return count
        board = newboard
        iter += 1

if __name__ == "__main__":
    print(f"Part 1 solution: {part1()}")
    print(f"Part 2 solution: {part2()}")
