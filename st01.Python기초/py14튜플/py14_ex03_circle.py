# 원의 넓이와 둘레를 동시에 반환하는 함수를 작성해 본다.
# 예시)

import math  # PI=3.14..............변수를 사용하기 위해서 import


def circle(radius):
    면적 = math.pi * radius
    둘레 = 2*math.pi * radius
    return(면적, 둘레)  # 튜플로 자료구조 1개를 리턴하는 것이다.


def main():
    str = input("원의 반지름을 입력하시오 : ")
    radius = float(str)  # 문자열을 실수로 형변환
    # 원의 넓이와 둘레를 계산한다.
    (x, y) = circle(radius)  # x==면적, y==둘레
    tmp = "원의 넓이는 %10.4f, 둘레는 %10.4f이다" % (x, y)
    print(tmp)

# main 함수 호출


if __name__ == "__main__":
    main()
