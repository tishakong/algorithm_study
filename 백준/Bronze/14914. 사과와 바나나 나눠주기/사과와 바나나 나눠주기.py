apple, banana = map(int, input().split())

n = 1

if apple < banana:
    smaller = apple
else:
    smaller = banana

while smaller >= n:
    if apple % n == 0 and banana % n == 0:
        print(n, apple // n , banana // n)
    n += 1
         
    