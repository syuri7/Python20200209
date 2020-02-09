# 참석자에 맞추어서 치킨(1인당 1마리), 맥주(1인당 2캔), 
# 케익(1인당 4개)를 출력하는 프로그램을 작성해보자.
number = input("참석자의 수를 입력하시오:")
number = int(number)

chickens = number
beers = number * 2
cakes = number * 4

print("치킨의 수:", chickens)
print("맥주의 수:", beers)
print("케익의 수:", cakes)
