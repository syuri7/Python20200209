
# 0번째부터 12번째 자리까지 있음.
# prov 길이는 13이다.
prov = "A barking Dog"


#################################
# 문자열 함수 / 문자열 메서드
#################################

# 문자열 길이: len() . 13이 출력
length = len(prov)
print("prov 문자열 길이: ", length)

# find 이용하여 첫번째 b 문자를 찾고 출력하시오.
찾기 = prov.find("b")
print("첫번째 b문자의 위치는: ", 찾기)

# 문자열 포함 여부 확인: find()
# 문자열에 "Dog"가 있으면 "Dog 있음"을 없으면 "Dog 없음" 을 출력하시오.
if prov.find("Dog") >= 0:
    print("Dog있음")
else:
    print("Dog없음")



# 문자열 치환: replace()
# Dog - -> Cat 으로 바꾸시오
치환 = prov.replace("Dog","Cat")
 


# prov 문자열에 Dog가 들어 있으면 Cat으로 바꾸어 출력하고
# 아니면 prov 출력하시오.

if prov.find("Dog") >= 0:
    치환 = prov.replace("Dog","Cat")
    print(치환)
else:
    print(prov)

# 문자열 치환: replace(). 정규표현식을 사용한 패턴 치환
# 정규 표현식: ^ - -> 시작
# $ - -> 끝
# []


# 문자열 prov 를 공백을 기준으로 자르고 결과를 출력하시오.
# 문자열 자르기: split()은 리스트로 돌려준다.
# 지정한 문자로 문자열을 나눈다.(리스트로 반환)
공백 = prov.split(" ")
for i in 공백:
    print(i, end=", ")

