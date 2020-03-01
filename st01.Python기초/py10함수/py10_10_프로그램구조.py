# 데이터 수집
def readList():
    nlist = []
    flag = True
    while flag:
        number = int(input("숫자를 입력하시오: "))
        if number < 0:
            flag = False
        else:
            nlist.append(number)
    return nlist

# 데이터 처리


def processList(nlist):
    nlist.sort()
    return nlist


# 데이터 출력
def printList(nlist):
    for i in nlist:
        print("성적=", i)

# 프로그램 시작


def main():
    nlist = readList()
    processList(nlist)
    printList(nlist)


# 이 모듈이 단독으로 사용되면 main()를 호출하라.
if __name__ == "__main__":
    main()
