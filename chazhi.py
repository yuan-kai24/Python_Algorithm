count = input()
userInfo = input()
userInfo = userInfo.split()
min = 10000
rel = 0
for i in range(0, userInfo.__len__()):
    for item in range(i+1, userInfo.__len__()):
        rel = int(userInfo[i]) - int(userInfo[item])
        rel = abs(rel)
        if rel < min:
            min = rel
print(min)