a=input("a입력")
b=input("b입력")

#문자열에 *,+ 연산자가 있다.
#문자열에는 / 연산자가 없다.



try:
    a=int(a)
    b=int(b)
    avg = (a+b)/2
except ValueError:
    pass


if avg>=160:
    print("합격")
else:
    print("불합격")
    
print("종료")
