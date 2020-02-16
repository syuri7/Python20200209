
# 포매팅 연산자( %) 에 사용 가능한 기호들에 대해 알아본다.
#
# 포맷 문자열	설명
# %s	문자열 (str() 함수를 이용한다.)
# %d	10진 정수(int() 함수를 이용한다.)
# %f	10진 실수(float()함수를 이용한다.)


# 문자열 포매팅 

print("I eat %d apples." %3) #'I eat 3 apples.'


number = 10
day = "three"
print("I ate %d apples. so I was sick for %s days." % (number, day)) 
# 'I ate 10 apples. so I was sick for three days.'


# 정렬과 공백(사용빈도 높음)

print("%10s" % "hi")  # '        hi'
print("%-10sjane." % 'hi')  # 'hi        jane.'


# 소수점 표현
print("%0.4f" % 3.42134234)  # '3.4213'
print("%10.4f" % 3.42134234)  # '    3.4213'
