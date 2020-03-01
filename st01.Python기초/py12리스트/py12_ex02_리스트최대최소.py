정수 = []
i = 0
while i < 10:
    x = input("정수를 입력하세요:")
    x = int(x)
    i = i+1
    정수.append(x)
print("INPUT : ", 정수)
print("리스트 정렬 전 : ", 정수)
정수 = sorted(정수)
print("리스트 정렬 후 : ", 정수)
print("최소값 : ", 정수[0])
print("최대값 : ", 정수[-1])
