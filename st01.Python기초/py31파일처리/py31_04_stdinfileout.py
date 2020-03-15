
#########################
## 키보드 입력을 파일에 쓰는 프로그램을 작성하여 본다.
#########################

## 좀 더 수정해야 할듯

outfile = open("./st01.Python기초/py31파일처리/file/새파일.txt",
               "r+", encoding="UTF-8")


# 파일 처리
while True:
    data = input("입력하시오 : ")
    if data == "종료":
        break
    outfile.write(data)

while True:
    line = outfile.readline()
    if not line:
        break
    print(line)
       

# 파일 닫기
outfile.close()