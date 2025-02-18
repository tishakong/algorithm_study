appleA, orangeA = map(int,input().split())
appleB, orangeB = map(int,input().split())

case1 = appleA + orangeB
case2 = appleB + orangeA

if case1 > case2:
    print(case2)
else:
    print(case1)

