usercount = int(input())
chess = []  # 棋局情况
resualt = [0 for item in range(0, usercount)]  # 结果存储
index = 0  # 当前计算的局数
status = []  # 记忆

def init():
    newChess = []
    for item in range(1, usercount*3+1):
        newc = input()
        newChess.append(newc.split(" "))
        if item % 3 == 0:
            chess.append(newChess)
            newChess = []


def res(val, num):
    num = num + 1
    if val == "2":
        num = -num
    if abs(num) > resualt[index]:
        resualt[index] = num


def findz(val, v):
    count = 0
    for item in range(0, 3):
        for item2 in range(0, 3):
            if val[item][item2] == "0":
                count = count + 1
    res(v, count)

def pd(val):
    if val[0][0] == val[0][1] == val[0][2] != '0':  # 横1
        findz(val, val[0][0])
        return True
    if val[1][0] == val[1][1] == val[1][2] != '0':  # 横2
        findz(val, val[1][0])
        return True
    if val[2][0] == val[2][1] == val[2][2] != '0':  # 横3
        findz(val, val[2][0])
        return True

    if val[0][0] == val[1][0] == val[2][0] != '0':  # 竖1
        findz(val, val[0][0])
        return True
    if val[0][1] == val[1][1] == val[2][1] != '0':  # 竖2
        findz(val, val[0][1])
        return True
    if val[0][2] == val[1][2] == val[2][2] != '0':  # 竖3
        findz(val, val[0][2])
        return True

    if val[0][0] == val[1][1] == val[2][2] != '0':  # 正斜
        findz(val, val[0][0])
        return True
    if val[0][2] == val[1][1] == val[2][0] != '0':  # 反斜
        findz(val, val[0][2])
        return True
    if not '0' in val[0] and not '0' in val[1] and not '0' in val[2]:
        return True
    if '0' in val[0] and '0' in val[1] and '0' in val[2]:
        return True
    return False


def dp(val, count):
    if pd(val):
        return

    if val in status:
        return
    for item in range(0, 3):
        for ite in range(0, 3):
            if val[item][ite] == '0':
                if count % 2 == 0:
                    val[item][ite] = '1'
                else:
                    val[item][ite] = '2'
                status.append(val)
                dp(val, count+1)
                val[item][ite] = '0'


def main():
    init()
    for item in range(0, usercount):
        global status
        status = []
        global index
        index = item
        dp(chess[item], 0)


main()
print("\r\n".join(str(item) for item in resualt))