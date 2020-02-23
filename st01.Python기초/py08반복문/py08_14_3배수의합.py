i = 1
sum = 0

for i in range(1,101,1):
    #3의 배수이면 sum을 아니면 pass
    #3의 배수 <==> i%3==0
    if i%3==0:
        sum=sum+i
    else:
        pass
    

str = "1부터 100사이의 3의 배수의 합은 %s입니다." % (sum)
print(str)


i = 1
sum = 0


while i <= 100:
    #3의 배수이면 sum을 아니면 pass
    #3의 배수 <==> i%3==0
    if i % 3 == 0:
        sum = sum+i
    else:
        pass
    
    #i를 1씩 증가시키면서
    i = i+1

str = "1부터 100사이의 3의 배수의 합은 %s입니다." % (sum)
print(str)
