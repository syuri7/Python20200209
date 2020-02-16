#예외문 처리
#형변환 오류가 발생하는 문장을 정상 종료처리 하기 위해 
#try로 처리해서 오류 발생하지 않게...

# 숫자가 아닌 것을 정수로 변환하려고 할 때
try:
    i=int("안녕하세요")
    print(i) #문장이 실행되지 않음
except ValueError : #형변환시 발생하는 오류코드(종류) 입력
    pass #넘어간다.

# 숫자가 아닌 것을 실수로 변환 할 때
try:
    f=float("안녕하세요")
    print(f)
except ValueError :
    pass


# 소수점이 있는 숫자 형식의 문자열을 int() 함수로 변환 할 때
try:
    i=int("52.273")
    print(i)
except ValueError :
    pass