# 사용자 함수 만들기
# 두 개의 정수가 주어지면 두수 중에서 더 큰 수를 찾아서 이것을 반환하는 함수를 만들어보자. 


# 함수정의
# x : 매개변수
# y : 매개변수

def getmax(x, y):
    if x>y:
        return x # x 반환
    else:
        return y # y 반환
    
# return은 한 번만 사용하는게 좋음
def getmax(x, y):
    result = None # None : 값이 없다.
    
    if x>y:
        result = x # x 반환
    else:
        result = y # y 반환
    
    return result

n1 = input("첫번째 정수 입력 : ")
n1 = int(n1)

n2 = input("두번째 정수 입력 : ")
n2 = int(n2)

# 똑같은 코드는 함수로 만듬

def myinput() :
    n1 = input("첫번째 정수 입력 : ")
    n1 = int(n1)
    return n1

n1 = myinput()

# 입력받는 정수의 메시지가 다르므로, mesg처리
def myinput(mesg) :
    try:  # 예외처리
        n1 = input(mesg)
        n1 = int(n1)        
    except ValueError as ex:
        print(ex)

    return n1


# 입력 처리
n1 = myinput("첫번째 정수 입력: ")
n2 = myinput("두번째 정수 입력: ")

# 최대값 출력

val = getmax(n1, n2)
print(val)


# 입력처리, 최대값 출력을 main 함수에 넣어서 사용
# 왜 main 함수를 만들어 사용하는가?
# 프로그래맹에서 지향하는 방식은 전역변수를 사용하지 않는다.

def main():
    # 입력 처리
    n1 = myinput("첫번째 정수 입력: ")
    n2 = myinput("두번째 정수 입력: ")

    # 최대값 출력

    val = getmax(n1, n2)
    print(val)


main()