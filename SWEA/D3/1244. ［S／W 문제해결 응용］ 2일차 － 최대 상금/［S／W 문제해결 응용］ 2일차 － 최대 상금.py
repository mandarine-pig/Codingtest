nums = []
ans = 0
def dfs(n, k):
    global nums, ans

    if k==0:
        curr = ""
        for num in nums:
            curr += num
        ans = max(ans, int(curr))
        return

    for i in range(n):
        for j in range(i+1, n):
            nums[j], nums[i] = nums[i], nums[j]
            dfs(n, k - 1)
            nums[j], nums[i] = nums[i], nums[j]

    return


def solution():
    global nums, ans
    nums = []
    ans = 0
    n, k = input().split()
    for i in n:
        nums.append(i)

    now_k = len(nums) if int(k)>len(nums) else int(k)
    dfs(len(nums), now_k)

    if int(k)>len(nums):
        if int(k) - len(nums) % 2 == 1:
            nums[-2], nums[-1] = nums[-1], nums[-2]

        curr = ""
        for num in nums:
            curr += num
        ans = max(ans, int(curr))

    return ans

T = int(input())
for t in range(1, T + 1):
    print("#%d" % t, solution())