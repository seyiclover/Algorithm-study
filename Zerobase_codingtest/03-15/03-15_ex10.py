<내 코드>
# 최대값의 합이 최소가 되게 하기 위해서는 큰숫자는 큰숫자 끼리 작은 숫자는 작은 숫자끼리 묶어줘야 한다. 


# 1
def solution(arr, K):

    arr.sort(reverse=True)

    nations = []
    while True:
        nations.append(arr[:K])
        del arr[:K]
        if len(arr) == 0:
            break

    maxNums = []

    for i in nations:
        mx = 0
        for j in i:
            if j >= mx:
                mx = j
                maxNums.append(mx)
                
    return sum(maxNums)
  
# 2
def solution(arr, K):
    arr.sort()
    kings = []
    for i in range(0,len(arr),K):
        kings.append(arr[i:i+K][-1])
    return sum(kings)
  
<정답코드>
from functools import reduce


def solution(arr, K):
    """
    :param arr: int[]
    :param K: int
    :return: int
    """

    arr.sort()

    kings = []

    i = 0
    while i < len(arr):
        king = 0

        for sumCount in range(K):
            king = max(king, arr[i])
            i += 1

        kings.append(king)

    return reduce(lambda x, y: x + y, kings, 0)
