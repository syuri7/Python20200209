x=input("x값을 입력하세요>>")
x=int(x)
y=input("y값을 입력하세요>>")
y=int(y)

print("교환 전:",x,y)

temp=x
x=y
y=temp

print("교환 후:",x ,y)