#2차원 dp
n, m = map(int, input().split())
small = []
for i in range(m):
    small.append(int(input()))

MAX_INT = n
MAX_JUMP = int(((n*2)**(1/2)))+2
dp = [[MAX_INT]*(MAX_JUMP) for _ in range(n+1)]

#dp[돌번호][가속점프] = 점프 횟수
if not 1 in small and not 2 in small:
    dp[1][0] = 0
    dp[2][1] = 1

for i in range(2, n):
    if i in small:
        continue

    for j in range(1, MAX_JUMP):
        if dp[i][j] == MAX_INT:
            continue

        #감속
        if j-1>0 and i+j-1<=n and j-1 <=n:
            dp[i+j-1][j-1] = min(dp[i][j] + 1, dp[i+j-1][j-1])

        #가속
        if i + j + 1 <= n and j + 1 <= n:
            dp[i+j+1][j+1] = min(dp[i][j] + 1, dp[i+j+1][j+1])

        #정속
        if i + j <= n:
            dp[i+j][j] = min(dp[i][j] + 1, dp[i+j][j])

ans = min(dp[-1])
if ans == MAX_INT or n in small:
    print(-1)
else:
    print(ans)