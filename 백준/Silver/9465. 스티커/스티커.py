def solution():
    n = int(input())
    num = [list(map(int, input().split())) for _ in range(2)]
    dp = [[0]*(n+1) for _ in range(2)]

    dp[0][1], dp[1][1] = num[0][0], num[1][0]

    for j in range(2, n+1):
        for i in range(2):
            dp[i][j] = max(dp[i-1][j-1], dp[i][j-2], dp[i-1][j-2])+num[i][j-1]

    return max(dp[0]+dp[1])


t = int(input())
for i in range(t):
    print(solution())