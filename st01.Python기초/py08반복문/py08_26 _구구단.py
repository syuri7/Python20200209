x = input("시작 단수를 입력하세요:")
y = input("종료 단수를 입력하세요:")

x = int(x)
y = int(y)

if x>y:
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


x = input("시작 단수를 입력하세요:")
y = input("종료 단수를 입력하세요:")

x = int(x)
y = int(y)

if x>y:
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
