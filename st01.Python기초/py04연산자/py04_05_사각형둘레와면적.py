#아래와 같이 나눠서 표현 가능
w=input("사각형의 가로를 입력하시오: ") #문자열
h=input("사각형의 세로를 입력하시오: ") #문자열

w=float(w) #문자열을 실수로 전환
h=float(h) #문자열을 실수로 전환

area = w*h
perimeter = 2*(w+h)

print("사각형의 넓이: ", area)
print("사각형의 둘레: ", perimeter)


#아래와 같이 합쳐서 표현보다는 위와 같이 표현...!!!
w=float(input("사각형의 가로를 입력하시오: "))
h=float(input("사각형의 세로를 입력하시오: "))


area = w*h
perimeter = 2*(w+h)

print("사각형의 넓이: ", area)
print("사각형의 둘레: ", perimeter)


#형변환 오류인 경우 => 예외문 처리

w=input("사각형의 가로를 입력하시오: ") #문자열
h=input("사각형의 세로를 입력하시오: ") #문자열

try:
    w=float(w) #문자열을 실수로 전환
    h=float(h) #문자열을 실수로 전환
except ValueError :
    pass

area = w*h
perimeter = 2*(w+h)

print("사각형의 넓이: ", area)
print("사각형의 둘레: ", perimeter)



