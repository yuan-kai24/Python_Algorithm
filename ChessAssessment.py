usercount = int(input())  # 用户输入
chess = []  # 棋局存储
resualt = [0 for item in range(0, usercount)]  # 结果初始化
index = 0  # 棋局编号（存储结果用）
status = []  # 状态存储（动态规划用，去重）


def init():  # 用户输入
    newChess = []
    for item in range(1, usercount*3+1):
        newc = input()
        newChess.append(newc.split(" "))
        if item % 3 == 0:  # 每三行（一局棋盘）录入一次
            chess.append(newChess)
            newChess = []


def res(val, num):  # 结果
    num = num + 1
    if val == "2":
        num = -num
    if abs(num) > resualt[index]:
        resualt[index] = num


def findz(val, v):  # 查询
    count = 0
    for item in range(0, 3):
        for item2 in range(0, 3):
            if val[item][item2] == "0":  # 记录null
                count = count + 1
    res(v, count)


def pd(val):
    if val[0][0] == val[0][1] == val[0][2] != '0':  # 一
        findz(val, val[0][0])
        return True
    if val[1][0] == val[1][1] == val[1][2] != '0':  # 二
        findz(val, val[1][0])
        return True
    if val[2][0] == val[2][1] == val[2][2] != '0':  # 三
        findz(val, val[2][0])
        return True

    if val[0][0] == val[1][0] == val[2][0] != '0':  # I
        findz(val, val[0][0])
        return True
    if val[0][1] == val[1][1] == val[2][1] != '0':  # II
        findz(val, val[0][1])
        return True
    if val[0][2] == val[1][2] == val[2][2] != '0':  # III
        findz(val, val[0][2])
        return True

    if val[0][0] == val[1][1] == val[2][2] != '0':  # 斜
        findz(val, val[0][0])
        return True
    if val[0][2] == val[1][1] == val[2][0] != '0':  # 反
        findz(val, val[0][2])
        return True
    if not '0' in val[0] and not '0' in val[1] and not '0' in val[2]:  # end
        return True
    if '0' in val[0] and '0' in val[1] and '0' in val[2]:  # all null
        return True
    return False


def dp(val, count):
    if pd(val):
        return
    if val in status:  # 去重
        return
    for item in range(0, 3):
        for ite in range(0, 3):
            if val[item][ite] == '0':
                if count % 2 == 0:
                    val[item][ite] = '1'
                else:
                    val[item][ite] = '2'
                status.append(val)  # 记录走过的步数
                dp(val, count+1)
                val[item][ite] = '0'  # 回溯


def main():
    init()
    for item in range(0, usercount):  # 棋局传送
        global status
        status = []
        global index
        index = item  # 更新编号
        dp(chess[item], 0)
    print("\r\n".join(str(item) for item in resualt))  # 结果

main()
