# 2단의 구구단을 출력하는 프로그램을 만드시오.
# 1부터 9까지 2단의 구구단을 출력하시오.
# rang()함수를 사용한다.

for x in range(1,10,1):
    print("2*",x,"=",2*x)
    

for x in range(1,10,1):
    print("2*%s=%2s" %(x, 2*x))

for x in range(1,10,1):
    print("2*%d=%2d" %(x, 2*x))