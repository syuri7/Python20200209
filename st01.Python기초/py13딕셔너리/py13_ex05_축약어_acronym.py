# 1. 문자열 입력 받기
# 2. 문자열을 split()해서 array 리스트로 만든다.
# 3. 반복문을 사용하여 array 리스트를 루프를 돌면서 딕셔너리 table에서 찾는다.
# ==> table에서 찾을 때는 get()메서드나 in 연산자를 이용한다.
# 3-1. 찾았다면 바꾼다. - replace()
# 4. 출력한다. 문자열 join() 메서드를 사용하는 것으로 작성한다.

table = {"B4": "Before",
         "TX": "Thanks",
         "BBL": "Be Back Later",
         "BCNU": "Be Seeing You",
         "HAND": "Have A Nice Day"}


입력 = input("번역할 문장을 입력하시오 : ")


arr = 입력.split(" ")


for i in range(0, len(arr), 1):  # for i in arr: 로 사용해도 됨
    if arr[i] in table:
        print(table[arr[i]], end=" ")

    else:
        print(arr[i], end=" ")

print()

#############################################
######### 아래 2개 동일함 ##############
# for i in range(0, len(arr), 1):
#     print(arr[i])
# for i in arr:
#     print(i)
#############################################

# 선생님 답

# 1.
str = input("번역할 문장을 입력하시오 : ")

# 2.
array = str.split(" ")

result = ""  # 출력할 문자열
# 3.
for i in array:

    # 3-1. table에서 찾는다.
    # 찾을 때는 get()메서드나 in 연산자를 사용한다.
    # 찾았다면 바꾼다.
    # array[0] = TX 일때 table엣 찾을려면 (get(), in)
    # array[1] = Mr. 일때 table엣 찾을려면 (get(), in)
    # array[2] = Park! 일때 table엣 찾을려면 (get(), in)
    value = table.get(i)
    if value == None:
        result = result + i + " "
    else:
        result = result + value + " "   # value = table.get(i)


# 4.
print(result)
