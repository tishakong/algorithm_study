import sys

time = 0
while (time<3):
    n = int(sys.stdin.readline()) #입력 정수 개수
    s = 0
    for i in range(n):
        s += int(sys.stdin.readline())
    if(s == 0):
        print('0')
    elif(s > 0):
        print('+')
    else:
        print('-')
    time += 1