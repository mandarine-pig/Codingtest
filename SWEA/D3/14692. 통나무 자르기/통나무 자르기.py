def solution():
    num = int(input())
    ans = "Alice" if num%2 == 0 else "Bob"
    return ans

T = int(input())
for i in range(1, T+1):
    print("#%d"%i, solution())


