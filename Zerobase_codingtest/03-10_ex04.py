def solution(useageArr, fee):

    totalFee = 0
    for each in useageArr:
        totalFee += each * fee
        
    return totalFee

# 정답코드
from functools import reduce


def solution(usageArr, fee):
    """
    :param usageArr: int[]
    :param fee: int
    :return: int
    """

    totalUsage = reduce(lambda pre, cur: pre + cur, usageArr, 0)
    return totalUsage * fee
