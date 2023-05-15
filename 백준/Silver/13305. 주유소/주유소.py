import sys
#greedy

n = int(input())
dist = list(map(int, input().split()))
price = list(map(int, input().split()))

curr = sys.maxsize
ans = 0
for i in range(n-1):
    if price[i]<curr:
        curr = price[i]

    ans += dist[i]*curr
    
print(ans)