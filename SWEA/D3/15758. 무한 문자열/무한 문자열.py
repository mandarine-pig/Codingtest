T = int(input())
for i in range(1, T+1):
    s, t = input().split()
    s, t = s*len(t), t*len(s)

    ans = "yes" if s==t else "no"
    print("#%d"%i, ans)

