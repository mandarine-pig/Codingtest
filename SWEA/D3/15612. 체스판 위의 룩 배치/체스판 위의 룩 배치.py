def solution():
    row = [False]*8
    column = [False]*8
    
    cnt = 0
    chess = [input() for _ in range(8)]
    for i in range(8):
        for j in range(8):
            if chess[i][j] == "O":
                if row[i] or column[j]:
                    return "no"
                row[i], column[j] = True, True
                cnt += 1

    return "yes" if cnt==8 else "no"

T = int(input())
for i in range(1, T+1):
    print("#%d"%i, solution())