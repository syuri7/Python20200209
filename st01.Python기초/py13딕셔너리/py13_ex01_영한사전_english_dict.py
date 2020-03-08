dictionary = {"one": "하나", "two": "둘", "three": "셋", }

단어 = ""

while True:
    단어 = input("단어를 입력하시오 : ")
    if 단어 in dictionary:
        print(dictionary[단어])
    else:
        print("없음")
    if 단어 == "":
        break
