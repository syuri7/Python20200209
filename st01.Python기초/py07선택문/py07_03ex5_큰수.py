x=input("첫 번째 정수:")
x=int(x)
y=input("두 번째 정수:")
y=int(y)



if x>y:
    print("큰 수는", x)
else: # x=y면 여기에 걸림
    print("큰 수는", y)
    
    
if x>y:
    print("큰 수는", x)
elif x==y:
    print("x=y이며, 입력된 숫자는", x)
else: 
    print("큰 수는", y)
    