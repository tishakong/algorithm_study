N, X = map(int,input().split())

lst = list(map(int,input().split()))
result = 0

for i in lst:
    if i < X:
        print(i, end=" ")