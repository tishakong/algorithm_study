test = input()

if len(test) > 2 and test[0] == "\"" and test[-1] == "\"":
    print(test[1:-1])
else:
    print("CE")