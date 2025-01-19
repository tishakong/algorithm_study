
lst = []
for i in range(1,10001):
    lst.append(i)    

for i in range(1,10001):
    tmp = i
    spliting = list(str(i))
    for j in spliting:
        tmp += int(j)

    if tmp in lst:
        lst.remove(tmp)
        
for i in lst:
    print(i)
    
    