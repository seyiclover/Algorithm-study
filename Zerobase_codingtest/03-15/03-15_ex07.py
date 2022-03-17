<내 코드>
def solution(n):

    nums = []
    for i in range(n+1):
        nums.append(i)

    biNums = []
    for num in nums:
        biNum = format(num, 'b')
        biNums.append(biNum)

    cnt = 0
    for i in biNums:
        for j in i:
            if j == '1':
                cnt += 1

    return cnt
  
<정답코드>
from functools import reduce


def solution(n):
    """
    :param n: int
    :return: int
    """

    # 중복된 결과를 저장
    dp = [0]

    # 2의 배수로 반복되는 bit 처리를 위함
    offset = 1

    for i in range(1, n + 1):
        if offset * 2 == i:
            offset *= 2

        dp.insert(i, dp[i - offset] + 1)

    # 0부터 n까지 필요한 붉은색 종이수
    return reduce(lambda a, b: a + b, dp, 0)
