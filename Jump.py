

# 跳一跳
def jump():
    scan = input()
    scan = scan.split(" ")

    jump = 0
    tag = 1

    for num in scan:
        if num == "0":# 等于零时退出
            break
        if num == "1":# 跳上去，没跳到中心情况
            tag = 1
            jump = jump + tag
        if num == "2":# 跳到中心情况
            if tag == 1:# 第一次跳到中心
                tag = 2
            else:# 第二次后跳到中心
                tag = tag + 2
            jump = jump + tag# 加分

    print(jump)


def main():
    jump()


main()