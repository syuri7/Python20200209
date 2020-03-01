# a. 문자열 자르기 --> 리스트를 얻게 됨.
temp3 = "74 874 9883 73 9 73646 774"
array1 = temp3.strip().split(" ")
print(array1)  # ['74', '874', '9883', '73', '9', '73646', '774']

# b. 문자열을 정수 리스트로 만든다.
array2 = []
for n in array1:
    n = int(n)
    array2.append(n)


print(array2)  # [74, 874, 9883, 73, 9, 73646, 774]

# c. 정수리스트를 오름차순 정렬하시오.
array3 = sorted(array2)
print(array3)
print("---------------------------")

# d. 정수리스트에서 합계, 평균, 최대값, 최소값을 구하시오.


def ave(array2):
    x = sum(array2) / len(array2)

    return x


def main():

    합계 = sum(array2)
    print("합계는:", 합계)

    평균 = ave(array2)
    print("평균은:", 평균)

    최대값 = max(array2)
    print("최대값은:", 최대값)

    최소값 = min(array2)
    print("최소값은:", 최소값)


main()
