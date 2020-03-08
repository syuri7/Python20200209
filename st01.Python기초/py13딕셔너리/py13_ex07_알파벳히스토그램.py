# 1. 파일 읽고 문자열에 텍스트 저장
# 2. 줄바꿈 (\n)을 제거한다. replace("\n","")
# 2. 딕셔너리 table을 만든다.
# 3. 문자열을 split()해서 array 리스트로 만든다.
# 4. 반복문을 사용하여 array 리스트를 루프를 돌면서
#    1. 리스트 요소에서 첫글자를 추출한다. 선택 연산자 []사용
#       val = array[i][0] 또는 val=i[0]
#    2. 딕셔너리 table에서 키 값 중에 val 있는지 찾는다.
#       ==찾을 때는 get()메서드나 in 연산자를 사용한다.
#    3. 대문자와 소문자를 구분하지 않도록 소문자로 치환한다.
#       val = val.upper()
#    4. 찾았다면 table[val] = table[val] + "-"
#       아니면 table[val] = "-"
#       ==찾는다. 을 때는 get()메서드나 in 연산자를 이용한다.
# 5. 찾기가 끝나면 table 출력한다.

str = """This was a great help. 
I applied this method to similiar problem 
and rather than concat a SELECT statement 
I created an event scheduled every couple 
hours to rebuild a view that pivots n amount 
of rows from one table into n columns on the other. 
It is a big help because before I was rebuilding 
the query using PHP on every execution of the SELECT. 
Even though views can not leverage Indexes, 
I am thinking filtering performance will not 
be an issue as the pivoted rows->columns 
represent types of training employees at a 
franchise have so the view will not ever break 
a few thousand rows."""

str = str.replace("\n", "")
array = str.split(" ")
table = {}


for i in range(0, len(array), 1):
    # array[0] == This ==> 0번 방의 첫글자 : array[0][0] == T
    # array[1] == was ==> 0번 방의 첫글자 : array[1][0] == w
    key = array[i][0]  # 리스트 요소에서 첫글자를 추출
    key = key.upper()
    tmp = table.get(key)
    if tmp == None:
        # 미존재
        # table[key] = "-" <== 문자로 저장
        table[key] = 1  # <== 숫자로 저장
    else:
        # 미존재
        # table[key] = table[key] + "-"
        table[key] = table[key] + 1


for item in table.items():
    # item[0]을 item[1]번 반복하시오.
    # item = (T,17) ==> TTTTTTTTTTTTTTTTTT
    print(item[0], item[1], item[0]*item[1])
