count = [int(item) for item in input().split()]

userIfo = []
for item in range(0, count[1]):# 存储用户数据
    userIfo.append([int(ite) for ite in input().split()])

def returnkey(map = {}):# 返回键
    return [item for item in map.keys()][0]

def returnValue(map = {}):# 返回值
    return  map[returnkey(map)]

def sorting(map=[]):# 排序列表里的map
    for item in range(0, map.__len__()-1):
        for ite in range(item, map.__len__()):
            if returnkey(map[item]) > returnkey(map[ite]):
                swap = map[ite]
                map[ite] = map[item]
                map[item] = swap

path = []# 地图存储
for item in range(0, count[1]):# 存储为map格式--（起始位置，[结束位置, {道路类型: 距离}])
    path.append({userIfo[item][1]:[userIfo[item][2], {userIfo[item][0]: userIfo[item][3]}]})# 地图整理
sorting(path)# 地图排序
# print(path)

data = []
def dfs(end, index, map=[]):
    global path
    global data
    if end == count[0]:
        data.append(map.copy())
    map.append(index)
    for item in range(end-1, path.__len__()):# 遍历所有元素
        if end == returnkey(path[item]):# 查询与上一个路口最后到达的
            map[index] = returnValue(path[item])[1]# 添加
            dfs(returnValue(path[item])[0],index+1,map)# 搜索
    del map[index]

def returnMin(data):# 遍历最小值
    xmin = None
    num = 0
    for item in range(0, data.__len__()):
        value = 0
        for ite in range(0, data[item].__len__()):
            if returnkey(data[item][ite]) == 0:
                value = value + (num*num)# 结算小路疲劳值
                num = 0# 统计完小路后置零，因为已经被大路中断
                value = value + returnValue(data[item][ite])# 大路疲劳值
            else:
                num = num + returnValue(data[item][ite]) # 累计小路疲劳值
        value = value + (num*num)
        num = 0# 置零操作
        if xmin == None:
            xmin = value
        else:
            if xmin > value:
                xmin = value
    return xmin

dfs(1, 0)
# print(data)
print(returnMin(data))