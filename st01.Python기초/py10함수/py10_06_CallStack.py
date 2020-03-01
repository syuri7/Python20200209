# 함수의 호출과 Stack 메모리 구조를 이해한다.
# 함수가 호출될 때마다 Stack 에 쌓이게 된다.


def secondMethod():
    print("secondMethod()")


def firstMethod():
    secondMethod()


def main():
    firstMethod()


main()
