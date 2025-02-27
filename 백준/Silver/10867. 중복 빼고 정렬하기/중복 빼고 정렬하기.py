import sys

n = int(sys.stdin.readline())
lst = list(set(map(int,sys.stdin.readline().split())))

lst.sort()

for i in lst:
    print(i, end=' ')