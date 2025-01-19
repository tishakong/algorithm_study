import sys

n = int(sys.stdin.readline())
student = []

for i in range(n):
    student.append(list(sys.stdin.readline().rstrip().split()))

#다 입력 받으면 2차원 배열 형태.
#세로로 비교해서 같은 걸 찾으면 더해주기

cnt = {} #중복 숫자 세기
for i in range(n):
    cnt[i] = set()
    
#일일이 비교하면 시간복잡도가 너무 클거같긴한데
for i in range(5): #열
    for j in range(n): #행
        for k in range(j+1, n):
            me = student[j][i]
            if me == student[k][i]:
                cnt[j].add(k)
                cnt[k].add(j)

#교집합 개념으로도 풀 수 있나?

result = 0
max_tmp = 0
for i in range(n):
    if len(cnt[i]) > max_tmp:
        result = i
        max_tmp = len(cnt[i])
        
print(result+1)