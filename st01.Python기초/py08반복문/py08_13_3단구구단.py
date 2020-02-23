#while문을 사용하여 3단을 출력하시오.

i=1
while i<10:
    str= "i=%s,%s*%s=%2s" %(i,3,i,3*i)
    print(str)
    i=i+1 #i를 1씩 증가시킨다.
    
print("while문 종료")
