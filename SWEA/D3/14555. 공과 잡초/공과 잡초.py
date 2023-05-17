def solution():
    grass = input()
    cnt = 0
    i = 0
    while i<len(grass):
        if grass[i] == '(':
            cnt+=1
            i+=2
            continue
        elif grass[i] == ')' and grass[i-1]=='|':
            cnt += 1

        i+=1
    return cnt

T = int(input())
for i in range(1, T+1):
    print("#%d"%i, solution())


