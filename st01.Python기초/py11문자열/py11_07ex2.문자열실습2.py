# -*- coding: utf-8 -*-


# 도전 2. 형변환. 문자열을 정수로 바꾸기.
# 문자열 "3"을 정수 3으로 바꾸시오. 구글 검색
# temp2 = "3"

# 도전 3. 문자열에서 가장 큰 수를 찾으시오.
# a. 문자열 자르기 --> 리스트를 얻게 됨.
# b. 문자열을 정수 리스트로 만든다.
# c. 정수리스트를 오름차순 정렬하시오.
# d. 정수리스트에서 최대값을 찾는다.

# a. 문자열 자르기 --> 리스트를 얻게 됨.
temp3 = "74 874 9883 73 9 73646 774"
array1 = temp3.split(" ")
print(array1)  # ['74', '874', '9883', '73', '9', '73646', '774']

print("---------------------------")

# array1의 값을 출력
# array1의 방번호는 0번 부터 시작한다.
print(array1[0], type(array1[0]))  # "74", str
print(array1[1], type(array1[1]))  # "874", str
print(array1[2], type(array1[2]))  # "9883", str

print("---------------------------")

# b. 문자열을 정수 리스트로 만든다.
array1[0] = int(array1[0])
array1[1] = int(array1[1])
array1[2] = int(array1[2])

print(array1[0], type(array1[0]))  # "74", int

for i in range(0, len(array1), 1):
    array1[i] = int(array1[i])

print(type(array1), array1)
print("---------------------------")

# append 안 배운것임
array2 = []
for n in array1:
    n = int(n)
    array2.append(n)


print(array2)  # [74, 874, 9883, 73, 9, 73646, 774]

print("---------------------------")

# c. 정수리스트를 오름차순 정렬하시오.
array3 = sorted(array2)
print(array3)
print("---------------------------")

# d. 정수리스트에서 최대값을 찾는다.
print(array3[len(array3) - 1])  # 마지막 방에 있는 값. len(array3) -1 ==6
# 마지막 방에 있는 값이므로 무조건 오름차순 정렬이 되어 있어야 함.

print("---------------------------")

최대값 = max(array2)  # max를 구하므로, 오름차순 정렬 상관없음
print(최대값)

print("종료")


# main 함수 사용

def main():

    # a. 문자열 자르기 --> 리스트를 얻게 됨.
    temp3 = "74 874 9883 73 9 73646 774"
    array1 = temp3.split(" ")
    print(array1)  # ['74', '874', '9883', '73', '9', '73646', '774']

    print("---------------------------")

# array1의 값을 출력
# array1의 방번호는 0번 부터 시작한다.
    print(array1[0], type(array1[0]))  # "74", str
    print(array1[1], type(array1[1]))  # "874", str
    print(array1[2], type(array1[2]))  # "9883", str

    print("---------------------------")

# b. 문자열을 정수 리스트로 만든다.
    array1[0] = int(array1[0])
    array1[1] = int(array1[1])
    array1[2] = int(array1[2])

    print(array1[0], type(array1[0]))  # "74", int

    for i in range(0, len(array1), 1):
        array1[i] = int(array1[i])

    print(type(array1), array1)
    print("---------------------------")

# append 안 배운것임
    array2 = []
    for n in array1:
        n = int(n)
        array2.append(n)

    print(array2)  # [74, 874, 9883, 73, 9, 73646, 774]

    print("---------------------------")

# c. 정수리스트를 오름차순 정렬하시오.
    array3 = sorted(array2)
    print(array3)
    print("---------------------------")

# d. 정수리스트에서 최대값을 찾는다.
    print(array3[len(array3) - 1])  # 마지막 방에 있는 값. len(array3) -1 ==6
# 마지막 방에 있는 값이므로 무조건 오름차순 정렬이 되어 있어야 함.

    print("---------------------------")

    최대값 = max(array2)  # max를 구하므로, 오름차순 정렬 상관없음
    print(최대값)


main()
