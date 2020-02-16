x=3
y=4

r=((x==3) and (y==3)) #True and False
print("(x==3) and (y==3)): ", r) #False

r=((x==3) and (y!=3)) #True and True
print("(x==3) and (y!=3)): ", r) #True

r=((x==3) or (y==3)) #True or False
print("(x==3) or (y==3)): ", r) #True

r=((x==3) or (y==4)) #True or True
print("(x==3) or (y==4)): ", r) #True

r=((x!=3) or (y==4)) #False or True
print("(x!=3) or (y==3)): ", r) #True

r=((x!=3) or (y!=4)) #False or False
print("(x!=3) or (y!=4)): ", r) #False


#변수 선언과 초기화
x=3
y=4
print((x==y) and (x!=y)) #False and True -> False
print((x>y) or (x<y)) #False and True -> True
print((x>=y) or (x<=y)) #False or True -> True
print((x==y) and (x!=y) or (x<y)) #False and True or True -> True