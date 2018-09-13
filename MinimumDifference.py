count = input()
userInfo = input()
userInfo = [int(item) for item in userInfo.split()]# 拆分并转换
min = 10000 # 数字已经限定不过一万
rel = 0
for i in range(0, userInfo.__len__()):# 遍历每个数据
    for item in range(i+1, userInfo.__len__()):# 用每个数据依次与其他数据遍历
        rel = abs(userInfo[i] - userInfo[item])
        if rel < min:
            min = rel
        # min = abs(userInfo[i] - userInfo[item]) if abs(userInfo[i] - userInfo[item]) < min else min # 三目运算符版（效率一样）
print(min)

