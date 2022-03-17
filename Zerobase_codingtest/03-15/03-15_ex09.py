<내 코드>
# 가로로 이동하는 경우의 수는 w-1, 세로로 이동하는 경우의 수는 h-1 이다.
# 전체 경우의 수는 가로로 이동하는 경우 와 세로로 이동하는 경우를 일렬로 나열한 값이다.(순열)
# 전체 경우의 수: ((w-1) + (h-1))! / (w-1)! * (h-1)!

def solution(h, w):

    import math

    h = h-1
    w = w-1

    cnt = math.factorial(h + w) / (math.factorial(h) * math.factorial(w))

    return cnt

<정답코드>
import numpy


def solution(h, w):
    """
    :param h: int
    :param w: int
    :return: int
    """

    # h x w 크기의 배열에, 해당 지점까지 갈 수 있는 경우의 수를 저장
    dp = numpy.ones(shape=(h, w))

    # dp[i][j] 까지 갈 수 있는 경우의 수는,
    # dp[i][j]의 좌측과 상단까지 갈 수 있는 경우의 수를 더한 것과 같다.
    for i in range(1, h):
        for j in range(1, w):
            dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

    return dp[h - 1][w - 1]
