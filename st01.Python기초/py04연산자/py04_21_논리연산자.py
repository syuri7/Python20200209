x=3
y=4

r=((x==3) and (y==3)) #False
print("(x==3) and (y==3)): ", r)

r=((x==3) and (y!=3)) #True
print("(x==3) and (y!=3)): ", r)

r=((x==3) or (y==3)) #True
print("(x==3) or (y==3)): ", r)

r=((x==3) and (y==4)) #True
print("(x==3) and (y==4)): ", r)


