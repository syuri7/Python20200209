
#  proverbs.txt 파일에서 줄 단위로 읽어서 output.txt 에 쓰시오 

infile = open("./st01.Python기초/py31파일처리/file/proverbs.txt",
               "r", encoding="UTF-8") 

for line in infile.readlines():
    print(line)  # 표준(모니터) 출력
  
    outfile = open("./st01.Python기초/py31파일처리/file/output.txt",
               "w", encoding="UTF-8") 
    outfile.write(line)
    outfile.close()
    
infile.close()    
    