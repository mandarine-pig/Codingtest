def solution():
    n = input()
    win = 0
    for i in n:
        if i=="o":
            win+=1

    win += 15-len(n)

    ans = "YES" if win>=8 else "NO"
    return ans

T = int(input())
for i in range(1, T+1):
    print("#%d"%i, solution())