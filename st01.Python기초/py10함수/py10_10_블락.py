def get_sum(x, y):
    sum = 0
    for i in range(x, y+1, 1):
        sum = sum+i
        print(a)  # a 값은 없으나, 실행하면 3 출력(전역변수는 함수에서 접근이 가능하기 때문)
    return sum  # 나오는 값 : return 변수명

# 함수 호출


a = 3
b = 7
get_sum(a, b)


# 변수의 종류
# 전역변수 : a,b ==> 함수에서 접근이 가능하다. (if문, for문, 함수 등에 밖에 있는 변수)
# 지역변수 : i,sum,x,y(if문, for문, 함수 등 안에서 사용하는 변수, 매개변수이면 무조건 지역변수도 된다.)
# 매개변수 : x,y(함수에서 사용하는 변수)
