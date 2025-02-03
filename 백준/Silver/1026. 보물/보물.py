n = int(input())
A = list(map(int,input().split()))
B = list(map(int,input().split()))

#B는 고정, A를 움직여야함.
#최솟값이려면 B 제일 큰 곳에 A 제일 작은. 순위를 매겨야함
A.sort()

B_rank = []
memo = {}

for i in B:
    if i in memo:
        B_rank.append(memo[i])
        continue
    tmp = 0
    for j in range(n):
        if i > B[j]:
           tmp += 1
    B_rank.append(tmp)
    memo[i]=tmp

#B_rank의 값이 클수록 그 값이 큰 값임
#B_rank 값은 n-1이 가장 큰 수
S = 0
flag = 0

for i in range(n-1,-1,-1):
    while True:
        if i in B_rank:
            maxValueIndex = B_rank.index(i)
            B_rank[maxValueIndex] = n+1 #이미 뽑힌거 또 못쓰게 범위밖 값으로 수정
            S += A[flag]*B[maxValueIndex]
            #print("A[flag]", A[flag])
            #print("B[maxValueIndex]", B[maxValueIndex])
            #print("현재 S ",S)
            flag += 1
        else:
            break
        
print(S)
    