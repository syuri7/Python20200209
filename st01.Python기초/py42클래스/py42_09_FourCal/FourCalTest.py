
# 작업 순서
# 1. 모듈 또는 클래스 import
# 2. main() 메서드 만들기
#     인스턴스 생성
# 3. 이 모듈이 단독으로 사용되면 main()를 호출하라.
#    if __name__ == "__main__":
#    main()

# 코딩 하기

import FourCal


def main():
    four = FourCal.FourCal(2, 4)
    print("First num : ", four.getFirst())
    print("Second num : ", four.getSecond())
    print("Add : ", four.add())
    print("Minus : ", four.min())
    print("Mul : ", four.mul())
    print("Div : ", four.div())
    print(four.__str__())
    print(four.self_to_string())


if __name__ == "__main__":
    main()
