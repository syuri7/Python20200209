
address = input("이메일 주소를 입력하시오 : ")
(id, domain) = address.split("@")

print(address)
print('         ' + id)
print('         ' + domain)

print("------------------")

arr = address.split("@")
# id = arr[0]
# domain = arr[1]
(id, domain) = arr
print(address)
print('         ' + id)
print('         ' + domain)
