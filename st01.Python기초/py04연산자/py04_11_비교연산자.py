flag =True
print(flag)

flag = (2>3)
print(flag)

print(True)
print(False)

#글자의 비교연산자는 사전으로 이해하자.
#문자열도 비교 연산이 가능하다.
print("가방" < "하마") #True
print("가방" > "하마") #False

x=25
print(10<x<30) #True --파이썬에서만 지원
print(10<x and x<30) #True

print(40<x<60) #False --파이썬에서만 지원
print(40<x and x<60) #True