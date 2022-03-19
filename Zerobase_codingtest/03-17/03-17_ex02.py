<정답코드>
# key, value로 구성된 dictionary 자료형 사용 
# 같은 이름과 같은 전화번호를 가진 경우를 제외하고 dictionary 자료형에 추가해준다. 

def solution(address_book):
    book = {}
    for name, number in address_book:
        number = number.replace('-', '').replace(' ', '')
        if name not in book:
            book[name] = set()   # set()은 중복을 허용하지 않는다. {}로 자료형을 정의하지만 key 값이 존재하지 않는다. 
        book[name].add(number)   # key 값이 name인 곳에 number를 value로 추가해준다. 

    answer = 0
    for name in book:
        num = len(book[name])
        if num > 1:
            answer += num
    
    return answer
