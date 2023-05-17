def solution(n):
    num = input()

    nums = [int(num)]
    for i in range(len(num)-1):
        for j in range(i+1, len(num)):
            if i == 0 and num[j] == '0':
                continue
            new_num = num[:i]+num[j]+num[i+1:j]+num[i]+num[j+1:]
            nums.append(int(new_num))

    print("#%d"%n, min(nums), max(nums))

T = int(input())
for i in range(1, T+1):
    solution(i)


