성적 = []
while True:
    x = input("성적을 입력하시오:")
    x = int(x)
    if x < 0:
        break
    성적.append(x)
    합계 = sum(성적)
    평균 = 합계 / len(성적)
print(합계)
print(평균)
