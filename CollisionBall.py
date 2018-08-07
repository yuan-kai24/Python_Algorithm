ballinfo = input()  # 第一行输入
ballpos = input()  # 第二行
ballinfo = ballinfo.split(" ")  # 拆分
ballpos = ballpos.split(" ")
ballmove = []  # 移动方向


def isMove():
    for itemi in range(0, len(ballpos)):
        if int(ballpos[itemi]) == int(ballinfo[1]) or int(ballpos[itemi]) == 0:
            ballmove[itemi] = -ballmove[itemi]
        for ite in range(itemi, len(ballpos)):
            if itemi != ite and int(ballpos[itemi]) == int(ballpos[ite]):
                ballmove[itemi] = -ballmove[itemi]
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
    print(" ".join([str(item) for item in ballpos]), end="")


main()