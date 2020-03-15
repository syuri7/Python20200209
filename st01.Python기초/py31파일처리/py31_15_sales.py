# 입력 파일 이름과 출력 파일 이름을 받는다.

# 입력과 출력을 위한 파일을 연다.

# 합계와 횟수를 위한 변수를 정의한다.

# 입력 파일에서 한 줄을 읽어서 합계를 계산한다.

# 총매출과 일평균 매출을 출력 파일에 기록한다.

infile = open("./st01.Python기초/py31파일처리/file/sales.txt",
              "r", encoding="UTF-8")


i = 0
sum = 0
ave = 0

for line in infile.readlines():
    line = int(line)
    i = i + 1
    sum = sum + line
    ave = sum / i

outfile = open("./st01.Python기초/py31파일처리/file/summary.txt",
               "w", encoding="UTF-8")

outfile.write("총매출 = "+str(sum))  # write는 문자열만 입력 가능해서, str로 변경되어야 함
outfile.write("\n평균 일매출 = "+str(ave))
outfile.close()

infile.close()
