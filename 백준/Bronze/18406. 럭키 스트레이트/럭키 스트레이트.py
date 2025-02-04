n = list(str(input()))

middle = len(n) // 2
flag = 0
result = 0


for i in n:
    i = int(i)
    if flag < middle:
        result += i        
        flag += 1
    else:
        result -= i

if result == 0:
    print("LUCKY")
else:
    print("READY")