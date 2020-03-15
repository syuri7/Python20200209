
# 작업 순서 
# 1. 모듈 또는 클래스 import
# 2. main() 메서드 만들기 
#     인스턴스 생성
# 3. 이 모듈이 단독으로 사용되면 main()를 호출하라.
#    if __name__ == "__main__":
#    main()

# 코딩 하기 

import Counter

def main():
    instance1 = Counter.Counter() # 파일명(모듈명).
    print(instance1.__str__())
    
    instance1.increment()
    instance1.increment()
    
    count = instance1.getCount()
    print("count", count)
    print(instance1.__str__())
    
if __name__ == "__main__":
    main()
   
    