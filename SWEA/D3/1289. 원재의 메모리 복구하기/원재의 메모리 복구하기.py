T = int(input())
for t in range(1, T+1):
    after = input()
    origin = "0"
    cnt = 0
    for i in range(len(after)):
        if origin != after[i]:
            origin = after[i]
            cnt+=1
    print("#%d"%t, cnt)