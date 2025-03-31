import sys 

n = int(sys.stdin.readline())

#1~N까지 번호 N이 맨아래
#제일 위에 있는 카드 버리고 버린 카드 다음위에 있던 카드를 아래로 옮김

lst = []

for i in range(1, n+1):
    lst.append(i)
    
while len(lst)!=1:
    print(lst.pop(0), end=' ')
    tmp = lst.pop(0)
    lst.append(tmp)

print(lst[0])    
