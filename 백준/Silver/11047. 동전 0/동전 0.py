
#제일 간단한 알고리즘. 제일 비싼거 부터 그냥 빼보기.
#근데 타겟값보다 비싼게 너무 터무니 없이 많으면 비효율적임
#오름차순으로 정렬되어 있으니까 나보다 작은 애 먼저 찾고 그 후부터 계산하면?
#근데 만약 주어진 동전으로 K를 만들 수 없을 경우는 고려하지 않아도 되는건가?

#입력 단계
#n은 동전의 종류 개수, k는 목표값
'''
n, k = map(int, input().split())
coin_list = []

for i in range(n):
    coin_list.append(int(input()))
'''

import sys

n, k = map(int, sys.stdin.readline().split())
coin_list = [int(sys.stdin.readline()) for _ in range(n)]
    
#풀이 단계

'''
풀이 1
이유를 모르겠지만 아래 코드는 백준에서 실패나고 있음.. 근데 예제 돌렸을땐 답 나옴옴
result = 0
flag = n // 2
memo = []

while True:
    if flag in memo:
        break
    
    if coin_list[flag] > k:
        flag = flag // 2
        continue
    elif(coin_list[flag] <= k):
        flag += 1    
    memo.append(flag)

while k != 0:
    if k >= coin_list[flag]:
        k -= coin_list[flag]
        result += 1
    else:
        flag -= 1
'''

'''
풀이2
시간초과
result = 0
flag = n-1

while k != 0:
    if k >= coin_list[flag]:
        k -= coin_list[flag]
        result += 1
    else:
        flag -= 1
'''

#풀이3 몫을 구해서 result를 몫만큼 더하고 나머지로 k 계산
result = 0

for i in range(n - 1, -1, -1):
    if k == 0:
        break
    if k >= coin_list[i]:
        result += k // coin_list[i]
        k %= coin_list[i]

#출력
print(result)