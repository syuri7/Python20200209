import os.path

outfile = open("phones.txt", "w", encoding="UTF-8")

if os.path.isfile("phones.txt"):
    outfile.write("홍길동 010-1234-5678")  # \n 줄바꿈
    outfile.write("\n김철수 010-1234-5679")
    outfile.write("\n김영희 010-1234-5680")

else:
    print("동일한 이름의 파일이 이미 존재합니다.")

outfile.close()
