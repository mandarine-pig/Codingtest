def solution():
    alpha = input()
    now = ord('a')
    ans = 0

    for i in alpha:
        if ord(i) == now:
            ans += 1
            now += 1
        else:
            break

    return ans

T = int(input())
for i in range(1, T+1):
    print("#%d"%i, solution())