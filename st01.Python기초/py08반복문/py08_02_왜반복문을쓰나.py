# 왜 반복을 사용하나?


# 순차문
print("환영합니다.")
print("환영합니다.")
print("환영합니다.")
print("환영합니다.")
print("환영합니다.")

# for 문
for x in range(5):  #range(5) : 0부터 5전까지 1씩
    print(x, "환영합니다.") 

#위의 구문보다는 아래 구문으로 사용(생략없이 전체 채우기)
for x in range(0,5,1):  #range(5) : 0부터 5전까지 1씩
    print(x, "환영합니다.") 
        
# while 문
