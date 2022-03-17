<내 코드>
# 1
def solution(arr):

    wordCnts = []
    for i in arr:
        cnt = len(i.split(' '))
        wordCnts.append(cnt)

    result = max(wordCnts)

    return result
  
 
# 2
def solution(arr):

    return max(list(map(lambda x: len(x.split()),arr)))
  
<정답코드>
from functools import reduce


def solution(arr):
    """
    :param arr: str[]
    :return: int
    """

    counts = list(map(lambda s: countWords(s), arr))
    return reduce(lambda pre, cur: max(pre, cur), counts, 0)


def countWords(s):
    return len(s.split(' '))
