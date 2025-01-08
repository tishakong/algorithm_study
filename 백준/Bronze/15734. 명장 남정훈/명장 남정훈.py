L, R, A = map(int,input().split())

if L == R:
    if A % 2 == 0:
        print(L+R+A)
    else:
        print(L+R+A-1)
else:
    if L > R:
        big, small = L, R
    else:
        big, small = R, L

    if small+A <= big:
        print((small+A)*2)
    else:
        remain = A - (big - small)
        if remain % 2 == 0:
            print(big*2+remain)
        else:
            print(big*2+remain-1)
        