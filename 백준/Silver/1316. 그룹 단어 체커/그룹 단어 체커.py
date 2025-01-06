import sys

n = int(sys.stdin.readline())
result = 0

for i in range(n):
    word = sys.stdin.readline()
    is_group = True
    memo = []
    
    for i in word:
        if i in memo:
            if last == i:
                continue
            else:
                is_group =False
                break
        else:
            memo.append(i)
        last = i

            
    if(is_group):
        result += 1
        
print(result)