count = int(input())
userInfo = []
for item in range(0, count):
    userInfo.append(input().split())# 存储数据
coor = [0, 0]# 坐标初始化
coorx = [0, 0]# 坐标移动
num = 0# 坐标头
numx = count - 1 #过半时操作
fx = True
for item in range(0, count*2):# 斜面执行2n-1次
    #  思路：先把每条斜线的第一个元素找到，再用增量增减坐标输出
    # 奇数（包括零）走向为上，偶数走向为下
    # 前后半段参数不一样
    if item < count: #判断是否过半
        num = item
        if (num%2) == 0:# 前半段移动
            coor[0] = num
            coor[1] = 0
            coorx[0] = -1
            coorx[1] = 1
        else:
            coor[0] = 0
            coor[1] = num
            coorx[0] = 1
            coorx[1] = -1
    else:# 后半段操作
        num = numx - (item - numx) # 后半段斜线元素个数
        if (num%2) == 0:
            coor[0] = count - 1
            coor[1] = count - (num + 1)
            coorx[0] = -1
            coorx[1] = 1
        else:
            coor[0] = count - (num + 1)
            coor[1] = count - 1
            coorx[0] = 1
            coorx[1] = -1
    #print(userInfo[coor[0]][coor[1]], coor, coorx, num)
    for ite in range(0, num + 1):
        print(userInfo[coor[0]][coor[1]], end=" ")
        coor[0] = coor[0] + coorx[0]
        coor[1] = coor[1] + coorx[1]