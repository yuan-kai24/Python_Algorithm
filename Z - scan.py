count = int(input())
userInfo = []
for item in range(0, count):
    userInfo.append(input().split())# 存储数据
coor = [0, 0]# 坐标初始化
coorx = [0, 0]# 坐标移动
num = 0# 坐标头
numx = count - 1 #过半时操作
fx = True
for item in range(0, count*2-1):# 斜面执行2n-1次
    if fx: #判断是否过半
        num = item
        if (num%2) == 0:
            coor[0] = num
            coor[1] = 0
        else:
            coor[0] = 0
            coor[1] = num
    else:
        num = numx - (item - numx) + 1
        if (num%2) == 0:
            coor[0] = num
            coor[1] = count-1
        else:
            coor[0] = count-1
            coor[1] = num
    if (count-1) == item:
        fx = False
    for ite in range(0, num):
        pass
