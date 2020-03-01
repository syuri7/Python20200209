def add(x,y): # x,y는 매개변수라고 칭한다.
    result = x+y
    return result

a=3
b=4
value = add(a,b) # a,b는 인자라고 칭한다.
print(value)

# a,b와 x,y는 다름. 메모리도 다른데 저장
# 디버깅시 함수는 F11(F5 후에 F11 누르면 함수로 들어감), CALL STACK에서 확인