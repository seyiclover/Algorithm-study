def solution(n):

    cnt = 0
    for i in range(1, n+1):
        cnt += i

    return cnt

# 정답코드
# 공차가 1인 등차 수열에 해당한다는 점에 착안해 등차수열의 일반항과 합공식을 사용 
# 일반항: a1(n-1) + d
# 합공식: (a1 + an) * n/2
def solution(n):

    return (1 + n) * n / 2
