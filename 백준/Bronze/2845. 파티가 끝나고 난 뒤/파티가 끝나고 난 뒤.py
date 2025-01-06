#입력 단계
import sys

x, y = map(int, (sys.stdin.readline().split()))
lst = list(map(int,(sys.stdin.readline().split())))

#풀이 단계
total = x * y
for i in range(len(lst)):
    lst[i] = lst[i] - total
    
#출력 단계
for i in lst:
    print(i,end=' ')