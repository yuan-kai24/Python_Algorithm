user = input()
user = user.split(" ")# 输入格式拆分
photo = []
for item in range(0, int(user[0])):
    userin = input()
    photo.append(userin.split(" "))# 以行为单位存储数据

countx = int(user[1])-1
while countx >= 0:
    for item in range(0, int(user[0])):# 从行最后反向从列遍历
        print(photo[item][countx], end=" ")
    print()# 换行
    countx = countx - 1 # 递减
