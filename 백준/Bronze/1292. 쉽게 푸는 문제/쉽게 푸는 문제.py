start, end = map(int,input().split())

lst = []
i=1
result = 0

while len(lst)<1000:
    for j in range(i):
        lst.append(i)
    i += 1

for i in range(start-1, end):
    result += lst[i]
    
print(result)