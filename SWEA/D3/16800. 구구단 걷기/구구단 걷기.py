import math

def solution():
    n = int(input())
    ans = 0
    for i in range(1, int(math.sqrt(n))+1):
        if n%i == 0:
            ans = n//i+i-2

    return ans

t = int(input())
for i in range(1, t+1):
    print("#%d"%i, solution())
