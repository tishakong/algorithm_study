n = int(input())
second = 1

for i in range(2,n+1):
    second *= i

print(int(second/7/24/60/60))