

# 满分版本。。。
A = []


def rck(i, val):  # 横
    return val == A[i][0] == A[i][1] == A[i][2]


def cck(j, val):  # 竖
    return val == A[0][j] == A[1][j] == A[2][j]


def dck(val):  # 斜
    return (A[0][0] == val == A[1][1] == A[2][2]) or (A[0][2] == val == A[1][1] == A[2][0])


def zeroCpt():
    res = 0
    for item in range(0, 3):
        for ite in range(0, 3):
            if A[item][ite] == 0:
                res = res + 1
    if res == 9:
       return 0
    else:
       return res


def win(player):
    r = rck(0, player) or rck(1, player) or rck(2, player)
    c = cck(0, player) or cck(1, player) or cck(2, player)
    d = dck(player)
    w = r or c or d
    if not w:
        return 0
    w = zeroCpt() + 1
    return player == 1 and w or -w


def dfs(player):
    if zeroCpt() == 0:
        return 0
    Min = 10
    Max = -10
    global A
    for item in range(0, 3):
        for ite in range(0, 3):
            if A[item][ite] == 0:
                A[item][ite] = player
                w = win(player)
                if w != 0:
                    A[item][ite] = 0
                    if w > 0:
                        return max(Max, w)
                    else:
                        return min(Min, w)
                if player == 1:
                    Max = max(Max, dfs(2))
                else:
                    Min = min(Min, dfs(1))
                A[item][ite] = 0
    if player == 1:
        return Max
    else:
        return Min


def main1():
    T = int(input())
    global A
    while T > 0:
        for item in range(0, 3):
            A.append(input().split())
            for ite in range(0, 3):
                A[item][ite] = int(A[item][ite])
        x = win(1)
        y = win(2)
        if x != 0:
            print(x)
        elif y != 0:
            print(y)
        else:
            print(dfs(1))
        A = []
        T = T-1



# 90分版本。。。。无语（----------逻辑没问题----------）
usercount = int(input())  # 用户输入
chess = []  # 棋局存储


def init():  # 用户输入
    newChess = []
    for item in range(1, usercount*3+1):
        newc = input()
        newChess.append(newc.split())
        if item % 3 == 0:  # 每三行（一局棋盘）录入一次
            chess.append(newChess)
            newChess = []


def findspa(val, v):  # 查询空格
    count = 0
    for item in range(0, 3):
        for item2 in range(0, 3):
            if val[item][item2] == "0":  # 记录空格
                count = count + 1
    count = count + 1
    if v == '1':
        return count
    else:
        return -count


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
    if ['0', '0', '0'] == val[0] == val[1] == val[2]:  # emmmm
        return 0
    if not '0' in val[0] and not '0' in val[1] and not '0' in val[2]:
        return 0
    return fenshu


def dfs(val, count):
    if win(val) == 0:
        return 0
    Max = -10  # 策略1号最优
    Min = 10  # 策略2号最优
    for item in range(0, 3):
        for ite in range(0, 3):
            if val[item][ite] == '0':  # 判断是否可以落子
                val[item][ite] = str(count)
                w = win(val)
                if w != -10:  # 判断胜负
                    val[item][ite] = '0'
                    if w > 0:
                        return max(w, Max)
                    else:
                        return min(w, Min)

                if count == 1:  # 判断下棋人
                    Max = max(Max, dfs(val, 2))
                else:
                    Min = min(Min, dfs(val, 1))
                val[item][ite] = '0'  # 回溯
    if count == 1:
        return Max
    else:
        return Min


def main2():
    init()
    for item in range(0, usercount):  # 棋局分配
        w = win(chess[item])
        if w != -10:
            print(w)
        else:
            print(dfs(chess[item], 1))


main2()