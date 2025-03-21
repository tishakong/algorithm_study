n = int(input())

for i in range(n):
    password_len = len(str(input()))
    if password_len >= 6 and password_len <= 9:
        print("yes")
    else:
        print("no")