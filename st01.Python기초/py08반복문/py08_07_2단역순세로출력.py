Number = input("Number:")
Number = int(Number)


for x in range(9, 0, -1):
    str = "%s*%s=%2s" % (Number, x, Number*x)
    print("Result:")
    print(str)
