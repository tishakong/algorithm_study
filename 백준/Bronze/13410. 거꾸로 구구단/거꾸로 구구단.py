import sys

n, k = map(int, sys.stdin.readline().split())

#가장 크려면
#1. 단위수가 제일 커야하고(단 맨 마지막이 0이면 아님)
#2. 맨 마지막~처음 숫자 중 제일 큰 순서대로임

lst = []

#구구단 정상 결과 기입
for i in range(1, k+1):
    lst.append(int(str(n*i)[::-1]))

print(max(lst))



'''
#n이 2자리 이상일 경우 무한루프 도는 오류 왜..?

firstList = []

while True:
    #맨뒤가 자리수가 제일 클거임
    firstList.append(lst.pop())
    maxLen = len(firstList[0])

    while True:
        if lst:
            tmp = lst.pop()
            if len(tmp) == maxLen:
                firstList.append(tmp)
            else:
                break

    #자리수가 유일하게 제일 큰데 끝자리가 0일 경우 처음으로 돌아가서 다음 자리수 확인인
    if len(firstList) == 1 and firstList[0][-1] == "0":
        firstList = []
        #0 떼고 넣기
        firstList.append(firstList[0][0:-1])
        continue
    else:
        maxNum = firstList[0]
        for i in firstList:
            for j in reversed(range(maxLen)):
                if maxNum[j] < i[j]:
                    maxNum = i
                    break
        
        maxNum = maxNum[::-1]
        print(int(maxNum))
        break
'''