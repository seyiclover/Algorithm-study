<정답 코드>
from itertools import combinations

def solution(nums):
    n = len(nums)
    for i in range(1, 5):
        for indices in combinations(range(n), i):
            summation = 0
            for index in indices:
                summation += nums[index]
            if summation == 0:
                return i 
    return -1
