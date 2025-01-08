#최소값이 목표. 그렇다면 가능한 -하는 값이 제일 크면 됨
#-가 나오면 다시 -가 나올때까지 나오는 모든 수를 빼기
#근데 마이너스 나온 순간부턴 다 뺄수있는 거 아닌가?

#입력 단계
#s => 숫자 식
str = input()
result = 0
lst = []
last = ''

#풀이단계

#파싱

for i in str:
    if i != "-" and i != "+": #숫자일때
        last = last+i
    else: #부호일때
        lst.append(last) #숫자 먼저 넣고
        last = ''
        lst.append(i) #부호 넣기

lst.append(last) #마지막 숫자 넣기

#리스트 안에 든 식 갖고 풀기
isCanMinus = False
for i in lst:
    if i != "-" and i != "+": #숫자일때
        if isCanMinus:
            result -= int(i)
        else:
            result += int(i)
    elif(i == '-'):
        isCanMinus = True

#출력
print(result)