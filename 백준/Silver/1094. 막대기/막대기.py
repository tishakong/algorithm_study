#입력 단계
#X은 목표 cm
import sys

x = int(sys.stdin.readline())

#풀이 단계
result = 0
total = 64
lst = [64]

while total > x:
    tmp = lst.pop()
    tmp = tmp // 2 #가장 짧은 것을 절반으로 자른다
    lst.append(tmp) #하나는 보관
    if(total - tmp >= x): #하나를 버렸을때 총 길이가 x보다 크거나 같다면 하나를 버림
        total -= tmp
    else:
        lst.append(tmp) #작으면 나머지 하나도 보관
    
for i in lst:
    if x == 0:
        break
    if x >= i:
        x -= i
        result += 1
    
#출력 단계
print(result)