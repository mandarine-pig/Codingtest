import math
T = int(input())
for i in range(1, T+1):
    n, d = map(int, input().split())
    ans = math.ceil(n/(2*d+1))
    print("#%d"%i, ans)