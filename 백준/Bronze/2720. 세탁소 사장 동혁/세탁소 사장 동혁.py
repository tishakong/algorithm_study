
t = int(input())
lst = []

for i in range(t):
    lst.append(int(input()))

#25센트 10센트 5센트 1센트
for i in lst:
    q = i // 25
    i -= 25 * q
    
    d = i // 10
    i -= 10 * d
    
    n = i // 5
    i -= 5 * n
    
    p = i // 1
    i -= 1 * p
    print(q,d,n,p)