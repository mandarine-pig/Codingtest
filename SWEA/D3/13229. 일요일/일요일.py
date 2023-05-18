day = {"MON": 1, "TUE" : 2, "WED" : 3, "THU" : 4, "FRI":5, "SAT":6, "SUN":0}
def solution():
    global day
    n = day[input()]
    return 7-n

T = int(input())
for i in range(1, T+1):
    print("#%d"%i, solution())