def solution():
    n = int(input())
    board = [input() for _ in range(n)]
    start, end = None, None
    for i in range(n):
        for j in range(n):
            if board[i][j] == "#":
                if not start:
                    start, end = (i, j), (i, j)
                else:
                    end = (i, j)

    ans = "yes" if end[0]-start[0] == end[1]-start[1] else "no"
    
    for i in range(start[0], end[0]+1):
        for j in range(start[1], end[1]+1):
            if board[i][j] != "#":
                ans = "no"

    return ans

T = int(input())
for i in range(1, T+1):
    print("#%d"%i, solution())