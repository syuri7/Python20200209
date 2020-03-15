
# 작업 순서 
# 1. 모듈 또는 클래스 import
# 2. main() 메서드 만들기 
#     인스턴스 생성
# 3. 이 모듈이 단독으로 사용되면 main()를 호출하라.
#    if __name__ == "__main__":
#    main()

# 코딩 하기 


import Circle

def main():
    circle = Circle.Circle(10) 
    print("원의 반지름 = ", circle.getRadius())
    print("원의 넓이 = ", circle.calcArea())
    print("원의 둘레 = ", circle.calcCircum())
    
if __name__ == "__main__":
    main()