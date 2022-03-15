# 문자열에서 숫자를 구분해주는 함수 isdigit() 사용
def solution(s):
    # 숫자 다음에 +, -  연산자를 인식 시키기 위해서 문자열을 거꾸로 조회한다. 
    z = s[::-1]
    total = 0
    calcu = 0
    multi = 1
    for each in z:
        if each.isnumeric():
            # 연속되는 숫자에서 자릿수를 인식해주기 위해 10을 곱해준다. 
            calcu += int(each)*multi
            multi *= 10
        else:
            if each == "-":
                total -= calcu
            else:
                total += calcu
            # 변수 초기화 
            calcu = 0
            multi = 1
    # 첫번 째 숫자에 연산자가 없을 경우 더해준다.
    if s[0].isnumeric():
        total += calcu
    return int(total)

print(solution('-3+36-7'))


<정답코드>
def solution(s):
    """
    :param s: str
    :return: int
    """

    nums = []
    ops = []
    save(s, nums, ops)

    return calc(nums, ops)


def save(s, nums, ops):
    i = 0
    tmpNum = ''
    while (i < len(s)):
        c = s[i]

        if isNumber(c):
            tmpNum += c
        else:
            if i == 0:
                nums.append(0)
                ops.append(c)
            else:
                nums.append(int(tmpNum))
                ops.append(c)

            tmpNum = ''

        i = i + 1

    nums.append(int(tmpNum))


def calc(nums, ops):
    if len(nums) == 1:
        return nums[0]

    num1 = nums.pop(0)
    num2 = nums.pop(0)

    calcNum = add(num1, num2) if ops.pop(0) == '+' else sub(num1, num2)
    nums.insert(0, calcNum)
    return calc(nums, ops)


def add(num1, num2):
    return num1 + num2


def sub(num1, num2):
    return num1 - num2


def isNumber(c):
    charCode = ord(c)
    return 48 <= charCode <= 57
