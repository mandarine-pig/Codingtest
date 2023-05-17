n = int(input())

for i in range(1, n+1):
    num = 0
    for j in ["3", "6", "9"]:
        num += str(i).count(j)

    ans = i if num==0 else "-"*num

    print(ans, end=" ")
