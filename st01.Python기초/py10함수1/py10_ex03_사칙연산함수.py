def Add(first, second):
    result = first + second
    return result  # 결과 반환


def Minus(first, second):
    result = first - second
    return result  # 결과 반환


def Mul(first, second):
    result = first * second
    return result  # 결과 반환


def Div(first, second):
    result = first / second
    return result  # 결과 반환


# 입력 받기

x = input("First num : ")
y = input("Second num : ")

# 문자열 정수변환
x = int(x)
y = int(y)

# Add 함수 호출
value = Add(x, y)
print("Add:", value)  # Add() 결과 출력

# Minus 함수 호출
value = Minus(x, y)
print("Minus:", value)  # Minus() 결과 출력

# Mul 함수 호출
value = Mul(x, y)
print("Mul:", value)  # Mul() 결과 출력

# Div 함수 호출
value = Div(x, y)
print("Div:", value)  # Div() 결과 출력
