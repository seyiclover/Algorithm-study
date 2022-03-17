def solution(nums, k):
    n = len(nums)
    answer = 0 
    lt = 0
    cnt = 0

    for rt in range(n):
        if nums[rt] == 0:
            cnt += 1
        while (cnt > k):
            if nums[lt] == 0:
                cnt -= 1
            lt += 1
        answer = max(answer, rt - lt + 1)

    return answer 

print(solution([1, 0, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 0, 0, 1], 2))
