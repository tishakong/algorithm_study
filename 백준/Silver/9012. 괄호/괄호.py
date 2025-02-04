#스택을 사용하면 좋을 듯 함

#입력
t = int(input()) #테스트케이스 개수
allTestCase = []

for i in range(t):
    testCase =  list(input())
    allTestCase.append(testCase)


#구현 및 출력
for lst in allTestCase:
    isVPS = True
    right = 0 # ) 개수 관리
    
    while lst:
        tmp = lst.pop()
        if tmp == ')':
            right += 1
        elif tmp == '(':
            if right > 0:
                right -= 1
            else:
                isVPS = False
                break
            
    if isVPS == True and right == 0:
        print("YES")
    else:
        print("NO")