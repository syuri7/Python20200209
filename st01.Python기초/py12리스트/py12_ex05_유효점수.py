
# step1. ArrayList 인스턴스, list  만들기.
# step2. 심사 위원수를 입력 받는다.
# step3. 심사 위원의 점수 입력 받아서 list에 저장.
#     몇 번 입력 받아야 하는가? 심사 위원수 만큼
# step4. 합계를 구하는 메서드 만들기
#     1번방부터 마지막방 -1 까지
# step5. 평균을 구하는 메서드 만들기.
#     평균값 = (double)sum / ( list.size() - 2 )
# step6. ArrayLis 정렬하기.
# step7. 합계를 구하고 출력한다.
# step8. 평균을 구하고 출력한다.

심사위원수 = input("심사 위원수를 입력하시오:")
심사위원수 = int(심사위원수)
i = 0
점수 = []

while i < 심사위원수:
    x = input("심사 위원의 점수 입력 : ")
    x = int(x)
    점수.append(x)
    정렬 = sorted(점수)
    최소값 = 정렬[0]
    최대값 = 정렬[-1]
    합계 = sum(정렬) - 최소값 - 최대값
    평균 = 합계 / (심사위원수-2)
    i = i + 1


print("유효점수: ", 정렬[1:심사위원수-1])
print("합계: ", 합계)
print("평균: ", 평균)
