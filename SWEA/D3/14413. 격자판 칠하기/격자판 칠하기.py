def in_range(x, y, n, m):
    return x>=0 and y>=0 and x<n and y<m

def solution():
    n, m = map(int, input().split())
    origin = [input() for _ in range(n)]
    new = [["?"]*m for _ in range(n)]

    dxs = [0, 0, 1, -1]
    dys = [1, -1, 0, 0]
    for i in range(n):
        for j in range(m):
            new[i][j] = origin[i][j]
            #사방 보기
            for dx, dy in zip(dxs, dys):
                nx, ny = i + dx, j + dy
                if in_range(nx, ny, n, m) and new[nx][ny] in ["#", "."]:
                    if new[i][j] in ["#", "."] and new[i][j] == new[nx][ny]:
                        return "impossible"
                    new[i][j] = "#" if new[nx][ny] =="." else "."


    return "possible"

T = int(input())
for i in range(1, T+1):
    print("#%d"%i, solution())


