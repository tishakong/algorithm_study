n = int(input())
lopes = []
 
for i in range(n):
    lopes.append(int(input()))

lopes.sort()

maxResult = 0
cnt = n

for i in lopes:
    if i*cnt > maxResult:
        maxResult = i*cnt
    cnt -= 1

print(maxResult)