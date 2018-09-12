# 解析输入资源
userInfo = input()
userInfo = userInfo.split()
userInfo[0] = int(userInfo[0])
userInfo[1] = int(userInfo[1])
# 记录被淘汰的次数
count = 1
numx = 0
num = []
index = 0
# 存储小朋友 True没被淘汰
for item in range(0, userInfo[0]):
    num.append(True)
while count < userInfo[0]:# 如果淘汰次数达到极限则退出
    if num[index]:# 如果没被淘汰则进入，执行内部数数操作
        numx = numx + 1
        if numx % userInfo[1] == 0:# 判断当前数数是否符合条件
            num[index] = False
            count = count + 1
    index = index + 1# 寻找下一个小朋友
    if index == userInfo[0]:
        index = 0

for item in range(0, userInfo[0]):
    if num[item]:
        print(item+1)
        break