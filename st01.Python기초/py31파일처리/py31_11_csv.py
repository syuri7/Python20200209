
#########################
##
#########################


# 파일을 연다.

# 파일 안의 각 줄을 처리한다.

# 공백 문자를 없앤다.

# 줄을 출력한다.

# 줄을 쉼표로 분리한다.

# 각 줄의 필드를 출력한다.

infile = open("./st01.Python기초/py31파일처리/file/data.csv",
              "r")


for line in infile.readlines():
    line = line.strip()  # .strip() 양쪽에 공백 제거
    part = line.split(",")  # .split(",") 쉼표로 분리
    print(line)
    for i in part:
        print(" ", i)
