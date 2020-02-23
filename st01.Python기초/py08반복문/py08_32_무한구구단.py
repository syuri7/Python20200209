while True:
    x = input("시작 단수를 입력하세요:")
    y = input("종료 단수를 입력하세요:")

    # 예외문 처리 - 단수 대신 문자가 입력될 경우 int 처리시 에러가 발생하므로, 예외처리문 넣기
    try:
        x = int(x)
        y = int(y)
    except ValueError as identifier:
        break

    if x <= 0 or y <= 0:
        break

    if x > y:
        temp = x
        x = y
        y = temp

    for i in range(x, y+1, 1):
        for j in range(1, 10, 1):
            str = "%2s*%s=%3s" % (i, j, i*j)
            if j == 9:
                print(str, end=".")
            else:
                print(str, end=",")
        print()


print("--------------------")
