a=input("첫번째수를 입력하세요.:")
b=input("두번째수를 입력하세요.:")
c=input("세번째수를 입력하세요.:")

a=int(a)
b=int(b)
c=int(c)

#중첩 IF방식  

if a>=b:
    if a>=c:
        print("입력 받은 수 중 가장 큰 수는",a, "입니다")
    else:
        print("입력 받은 수 중 가장 큰 수는", c, "입니다")
else:
    if b>=c:
        print("입력 받은 수 중 가장 큰 수는",b, "입니다")
    else:
        print("입력 받은 수 중 가장 큰 수는", c, "입니다")

#연속 IF방식
        
if a>=b and a>=c:
    print("입력 받은 수 중 가장 큰 수는",a, "입니다")
elif a<=b and b>=c:
    print("입력 받은 수 중 가장 큰 수는",b, "입니다")
else:
    print("입력 받은 수 중 가장 큰 수는", c, "입니다")
