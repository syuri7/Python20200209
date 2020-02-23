# 중첩 for문
for i in range(2,20,1):
    for j in range(1,10,1):
        str="%2s*%s=%3s" %(i,j,i*j) #%2s, %3s는 자리수를 맞추기 위해서
        print(str)


print("--------------------")        