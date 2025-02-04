n = int(input())

for i in range(n):
    m= int(input())
    maxPrice = 0
    maxPlayer = ""
    for j in range(m):
        player = input().split()
        if int(player[0]) > maxPrice:
            maxPrice = int(player[0])
            maxPlayer = player[1]
    print(maxPlayer)
        