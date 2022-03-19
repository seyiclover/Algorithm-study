<정답 코드>
# itertools 모듈의 combinations 함수 기능: combinations(n, r) => n에서 r개를 뽑아서 나열하는 모든 경우 생성 

from itertools import combinations

def solution(nums):
    n = len(nums)
    # 답이 5보다 크면 -1을 출력하기 때문에 합을 0으로 만드는 정수 개수의 최대값은 5개이다. 
    for i in range(1, 6):  # nCr 에서 r 지정 
        for indices in combinations(range(n), i):   # nCi 의 모든 경우 나열 
            summation = 0
            for index in indices:                   # i개 뽑은 인덱스를 넣었을 때 그 합이 0인 경우를 찾는다. 
                summation += nums[index]
            if summation == 0:
                return i 
    return -1
