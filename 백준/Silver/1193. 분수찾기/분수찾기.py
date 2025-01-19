x = int(input())

#맨 첫줄 분모가 짝수면 오른쪽 위에서 왼쪽 아래로 방향
#홀수면 왼쪽 아래서 오른쪽 위로 방향

i = 0

while True:
    i += 1   
    if x > i:
        x = x - i
        continue
    else:
        break
    
if i % 2 == 0:
    #짝수면
    y = 1 #분자
    z = i #분모
    while x > 1:
        x = x - 1
        y += 1
        z -= 1
else:
    #홀수면
    y = i #분자
    z = 1 #분모
    while x > 1:
        x = x - 1
        y -= 1
        z += 1
        
print(y,"/",z, sep="")
        

