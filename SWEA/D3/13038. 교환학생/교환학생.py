T = int(input())
for i in range(1, T+1):
    n = int(input())
    day = list(map(int, input().split()))
    ans = []

    for j in range(7):
        idx = j
        cnt = n
        total = 0
        while cnt!=0:
            if day[idx] == 1:
                cnt-=1
            total+=1
            idx = (idx+1)%7
        ans.append(total)

    print("#%d"%i, min(ans))