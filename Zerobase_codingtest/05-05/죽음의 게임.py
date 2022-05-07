# 순서를 고려하여 n-1개 중에서 m-2개를 선택하는 경우의 수 >> 순열 

<정답 코드>
from math import perm

def solution(n, m):
    max_div = m // 2 + 1

    answer = 0
    for div in range(1, max_div):
        q, r = divmod(m, div)    # 몫과 나머지를 튜플 형식으로 반환 
        if (r == 0) and (q <= n):
            answer += perm(n -1, q - 1)

    return answer % 100007

