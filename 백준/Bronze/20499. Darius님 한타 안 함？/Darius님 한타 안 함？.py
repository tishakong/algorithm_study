K,D,A = map(int,input().split("/"))

if K+A < D:
    print("hasu")
elif D == 0:
    print("hasu")
else:
    print("gosu")