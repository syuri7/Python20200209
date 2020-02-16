# 0부터 9까지의 합계를 구하시오

sum=0 # 합계를 저장하는 변수

for x in range(0,10,1):
    sum=sum+x
    
print("sum= ", sum) #sum = 45

####################
# 문제 0부터 100까지의 짝수의 합계를 구하시오
####################

sum=0
for x in range(0,100,2):
    sum=sum+x
    
print("sum= ", sum)