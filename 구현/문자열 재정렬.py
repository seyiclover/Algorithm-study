data = input()
result = []
value = 0

# isalpha():  알파벳이면 True
# isdigit():  숫자이면 True
# isalnum():  알파벳이거나 숫자이면 True

for i in data:
    if i.isalpha():
        result.append(i)
    else:
        value += int(i)

result.sort()

if value != 0:
    result.append(str(value))

# 리스트에 있는 내용을 문자열로 반환 
print(''.join(result))
