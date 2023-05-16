#q, sort 활용한 그리디
from collections import deque
def solution():
    n = int(input())
    sold = deque(list(map(int, input().split())))

    curr_max = max(sold)
    buy_item = 0
    buy_price = 0
    ans = 0
    while sold:
        i = sold.popleft()
        if i == curr_max:
            ans += i*buy_item-buy_price
            buy_item, buy_price = 0, 0
            curr_max = max(sold) if sold else 0

        if i < curr_max:
            buy_item += 1
            buy_price += i

    return ans

T = int(input())
for i in range(1, T+1):
    print("#%d"%i, solution())
