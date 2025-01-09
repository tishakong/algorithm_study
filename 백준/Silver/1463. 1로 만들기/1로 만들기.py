import sys

x = int(sys.stdin.readline())


'''
풀이 1 시간초과
memo = {1:'0', 2:1, 3:1}
start = 2
nextStart = [3]

while not memo.get(x): #get 하면 없을 경우 None이 나옴:
    current = memo[start]
    
    add1 = start + 1
    mul2 = start * 2
    mul3 = start * 3
    
    if not memo.get(add1):
        memo[add1] = current + 1
        nextStart.append(add1)
    elif current + 1 < memo.get(add1):
        memo[add1] = current + 1

    if not memo.get(mul2):
        memo[mul2] = current + 1
        nextStart.append(mul2)
    elif current + 1 < memo.get(mul2):
        memo[mul2] = current + 1

    if not memo.get(mul3):
        memo[mul3] = current + 1
        nextStart.append(mul3)
    elif current + 1 < memo.get(mul3):
        memo[mul3] = current + 1
    
    start = nextStart.pop(0)
            
print(str(memo.get(x)))
'''

'''
풀이 2 시간초과 (더 작은지 검증하는 작업 추가가)
memo = {1:'0', 2:1, 3:1}
start = 2
nextStart = [3]

while not memo.get(x): #get 하면 없을 경우 None이 나옴:
    current = memo[start]
    
    add1 = start + 1
    mul2 = start * 2
    mul3 = start * 3
    
    if not memo.get(add1):
        memo[add1] = current + 1
        nextStart.append(add1)

    if not memo.get(mul2):
        memo[mul2] = current + 1
        nextStart.append(mul2)

    if not memo.get(mul3):
        memo[mul3] = current + 1
        nextStart.append(mul3)
    
    start = nextStart.pop(0)
            
print(str(memo.get(x)))
'''

memo = {x:0}
start = x
nextStart = []

#반대로 생각. x를 만드려면 필요한 단계
#10을 만드려면 9나 5가 있어야함.
#9를 만드려면 8, 3
#5는 4
#8은 4,2
if x == 1:
    print("0")
else:
    while not memo.get(1): #get 하면 없을 경우 None이 나옴
        current = memo.get(start)
    
        add1 = start - 1
        if not memo.get(add1):
            memo[add1] = current + 1
            nextStart.append(add1)
            
        if start % 2 == 0:
            mul2 = start // 2
            if not memo.get(mul2):
                memo[mul2] = current + 1
                nextStart.append(mul2)

        if start % 3 == 0:
            mul3 = start // 3
            if not memo.get(mul3):
                memo[mul3] = current + 1
                nextStart.append(mul3)
        
        start = nextStart.pop(0)        
    print(str(memo.get(1)))