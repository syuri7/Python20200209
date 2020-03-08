#################################
# datetime 모듈의 사용법을 익힌다.
#
# datetime.now()	현재 년월일시분초 가져오기
# datetime.timedelta()	시간 가감로세스를 주어진 초만큼 정지
# datetime.replace()	시간 교체
#################################


# 모듈을 읽어 들입니다.

import datetime


########################
# 현재 년,월,일,시,분,초 출력하기
# 예시)  년 2020
#        월 3
#        일 2
#        시 15
#        분 15
#        초 58
now = datetime.datetime.now()  # 패키지명, 모듈명, 함수명
print(now)  # 2020-03-08 16:23:28.745471
print("년", now.year)
print("월", now.month)
print("일", now.day)
print("시", now.hour)
print("분", now.minute)
print("초", now.second)

########################
# 시간 출력 방법
# 예시) 15:15:58
str = "%2d:%2d:%2d" % (now.hour, now.minute, now.second)
print(str)


########################
# 시간 출력 방법
# 예시) 15시 15분 58초

str = "%2d시%2d분%2d초" % (now.hour, now.minute, now.second)
print(str)

########################
# 현재 시간이 오전/오후 인지를 출력하시오.
# 파이썬에서 오전/오후를 구별하느 방법이 없다.
# 시간으로 오전/오후를 판별해야 한다.
# 예시) 현재 시간은 15시로 오후입니다!
hour = now.hour  # 현재시간

if hour > 12:
    str = "현재 시간은 %2d시로 오후입니다. " % hour
    print(str)
else:
    str = "현재 시간은 %2d시로 오전입니다. " % hour
    print(str)


########################
# 계절을 확인합니다.
# 현재 날짜/시간을 구하고 월을 변수에 저장합니다.
# 조건문으로 계절을 확인합니다. now.month를 이용하여 판별한다.
# 예시) 현재는 봄입니다.


# date 출력함수 만들기 : 예시) 2020-03-02 16:42:06
def dateFormat(tm):
    print(tm)
    str = "%04d-%02d-%02d %02d:%02d:%02d" % (tm.year,
                                             tm.month, tm.day, tm.hour, tm.minute, tm.second)
    return str

########################
# 중요!!!!!!!!!!!!!, 이걸로 사용
# 특정 시간 구하기 : datetime.timedelta() 메서드
# datetime.timedelta()로 시간 더하기 >> 현재에 1주 1일 1시간 1분 1초를 더해서 출력하시오.
# 예시) 현재 2020-03-02 16:42:06
#       수정 2020-03-10 17:43:07


now = datetime.datetime.now()  # 현재 날짜와 시간
print("datetime.timedelta()로 시간 더하기 >> 현재에 1주 1일 1시간 1분 1초를 더해서 출력하시오.")
print("현재", dateFormat(now))
after = now + datetime.timedelta(
    weeks=1,
    days=1,
    hours=1,
    minutes=1,
    seconds=1
)
print("수정", dateFormat(after))

print("datetime.timedelta()로 시간 더하기 >> 오늘부터 100일 전 날짜를 출력하시오.")
after = now + datetime.timedelta(
    days=- 100
)
print("100일전", dateFormat(after))


########################
# 특정 시간 요소 교체하기 : replace() 메서드
# datetime.replace()로 시간 더하기 >> 1년 1주 더하기
# 예시) 현재 2020-03-02 16:44:19
#       수정 2021-03-09 16:44:19

now = datetime.datetime.now()  # 현재 날짜와 시간
print("datetime.replace()로 시간 더하기 >> 1년 1주 더하기")
print("현재", dateFormat(now))
after = now.replace(
    year=now.year + 1,
    day=now.day + 7
)

print("수정", dateFormat(after))
