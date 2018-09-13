count = int(input())
userInfo = []
for item in range(0, count):
    userInfo.append(input().split())# 存储数据
# for item in range(0, count*2-1):# 斜面执行2n-1次
#     while True:
#         coor[0] = coor[0] + coorC[0]  # 坐标增减
#         coor[1] = coor[1] + coorC[1]  # 同上
#         print(userInfo[coor[0]][coor[1]], end=" ")# 输出
#         if coor == 0 or coor[1] == 0:# 推出条件
#             if coor[0] == 0:
#                 coor[1] = coor[1] + 1
#             else:
#                 coor[0] = coor[0] + 1
#             print(userInfo[coor[0]][coor[1]], end=" ")  # 输出
#             break
#         if coor[0] == (count-1) or coor[1] == (count-1):
#             if coor[0] == (count-1):
#                 coor[1] = coor[1] + 1
#             else:
#                 coor[0] = coor[0] + 1
#             print(userInfo[coor[0]][coor[1]], end=" ")  # 输出
#             break
#     if coor[0] == 0:# 增量改变方式
#         coorC[0] = -1
#         coorC[1] = 1
#     if coor[1] == 0:
#         coorC[0] = 1
#         coorC[1] = -1
coor = [0, 0]
coorx = [0, 0]
num = 0
numx = count - 1
fx = True
for item in range(0, count*2-1):# 斜面执行2n-1次
    if item < count:
        num = item
    else:
        num = numx - (item - numx) + 1
    if fx:
        if (num%2) == 0:
            coor[0] = num
            coor[1] = 0
        else:
            coor[0] = 0
            coor[1] = num
    else:
        if (num%2) == 0:
            coor[0] = num
            coor[1] = count-1
        else:
            coor[0] = count-1
            coor[1] = num
    if (count-1) == item:
        fx = False
    if item == (2*count-2):
        coor[0] = coor[1] = count-1
    print(userInfo[coor[0]][coor[1]], "-----------------", num ,coor)
