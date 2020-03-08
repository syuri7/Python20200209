

#########################
# readline() 파일에서 한 줄씩 읽기


#########################
##

# 파일 존재유무 확인
import os
print("현재 작업 디렉토리:", os.getcwd())
if os.path.isfile("./st01.Python기초/py31파일처리/file/phones.txt"):
    print("파일 존재")
else:
    print("파일 없음")


#########################
##
print("readline() 파일에서 한 줄씩 읽기")
infile = open("./st01.Python기초/py31파일처리/file/phones.txt",
              "r", encoding="UTF-8")
s = infile.readline()
print(s, end="")
s = infile.readline()
print(s,end="")
s = infile.readline()
print(s,end="")
infile.close()


#######################
# 반복문으로 처리하기

print("반복문으로 파일에서 읽어서 모니터에 출력하기")
infile = open("./st01.Python기초/py31파일처리/file/phones.txt",
              "r", encoding="UTF-8")
line = infile.readline()
while line != "":
    print(line,end="")
    line = infile.readline()

infile.close()
