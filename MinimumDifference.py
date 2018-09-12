count = input()
userInfo = input()
userInfo = userInfo.split()# 拆分
min = 10000
rel = 0
for i in range(0, userInfo.__len__()):# 遍历每个数据
    for item in range(i+1, userInfo.__len__()):# 用每个数据依次与其他数据遍历
        rel = int(userInfo[i]) - int(userInfo[item])
        rel = abs(rel)# 绝对值
        if rel < min:
            min = rel
print(min)