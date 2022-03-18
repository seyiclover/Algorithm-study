<정답코드>
def solution(address_book):
    book = {}
    for name, number in address_book:
        number = number.replace('-', '').replace(' ', '')
        if name not in book:
            book[name] = set()
        book[name].add(number)

    answer = 0
    for name in book:
        num = len(book[name])
        if num > 1:
            answer += num
    
    return answer
