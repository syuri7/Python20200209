# 사용자 함수 만들기
# 양의 정수가 소수가 되려면 1과 자신만을 약수로 가져야 한다. 예를 들어서 17은 1과 17만이 약수이므로 소수이다.
# 소수를 판별하는 함수 isprime()을 작성하여 사용하여 보자.
# 사용자로 부터 정수를 입력 받아서 변수 n에 저장한다.
#
# i를 2부터 n까지 1씩 증가시키면서
#     n을 I 로 나누어 나머지가 0인지 본다.
#     나머지가 0이면 약수가 있는 것이므로  소수가 아니다.
#
# 반복이 정상적으로 종료되고 나머지가 0인 수가 없다면 소수이다.
#


def isprime(n):
    for i in range(2, n, 1):
        if n % i == 0:
            return False
    return True


def myinput(mesg):
    try:  # 예외처리
        n = input(mesg)
        n = int(n)
    except ValueError as ex:
        print(ex)

    return n


def main():
    # 입력 처리
    n = myinput("숫자를 입력하세요.")
    n = int(n)

    # 결과출력
    prime = isprime(n)
    print("%s 소수 여부 >>" % n, prime)


main()

# 도전. 위의 코드를 이용하여 1부터 100 사이의 모든 소수를 찾는 코드를 작성하시오.

for n in range(1, 100, 1):
    prime = isprime(n)
    print("%s 소수 여부 >>" % n, prime)
