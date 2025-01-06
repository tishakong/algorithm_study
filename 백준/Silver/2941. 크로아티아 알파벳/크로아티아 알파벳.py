import sys

word = sys.stdin.readline()
result = 0
last = '0'
check1 = ['c', 'd', 'l', 'n', 's', 'z','j','=','-','\n']
check2 = ['c=','c-','d-','lj','nj','s=','z=','dz=']

for i in word:
    if i not in check1:
        result += 1
        if last != '0':
            result += len(last)
            last ='0'
        continue
    elif (i in check1) & (last == '0'):
        last = i
        continue
    elif (i in check1) & (last != '0'):
        if last+i in check2:
            result += 1
            last = '0'            
        elif last+i == 'dz':
            last = 'dz'
            continue
        elif last+i not in check2:
            result += len(last)
            last = i

print(result)