

# 跳一跳
def jump():
    scan = input()
    scan = scan.split(" ")

    jump = 0
    tag = 1

    for num in scan:
        if num == "0":
            break
        if num == "1":
            tag = 1
            jump = jump + tag
        if num == "2":
            if tag == 1:
                tag = 2
            else:
                tag = tag + 2
            jump = jump + tag

    print(jump)


def main():
    jump()


main()
