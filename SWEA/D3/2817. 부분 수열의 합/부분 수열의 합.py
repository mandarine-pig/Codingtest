def dfs(i, curr):
    global ans, n, k, num
    if curr==k:
        ans+=1
        return

    if curr>k or i>=n:
        return

    dfs(i+1, curr+num[i])
    dfs(i+1, curr)

T = int(input())

for t in range(1, T+1):
    n, k = map(int, input().split())
    num = list(map(int, input().split()))
    ans = 0
    dfs(0, 0)
    print("#%d"%t, ans)