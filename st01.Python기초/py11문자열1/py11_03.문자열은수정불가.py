# 문자열을 수정할 수 없다는 의미는
# 새롭게 메모리가 할당된다는 의미다.
# id() 메모리 주소 확인하는 함수

str1 = "abc"
print("str1 주소값 출력", id(str1))
print()

str2 = str1  # 주소값의 복사가 발생
print("str1 주소값 출력", id(str1))
print("str2 주소값 출력", id(str2))
print()

str1 = "efg"  # 신규 메모리가 할당된다.
print("str1 주소값 출력", id(str1))
print("str2 주소값 출력", id(str2))
print()
