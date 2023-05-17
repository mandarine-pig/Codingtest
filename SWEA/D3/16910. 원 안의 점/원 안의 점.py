
def solution():
    n = int(input())
    goal = n**2

    ans = 0
    for i in range(-n, n+1):
        for j in range(-n, n+1):
            if i**2+j**2 <= goal:
                ans+=1

    return ans

t = int(input())
for i in range(1, t+1):
    print("#%d"%i, solution())
