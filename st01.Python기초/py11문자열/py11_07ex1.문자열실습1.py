
# 0번째부터 12번째 자리까지 있음.
# prov 길이는 13이다.
prov = "A barking Dog"


#################################
# 문자열 함수 / 문자열 메서드
#################################

# 문자열 길이: len().  prov의 길이를 출력하시오
length = len(prov)
print("prove 문자열 길이:", length)


print("---------------------------")

# 첫번째 b 문자를 찾고 위치를 출력하시오.
# 위치 찾는 메서드 : find(), index()
# find()를 사용 ==> 이유는 find()는 찾는 값이 없으면 -1을 리턴, index()는 에러메시지 출력
pos1 = prov.find("b")  # 있으면 0이나 양수, 없으면 -1을
print("첫번째 b 문자의 위치는:", pos1)

print("---------------------------")

# 문자열에 "Dog"가 있으면 "Dog있음"을 없으면 "Dog없음" 을 출력하시오
# "Dog 있음"
if prov.find("Dog") >= 0:
    print("Dog있음")
else:
    print("Dog없음")

print("---------------------------")

# 또는

if prov.find("Dog") == -1:
    print("Dog없음")
else:
    print("Dog있음")

print("---------------------------")

# 문자열 치환: replace()
# prov 문자열에 Dog가 들어 있으면 Cat으로 바꾸어 출력하고
# 아니면 prov 출력하시오.

# 없으면 Dog가 나오므로, 굳이 아래와 같이 if문 안써도 결과는 똑같음
str = prov.replace("Dog", "Cat")
print(str)

print("---------------------------")

if prov.find("Dog") >= 0:
    s07 = prov.replace("Dog", "Cat")
    print(s07)
else:
    print(prov)

print("---------------------------")

# 또는

if prov.find("Dog") == 0:
    print(prov)
else:
    s07 = prov.replace("Dog", "Cat")
    print(s07)

print("---------------------------")

# 문자열 prov 를 공백을 기준으로 자르고 그 결과를 출력하시오.
arr = prov.split(" ")
print(type(arr), arr)

print("---------------------------")

for i in arr:
    print(i, end=", ")
