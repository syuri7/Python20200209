# phones.txt 파일에 아래의 2줄 쓰고 저장하시오.
# 최무선  010-1111-2222
# 정중부  010-2222-3333

outfile = open("./st01.Python기초/py31파일처리/file/phones.txt",
               "a", encoding="UTF-8")


outfile.write("\n최무선 010-1111-2222")  # \n 줄바꿈
outfile.write("\n정중부 010-2222-3333")

outfile.close()
