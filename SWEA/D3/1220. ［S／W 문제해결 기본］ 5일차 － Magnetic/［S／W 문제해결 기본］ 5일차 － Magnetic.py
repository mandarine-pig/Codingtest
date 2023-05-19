#1이면 밑으로, 2 면 위로
dxs = [0, 1, -1]
dys = [0, 0, 0]
magnet = []

def in_range(x, y):
    global n
    return x>=0 and y>=0 and x<n and y<n

def move_magent():
    global board, magnet

    cnt = 0
    while magnet:
        x, y = magnet.pop()
        idx = board[x][y]
        nx, ny = x+dxs[idx], y+dys[idx]
        if not in_range(nx, ny):
            board[x][y] = 0
            continue
        elif board[nx][ny] == 0:
            board[x][y] = 0
            board[nx][ny] = idx
            cnt+=1

    return True if cnt!=0 else False

def set_magnet():
    global magnet, board
    magnet = []
    for i in range(n):
        for j in range(n):
            if board[i][j] != 0:
                magnet.append((i, j))

    return False

def cnt_ans():
    global board, n

    cnt = 0
    for j in range(n):
        prev = board[0][j]
        for i in range(1, n):
            if prev==1 and board[i][j]==2:
                cnt +=1
            prev = board[i][j]
    return cnt

def solution():
    global dxs, dys, board, magnet

    can_move = True
    while can_move:
        set_magnet()
        can_move = move_magent()

for t in range(1, 11):
    n = int(input())
    board = [list(map(int, input().split())) for _ in range(n)]
    solution()
    print("#%d"%t, cnt_ans())