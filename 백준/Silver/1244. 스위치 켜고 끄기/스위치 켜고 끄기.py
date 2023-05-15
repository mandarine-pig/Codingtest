
def change_switch(idx):
    global switch
    switch[idx] = 0 if switch[idx] == 1 else 1

def man(num):
    global n, switch
    for i in range(1, n//num+1):
        change_switch(i*num-1)

def woman(num):
    global n, switch
    l, r = num-1, num+1

    change_switch(num)

    while (l>=0 and r>= 0 and l<n and r<n):
        if switch[l] != switch[r]:
            return

        change_switch(l)
        change_switch(r)
        l -=1
        r +=1

n = int(input())
switch = list(map(int, input().split()))
t = int(input())
for i in range(t):
    gender, num = map(int, input().split())
    if gender == 1:
        man(num)
    else:
        woman(num-1)

line = 1
for i in switch:
    if line%20 ==0:
        print(i)
    else:
        print(i, end=" ")
    line+=1