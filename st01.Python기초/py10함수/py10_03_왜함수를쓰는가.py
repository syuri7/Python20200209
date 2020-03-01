# 1부터 10까지의 합계를 구하고
# 그 합계를 sum에 저장하고 sum 값을 한번만 출력한다.

sum1 = 0
for i in range(1, 11, 1):
    sum1 = sum1+i
str = "%s부터 %s까지의 합계" % (1, 10)
print(str, sum1)


# 1부터 100까지의 합계를 구하고
# 그 합계를 sum2 에 저장하고 sum2 값을 한번만 출력한다.

sum2 = 0
for j in range(1, 101, 1):
    sum2 = sum2+j
str = "%s부터 %s까지의 합계" % (1, 100)
print(str, sum2)


# 100부터 sum2까지의 합계를 구하고
# 그 합계를 sum3 에 저장하고 sum3 값을 한번만 출력한다.

sum3 = 0
for k in range(100, sum2+1, 1):
    sum3 = sum3+k
str = "%s부터 %s까지의 합계" % (100, sum2)
print(str, sum3)

print("--------------------------------------")


# 반복되는 코드는 함수로 만들어서 사용한다.
# get_sum()
# 함수에서 바뀌는 값, 입력으로 처리한다.입력이란 매개 변수다.
# 매개 변수는 함수에서 입력으로 사용되는 변수다.

def get_sum(x, y):
    sum = 0
    for i in range(x, y+1, 1):
        sum = sum+i
    str = "%s부터 %s까지의 합계" % (x, y)
    print("함수출력", str, sum)
    return sum  # 나오는 값 : return 변수명


# 함수 호출 == 함수 사용
sum1 = get_sum(1, 10)  # 1부터 10까지의 합계를 구하고 출력
sum2 = get_sum(1, 100)  # 1부터 100까지의 합계를 구하고 출력
sum3 = get_sum(100, sum2)  # 100부터 sum2까지의 합계를 구하고 출력
