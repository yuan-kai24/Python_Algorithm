user = input()
user = user.split(" ")
photo = []
for item in range(0, int(user[0])):
    userin = input()
    photo.append(userin.split(" "))

countx = int(user[1])-1
while countx >= 0:
    for item in range(0, int(user[0])):
        print(photo[item][countx], end=" ")
    print()
    countx = countx - 1