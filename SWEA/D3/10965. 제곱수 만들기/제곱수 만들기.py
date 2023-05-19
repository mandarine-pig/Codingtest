import math

result = []
prime = [2, 3, 5, 7, 11, 13, 17]
def make_prime():
    global prime
    for i in range(18, int(math.sqrt(10**7))+1):
        prime.append(i)
        for p in range(len(prime)-1):
            if i%prime[p] == 0:
                prime.pop()
                break

def solution(n):
    global prime
    ans = 1
    if math.sqrt(n).is_integer():
        result.append(ans)
        return

    for p in prime:
        cnt = 0
        while n%p==0:
            n = n // p
            cnt+=1
        if cnt%2==1:
            ans *= p

    result.append(ans*n)

T = int(input())
make_prime()
for t in range(1, T + 1):
    n = int(input())
    solution(n)

for t in range(1, T + 1):
    print("#%d" % t, result[t-1])
