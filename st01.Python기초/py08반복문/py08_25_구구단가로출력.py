#2단부터 19단까지 1씩 증가시키면서
  #1부터 9까지 1씩 증가시키면서
    #구구단을 출력하시오.

for i in range(2,20,1):
    for j in range(1,10,1):
        str="%2s*%s=%3s" %(i,j,i*j) #%2s, %3s는 자리수를 맞추기 위해서
        if j==9 :
            print(str, end=".")
        else:
            print(str,end=",")
    print()

print("--------------------")        