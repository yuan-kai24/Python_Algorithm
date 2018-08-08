import time

usercount = int(input())  # 用户输入
chess = []  # 棋局存储


def init():  # 用户输入
    newChess = []
    for item in range(1, usercount*3+1):
        newc = input()
        newChess.append(newc.split(" "))
        if item % 3 == 0:  # 每三行（一局棋盘）录入一次
            chess.append(newChess)
            newChess = []


def findspa(val, v):  # 查询空格
    count = 0
    for item in range(0, 3):
        for item2 in range(0, 3):
            if val[item][item2] == "0":  # 记录空格
                count = count + 1
    if count == 0:  # 棋局下完，平局情况
        return count
    count = count + 1
    return v == '1' and count or -count


def win(val):  # 判断胜负
    fenshu = -10
    for item in range(0, 3):  # 横向
            if val[item][0] == val[item][1] == val[item][2] != '0':
                fenshu = findspa(val, val[item][0])

    for item in range(0, 3):  # 纵向
        if val[0][item] == val[1][item] == val[2][item] != '0':
            fenshu = findspa(val, val[0][item])

    if val[0][0] == val[1][1] == val[2][2] != '0':  # 斜
        fenshu = findspa(val, val[0][0])
    if val[0][2] == val[1][1] == val[2][0] != '0':  # 反
        fenshu = findspa(val, val[0][2])
    if not '0' in val[0] and not '0' in val[1] and not '0' in val[2]:  # end
        return 0
    if ['0', '0', '0'] == val[0] == val[1] == val[2]:  # emmmm
        return 0
    return fenshu


def dp(val, count):
    Max = 0  # 策略1号最优
    Min = 0  # 策略2号最优
    for item in range(0, 3):
        for ite in range(0, 3):
            if val[item][ite] == '0':  # 判断是否可以落子
                w = win(val)
                if w != -10:  # 判断胜负
                    return w > 0 and max(w, Max) or min(w, Min)  # 选极值
                if count == 1:  # 判断下棋人
                    val[item][ite] = '1'
                    Max = dp(val, 2)
                else:
                    val[item][ite] = '2'
                    Min = dp(val, 1)
                val[item][ite] = '0'  # 回溯
    return count == 1 and Min or Max


def main():
    init()
    # start = time.clock()
    for item in range(0, usercount):  # 棋局分配
        print(dp(chess[item], 1))
    # end = time.clock()
    # print(end-start)
main()