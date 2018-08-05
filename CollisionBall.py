ballinfo = input()  # 第一行输入
ballpos = input()  # 第二行
ballinfo = ballinfo.split(" ")  # 拆分
ballpos = ballpos.split(" ")
ballmove = []  # 移动方向


def isMove():
    for item in range(0, len(ballpos)):
        if int(ballpos[item]) == int(ballinfo[1]) or int(ballpos[item]) == 0:
            ballmove[item] = -ballmove[item]
        for ite in range(item, len(ballpos)):
            if item != ite and int(ballpos[item]) == int(ballpos[ite]):
                ballmove[item] = -ballmove[item]
                ballmove[ite] = -ballmove[ite]


def main():
    for item in ballpos:
        ballmove.append(1)  # 初始化
    count = 0
    while count < int(ballinfo[2]):
        for item in range(0, len(ballpos)):
            ballpos[item] = int(ballpos[item]) + ballmove[item]
        isMove()
        count = count + 1


main()
print(" ".join([str(item) for item in ballpos]))