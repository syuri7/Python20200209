# import 방식
# 모듈 import : import 모듈이름
# ==> 사용방법 : 모듈명.함수명     
# 함수 import : from 모듈이름 import 모듈함수
# ==> 사용방법 : 함수명
# as import

# 이 모듈이 단독으로 사용되면 main()를 호출하라.

import fibo # 같은 폴더에 있는 경우 파일명만



def main():
    # 사용방법 : 모듈명.함수명
    val = fibo.fib2(10)
    print(val)
    
if __name__ == "__main__":
    main()




