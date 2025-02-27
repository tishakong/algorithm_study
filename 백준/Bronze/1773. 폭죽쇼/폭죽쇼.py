import sys

n, c = map(int, sys.stdin.readline().split())
#n = 학생 수 c = 끝나는 시간

timeTable = [False] * (c+1)
lst = []

for i in range(n):
    num = int(sys.stdin.readline())
    
    for j in range(num, c + 1, num):
        timeTable[j] = True

print(sum(timeTable))