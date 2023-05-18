ans = "impossible"
def solution(curr, n, used):
    global ans

    if len(curr) == len(n):
        if curr != n and int(curr)%int(n) == 0:
            ans = "possible"
        return

    for i in range(len(n)):
        if used[i] == False:
            used[i] = True
            solution(curr+n[i], n, used)
            used[i] = False

T = int(input())
for i in range(1, T+1):
    ans = "impossible"
    n = input()
    solution("", n, [False]*len(n))
    print("#%d"%i, ans)