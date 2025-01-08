M = int(input())
D = int(input())

if M > 2:
    print("After")
elif M == 2:
    if D == 18:
        print("Special")
    elif D > 18:
        print("After")
    else:
        print("Before")
else:
    print("Before")