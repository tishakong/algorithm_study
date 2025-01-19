import sys

def merge_sort(lst):
    if len(lst) <= 1:
        return lst

    mid = len(lst) // 2
    left = merge_sort(lst[:mid])
    right = merge_sort(lst[mid:])

    return merge(left, right)

def merge(left, right):
    sorted_list = []
    i = j = 0

    while i < len(left) and j < len(right):
        if int(left[i][0]) <= int(right[j][0]):
            sorted_list.append(left[i])
            i += 1
        else:
            sorted_list.append(right[j])
            j += 1

    sorted_list.extend(left[i:])
    sorted_list.extend(right[j:])

    return sorted_list

n = int(sys.stdin.readline().rstrip())
lst = []

for i in range(n):
    lst.append(list(sys.stdin.readline().rstrip().split()))
    
sorted_list = merge_sort(lst)

for i in sorted_list:
    print(i[0],i[1])
'''
#버블 정렬쓰면 될듯
#버블정렬 쓰니까 시간초과남

for i in range(n):
    for j in range(0, n-1-i):
        if int(lst[j][0]) > int(lst[j+1][0]):
            lst[j][0], lst[j+1][0] = lst[j+1][0], lst[j][0]
            lst[j][1], lst[j+1][1] = lst[j+1][1], lst[j][1]


'''


#정렬 안정성 있고 더 효율적인 머지소트?