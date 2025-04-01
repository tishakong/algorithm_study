import sys

#n==총 초
n = int(sys.stdin.readline())

#A는 300초 B는 60초 C는 10초
A = 0
B = 0
C = 0

if str(n)[-1] != "0":
    print("-1")
else:
    if n >= 300:
        A = n // 300
        n = n % 300

    if n >= 60:
        B = n // 60
        n = n % 60

    if n >= 10:
        C = n // 10

    print(A,B,C)