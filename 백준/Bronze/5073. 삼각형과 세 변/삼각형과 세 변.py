while True:
    num = list((map(int, input().split())))
    if num[0] == 0 and num[1] == 0 and num[2] == 0:
        break

    num.sort()
    if num[2]>= num[1]+num[0]:
        print("Invalid")
    elif num[0] == num[1] or num[1] == num[2] or num[2] == num[0]:
        if num[0] == num[1] and num[1] == num[2]:
            print("Equilateral")
        else:
            print("Isosceles")
    else:
        print("Scalene")