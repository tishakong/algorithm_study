total = int(input())
result = 0

change = 1000-total

for i in [500,100,50,10,5,1]:
    if change >= i:
        result += change // i
        change = change % i
    if change == 0:
        break

print(result)