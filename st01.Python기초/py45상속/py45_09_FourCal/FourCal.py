
# 작업 순서 
# 1. 모듈 또는 클래스 import
# 2. 클래스명은 파스칼 표기법으로 정한다. 첫글자는 대문자로.
#     생성자 선언 : 인스턴스가 생성될 때 실행
#     소멸자 선언 : 소멸자는 인스턴스가 소멸할 때 실행
#     __str__() 메서드 오버라이딩
#     접근자( getter ) 메서드 선언. 비공개 인스턴스 변수 읽기
#     설정자( setter ) 메서드 선언. 비공개 인스턴스 변수 수정
#     사용자 메서스 선언
# 3. main() 메서드 만들기 
#     인스턴스 생성
# 4. 이 모듈이 단독으로 사용되면 main()를 호출하라.
#    if __name__ == "__main__":
#    main()


# 코딩 하기 


# 작업 순서 
# 1. 모듈 또는 클래스 import
# 2. 클래스명은 파스칼 표기법으로 정한다. 첫글자는 대문자로.
#     생성자 선언 : 인스턴스가 생성될 때 실행
#     소멸자 선언 : 소멸자는 인스턴스가 소멸할 때 실행
#     __str__() 메서드 오버라이딩
#     접근자( getter ) 메서드 선언. 비공개 인스턴스 변수 읽기
#     설정자( setter ) 메서드 선언. 비공개 인스턴스 변수 수정
#     사용자 메서스 선언
# 3. main() 메서드 만들기 
#     인스턴스 생성
# 4. 이 모듈이 단독으로 사용되면 main()를 호출하라.
#    if __name__ == "__main__":
#    main()


# 코딩 하기 


class FourCal:
    def __init__(self, first, second):
        self.__first = first
        self.__second = second
    
    def add(self):
        result = self.__first + self.__second
        return result
    
    def min(self):
        result = self.__first - self.__second
        return result
    
    def mul(self):
        result = self.__first * self.__second
        return result

    def div(self):
        result = self.__first / self.__second
        return result
                    
    def getFirst(self):  # getter을 만들때는 get변수명(변수명에서 첫글자는 대문자로)
        return self.__first
    
    def getSecond(self):  # getter을 만들때는 get변수명(변수명에서 첫글자는 대문자로)
        return self.__second
    
    # setter 사용법 확인 필요
    def setFirst(self, first):  
        self.__first = first
        
    def setSecond(self, second):  
        self.__first = second
    
    
    def __str__(self):
        add = self.__first + self.__second
        str = "first : %s, second : %s, add : %s" %(self.__first, self.__second, add)
        return str

    def self_to_string(self):
        add = self.__first + self.__second
        str1 = "first : %s, second : %s, add : %s" %(self.__first, self.__second, add)
        return str1

    
def main():
    print()

if __name__ == "__main__":
    main()