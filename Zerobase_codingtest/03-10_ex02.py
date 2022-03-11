def solution(n):

    cnt = 0
    for i in range(1, n+1):
        cnt += i

    return cnt

# 정답코드
def solution(n):
    """
    :param n: int
    :return: int
    """

    return (1 + n) * n / 2
